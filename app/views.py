from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.urls import reverse
from django.views import View
from api.models import Post
from django.contrib import messages
from userprofile.models import Token
from app.models import UserSites

# Create your views here.

class AdminPageView(View):
    
    def get(self, request, **kwargs):

        context = {
            "posts": Post.objects.all() #get_object_or_404(Post, creator = request.user)
        }
        return render(request, "admin.html", context=context)

    def post(self, request, **kwargs):
        # Define the collected data

        title = request.POST["title"]
        content = request.POST["content"]
        # if content is None or content == None or content.strip() is None or content.strip() == '<p><br></p>':
        #     messages.info(request, 'Summernote editor is empty')
        #     # return redirect("/dashboard/admin")


        if "publish" in request.POST:
            publish = True
        else:
            publish = False

        if "featured" in request.POST:
            featured = True
        else:
            featured = False

        create_post = Post.objects.create(
            creator = request.user,
            title = title,
            body= content,
            publish = publish,
            featured = featured
        )

        if request.FILES:
            image = request.FILES["image"]
            create_post.image = image
        create_post.save()

        messages.info(request, "You've successfully created this Post!")

        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


class PostEditView(View):

    def get(self, request, post_id, **kwargs):

        post_ = get_object_or_404(Post, custom_id = post_id, creator = request.user)
        context = {
            "post": post_
        }
        return render(request, "edit-post.html", context)

    def post(self, request, post_id, **kwargs):
    
        post_ = get_object_or_404(Post, custom_id = post_id, creator = request.user)

        post_.title = request.POST["title"]
        post_.body = request.POST["content"]
        # if content is None or content == None or content.strip() is None or content.strip() == '<p><br></p>':
        #     messages.info(request, 'Summernote editor is empty')
        #     # return redirect("/dashboard/admin")


        if "publish" in request.POST:

            publish = True
        else:
            publish = False

        if "featured" in request.POST:
            featured = True
        else:
            featured = False

        post_.publish = publish
        post_.featured = featured

        if request.FILES:
            image = request.FILES["image"]
            post_.image = image
        post_.save()

        messages.info(request, "You've successfully updated this Post!")

        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


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
                print(0)
                homePage = request.POST["homePage"]
                print(1)
                blogPage = request.POST["blogPage"]
                individualPostPage = request.POST["individualPostPage"]

                sites = get_object_or_404(UserSites, user = request.user)

                sites.home_page = homePage
                sites.blog_page = blogPage
                sites.individual_blog_post = individualPostPage

                sites.save()

                messages.success(request, "Your site url's have been sucessfully updated!")
                return redirect("/dashboard/api")

        except:
            messages.error(request, "Couldn't update your site urls!")
            return redirect("/dashboard/api")

def rest(request):
    if request.method == "POST":
        print(0)
        homePage = request.POST["homePage"]
        print(1)
        blogPage = request.POST["blogPage"]
        individualPostPage = request.POST["individualPostPage"]

        sites = get_object_or_404(UserSites, user = request.user)

        sites.home_page = homePage
        sites.blog_page = blogPage
        sites.individual_blog_post = individualPostPage

        sites.save()
        print(1)
        return JsonResponse({
            "Success": "Edited successfully"
        })
