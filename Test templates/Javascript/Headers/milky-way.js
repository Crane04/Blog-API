const bloggit_header = document.getElementById("bloggit-header")
if(bloggit_conf["header"] && bloggit_header){


bloggit_header.innerHTML = `
<nav class="navbar navbar-expand-lg navbar-light bg-light" id="brand-name">
</nav>
`
const brand_name = document.getElementById("brand-name")
const brand_name_a = document.createElement("a")
brand_name_a.href = data["home_page"]
brand_name_a.className = "navbar-brand"
if(bloggit_conf["header"]["brand_name"]){
    brand_name_a.innerText = bloggit_conf["header"]["brand_name"]
    brand_name.append(brand_name_a)
}

brand_name.innerHTML += `
    <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
        <span class="navbar-toggler-icon"></span>
    </button>
    <div class="collapse navbar-collapse" id="navbarNav">
        <ul class="navbar-nav ml-auto" id="ul_bloggit">

        </ul>
    </div>
`
const ul_bloggit = document.getElementById("ul_bloggit")

if(bloggit_conf["header"]["links"]){
    Object.keys(bloggit_conf.header.links).forEach(key => {
        ul_bloggit.innerHTML += `
            <li class="nav-item">
                <a class="nav-link" href="${bloggit_conf.header.links[key]}">${key}</a>
            </li>
        `
    });
}
}