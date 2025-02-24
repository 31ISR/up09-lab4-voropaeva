from django.shortcuts import render, redirect
from .models import Communities
from django.contrib.auth.decorators import login_required

def communities_list(request):
    communities = Communities.objects.all().order_by('-date')
    return render(request, 'communities/communities_list.html', {'communities': communities})

def communities_page(request, slug):
    communities = Communities.objects.get(slug=slug)
    return render(request, 'communities/communities_page.html', {'communities': communities})

from . import forms 

@login_required(login_url="/users/login/")
def communities_new(request):
    if request.method == 'POST': 
        form = forms.CreateCommunities(request.POST, request.FILES) 
        if form.is_valid():
            newcommunities = form.save(commit=False) 
            newcommunities.author = request.user 
            newcommunities.save()
            return redirect('communities:list')
    else:
        form = forms.CreateCommunities()
    return render(request, 'communities/communities_new.html', { 'form': form })