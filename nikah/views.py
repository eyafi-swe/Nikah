from django.shortcuts import render,redirect
from nikah.forms import postForm
from nikah.models import post
from accounts.models import userProfile
from accounts.forms import userProfileForm
from django.contrib import messages 
from notifications.signals import notify
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
# Create your views here.
def index(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        return render(request,'index.htm')
@login_required
def home(request):
    form = postForm()
    
    if request.method == "POST":
        form = postForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.author = request.user
            obj.save()
            messages.success(request,"প্রকাশিত হয়েছে")
            return redirect('home')
    posts = post.objects.all()
    return render(request,'home.htm',{'form':form,'posts':posts})
@login_required
def profile(request):
    user = request.user
    
    return render(request,'profile.htm',{'user':user})

@login_required
def deletePost(request, id):
    post.objects.get(id=id).delete()
    return redirect('profile')
@login_required
def interest(request, id):
    Post = post.objects.get(id=id)
    notify.send(request.user, recipient = Post.author,  verb="আগ্রহ প্রকাশ করেছেন ।"+ f''' <a href="/accounts/otherprofile/{request.user.username}/">See profile</a>''' )
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
@login_required
def notification(request):
    return render(request,'notifications.htm')

