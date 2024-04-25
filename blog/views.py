from django.shortcuts import render
from django.views import generic
from .models import Post
from .forms import ContactForm

# Create your views here.

class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1)
    template_name = "blog/index.html"
    paginate_by = 6

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
