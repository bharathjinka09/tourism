from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Post, Contact
from django.contrib import messages

# Create your views here.


def index(request):
    if request.method == 'POST':
        if request.POST.get('name') and request.POST.get('phone') and request.POST.get('email') and request.POST.get('message'):
            if form.is_valid():
                messages.success(request, 'Form submission successful')
            contact = Contact()
            contact.name = request.POST.get('name')
            contact.phone = request.POST.get('phone')
            contact.email = request.POST.get('email')
            contact.message = request.POST.get('message')
            contact.save()

            return render(request, 'index.html')

    else:
        return render(request, 'index.html')


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
