const submit_comment_btn = document.getElementById("bloggit-submit-comment")

if(submit_comment_btn){
submit_comment_btn.addEventListener("click", function(e){

    e.preventDefault()
    let comment = document.getElementById("comment-comment")
    let comment_name = document.getElementById("comment-name")
    let comment_email = document.getElementById("comment-email")
    
    if(!comment.value|| !comment_name.value){
        document.getElementById("comment-status").innerText = 'Name or Comment fields can\'t be empty!'
        setTimeout(() => {
            document.getElementById("comment-status").innerText = ''
        }, 4000);

        return
    }
    data = {
        "comment": comment.value,
        "name": comment_name.value,
        "email": comment_email.value
    }
    fetch("http://127.0.0.1:8000/comment/" + api_key + "/" + new URLSearchParams(url_parameters).get("id"), {
        body: JSON.stringify(data),
        method: "POST",
        headers: {
            'Content-Type': "application/json"
        }
    })
    .then(response => {
        if(response.status == '201'){
            comment.value = comment_email.value = comment_name.value = ""

            document.getElementById("comment-status").innerText = 'Your comment has been added!'
            setTimeout(() => {
                document.getElementById("comment-status").innerText = ''
            }, 4000);

            if(data["comment_rf"]){
                
            }
        }
        return response.json();

    })
    .then(data => {
    })
    .catch(error => {
        console.error(error);
    });
})
}
