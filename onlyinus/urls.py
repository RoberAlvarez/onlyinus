from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('feedback.urls')),
]
handler404 = 'feedback.views.custom_page_not_found'