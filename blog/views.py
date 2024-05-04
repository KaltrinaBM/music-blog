"""
Views for the blog application, including:

- A list of published blog posts with pagination.
- Detailed view of individual posts with comment handling.
- Contact form handling and success feedback.
- Comment editing and deletion views with user authentication checks.
"""

from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.views import generic
from django.contrib import messages
from django.http import HttpResponseRedirect
from .models import Post, Comment
from .forms import ContactForm, CommentForm


class PostList(generic.ListView):
    """
    Displays a paginated list of published blog posts.
    """
    queryset = Post.objects.filter(status=1)
    template_name = "blog/index.html"
    paginate_by = 3


def post_detail(request, slug):
    """
    Displays an individual blog post and its comments.

    - Retrieves the post by its slug.
    - Handles comment submissions and form validation.
    """
    queryset = Post.objects.filter(status=1)
    post = get_object_or_404(queryset, slug=slug)
    comments = post.comments.all().order_by("-created_on")
    comment_count = post.comments.filter(approved=True).count()

    if request.method == "POST":
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.author = request.user
            comment.post = post
            comment.save()
            messages.success(request, 'Comment submitted and awaiting approval')

    comment_form = CommentForm()

    return render(
        request,
        "blog/post_detail.html",
        {
            "post": post,
            "comments": comments,
            "comment_count": comment_count,
            "comment_form": comment_form,
        },
    )


def contact_us(request):
    """
    Handles contact form submissions.
    """
    if request.method == 'POST':
        form = ContactForm(data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your message has been sent successfully!')
            return redirect('contact_us_success')  # Redirect to the success view
    else:
        form = ContactForm()

    return render(request, 'blog/index.html', {'form': form})


def contact_us_success(request):
    """
    Renders a success page after contact form submission.
    """
    return render(request, 'blog/contact_us_success.html')


def comment_edit(request, slug, comment_id):
    """
    Edits a comment on a specific blog post.

    - Requires authentication and checks if the user is the comment's author.
    - Updates the comment upon valid form submission.
    """
    if request.method == "POST":
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comment = get_object_or_404(Comment, pk=comment_id)
        comment_form = CommentForm(data=request.POST, instance=comment)

        if comment_form.is_valid() and comment.author == request.user:
            comment.save()
            messages.success(request, 'Comment updated!')
        else:
            messages.error(request, 'Error updating comment!')

    return HttpResponseRedirect(reverse('post_detail', args=[slug]))


def comment_delete(request, slug, comment_id):
    """
    Deletes a comment on a specific blog post.

    - Requires authentication and checks if the user is the comment's author.
    - Deletes the comment upon successful validation.
    """
    queryset = Post.objects.filter(status=1)
    post = get_object_or_404(queryset, slug=slug)
    comment = get_object_or_404(Comment, pk=comment_id)

    if comment.author == request.user:
        comment.delete()
        messages.success(request, 'Comment deleted!')
    else:
        messages.error(request, 'You can only delete your own comments!')

    return HttpResponseRedirect(reverse('post_detail', args=[slug]))
