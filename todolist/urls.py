from django.urls import path
from todolist.views import register
from todolist.views import login_user
from todolist.views import logout_user
from todolist.views import show_todolist
from todolist.views import create_task
from todolist.views import delete_task
from todolist.views import update_task
from todolist.views import show_todolist_json
from todolist.views import create_task_modal
from todolist.views import delete_task_ajax

app_name = 'todolist'

urlpatterns = [
    path('', show_todolist, name='show_todolist'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('create-task/', create_task, name='create-task'),
    path('delete-task/<int:id>/', delete_task, name='delete-task'),
    path('update-task/<int:id>/', update_task, name='update-task'),
    path('json/', show_todolist_json, name='show-todolist-json'),
    path('add/', create_task_modal, name='create-task-modal'),
    path('delete/<int:id>/', delete_task_ajax, name='delete-task-ajax'),
]
