from .classic import classic
from .slimyvue import slimy_vue
from .norender import no_render

def fetch_data(token, type):

    if type == "classic":
        return classic(token)
    
    elif type == "slimyvue":
        return slimy_vue(token)
    
    elif type == "no_render":
        return no_render(token)
    
    return classic(token)
    
    

