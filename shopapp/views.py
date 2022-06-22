from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import *

# Create your views here.
def index(request):
    '''
    Function that renders the landing page
    '''
    return render(request, 'index.html')


def profile(request):
    posts = Product.objects.all()
    current_user = request.user 
    
    if request.method=='POST':
        details_form = DetailsForm(request.POST, request.FILES)
        
        if details_form.is_valid():
            profile = details_form.save(commit=False)
            profile.user = current_user
            profile.save()
            
        return redirect('profile')
        
    else:
        details_form = DetailsForm
        
    return render(request,'profile.html', {'details_form':details_form})


def update_profile(request):
    current_user = request.user
    if request.method== 'POST':
        form = DetailsForm(request.POST, request.FILES)
        if form.is_valid():
            Profile.objects.filter(id=current_user.profile.id).update(bio=form.cleaned_data["bio"])
            profile = Profile.objects.filter(id=current_user.profile.id).first()
            profile.profile_pic.delete()
            profile.profile_pic=form.cleaned_data["profile_pic"]
            profile.save()
        return redirect('profile')
    else:
        form = DetailsForm()
    return render(request, 'update_profile.html', {"form":form})
