function Post(props) {
    return (
        <div>
            <div class="row">
                <div class="col-12 p-1 text-center"><strong>{props.title}:</strong></div>
            </div>
            <div class="row text-center">
                <div class="col-12 p-1">{props.body}</div>
            </div>
            <div class="row text-center">
                <div class="col-6 p-1">{props.author}</div>
                <div class="col-6 p-1">{props.likes}</div>
            </div>
            <div class="row text-center">
                <div class="col-6 p-1">{props.timestamp}</div>
                <div class="col-6 p-1"><button class="red-heart">&#9829;</button></div>
            </div>
        </div>
    );
}