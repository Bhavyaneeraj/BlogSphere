from django.db import models
from django.utils.text import slugify

class posts(models.Model):
    title=models.CharField(max_length=50)
    excert=models.CharField(null=True,max_length=100)
    date=models.DateTimeField(auto_now=True)
    image=models.ImageField(null=True,upload_to='posts')
    slug=models.SlugField(editable=False,null=True,unique=True,db_index=True)
    description=models.TextField()
    Author_details=models.ForeignKey("Author", on_delete=models.CASCADE,null=True)
    tag=models.ManyToManyField("Tags")
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(posts, self).save(*args, **kwargs)
    def __str__(self):
        return f"{self.title}"


class Author(models.Model):
    first_name=models.CharField(max_length=30)
    last_name=models.CharField(max_length=50)
    email=models.EmailField()
    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
class Tags(models.Model):
    simple_tag=models.CharField( null=True,max_length=100)

    def __str__(self):
        return f"{self.simple_tag}"
    
class CommentsModel(models.Model):
    name=models.CharField(max_length=30)
    comment=models.CharField(max_length=1000)
    post_com=models.ForeignKey("posts",on_delete=models.CASCADE,null=True)

    def __str__(self):
        return f"{self.comment} {self.post_com}"
    
class sign_upModel(models.Model):
     User_name=models.CharField(max_length=30)
     email=models.EmailField()
    

