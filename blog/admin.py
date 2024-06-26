from django.contrib import admin
from .models import Post, ContactFormEntry, Comment
from django_summernote.admin import SummernoteModelAdmin


#Admin class for managing Post objects.
@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):

    list_display = ('title', 'slug', 'status', 'created_on')
    search_fields = ['title', 'content']
    list_filter = ('status', 'created_on',)
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('content',)


#Admin class for managing ContactFormEntry objects.
@admin.register(ContactFormEntry)
class ContactFormEntryAdmin(SummernoteModelAdmin):
    list_display = ('name', 'email', 'subject', 'message', 'phone_number')
    summernote_fields = ('message',)


admin.site.register(Comment)
