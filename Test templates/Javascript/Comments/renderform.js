const comment_form_container = document.getElementById("bloggit-comment-rf")

if(comment_form_container){
    comment_form_container.innerHTML = `
    <div class="container mt-5">
    <h1>Leave a Comment</h1>
    <form>
        <div class="form-group">
            <label for="comment-name">Name:* (required)</label>
            <input type="text" class="form-control" id="comment-name" placeholder="Enter your name" required>
        </div>
        <div class="form-group">
            <label for="comment-email">Email: (not compulsory, and this won't be published)</label>
            <input type="email" class="form-control" id="comment-email" placeholder="Enter your email">
        </div>
        <div class="form-group">
            <label for="comment-comment">Comment:* (required)</label>
            <textarea class="form-control" id="comment-comment" rows="4" placeholder="Enter your comment" required></textarea>
        </div>
        <p id="comment-status"></p>
        <button type="submit" class="btn btn-primary" id="bloggit-submit-comment">Submit</button>
    
    </form>
    </div>
    `    
}else{
    console.log("Comment Form Container not defined!")
}
