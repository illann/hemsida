from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.core.context_processors import csrf
from forms import UserProfileForm
from forms import CategorySelectionForm
from django.contrib.auth.decorators import login_required

@login_required
def user_profile(request):
    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=request.user.profile)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/accounts/profile')
    else:
        user = request.user
        profile = user.profile
        form = UserProfileForm(instance=profile)
        
    args = {}
    args.update(csrf(request))
    
    args['form'] = form
    args['full_name'] = request.user.username
    
    return render_to_response('profile.html', args)   
	
@login_required
def category_selection(request):
    if request.method == 'POST':
        form = CategorySelectionForm(request.POST, instance=request.user.profile)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/accounts/category_selection')
    else:
        user = request.user
        profile = user.profile
        form = CategorySelectionForm(instance=profile)
        
    args = {}
    args.update(csrf(request))
    
    args['form'] = form
    
    return render_to_response('category_selection.html', args)   