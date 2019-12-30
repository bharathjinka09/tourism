from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('bharath.urls'))
]

admin.site.site_header = 'Tourism Admin Panel'                    # default: "Django Administration"
admin.site.index_title = 'Tourism'                 # default: "Site administration"
admin.site.site_title = 'Tourism Admin Panel' # default: "Django site admin"
