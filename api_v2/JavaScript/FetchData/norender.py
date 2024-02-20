def no_render(token):

    no_render_txt = """
            fetch(`http://127.0.0.1:8000/v2/main?location=${current_url}&id=${post_id}`,
        {
        "headers": {
        """
    no_render_txt += f"""
        "Authorization": "Token {token}"
        """
    
    no_render_txt+="""
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
    })
            
    .catch((error) =>{
        console.log(error)
    })

        """
    
    return no_render_txt