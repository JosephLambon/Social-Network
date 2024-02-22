from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseBadRequest
from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse

from .models import User, Post

from .forms import NewPostForm

from django.core.serializers import serialize
from django.core.serializers.json import DjangoJSONEncoder
from django.core.paginator import Paginator
import json

def serialise_posts(posts):
    # Serialisation allows us to transfer and store the
    # posts data in a way that remains accessible in JSX
    # AKA translates our Django 'Post' model data.
    # See defined natural key in models.py . By default, returns User ID, which is unhelpful.
    s_posts = [
        {
            'title': post.title,
            'body': post.body,
            'author': post.author.natural_key(), # Using natural key to retrieve username
            'timestamp': post.timestamp(),
            'created': post.created,
            'likes': post.likes,
            'id': post.id
        }
        for post in posts
    ]
    # Sort s_posts list by datetime objects.
    sorted_s_posts = sorted(s_posts, key=lambda x: x['created'], reverse=True)  

    # Serialize list of dictionary's defined above for each post into JSON string.
    # DjangoJSONEncoder allows serialisation of datetime objects.
    serialized_posts = json.dumps(sorted_s_posts, cls=DjangoJSONEncoder)
    return serialized_posts

def check_if_following(user, profile):
    check = False
    # Check if already following
    for person in user.following.all():
        if person.username == profile.username:
            check = True
    return check

def index(request):
    posts = Post.objects.order_by('-created')

    p = Paginator(posts, 10)
    page_no = request.GET.get('page')
    page_obj = p.get_page(page_no)
    # Serialise posts on the page selected
    serialized_posts = serialise_posts(page_obj.object_list)

    return render(request, "network/index.html", {
        "form": NewPostForm(),
        "posts": serialized_posts,
        "page_obj": page_obj
        })

def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "network/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "network/login.html")

def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))

def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "network/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "network/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "network/register.html")

@login_required
def new_post(request, user_id):
    user = User.objects.get(id=user_id)
    if request.method=="POST":
        form = NewPostForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data["title"]
            body = form.cleaned_data["body"]
        
        # Create new post
        post = Post(title=title,
                    body=body,
                    author=user)
        post.save()
    # Render all posts
    return HttpResponseRedirect(reverse("index"))

@login_required
def profile(request, profile_id):
    profile = User.objects.get(id=profile_id)
    user = User.objects.get(id=request.user.id)
    posts = Post.objects.filter(author=profile.id)
    posts = posts.order_by('-created')

    p = Paginator(posts, 10)
    page_no = request.GET.get('page')
    page_obj = p.get_page(page_no)
    # Serialise posts on the page selected
    serialized_posts = serialise_posts(page_obj.object_list)

    check = check_if_following(user, profile)

    return render(request, "network/profile.html", {
        "profile": profile,
        "posts": serialized_posts,
        "check": check,
        "page_obj": page_obj
    })

@login_required
def following(request):
    user = User.objects.get(id=request.user.id)
    following = user.following.all()
    # Use '__in' to filter the list
    posts = Post.objects.filter(author__in=following)
    posts = posts.order_by('-created')

    p = Paginator(posts, 10)
    page_no = request.GET.get('page')
    page_obj = p.get_page(page_no)
    # Serialise posts on the page selected
    serialized_posts = serialise_posts(page_obj.object_list)

    return render(request, "network/following.html", {
        "posts": serialized_posts,
        "page_obj": page_obj
    })

def follow(request, user_id, profile_id):
    profile = User.objects.get(id=profile_id)
    user = User.objects.get(id=request.user.id)

    posts = Post.objects.filter(author=profile.id)
    serialised_posts = serialise_posts(posts)
    check = check_if_following(user, profile)

    error_message = request.GET.get('message', None)
    
    if check == True:
        # UPDATE TO JUST RETURN PROFILE WITH SIMPLE ERROR MESSAGE VIA DJANGO VARIABLE.
        # Redirect with a query parameter for error message
        return redirect(reverse('profile', args=[profile.id]) + f'?error=Already following this user')

    else:
        # Have user follow profile
        user.following.add(profile)
        # Add user to profile's followers
        profile.followers.add(user)
        user.save()
        profile.save()
        return redirect('profile', profile_id=profile.id)

def unfollow(request, user_id, profile_id):
    profile = User.objects.get(id=profile_id)
    user = User.objects.get(id=user_id)

    posts = Post.objects.filter(author=profile.id)
    serialised_posts = serialise_posts(posts)

    check = check_if_following(user, profile)
    
    if check == True:
        # Have user unfollow profile
        user.following.remove(profile)
        # Remove user from profile's followers
        profile.followers.remove(user)
        user.save()
        profile.save()
        return redirect('profile', profile_id=profile.id)
    else:
        # Pass message to profile page to add error message to display
        return redirect(reverse('profile', args=[profile.id]) + f'?message=Error: Not following this user')
    
def update_post(request):
    if request.method == 'POST':
        # Parse JSON list to Python dictionary
        data = json.loads(request.body)
        post_id = data['id']
        new_title = data['newTitle']
        new_body = data['newBody']
        post = Post.objects.get(pk=post_id)
        post.title = new_title
        post.body = new_body
        post.save()
        return JsonResponse({'message': 'Post updated successfully'}, status=200)
    else:
        return JsonResponse({'error': 'Only POST requests are allowed'}, status=400)