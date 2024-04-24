from django.contrib import admin
from .models import Post, ContactFormEntry, Comment

# Register your models here.
admin.site.register(Post)
admin.site.register(ContactFormEntry)
admin.site.register(Comment)

