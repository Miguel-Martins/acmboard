from django.shortcuts import render,get_object_or_404
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import EventCard, Task

from .forms import TaskForm, EventCardForm
from bootstrap_modal_forms.generic import BSModalCreateView, BSModalUpdateView, BSModalDeleteView
from django.urls import reverse_lazy


@login_required
def home(request):
    events = EventCard.objects.all().filter(users__username=request.user.username)
    tasklist = {}
    for event in events:
        tasklist[event.event_name] = event.task_set.all().filter(
            users__username=request.user.username)
    context = {'events': events, 'tasklist': tasklist}
    return render(request, 'board/home.html', context)


class EventListView(LoginRequiredMixin, ListView):
    model = EventCard
    template_name = 'board/events.html'
    context_object_name = 'events'
    ordering = ['date']


class EventDetailView(LoginRequiredMixin, DetailView):
    model = EventCard


class EventCreateView(LoginRequiredMixin, CreateView):
    model = EventCard
    fields = ['event_name', 'small_description',
              'big_description', 'date', 'room']

    def form_valid(self, form):
        self.object = form.save()
        self.object.users.add(self.request.user)
        self.object.save()
        return super().form_valid(form)




class TaskCreateView(BSModalCreateView):
    template_name = 'board/create_task.html'
    form_class = TaskForm
    success_url = reverse_lazy('events')

    def form_valid(self, form):
        self.object = form.save()
        self.object.users.add(self.request.user)
        event=get_object_or_404(EventCard, pk=self.kwargs['pk'])
        print(self.kwargs['pk'])
        self.object.event = event
        self.object.save()
        return super().form_valid(form)

class TaskDeleteView(BSModalDeleteView):
    model = Task
    template_name = 'board/delete_task.html'
    success_message = 'Success: Task was deleted.'
    success_url = reverse_lazy('events')

class ModalEventEditView(LoginRequiredMixin, BSModalUpdateView):
    model = EventCard
    template_name = 'board/update-event.html'
    form_class = EventCardForm
    success_url = reverse_lazy('events')

class ModalEventDeleteView(BSModalDeleteView):
    model = EventCard
    template_name = 'board/delete_event.html'
    success_message = 'Success: Event was deleted.'
    success_url = reverse_lazy('events')
