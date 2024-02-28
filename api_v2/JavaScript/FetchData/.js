let bloggit_data = null 

    const current_url = window.location.href 

    const url_parameters = window.location.search; 

    const post_id = new URLSearchParams(url_parameters).get("id");

    const bloggit_header = document.getElementById("bloggit-header") 
const bloggit_preloader = document.getElementById("bloggit-preloader") 
const bloggit = document.getElementById("bloggit-container")

/* Added Code */
const comment_container = document.getElementById("bloggit-comment-container")
bloggit_preloader.style.cssText = `
  position: fixed;
  width: 100vw;
  height: 100vh;
  z-index: 1000;
  display: flex;
  align-items: center;
  justify-content: center;
  background-color: transparent;
`;
/* end*/
    bloggit_header.innerHTML = `
    <nav class="navbar navbar-expand-lg navbar-light bg-light">
        <a class="navbar-brand" href="#">Crane</a>
        <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
            <span class="navbar-toggler-icon"></span>
        </button>
         <div class="collapse navbar-collapse" id="navbarNav">
             <ul class="navbar-nav ml-auto">
                

                    <li class="nav-item">
                        <a class="nav-link" href="b">a</a>
                     </li>
    
            </ul>
        </div>
    </nav>`
    
        preloader = ` <div class="spinner-grow text-danger" role="status">
            <span class="sr-only">Loading...</span>
          </div>
          <div class="spinner-grow text-warning" role="status">
            <span class="sr-only">Loading...</span>
          </div>
          <div class="spinner-grow text-info" role="status">
            <span class="sr-only">Loading...</span>
          </div>`
    
        bloggit_preloader.innerHTML = preloader
    
        function convert_datetime(param){
        try{
        
            const dateComponents = param.match(/(\d{4})-(\d{2})-(\d{2})T(\d{2}):(\d{2}):(\d{2})/);

            const year = parseInt(dateComponents[1]);
            const month = parseInt(dateComponents[2]) - 1;
            const day = parseInt(dateComponents[3]);

            // Create a JavaScript Date object without considering the timezone
            const date = new Date(year, month, day);

            const time = new Date(param);

            // Get the hours, minutes, and seconds
            const hours = time.getHours();
            const minutes = time.getMinutes();
            const seconds = time.getSeconds();

            let __time__ = `${hours}:${minutes}:${seconds}`;

            // Format the date as "Month Day, Year"
            return   date.toLocaleDateString('en-US', { year: 'numeric', month: 'long', day: 'numeric' }).toString() + " ; " + __time__;
        }catch(error){
            return param
        }

        }
        function render_comment_form(){
            const comment_form_container = document.getElementById("bloggit-comment-rf")

            if(comment_form_container){
                comment_form_container.innerHTML = `
                <div class="container mt-5">
                <h1>Leave a Comment</h1>
                    <div class="form-group">
                        <label for="comment-name">Name:* (required)</label>
                        <input type="text" class="form-control" id="comment-name" placeholder="Enter your name" >
                    </div>
                    <div class="form-group">
                        <label for="comment-email">Email: (not compulsory, and this won't be published)</label>
                        <input type="email" class="form-control" id="comment-email" placeholder="Enter your email">
                    </div>
                    <div class="form-group">
                        <label for="comment-comment">Comment:* (required)</label>
                        <textarea class="form-control" id="comment-comment" rows="4" placeholder="Enter your comment"></textarea>
                    </div>
                    <p id="comment-status"></p>
                    <button class="btn btn-primary" id="submit-comment" onclick = "BloggitSendComment()">Submit</button>
                    <br /> <br/>
               
                </div>
                `    
            }else{
                console.log("Comment Form Container not defined!")
            }
        }

        function render_comments(data){
            if (comment_container){
                comment_container.classList += "container mt4"
            
                if (comment_container){
                    comment_container.innerHTML = `<h2>Comments</h2>
                    <div id="comments" class="mt-4">
            
                    </div>
                    `
                    const c_cont_inner = document.querySelector("#bloggit-comment-container #comments")
                    if(data["comments"] != [] || data["comments"]){
                        data["comments"].forEach(function(parameter){
                            let name = parameter.name
                            let comment = parameter.comment
                            let time = convert_datetime(parameter.time) 
                
                            c_cont_inner.innerHTML += `
                            <!-- Comments Display -->
                            
                                <!-- Comments will be displayed here -->
                                <div class="card mb-3">
                                    <div class="card-body">
                                        <h3 class="card-title">${name}</h3>
                                        <article class="card-text">${comment}</article>
                                        <time>${time}</time>
                                    </div>
                                </div>
                
                            `
                        })
                    }
                }
            }else{
                console.log('Comment Container not defined')
            }

        }

        function strip_tags(param){
            let post_body = document.createElement("p")
            post_body.innerHTML = param
            let elements_to_remove = post_body.querySelectorAll("table", "img", "iframe", "audio", "video", "picture", "figure", "canvas")

            elements_to_remove.forEach(function(element) {
                element.remove();
            });
            var words = post_body.innerText.split(/\s+/);

            // Select the first 120 words
            return words.slice(0, 30).join(' ');
        }

            fetch(`http://127.0.0.1:8000/v2/main?location=${current_url}&id=${post_id}`,
        {
        "headers": {
        
        "Authorization": "Token 420a3f9dbc5eaf8dfe3b5c22ea2f630385a9f4cc"
        
    }
        }
    )
    .then((response) => {
        if (response.status === 200) { // Replace with the expected status code
            return response.json(); // If expecting JSON response
        }
        else if(response.status === 404){
            return response.json()
        }
        else {
            throw new Error(`Couldn't fetch your data: ${response.data}`);
        }
    })
    .then((data) => {
    bloggit_data = data
        
    if(data["type"] === "all" && data["detail"] === "okay"){
    data["posts"].forEach(function(parameter){

        let title = parameter.title
        let body = parameter.body
        let image = parameter.image
        let post_id = parameter.custom_id
        let comments = parameter.comment_count

        let post_container = document.createElement('section')
        post_container.className = "blog-post"

        if(image){

            post_container.innerHTML += `
            <div class="post-content">
                <h2>${title}</h2>
                <p>${strip_tags(body)}</p>
                <date>${convert_datetime(parameter.time)}</date>
                <div>${comments} Comments</div>
                <div class="read-more">
                    <a href="${data["ind"]}?id=${post_id}">Read More</a>
                </div>
            </div>
            <div class="post-image">
                <img src="http://127.0.0.1:8000${image}" alt="${title}">
            </div>
            `
            bloggit.appendChild(post_container)
        }else{
            post_container.innerHTML += `
            <div class="post-content">
                <h2>${title}</h2>
                <p>${strip_tags(body)}</p>
                <date>${convert_datetime(parameter.time)}</date>
                <div>${comments} Comments</div>
                <div class="read-more">
                    <a href="${data["ind"]}?id=${post_id}">Read More</a>
                </div>
            </div>
                <div class="post-image">
                
                </div>
            `
            bloggit.appendChild(post_container)
        }
    
    })
    }else if(data["type"] == "one"){
        bloggit.className = "container mt-4"
        post = data["post"]

        bloggit.innerHTML+=`<h1> ${post.title}</h1>`
        if(post.image){
            bloggit.innerHTML += `<img src="http://127.0.0.1:8000${post.image }" class="img-fluid" alt="Image for the post">`
        }
        bloggit.innerHTML += `
            <p>${convert_datetime(post.time)}</p>
            <div class="mt-4">
            ${post.body}
            </div>`

        render_comments(data)
        render_comment_form()            
    }
        try{
            bloggit_preloader.style.display = "none"
        }catch(error){
        
        }
})
            
    .catch((error) =>{
        console.log(error)
    })


    
        function BloggitSendComment(){
        
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
            fetch("http://127.0.0.1:8000/commentv2/"  + new URLSearchParams(url_parameters).get("id"), {
                body: JSON.stringify(data),
                method: "POST",
                headers: {
                    'Content-Type': "application/json",
                    "Authorization": `Token 420a3f9dbc5eaf8dfe3b5c22ea2f630385a9f4cc`
                }
            })
            .then(response => {
                if(response.status == '201'){
                    const datetime = new Date()
                    const date = datetime.toLocaleDateString().replaceAll("/", "-") + " " + datetime.toLocaleTimeString()
                    document.getElementById("comment-status").innerText = 'Your comment has been added!'
                    setTimeout(() => {
                        document.getElementById("comment-status").innerText = ''
                    }, 4000);
        
                    if(document.querySelector("#bloggit-comment-container #comments")){
                        const c_cont_inner = document.querySelector("#bloggit-comment-container #comments")
                        c_cont_inner.innerHTML += `
                        <!-- Comments Display -->
                        
                            <!-- Comments will be displayed here -->
                            <div class="card mb-3">
                                <div class="card-body">
                                    <h3 class="card-title">${comment_name.value}</h3>
                                    <article class="card-text">${comment.value}</article>
                                    <time>${date}</time>
                                </div>
                            </div>
            
                        `
                    }
                    comment.value = comment_email.value = comment_name.value = ""
                }
                return response.json();
        
            })
            .then(data => {
                if(data["email"]){
                    document.getElementById("comment-status").innerText = data["email"][0]
                    setTimeout(() => {
                        document.getElementById("comment-status").innerText = ''
                    }, 4000);
                }
            })
            .catch(error => {
                console.error(error);
            });
        }