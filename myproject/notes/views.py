# notes/views.py

from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.messages.views import SuccessMessageMixin
from django.core.paginator import Paginator
from .models import Note
from .forms import NoteForm

class NoteListView(LoginRequiredMixin, ListView):
    model = Note
    paginate_by = 10

    def get_queryset(self):
        return Note.objects.filter(author=self.request.user).order_by('-created_at')

class NoteDetailView(LoginRequiredMixin, DetailView):
    model = Note

    def get_queryset(self):
        return Note.objects.filter(author=self.request.user)

class NoteCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Note
    form_class = NoteForm
    success_url = reverse_lazy('note_list')
    success_message = "Note created successfully."

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class NoteUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Note
    form_class = NoteForm
    success_url = reverse_lazy('note_list')
    success_message = "Note updated successfully."

    def get_queryset(self):
        return Note.objects.filter(author=self.request.user)

class NoteDeleteView(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    model = Note
    success_url = reverse_lazy('note_list')
    success_message = "Note deleted successfully."

    def get_queryset(self):
        return Note.objects.filter(author=self.request.user)

