from django.shortcuts import render,redirect,HttpResponseRedirect,HttpResponse
from blogapp.models import Newpost
from django.contrib.auth.models import User,auth
from django.views.generic import CreateView
from django.urls import reverse
from .forms import SignupForm
from django.contrib import messages #import messages
# Create your views here.


def home(request) :
    return render(request, "blogapp/index.html")

def viewblog(request) :
    newpostdata=Newpost.objects.all()
    return render(request, "blogapp/viewblog.html",{"newpostdata":newpostdata})

class CreatePost(CreateView):
    model=Newpost
    fields="__all__"
    def get_success_url(self):
        return reverse("blogapp/viewblog")

def signup(request):
    form=SignupForm()
    if request.method=="POST":
        form=SignupForm(request.POST)
        if form.is_valid():
            user=form.save()
            user.set_password(user.password)
            user.save()
            return HttpResponseRedirect("/accounts/login/")
    else:
        form=SignupForm()
    return render(request,"blogapp/signup.html",{"form":form})    


