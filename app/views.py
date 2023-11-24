from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.urls import reverse
from django.views import View
from api.models import Post
from django.contrib import messages
from userprofile.models import Token
from app.models import UserSites
import uuid

# Create your views here.

class AdminPageView(View):
    
    def get(self, request, **kwargs):

        context = {
            "posts":  Post.objects.filter(creator = request.user)
        }
        return render(request, "admin.html", context=context)

    def post(self, request, **kwargs):
        # Define the collected data
        if "submitpost" in request.POST:
            title = request.POST["title"]
            content = request.POST.get("content", "")
            category = request.POST["category"]
            if not content.strip() or content is None or content == None or content.strip() is None or content.strip() == '<p><br></p>':
                messages.info(request, 'Summernote editor is empty')
                return redirect("/dashboard/admin")

            if "publish" in request.POST:
                publish = True
            else:
                publish = False


            create_post = Post.objects.create(
                creator = request.user,
                title = title,
                body= content,
                publish = publish,
                categories = category
            )

            if request.FILES:
                image = request.FILES["image"]
                create_post.image = image
            create_post.save()

            messages.info(request, "You've successfully created this Post!")

            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
        elif "deletePost" in request.POST:
            post_id = request.POST["delete_id"]
            post_ = get_object_or_404(Post, custom_id = post_id, creator = request.user)
            post_.delete()
            messages.info(request, "You've successfully deleted this Post!")

            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
        else:
            messages.info(request, "Couldn't complete this action!")

class PostEditView(View):

    def get(self, request, post_id, **kwargs):

        post_ = get_object_or_404(Post, custom_id = post_id, creator = request.user)
        context = {
            "post": post_
        }
        return render(request, "edit-post.html", context)

    def post(self, request, post_id, **kwargs):
        if "submitpost" in request.POST:
            post_ = get_object_or_404(Post, custom_id = post_id, creator = request.user)

            post_.title = request.POST["title"]
            content = request.POST.get("content", "")
            category = request.POST["category"]

            if not content.strip() or content is None or content == None or content.strip() is None or content.strip() == '<p><br></p>':
                messages.info(request, 'Summernote editor is empty')
                return redirect("/dashboard/admin")

            post_.body = content

            if "publish" in request.POST:

                publish = True
            else:
                publish = False



            post_.publish = publish
            post_.categories = category

            if request.FILES:
                image = request.FILES["image"]
                post_.image = image
            post_.save()

            messages.info(request, "You've successfully updated this Post!")

            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
        
        elif "deletepost" in request.POST:
            post_ = get_object_or_404(Post, custom_id = post_id, creator = request.user)
            post_.delete()

            messages.info(request, "You've successfully deleted this Post!")
            return redirect("/dashboard/admin")
        else:
            messages.info(request, "Couldn't complete this action!")


class DocumentationView(View):
    template_name = "documentation.html"

    def get(self, request, *args, **kwargs):

        return render(request, self.template_name)

class ApiPageView(View):

    template_name = "api.html"

    def get(self, request, *args, **kwargs):
        token, create_token = Token.objects.get_or_create(user = request.user)
        try:
            user_sites = get_object_or_404(UserSites, user = request.user)
        except:
            user_sites = []
        if token:
            user_api_key = token.key
        elif token is None:
            user_api_key = create_token.key
        else:
            user_api_key = "Not Availabe for now!"

        context = {
            "api_key": user_api_key,
            "user_sites": user_sites
        }

        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        
        try:
            if request.method == "POST":
                if "update-sites" in request.POST:

                    blogPage = request.POST["blogPage"]
                    individualPostPage = request.POST["individualPostPage"]

                    sites = get_object_or_404(UserSites, user = request.user)

                    sites.blog_page = blogPage.replace("\\", "/")
                    sites.individual_blog_post = individualPostPage.replace("\\", "/")

                    sites.save()

                    messages.success(request, "Your site url's have been sucessfully updated!")
                    return redirect("/dashboard/api")

                elif "reset-api-key" in request.POST:
                    token = Token.objects.get(user = request.user)
                    token.key = str(uuid.uuid4()).replace("-","")
                    token.save()

                    messages.success(request, "Your API Key has been updated successfully!")
                    return redirect("/dashboard/api")

                else:
                    messages.error(request, "Could not complete your request")
                    return redirect("/dashboard/api")


        except:
            messages.error(request, "Couldn't update your site urls!")
            return redirect("/dashboard/api")

class AboutDevPage(View):
    template_name = "about-me.html"

    def get(self, request, *args, **kwargs):

        return render(request, self.template_name)