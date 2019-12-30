from django.urls import path
from bharath import views

urlpatterns = [
    path('', views.index,name="index"),
    path('create', views.createpost,name="create"),
    # path('contact', views.contact),
]
