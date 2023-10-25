const blogit = document.getElementById("blogit-container")
fetch(`http://127.0.0.1:8000/posts/api/${api_key}?url=${window.location.href}`)
.then((response) => {
    if (response.status === 200) { // Replace with the expected status code
        return response.json(); // If expecting JSON response
    } else {
        throw new Error(`Couldn't fetch your data: ${response.status}`);
    }
})
.then((data) => {
    console.log('Your posts have been loaded');
    console.log('Response data:', data);


    data.forEach(function(parameter){
        let title = parameter.title
        let body = parameter.body
        let image = parameter.image
        let time = String(parameter.time)
        let post_id = parameter.custom_id

        
        const dateComponents = time.match(/(\d{4})-(\d{2})-(\d{2})T(\d{2}):(\d{2}):(\d{2})/);


        const year = parseInt(dateComponents[1]);
        const month = parseInt(dateComponents[2]) - 1;
        const day = parseInt(dateComponents[3]);

        // Create a JavaScript Date object without considering the timezone
        const date = new Date(year, month, day);

        // Format the date as "Month Day, Year"
        const formattedDate = date.toLocaleDateString('en-US', { year: 'numeric', month: 'long', day: 'numeric' });
        

        let post_container = document.createElement('section')


        post_container.className = "post"
        
        if(image){
            post_container.innerHTML = `
            <section class="post-title">
                <h2>${title}</h2>
                </section>
                <section class="post-image">
                    <img src="${image}" alt="Post Image">
                </section>
                <section class="post-date">
                    <p>Posted on: ${date}</p>
                </section>
                <section class="post-content">
                    <article>
                        ${body}
                    </article>
            
            </section>
            `
        }else{
            post_container.innerHTML = `

            <section class="post-title">
                <h2>${title}</h2>
                </section>

                <section class="post-date">
                    <p>Posted on: ${formattedDate}</p>
                </section>

                <section class="post-content">
                    <article>
                        ${body}
                    </article>
            
            </section>

            `
        }

        blogit.appendChild(post_container)
    })

    
})
.catch((error) => {
    console.error(error);
});
