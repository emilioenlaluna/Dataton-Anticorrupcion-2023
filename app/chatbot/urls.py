from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("seleccionar", views.seleccionar, name="seleccionar"),
    path("chat", views.chat, name="chat"),
    path("chatbot_sistema1", views.chatbot_sistema1, name="chatbot_sistema1"),
    path("chatbot_sistema2", views.chatbot_sistema2, name="chatbot_sistema2"),
    path("chatbot_sistema3", views.chatbot_sistema3, name="chatbot_sistema3"),

path('chatbot_api/', views.chatbot_api, name='chatbot_api'),

]