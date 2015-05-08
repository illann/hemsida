from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.contrib import auth
from django.core.context_processors import csrf
#from forms import MyRegistrationForm
from django.contrib.auth.decorators import login_required

from django.contrib.auth.forms import AdminPasswordChangeForm
from django.views.decorators.debug import sensitive_post_parameters
from django.views.decorators.csrf import csrf_protect
from django.core.urlresolvers import reverse
from django.template.response import TemplateResponse


#EP. 9 users login and logout
def login(request):
    c = {}
    c.update(csrf(request))    
    return render_to_response('login.html', c)
    
def auth_view(request):
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')
    user = auth.authenticate(username=username, password=password)
	#Main check function above, password and username is passed into the function
	#If it finds a match it will return a user object
    
    if user is not None:
        auth.login(request, user)
        return HttpResponseRedirect('/accounts/profile')
    else:
        return HttpResponseRedirect('/accounts/invalid')
    
@login_required	
def profile(request):
	return render_to_response('loggedin.html', 
							{'full_name': request.user.username})
@login_required
def invalid_login(request):
    return render_to_response('invalid_login.html')

@login_required	
def logout(request):
	auth.logout(request)
	c = {}
	c.update(csrf(request)) 
	return render_to_response('login.html', c)
	
@login_required	
def contact(request):
	return render_to_response('contact.html')
	
	
@sensitive_post_parameters()
@csrf_protect
@login_required
def password_change(request,
                    template_name='change_password.html',
                    post_change_redirect=None,
                    password_change_form=AdminPasswordChangeForm,
                    current_app=None, extra_context=None):
    if post_change_redirect is None:
        post_change_redirect = reverse('profile')
    else:
        post_change_redirect = resolve_url(post_change_redirect)
    if request.method == "POST":
        form = password_change_form(user=request.user, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(post_change_redirect)
    else:
        form = password_change_form(user=request.user)
    context = {
        'form': form,
    }
    if extra_context is not None:
        context.update(extra_context)
    return TemplateResponse(request, template_name, context,
                            current_app=current_app)
	
@login_required
def password_change_done(request,
                         template_name='password_change_done.html',
                         current_app=None, extra_context=None):
    context = {}
    if extra_context is not None:
        context.update(extra_context)
    return TemplateResponse(request, template_name, context,
                            current_app=current_app)
	
	