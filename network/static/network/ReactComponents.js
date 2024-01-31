function Post(props) {
    return (
        <div>
            <div class="row">
                <div class="col-3 p-1"><strong>{props.title}:</strong></div>
                <div class="col-9 p-1">{props.body}</div>
            </div>
            <div class="row">
                <div class="col-3 p-1"><strong>{props.author}:</strong></div>
                <div class="col-9 p-1">{props.timestamp}</div>
            </div>
            <div class="row">
                <div class="col-3 p-1"><strong>{props.likes}:</strong></div>
                <div class="col-9 p-1"><button>Like</button></div>
            </div>
        </div>
    );
}