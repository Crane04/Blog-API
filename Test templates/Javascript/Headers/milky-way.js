const bloggit_header = document.getElementById("bloggit-header")
if(bloggit_conf["header"] && bloggit_header){
// console.log(bloggit_conf);

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


bloggit_header.innerHTML = `
<nav class="navbar navbar-expand-lg navbar-light bg-light" id="brand-name">
</nav>
`
const brand_name = document.getElementById("brand-name")
const brand_name_a = document.createElement("a")
brand_name_a.href = "/"
brand_name_a.className = "navbar-brand"
brand_name_a.innerText = "Mayowa"

brand_name.append(brand_name_a)

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
    Object.keys(bloggit_conf.header.links).forEach(key => {
        ul_bloggit.innerHTML += `
            <li class="nav-item">
                <a class="nav-link" href="${bloggit_conf.header.links[key]}">${key}</a>
            </li>
        `
    });
}