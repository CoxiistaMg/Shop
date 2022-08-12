from pipes import Template
from django.http import HttpResponse, Http404, HttpResponseBadRequest
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from .forms import UserForm
from django.contrib.auth.views import LoginView
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_str
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from .tokens import account_activation_token
from django.contrib.auth.models import User
from django.core.mail import EmailMessage
from django.contrib.auth import get_user_model
from .token_generator import BadToken , ExpiredToken , validate_token
from django.views import View
from .models import User


def logoutQ(request):
    if request.user.is_authenticated:
        backup = request.session['carrinho']
        logout(request)
        request.session['carrinho'] = backup
        request.session.modificad = True
        return redirect('index')
    
    raise Http404()


class Login(LoginView):
    template_name = 'login.html'
    redirect_authenticated_user = True
    

def createlogin(request):  
    if request.method == 'POST':  
        form = UserForm(request.POST)  
        if form.is_valid():  
            # save form in the memory not in database  
            user = form.save(commit=False)  
            user.is_active = False  
            user.save()  
            # to get the domain of the current site  
            current_site = get_current_site(request)  

            mail_subject = 'Confirme o registro em nosso site'  
            message = render_to_string('verificacao.html', {  
                'user': user,  
                'domain': current_site.domain,  
                'uid':urlsafe_base64_encode(force_bytes(user.pk)),  
                'token':account_activation_token.make_token(user),  
            })  
            to_email = form.cleaned_data.get('email')  
            email = EmailMessage(  
                        mail_subject, message, to=[to_email]  
            ) 
            email.fail_silently=False
            email.content_subtype = "html"
            email.send()  
            return HttpResponse('Please confirm your email address to complete the registration')  
    else:  
        form = UserForm()  
    return render(request, 'create_user.html', {'form': form})  


def activate(request, uidb64, token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        login(request, user)
        # return redirect('home')
        return HttpResponse('Thank you for your email confirmation. Now you can login your account.')
    else:
        return HttpResponse('Activation link is invalid!')


class VerificarEmail(View):
    def get(self, request):
        UserModel = get_user_model()
        token = request.GET['token']

        if not token:
            return  HttpResponseBadRequest('Error')
        
        try:
            user_id = validate_token(token)
        
        except BadToken:
            return HttpResponseBadRequest('Error')
        
        except ExpiredToken:
            return HttpResponseBadRequest('Error')
        
        user = User.objects.get(pk=user_id)

        if user.email_verified:
            return HttpResponseBadRequest('Error')
        
        user.is_activate = True
        user.save()
        return HttpResponse('Your account has been activated')


