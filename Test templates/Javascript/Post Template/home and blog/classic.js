const bloggit = document.getElementById("bloggit-container")
bloggit.className = "blog-container-1"


bloggit.innerHTML = `    
<div class="blog-post">
<div class="post-content">
  <h2>Post Title 2</h2>
  <p>Your post content goes here. Lorem ipsum dolor sit amet, consectetur adipiscing elit.</p>
</div>
<div class="post-image">
  <img src="C:/Users/Craennie/Desktop/Blog-API/Test templates/Images/human.jpeg" alt="Image 2">
</div>
</div>`


// function processResponseData(data){
    data["posts"].forEach(function(parameter){

        let title = parameter.title
        let body = parameter.body
        let image = parameter.image
        let post_id = parameter.custom_id

        let post_container = document.createElement('section')
        post_container.className = "blog-post"

        if(image){
            console.log(1);
            post_container.innerHTML += `
            <div class="post-content">
                <h2>${title}</h2>
                <p>${strip_tags(body)}</p>
                <date>${convert_datetime(parameter.time)}</date>
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
            </div>
                <div class="post-image">
                
                </div>
            `
            bloggit.appendChild(post_container)
        }
    
    
    })
    var newLink = document.createElement('link');
    // Set the attributes of the link element
    newLink.rel = 'stylesheet';
    newLink.type = 'text/css';
    newLink.href = 'https://maxcdn.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css';
    const bootstrap_js = [
        "https://code.jquery.com/jquery-3.5.1.slim.min.js",
        "https://cdn.jsdelivr.net/npm/@popperjs/core@2.11.6/dist/umd/popper.min.js",
        "https://maxcdn.bootstrapcdn.com/bootstrap/4.5.2/js/bootstrap.min.js",
    ]
    
    
    
    document.head.appendChild(newLink);
    for(let i = 0; i < bootstrap_js.length; i++){
        let script = document.createElement('script');
        script.src = bootstrap_js[i];
        script.type = 'text/javascript';
        document.body.appendChild(script)
    }