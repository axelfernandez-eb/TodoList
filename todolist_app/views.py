from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.utils import timezone
from django.views.generic import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Todo


class TodoListView(LoginRequiredMixin, ListView):
    login_url = '/login'
    redirect_field_name = ''

    def get_queryset(self):
        if self.request.user.is_authenticated:
            return Todo.objects.filter(assigned_user=self.request.user)
        return Todo.objects


class TodoCreate(LoginRequiredMixin, CreateView):
    model = Todo
    fields = ['title', 'description', 'done', 'priority']
    success_url = reverse_lazy('todo_list')

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.assigned_user = self.request.user
        self.object.created_by = self.request.user
        self.object.update_by = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('todo_view', args=(self.object.id,))

class TodoUpdateView(LoginRequiredMixin, UpdateView):
    model = Todo
    fields = ['title', 'description', 'done', 'priority']
    success_url = reverse_lazy('todo_list')


class TodoDeleteView(LoginRequiredMixin, DeleteView):
    model = Todo
    success_url = reverse_lazy('todo_list')


class TodoAssigned(LoginRequiredMixin, UpdateView):
    model = Todo
    fields = ['assigned_user']
    success_url = reverse_lazy('todo_list')


class TodoDetailView(LoginRequiredMixin, DetailView):
    model = Todo

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context



