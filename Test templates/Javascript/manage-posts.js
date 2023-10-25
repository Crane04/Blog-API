const blogit = document.getElementById("blogit-container")
const postList = document.querySelector('#manage-post tbody');
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

    number = 0
    data.forEach(function(parameter){
        let title = parameter.title
        let body = parameter.body
        let image = parameter.image
        let time = String(parameter.time)
        let post_id = parameter.custom_id

        number ++
        const dateComponents = time.match(/(\d{4})-(\d{2})-(\d{2})T(\d{2}):(\d{2}):(\d{2})/);


        const year = parseInt(dateComponents[1]);
        const month = parseInt(dateComponents[2]) - 1;
        const day = parseInt(dateComponents[3]);

        const date = new Date(year, month, day);
        const formattedDate = date.toLocaleDateString('en-US', { year: 'numeric', month: 'long', day: 'numeric' });
        
        const time_ = new Date(time);

        // Get the time in "a.m./p.m." format
        const formattedTime = time_.toLocaleTimeString('en-US', { hour: 'numeric', minute: 'numeric', hour12: true });
        
        console.log(formattedTime);


        let post_container = document.createElement('section')
        post_container.className = "post"
        
        const tr = document.createElement('tr');
        
        tr.innerHTML = `
            <td>${number}</td>
            <td>${title}</td>
            <td>${formattedDate}</td>
            <td>${formattedTime}</td>
            <td><button class="set-btn" onclick="editPost(${post_id})">Edit</button></td>
            <td><button class="set-btn" onclick="deletePost(${post_id})">Delete</button></td>
            <td><input type="checkbox" ${parameter.publish ? 'checked' : ''} disabled></td>
            <td><input type="checkbox" ${parameter.featured ? 'checked' : ''} disabled></td>
        `;
        postList.appendChild(tr);

    })

    
})
.catch((error) => {
    console.error(error);
});
