from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm, CustomAuthenticationForm
from django.contrib.auth import login as auth_login
#from .models import User # user를 불러오는데 아래 코드가 더 좋다 why?
# from .models import User
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required

# Create your views here.
def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('posts:index')
    else:
        form = CustomUserCreationForm()

    context = {
        'form': form,
    }

    return render(request, 'accounts/form.html', context)


def login(request):
    if request.method == 'POST':
        form = CustomAuthenticationForm(request, request.POST) # request.POST -> id/pw 정보
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)
            return redirect('posts:index')

    else:
        form = CustomAuthenticationForm()

    context = {
        'form': form,
    }

    return render(request, 'accounts/form.html', context)


def profile(request, username):
    User = get_user_model()

    user_info = User.objects.get(username=username)

    context = {
        'user_info': user_info,
    }

    return render(request, 'accounts/profile.html', context)

@login_required
def follow(request, username):
    User = get_user_model() # get_user_model()로 user를 불러와서 User에 넣는다.
    
    me = request.user # 지금 로그인한 사람
    you = User.objects.get(username=username)

    # 팔로잉이 이미 되어있는 경우
    # if me in you.follows.all():
    if you in me.following.all():
        me.following.remove(you)

    # 팔로일이 아직 안되어 있는 경우
    else:
        me.following.add(you)

    return redirect('accounts:profile', username=username)