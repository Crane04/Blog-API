// Variables
const title = document.getElementById("title"),
content = document.getElementById("content"),
image = document.getElementById("image"),
publish = document.getElementById("publish"),
featured = document.getElementById("featured"),
postBtn = document.getElementById("make-post")
   
   
postBtn.addEventListener("click", function (e) {
    e.preventDefault();

    // Define the API endpoint URL and data
    const apiUrl = 'http://127.0.0.1:8000/posts/api/' + api_key; // Replace with your API endpoint
    console.log(getCode())
    const data = new FormData();
    data.append('title', title.value);
    data.append('body', getCode());
    data.append('publish', publish.checked);
    data.append('featured', featured.checked);
    if(image.files[0]){
        data.append('image', image.files[0]);
    }else{
        data.append('image', "");
    }
    
   
   
    // Define request options
    const requestOptions = {
        method: 'POST',
        body: data,
        headers:{
            "Authorization": "Token " + api_key
        }
    };
   
       // Send the POST request
    fetch(apiUrl, requestOptions, )
    .then((response) => {
        if (response.status === 201) { // Replace with the expected status code
            return response.json(); // If expecting JSON response
        } else {
            throw new Error(`POST request failed with status: ${response.status}`);
        }
    })
    .then((data) => {
        console.log('POST request was successful');
        console.log('Response data:', data);
        // title.value = image.files = ""
        // featured.checked = publish.checked = false
        // $('#summernote').summernote('code') = ""
    })
    .catch((error) => {
        console.error(error);
    });
});