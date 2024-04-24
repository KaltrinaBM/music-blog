from django.shortcuts import render
from django.http import HttpResponse
from .forms import ContactForm

# Create your views here.
def home_blog(request):

    if request.method == "POST":
        return HttpResponse("You must have POSTed something")
    else:
        return HttpResponse(request.method)


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
