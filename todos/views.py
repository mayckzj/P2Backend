from django.views.generic import ListView
from .models import Todo
from django.urls import reverse_lazy



class TodoListView(ListView):
    model = Todo