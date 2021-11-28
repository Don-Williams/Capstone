from django.urls import path
from . import views

app_name = 'omnichat_web'

urlpatterns = [
    path('', views.index, name='index'),
    path('options', views.options, name='options'),
    path('logs', views.completions, name='completions'),
    path('send_message', views.send_message, name='send_message'),
    path('send_message_api', views.send_message_api,
         name='send_message_api'),
    path('editor', views.gpt_options, name='gpt_options'),
    path('save_model', views.gpt_options, name='save_gpt_model'),
    path('save_conversation', views.save_conversation, name='save_conversation'),
    path('clear_conversation', views.clear_conversation, name='clear_conversation'),
]
