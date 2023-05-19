from django.shortcuts import render, redirect
from .models import Post, User
from django.contrib.auth import authenticate, login, logout
from .forms import CustomAuthenticationForm
from .forms import RegistrationForm


def handler404(request, exception):
    return render(request, '404.html', status=404)


def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            # Create new user
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            User.objects.create_user(username=username, email=email, password=password)
            return redirect('login')
    else:
        form = RegistrationForm()
    return render(request, 'blog/register.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = CustomAuthenticationForm(data=request.POST)
        if form.is_valid():
            # Authenticate the user
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)

            # Log the user in if authentication succeeds
            if user is not None:
                login(request, user)
                return redirect('home')
    else:
        form = CustomAuthenticationForm()
    return render(request, 'blog/login.html', {'form': form})


def logout_view(request):
    if not request.user.is_authenticated:
        return render(request, 'blog/404.html')
    logout(request)
    return redirect('home')


def home(request):
    posts = Post.objects.order_by('-created_date')[:4]
    return render(request, 'blog/home.html', {'posts': posts})


def all_posts(request):
    posts = Post.objects.order_by('-created_date')
    return render(request, 'blog/all_posts.html', {'posts': posts})


# @login_required
def add_post(request):
    if not request.user.is_authenticated:
        return render(request, 'blog/404.html')
    if request.method == 'POST':
        post = Post(title=request.POST['title'], content=request.POST['content'], author=request.user)
        post.save()
        return redirect('home')
    return render(request, 'blog/add_post.html')


def user_count(request):
    count = User.objects.all().count()
    return render(request, 'blog/user_count.html', {'count': count})
