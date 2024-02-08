def pre_loader(option):
    if option == "veron":
        loader =  veron()
    
    elif option == "loda":
        loader =  loda()
    
    elif option == "growdan":
        loader = growdan()
    
    elif option == "traffic":
        loader =  traffic()
    
    else:
        loader = other()

    loader += """
        bloggit_preloader.innerHTML = preloader
    """

    return loader
    

def veron():
    pre_loader ="""

    preloader = ` <div id="preloader" class="spinner-border text-primary" role="status">
            <span class="sr-only">Loading...</span>
        </div>`"""
    
    return pre_loader

def loda():
    pre_loader = """
        preloader = `<div id="preloader" class="spinner-grow text-success" role="status">
            <span class="sr-only">Loading...</span>
          </div>`
    """
    return pre_loader

def growdan():
    pre_loader = """
        preloader = `<div id="preloader" class="spinner-grow text-danger" role="status">
            <span class="sr-only">Loading...</span>
          </div>`
    """

    return pre_loader

def traffic():
    pre_loader = """
        `<div class="spinner-grow text-danger" role="status">
            <span class="sr-only">Loading...</span>
          </div>
          <div class="spinner-grow text-warning" role="status">
            <span class="sr-only">Loading...</span>
          </div>
          <div class="spinner-grow text-info" role="status">
            <span class="sr-only">Loading...</span>
          </div>`
    """
    return pre_loader

def other():
    pre_loader = "`<p>Loading<p/>`"

    return pre_loader