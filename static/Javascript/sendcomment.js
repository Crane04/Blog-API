const submit_comment_btn = document.getElementById("bloggit-submit-comment")
const comment_container = document.getElementById("bloggit-comment-container")

if(submit_comment_btn){
submit_comment_btn.addEventListener("click", function(e){

    e.preventDefault()
    submit_comment_btn.disabled = true
    submit_comment_btn.style.cursor = "not-allowed"
    let comment = document.getElementById("comment-comment")
    let comment_name = document.getElementById("comment-name")
    let comment_email = document.getElementById("comment-email")
    let comment_time = convert_datetime(new Date().toLocaleString());
    
    if(!comment.value|| !comment_name.value){
        document.getElementById("comment-status").innerText = 'Name or Comment fields can\'t be empty!'
        setTimeout(() => {
            document.getElementById("comment-status").innerText = ''
        }, 4000);
        submit_comment_btn.disabled = false
        submit_comment_btn.style.cursor = "pointer"
        return
    }
    data = {
        "comment": comment.value,
        "name": comment_name.value,
        "email":  (!comment_email.value) ? "anonymous@gmail.com" : comment_email.value,
        "time": comment_time
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

            
            if(comment_container){
                const c_cont_inner = document.querySelector("#bloggit-comment-container #comments")
                c_cont_inner.innerHTML =  `
                <div class="card mb-3">
                    <div class="card-body">
                        <h3 class="card-title">${comment_name.value}</h3>
                        <time>${comment_time}</time>
                        <article class="card-text">${comment.value}</article>
                    </div>
                </div>

            ` + c_cont_inner.innerHTML
            }

            comment.value = comment_email.value = comment_name.value = ""

            document.getElementById("comment-status").innerText = 'Your comment has been added!'
            setTimeout(() => {
                document.getElementById("comment-status").innerText = ''
            }, 4000);

            if(data["comment_rf"]){
                
            }
        }
        submit_comment_btn.disabled = false
        submit_comment_btn.style.cursor = "pointer"
        return response.json();

    })
    .then(data => {
    })
    .catch(error => {
        console.error(error);
    });
})
}
