from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.contrib import auth
from django.core.context_processors import csrf
#from forms import MyRegistrationForm
from django.contrib.auth.decorators import login_required


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
	return render_to_response('profile.html', 
							{'full_name': request.user.username})
@login_required
def invalid_login(request):
    return render_to_response('invalid_login.html')

@login_required	
def logout(request):
    auth.logout(request)
    return render_to_response('logout.html')
	
	
	
"""	
#EP. 10 user registration basics	
def register_user(request):
    if request.method == 'POST':
        form = MyRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/accounts/register_success')
        
    args = {}
    args.update(csrf(request))
    
    args['form'] = MyRegistrationForm()
    
    return render_to_response('register.html', args)
	
def register_success(request):
    return render_to_response('register_success.html')

"""