def header(brand_name, links):

    destructure_links = ""

    if links is not None:
        for i in links:
            destructure_links += f"""

                    <li class="nav-item">
                        <a class="nav-link" href="{links[i]}">{i}</a>
                     </li>
    """
            
    header_content = f"""
    bloggit_header.innerHTML = `
    <nav class="navbar navbar-expand-lg navbar-light bg-light">
        <a class="navbar-brand" href="#">{brand_name}</a>
        <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
            <span class="navbar-toggler-icon"></span>
        </button>
         <div class="collapse navbar-collapse" id="navbarNav">
             <ul class="navbar-nav ml-auto">
                {destructure_links}
            </ul>
        </div>
    </nav>`
    """

    return header_content
