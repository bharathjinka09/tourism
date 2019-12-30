from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Post, Contact
from django.contrib import messages
from .forms import ContactForm

# Create your views here.


def index(request):
    form = ContactForm(request.POST or None)

    if form.is_valid():
        form.save()
        messages.success(request,"Message sent successfully!")
        form = ContactForm()

    context = {
        'form':form
    }
    return render(request,"index.html",context)

def createpost(request):
    if request.method == 'POST':
        if request.POST.get('title') and request.POST.get('content'):
            post = Post()
            post.title = request.POST.get('title')
            post.content = request.POST.get('content')
            post.save()

            return render(request, 'create.html')

    else:
        return render(request, 'create.html')


# def contact(request):
#     if request.method == 'POST':
#         if request.POST.get('name') and request.POST.get('phone') and request.POST.get('email') and request.POST.get('message'):
#             contact = Contact()
#             contact.name = request.POST.get('name')
#             contact.phone = request.POST.get('phone')
#             contact.email = request.POST.get('email')
#             contact.message = request.POST.get('message')
#             contact.save()

#             return render(request, 'contact.html')

#     else:
#         return render(request, 'contact.html')
