from django.shortcuts import render,redirect
from django.core.exceptions import ObjectDoesNotExist
# Create your views here.
def home(request):

         

    return render(request,'index.html')





def profile(request):
    current_user = request.user
    business = Business.objects.filter(business_owner = current_user)
    posts = Post.objects.filter(post_owner = current_user)
    try:   
        prof = Profile.objects.get(prof_user=current_user)
    except ObjectDoesNotExist:
        return redirect('new_profile')

    return render(request,'profile.html',{'profile':prof,'business':business,'posts':posts})


def new_profile(request):
    current_user = request.user
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.prof_user = current_user
            profile.profile_Id = request.user.id
            profile.save()
        return redirect('profile')
    else:
        form = ProfileForm()
    return render(request, 'new_profile.html', {"form": form})    
