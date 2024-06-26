from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

STATUS = ((0, "Draft"), (1, "Published"))


class Post(models.Model):
    """
    Represents a blog post with title, slug, author, content, and other attributes.

    - The status field indicates whether the post is a draft or published.
    - The author field links to the Django User model.
    - The featured_image field uses Cloudinary to manage image uploads.
    - Meta ordering sorts posts by creation date in descending order.
    """
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="blog_posts")
    featured_image = CloudinaryField('image', default='placeholder')
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    excerpt = models.TextField(blank=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return f"{self.title} | written by {self.author}"


class ContactFormEntry(models.Model):

    """
    Stores submissions from the contact form.

    - Includes fields for name, email, subject, message, and phone number.
    - The 'read' field indicates if the submission has been processed.
    - Meta ordering is based on the creation timestamp.
    """

    name = models.CharField(max_length=30)
    email = models.EmailField()
    subject = models.CharField(max_length=100, blank=True)
    message = models.TextField()
    phone_number = models.CharField(max_length=15, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    read = models.BooleanField(default=False)

    def __str__(self):
        return f"Name: {self.name}\nEmail: {self.email}\nSubject: {self.subject}"


class Comment(models.Model):
    """
    Represents a comment on a blog post.

    - Links to the Post model via a foreign key.
    - The author field references the Django User model.
    - Includes a 'body' field for the comment content.
    - The 'approved' field indicates if the comment is approved for publication.
    """
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name="comments")
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="commenter")
    body = models.TextField()
    approved = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["created_on"]

    def __str__(self):
        return f"Comment {self.body} by {self.author}"
