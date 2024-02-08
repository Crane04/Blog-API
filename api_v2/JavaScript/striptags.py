def strip_tags():

    strip_tags_funtion = """
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
"""

    return strip_tags_funtion
