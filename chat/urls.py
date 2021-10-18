from django.urls import path

from chat.views import *


urlpatterns = [
    path('dialogs/', DialogsView.as_view()),
    path('dialogs/create/(<user_id>)/', CreateDialogView.as_view()),
    path('dialogs/(<chat_id>)/', MessagesView.as_view()),
]