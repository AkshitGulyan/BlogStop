from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.core.mail import send_mail
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes, force_text
from .tokens import generate_token


from blogstop import settings

def home(request):
    return render(request, 'authentication/index.html')

def signup(request):

    if request.method == 'POST':
        username = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']

        if User.objects.filter(username=username):
            messages.error(request, 'Username already in use')
            return redirect('signup')
        
        if User.objects.filter(email=email):
            messages.error(request, 'E-Mail already registered')
            return redirect('signup')
        
        if pass1!=pass2:
            messages.error(request,"Passwords didn't match")
            return redirect('signup')
        
        if not username.isalnum():
            messages.error(request, 'Username should be alphanueric in nature')
            return redirect('signup')
        

        
        myuser = User.objects.create_user(username, email, pass1)
        myuser.first_name = fname
        myuser.last_name = lname
        myuser.isactive = False
        myuser.save()

        messages.success(request, "Your account has been successfully created!")

        #welcome mail
        subject = 'Welcome to BlogStop'
        message = "Hello "+ myuser.first_name + "!, It's nice to have you\n Thanks for registering with us!" 
        from_email = settings.EMAIL_HOST_USER
        to_list = [myuser.email]
        send_mail(subject, message, from_email, to_list, fail_silently= True)

        #confirmation mail
        current_site = get_current_site(request)
        email_subject = 'Activate Your Account for BlogStop'
        email_message = render_to_string('email_confirmation.html', {
            'name' = myuser.first_name,
            'domain' = current_site.domain,
            'uid' = urlsafe_base64_encode(force_bytes(myuser.pk)),
            'token' = generate_token.make_token(myuser)
        })



        return redirect('signin')


    return render(request, 'authentication/signup.html')

def signin(request):
    if request.method == "POST":
        username = request.POST['username']
        pass1 = request.POST['pass1']
        user = authenticate(username=username, password=pass1) 
        if user is not None:
            login(request, user)
            fname = user.first_name
            return render(request, "authentication/index.html", {'fname' : fname})

        else:
            messages.error(request, "Wrong Credentials")
            return redirect('home')


    
    return render(request, 'authentication/signin.html')

def signout(request):
    logout(request)
    messages.success(request, "You're successfully logged out")
    return redirect('home')
