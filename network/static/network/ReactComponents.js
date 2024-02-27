// SOURCE - get_Cookie()
// https://docs.djangoproject.com/en/5.0/howto/csrf/

function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

const Post = (props) => { 
    const Edit = () => {
        const item = document.getElementById(props.id);
        if (item.children[0].children[1].children[0].style.display == 'none') {
            // Leaving black to do nothing in this case.
        } else {
            console.log(item);
            // Hide post's current title
            const title = item.children[0].children[1].children[0];
            title.style.display = 'none';

            // Add new input element for desired new title.
            const new_title = document.createElement('input');
            new_title.type = 'text';
            new_title.value = title.innerText.slice(0,-1);
            // Display new title input where title was showing.
            title.parentNode.insertBefore(new_title, title.nextSibling);

            // Hide post's current body
            const body = item.children[1].children[0];
            console.log(body)
            const div = document.createElement('div');
            div.classList.add('col-12',  'p-4');
            body.style.display = 'none';
            // Add input element for body
            const new_body = document.createElement('input');
            new_body.type = 'text';
            new_body.value = body.innerText;
            // Display new title input where title was showing.
            body.parentNode.insertBefore(div, body.nextSibling);
            div.appendChild(new_body);

            // Add save button for changes
            const place = item.children[1];
            const save_div = document.createElement('div');
            save_div.classList.add('row', 'justify-content-end', 'mr-4');
            const save = document.createElement('button');
            save.innerText = 'Save changes';
            save.classList.add('btn-rounded');
            save.setAttribute('id',`save_btn_${props.id}`);
            save_div.appendChild(save);
            place.parentNode.insertBefore(save_div, place.nextSibling);

            // CONFIRM USER IS AUTHOR OF POST
            // if (props.author != )
            // Update post details on save.
            document.getElementById(`save_btn_${props.id}`).addEventListener('click', Save);
            document.getElementById(`like_btn_${props.id}`).addEventListener('click', Like);
        };
    };

    const Save = () => {
        const item = document.getElementById(props.id);
        if (UserUsername !== props.author) {
            alert("You are not authorised to edit this post!");
        } else {
            const title_div = item.children[0];
            const body_div = item.children[1];

            const newTitle = title_div.children[1].children[1].value;
            const newBody = body_div.children[1].children[0].value;

            console.log("New Title: ", newTitle);
            console.log("New Body: ", newBody);
            // // UPDATE THE DATABASE VALUES
            fetch('/update-post/', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    'X-CSRFToken': getCookie('csrftoken')
                },
                body: JSON.stringify({
                    id: props.id,
                    newTitle: newTitle,
                    newBody: newBody,
                }),
            })
            .then(response => {
                if (!response.ok) {
                    throw new Error('Failed to update post');
                }
            })
            .catch(error => {
                console.error('Error updating post:', error);
                // Handle error
            });

            // Update display
            title_div.children[1].children[0].innerHTML = newTitle + ":";
            title_div.children[1].children[0].style.display = 'block';
            title_div.children[1].children[1].style.display = 'none';
            
            body_div.children[0].innerHTML = newBody;
            body_div.children[0].style.display = 'block';
            body_div.children[1].style.display = 'none';

            const btn_div = item.children[2];
            btn_div.children[0].style.display = 'none';

            document.getElementById(`save_btn_${props.id}`).addEventListener('click', Save);
        };
    };

    const Like = () => {
        const item = document.getElementById(props.id);
        
        fetch('/like-post/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': getCookie('csrftoken')
            },
            body: JSON.stringify({
                id: props.id,
                liker_username: UserUsername
            }),
        })
        .then(response => {
            if (!response.ok) {
                throw new Error('Failed to like post');
            }
            // This line parses the JSON response
            // Hence, passes through the returned likes_count from the like view.
            return response.json();
        })
        .then(data => {
            const likes_div = item.children[3];
            const like_counter = likes_div.children[1];

            like_counter.innerHTML = data.likes_count;
        })
        .catch(error => {
            console.error('Error liking post:', error);
            // Handle error
        });
    };

    return (
        <div id={props.id}>
            <div class="row justify-content-end">
                {UserUsername == props.author && (
                    <button class="edit" onClick={Edit}>
                        <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-pencil-square" viewBox="0 0 16 16">
                            <path d="M15.502 1.94a.5.5 0 0 1 0 .706L14.459 3.69l-2-2L13.502.646a.5.5 0 0 1 .707 0l1.293 1.293zm-1.75 2.456-2-2L4.939 9.21a.5.5 0 0 0-.121.196l-.805 2.414a.25.25 0 0 0 .316.316l2.414-.805a.5.5 0 0 0 .196-.12l6.813-6.814z"/>
                            <path fill-rule="evenodd" d="M1 13.5A1.5 1.5 0 0 0 2.5 15h11a1.5 1.5 0 0 0 1.5-1.5v-6a.5.5 0 0 0-1 0v6a.5.5 0 0 1-.5.5h-11a.5.5 0 0 1-.5-.5v-11a.5.5 0 0 1 .5-.5H9a.5.5 0 0 0 0-1H2.5A1.5 1.5 0 0 0 1 2.5z"/>
                        </svg>
                    </button>
                )}
                <div class="col-12 p-1 text-center"><strong>{props.title}:</strong></div>
            </div>
            <div class="row text-center">
                <div class="col-12 p-4">{props.body}</div>
            </div>
            <hr color="black" size="10"></hr>
            <div class="row text-center">
                <div class="col-6 p-1">@{props.author}</div>
                <div class="col-6 p-1">{props.likes}</div>
            </div>
            <div class="row text-center">
                <div class="col-6 p-1 timestamp">{props.timestamp}</div>
                <div class="col-6 p-1">
                    <button id="like_btn_${props.id}" class="red-heart" onClick={Like}>&#9829;</button>
                    </div>
            </div>
        </div>
    );
}