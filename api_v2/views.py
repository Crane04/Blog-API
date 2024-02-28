from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from rest_framework.authtoken.models import Token
from app.models import UserConfig, UserSites, UserScript
from django.contrib import messages
from .utils import generate_script
import json
class DocumentationViewV2(View):
    template_name = "v2/documentation2.html"

    def get(self, request, *args, **kwargs):

        return render(request, self.template_name)


class ApiPageView(View):

    template_name = "v2/api.html"

    def get(self, request, *args, **kwargs):
        token, create_token = Token.objects.get_or_create(user = request.user)
        user_config, create = UserConfig.objects.get_or_create(user = request.user)
        try:
            user_sites = get_object_or_404(UserSites, user = request.user)
        except:
            user_sites = []
        if token:
            user_api_key = token.key
        elif token is None:
            user_api_key = create_token.key
        else:
            user_api_key = "Not Available for now!"


        rc_options = ["slimy-vue", "classic"]
        pl_options = ["veron", "loda", "growdan", "traffic"]
        context = {
            "api_key": user_api_key,
            "user_sites": user_sites, 
            "config": user_config,
            "rc_options": rc_options,
            "pl_options": pl_options,
            "links": json.dumps(user_config.header_links)
        }

        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        
        # try:
        if request.method == "POST":
            if "update-sites" in request.POST:

                blogPage = request.POST["blogPage"]
                individualPostPage = request.POST["individualPostPage"]

                sites = get_object_or_404(UserSites, user = request.user)

                sites.blog_page = blogPage.replace("\\", "/")
                sites.individual_blog_post = individualPostPage.replace("\\", "/")

                sites.save()

                messages.success(request, "Your site url's have been sucessfully updated!")
                return redirect("/v2/api-v2")

            elif "reset-api-key" in request.POST:
                token = Token.objects.get(user = request.user)
                token.delete()

                new_token = Token.objects.create(user = request.user)
                new_token.save()


                messages.success(request, "Your API Key has been updated successfully!")
                return redirect("/v2/api-v2")
            
            elif "site-config" in request.POST:
                have_header = request.POST.get("have_nav", False)
                brand_name = request.POST.get("brand_name", "")
                nav_bar_links = json.loads(request.POST["links"])
                p_loader = request.POST.get("preloader", "")
                cont_rend = request.POST.get("render_content", "")
                if(have_header == "on"):
                    have_header = True
                
                user_config, created = UserConfig.objects.get_or_create(user = request.user)
                user_config.brand_name = brand_name
                user_config.preloader = p_loader
                user_config.cont_rend = cont_rend
                user_config.have_header = have_header
                user_config.header_links = nav_bar_links

                user_config.save()

                generate_script(request)

                return redirect("/v2/api-v2")
            


            else:
                messages.error(request, "Could not complete your request")
                
                return redirect("/v2/api-v2")
            



        # except:
        #     messages.error(request, "Couldn't complete your request")
        #     return redirect("/v2/api-v2")
            