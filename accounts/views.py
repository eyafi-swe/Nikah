from django.shortcuts import render,redirect,HttpResponse
from django.contrib import messages 
from django.contrib.auth.models import User 
from django.contrib.auth  import authenticate, login, logout
from django.contrib.auth.decorators import login_required
# Create your views here.
def createAccount(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        username = request.POST['username']
        password = request.POST['password']
        
        if name == "" or email == "" or username == "" or password == "":
            messages.error(request, "ভ্যালিড তথ্য দিন")
            return redirect('createAccount')
        if User.objects.filter(email=email).exists():
            messages.error(request, "এই ইমেইল পূর্বে ব্যবহৃত হয়েছে")
            return redirect('createAccount')
        if User.objects.filter(username=username).exists():
            messages.error(request, "এই ইউজারনেইম পূর্বে ব্যবহৃত হয়েছে")
            return redirect('createAccount')
        if " " in username:
            messages.error(request,"ইউজারনেইমে স্পেস ব্যবহার করা যাবে না")
            return redirect('createAccount')
        else:
            first_name = name.split()[0]
            last_name = name.split()[1]
            user = User.objects.create_user(username=username,first_name=first_name,last_name=last_name,email=email,password=password)
            user.save()
            messages.success(request, "অ্যাকাউন্ট খোলা সফল হয়েছে")
            return redirect('createAccount')
    else:
        return render(request,'register.htm')


def log_in(request):
    if request.method == "POST":
        loginUsername = request.POST['loginUsername']
        loginPassword = request.POST['loginPassword']
        user = authenticate(username = loginUsername, password = loginPassword)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request,"ইউজার নেইম অথবা পাসওয়ার্ড ভুল")
            return redirect('login')
    else:
        return render(request,'login.htm')

@login_required
def log_out(request):
    logout(request)
    return redirect('/')



from .models import userProfile
from .forms import userProfileForm

@login_required
def editProfile(request):
    try:
        instance= userProfile.objects.get(user=request.user)
    except userProfile.DoesNotExist:

        instance=None
    
    if request.method == "POST":
        if instance:
            form = userProfileForm(request.POST, request.FILES, instance = instance)
        else:
            form = userProfileForm(request.POST, request.FILES)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.user = request.user
            obj.save()
            
            return redirect('profile')
    
    else:
        form = userProfileForm(instance=instance)
    
    context = {
        'form':form
    }
    return render(request,'editProfile.htm',context)

@login_required
def otherprofile(request,username):
    user = User.objects.get(username=username)
    return render(request,'otherprofile.htm',{'user':user})
