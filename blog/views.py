from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import Post
from .forms import ContactForm

# Create your views here.

class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1)
    template_name = "blog/index.html"
    paginate_by = 6


def post_detail(request, slug):
    """
    Display an individual :model:`blog.Post`.

    **Context**

    ``post``
        An instance of :model:`blog.Post`.

    **Template:**

    :template:`blog/post_detail.html`
    """

    queryset = Post.objects.filter(status=1)
    post = get_object_or_404(queryset, slug=slug)

    return render(
        request,
        "blog/post_detail.html",
        {"post": post},
    )


def contact(request):
  if request.method == 'POST':
    # Handle form submission
    form = ContactForm(request.POST)
    if form.is_valid():
      # Process form data (e.g., send email)
      name = form.cleaned_data['name']
      email = form.cleaned_data['email']
      message = form.cleaned_data['message']
      # Your logic to process the data (e.g., send email)
      # ...
      # After processing, redirect to a success page
      return HttpResponseRedirect('/success/')
  else:
    # Display the form
    form = ContactForm()
  return render(request, 'contact_form.html', {'form': form})
