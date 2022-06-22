from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import *

# Create your views here.
def index(request):
    products = Product.objects.all()
    
    try:
        products = products[::-1]
        
    except Product.DoesNotExist:
        hoods  = None

    return render(request, 'index.html', {'hoods':hoods})


def profile(request):
    # posts = Product.objects.all()
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

def search_product(request):
    if 'product' in request.GET and request.GET["product"]:
        search_term = request.GET.get("product")
        searched_products = Product.search_by_name(search_term)
        message = f"{search_term}"
        
        return render(request, 'search.html', {"message":message, "products":searched_products})
    
    else:
        message = "You haven't searched for any term"
        return render(request, 'search.html', {"message":message})
