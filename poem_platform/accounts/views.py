from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .forms import CustomUserCreationForm, PoemForm, ProfileForm
from .models import Poem, Comment, Like, CustomUser, Profile
from django.contrib.auth.decorators import login_required

def home(request):
    recent_poems = Poem.objects.all().order_by('-created_at')[:10]
    liked_poems = list(request.user.liked_poems.values_list('id', flat=True))
    if request.user.is_authenticated:
        liked_poems = list(request.user.liked_poems.values_list('id', flat=True))
    context = {
        'recent_poems': recent_poems,
        'liked_poems': liked_poems,
    }
    return render(request, 'poem/home.html', context)

def profile_detail(request, username):
    user = get_object_or_404(CustomUser, username=username)
    
    try:
        profile = user.profile 
    except Profile.DoesNotExist:
        profile = None
    
    poems = Poem.objects.filter(author=user)
    
    context = {
        'profile': profile,
        'user': user,
        'poems': poems,
    }
    
    return render(request, 'poem/profile_detail.html', context)

@login_required
def create_poem(request):
    if request.method == 'POST':
        form = PoemForm(request.POST)
        if form.is_valid():
            poem = form.save(commit=False)
            poem.author = request.user
            poem.save()
            form.save_m2m()  # Save many-to-many relations
            return redirect('poem_detail', pk=poem.pk)
    else:
        form = PoemForm()
    return render(request, 'poem/create_poem.html', {'form': form})

def poem_detail(request, pk):
    poem = get_object_or_404(Poem, pk=pk)
    comments = Comment.objects.filter(poem=poem)
    liked = poem.likes.filter(id=request.user.id).exists() if request.user.is_authenticated else False
    context = {'poem': poem, 'comments': comments, 'liked': liked}
    if request.method == 'POST':
        content = request.POST.get('content')
        if content:
            Comment.objects.create(poem=poem, author=request.user, content=content)
            messages.success(request, 'Comment added successfully.')
            return redirect('poem_detail', pk=pk)
    return render(request, 'poem/poem_detail.html', context)

@login_required
def like_poem(request, pk):
    poem = get_object_or_404(Poem, pk=pk)
    if request.user in poem.likes.all():
        poem.likes.remove(request.user)
        messages.success(request, 'Unliked the poem.')
    else:
        poem.likes.add(request.user)
        messages.success(request, 'Liked the poem.')
    return redirect('poem_detail', pk=pk)

@login_required
def add_comment(request, pk):
    poem = get_object_or_404(Poem, pk=pk)
    if request.method == 'POST':
        content = request.POST.get('content')
        if content:
            Comment.objects.create(poem=poem, author=request.user, content=content)
            messages.success(request, 'Comment added successfully.')
        else:
            messages.error(request, 'Comment content is required.')
    return redirect('poem_detail', pk=pk)

def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account created successfully.')
            return redirect('login')
    else:
        form = CustomUserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})

@login_required
def edit_profile(request):
    profile = request.user.profile
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully.')
            return redirect('profile_detail', username=request.user.username)
    else:
        form = ProfileForm(instance=profile)
    return render(request, 'registration/edit_profile.html', {'form': form})

def poem_search(request):
    query = request.GET.get('q')
    if query:
        poems = Poem.objects.filter(title__icontains=query) | \
            Poem.objects.filter(author__username__icontains=query) | \
            Poem.objects.filter(categories__name__icontains=query) | \
            Poem.objects.filter(tags__name__icontains=query)
    else:
        poems = Poem.objects.all()
    return render(request, 'poem/poem_search.html', {'poems': poems, 'query': query})

def edit_poem(request, pk):
    poem = get_object_or_404(Poem, pk=pk)
    if request.method == 'POST':
        form = PoemForm(request.POST, instance=poem)
        if form.is_valid():
            form.save()
            messages.success(request, 'Poem updated successfully.')
            return redirect('poem_detail', pk=poem.pk)
    else:
        form = PoemForm(instance=poem)
    
    context = {'form': form, 'poem': poem}
    return render(request, 'poem/edit_poem.html', context)