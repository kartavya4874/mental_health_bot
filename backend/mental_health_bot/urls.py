# Project URLs including chatbot and user APIs
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/chat/', include('chatbot.urls')),
    path('api/auth/', include('users.urls')),
    path('', TemplateView.as_view(template_name='chat.html')),
]

