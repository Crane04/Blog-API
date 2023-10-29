// Define Variables
let current_url = window.location.href
let api_key = bloggit_conf.api_key
let cont_rend = bloggit_conf.cont_rend
fetch(`http://127.0.0.1:8000/posts/api/${api_key}?url=${current_url}&cont_rend=${cont_rend}`)
    .then((response) => {
        if (response.status === 200) { // Replace with the expected status code
            return response.json(); // If expecting JSON response
        } else {
            throw new Error(`Couldn't fetch your data: ${response.status}`);
        }
    })
    .then((data) => {
        let response_data = data

        console.log('Your posts have been loaded');
        console.log('Response data:', data);

        var newLink = document.createElement('link');

        // Set the attributes of the link element
        newLink.rel = 'stylesheet';
        newLink.type = 'text/css';
        newLink.href = './CSS/slimy-vue.css';
        document.head.appendChild(newLink);

        // var newScript = document.createElement('script');
        // newScript.src = 'C:/Users/Craennie/Desktop/Blog-API/Test templates/Javascript/slimy-vue.js';
        // newScript.onload = function() {
        //     console.log('Script has been loaded.');
        //     processResponseData(response_data);
        // };

        // document.head.appendChild(newScript);
        const jsCodeString = data["script"].join('\n');

        // Execute the JavaScript code
        eval(jsCodeString);
        // processResponseData()

    })
    .catch((error) => {
        console.error(error);
    });
