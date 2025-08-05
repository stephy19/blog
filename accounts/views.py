from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect
from accounts.forms import RegistrationForm
from django.contrib.auth.decorators import login_required
from accounts.forms import UserEditForm, ProfileEditForm
from accounts.models import Profile
# Create your views here.

def login_view(request):
 if not request.user.is_authenticated:
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('blogapp:post_list')
        else:
            return render(request, 'registrations/login.html', {'error': 'Nom d\'utilisateur ou mot de passe incorrect.'})
    else:
         return render(request, 'registrations/login.html')
 else:
     return redirect('blogapp:post_list')
 
def logout_view(request):
    logout(request)
    return redirect('blogapp:post_list')


def register_view(request):
    if request.method == 'POST':
        user_form = RegistrationForm(request.POST, request.FILES)
        if user_form.is_valid() :
           new_user = user_form.save(commit=False)
           new_user.set_password(user_form.cleaned_data['password'])
           new_user.save()
           Profile.objects.create(user=new_user) #creation de la clé de connexion user pour le profil
           return redirect('accounts:login')
        else:
         return render(request, 'registrations/register.html', {'user_form': user_form})
    else:
        user_form = RegistrationForm()
        context = {
             'user_form': user_form,
            }
    return render(request, 'registrations/register.html',context)


@login_required
def dashboard_view(request):
    user = Profile.objects.filter(user=request.user).first()
    form = ProfileEditForm(instance=user)
    if request.method == 'POST':
        form = ProfileEditForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.save()
        return redirect('accounts:dashboard')
    return render(request, 'registrations/profile/dashboard.html',{'user': user , 'form': form})
    
    
@login_required
def edit_profile(request):
    if request.method == 'POST':
        user_form = UserEditForm(instance=request.user, data=request.POST)
        # profile_form = ProfileEditForm(instance=request.user , data=request.POST,files=request.FILES)
        if user_form.is_valid() :
            user_form.save()
            # profile_form.save()
            return redirect('accounts:dashboard')
    else:
        user_form = UserEditForm(instance=request.user)
        # profile_form = ProfileEditForm(instance=request.user)
        
    return render(request, 'registrations/profile/edit.html',{'user_form': user_form})

       
        
    