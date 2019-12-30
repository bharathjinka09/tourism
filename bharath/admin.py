from django.contrib import admin
from .models import Post, Contact
# Register your models here.


class ContactAdmin(admin.ModelAdmin):
    # model = Contact
    list_display = ('name', 'email', 'phone', 'message')


admin.site.register(Post)
admin.site.register(Contact)
