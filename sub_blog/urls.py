from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

from .forms import CustomLoginForm

urlpatterns=[
    path("",views.starting_page,name="starting_page"),
    path("posts/",views.post,name="posts"),
    path("blog_form/",views.blog_form,name="blog_form"),
    path("sign_up",views.signup,name='sign_up'),
    path('logout/', auth_views.LogoutView.as_view(next_page='starting_page'), name='logout'),
    path("about_us/",views.aboutus,name="about_us"),
    path('login/', auth_views.LoginView.as_view(template_name='sub_blog/login.html', authentication_form=CustomLoginForm), name='login'),
    path('search/',views.search_view,name='search'),
    path('Authors_page/<int:post_id>/',views.Authors,name="Authors_page"),
    path('comment/edit/<int:comment_id>/', views.edit_comment, name='edit_comment'),
    path("posts/<slug:slug>",views.post_detail,name="post-detail-page"),
]
