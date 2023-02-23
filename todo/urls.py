from django.urls import path

from todo.views import todo_home, chat_add,add_todo, update_todo, delete_todo, delete_chats, chats

urlpatterns = [
    
    path('', todo_home, name='todo_home'),
    path('add_todo', add_todo, name="add_todo"),
    path('update/<int:pk>', update_todo, name='update_todo' ),
    path('delete/<int:pk>', delete_todo, name='delete_todo' ),
    path('chat_add', chat_add, name="chat_add"),
    path('chats', chats, name="chats"),
    # path('chat_response', chat_response, name="chat_response"),
    path('delete_chats', delete_chats, name="delete_chats"),
]