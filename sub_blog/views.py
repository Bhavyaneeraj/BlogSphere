from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.db.models import Q

from django.urls import reverse
from django.shortcuts import get_object_or_404

from .models import posts,CommentsModel,sign_upModel
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm

from .forms import BlogForm,AuthorDetailForm,CommentForm,CustomUserCreationForm
def starting_page(request):
    info=posts.objects.all().order_by("-date")[:3]
    return render(request,"sub_blog/index.html", {'posts':info})
@login_required
def post(request):
    all_posts=posts.objects.all()
    return render(request,"sub_blog/allposts.html",{'posts':all_posts})

def post_detail(request, slug):
    single_post = posts.objects.get(slug=slug)
    comments = CommentsModel.objects.filter(post_com=single_post)

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post_com = single_post 
            comment.save()
            return HttpResponseRedirect(reverse('starting_page'))
    else:
        form = CommentForm()

    return render(request, "sub_blog/post-detail.html", {
        'single_post': single_post,
        'form': form,
        'comments': comments,
    })


def blog_form(request):
    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES)
        if form.is_valid():
            post_instance=form.save()
            return HttpResponseRedirect(reverse('Authors_page', kwargs={'post_id': post_instance.id}))
        form = BlogForm()
    else:
        form=BlogForm()

    return render(request, 'sub_blog/blog_form.html', {'form': form})

def Authors(request,post_id):
    if request.method=='POST':
        form=AuthorDetailForm(request.POST,request.FILES)
        if form.is_valid():
            author_instance=form.save()
            post_instance = posts.objects.get(id=post_id)
            post_instance.Author_details=author_instance
            post_instance.save()
            return HttpResponseRedirect(reverse('starting_page'))
    AuthorForm=AuthorDetailForm()
    return render(request,'sub_blog/Author_details.html',{'form':AuthorForm})


def edit_comment(request, comment_id):
    comment = get_object_or_404(CommentsModel, id=comment_id)  
    
    if request.method == 'POST':
        form = CommentForm(request.POST, instance=comment)  
        if form.is_valid():
            form.save() 
            return HttpResponseRedirect(reverse('post_detail', args=[comment.post_com.slug])) 
    else:
        form = CommentForm(instance=comment)

    return render(request, 'sub_blog/edit_comment.html', {'form': form, 'comment': comment})

def aboutus(request):
    return render(request,"sub_blog/about_us.html")

def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            sign_upModel.objects.create(
                User_name=user,
                email=form.cleaned_data.get('email'),
            )
            login(request, user)  
            return HttpResponseRedirect(reverse('starting_page'))  
    else:
        form = CustomUserCreationForm()
    return render(request, 'sub_blog/signup.html', {'form': form})

def search_view(request):
    query=request.GET.get('query')
    if query:
        results = posts.objects.filter(
            Q(title__icontains=query) |
            Q(description__icontains=query) |
            Q(tag__simple_tag__icontains=query)  # Use 'simple_tag' for the related Tag model
        ).distinct()
    else:
        results = posts.objects.none()
    return render(request,'sub_blog/search_detail.html',{'results':results})

