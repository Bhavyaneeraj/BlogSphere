from django.contrib import admin

# Register your models here.


from .models import posts,Author,Tags,CommentsModel,sign_upModel


admin.site.register(Author)
admin.site.register(Tags)
admin.site.register(CommentsModel)

class PostsAdmin(admin.ModelAdmin):
    list_display = ['title', 'date', 'Author_details']
    search_fields = ['title', 'description']
    filter_horizontal = ('tag',)
admin.site.register(posts, PostsAdmin)
admin.site.register(sign_upModel)