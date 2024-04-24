from django.db import models
from django.contrib.auth.models import User

STATUS = ((0, "Draft"), (1, "Published"))


# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(
    User, on_delete=models.CASCADE, related_name="blog_posts")
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)


class ContactFormEntry(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField()
    subject = models.CharField(max_length=100, blank=True)  # Optional subject field
    message = models.TextField()
    phone_number = models.CharField(max_length=15, blank=True)  # Optional phone number field
    created_at = models.DateTimeField(auto_now_add=True)  # Optional: Timestamp for submission

    def __str__(self):
        return f"{self.name} - {self.email}"  # Customize the string representation of the model instance



