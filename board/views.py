from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import EventCard, Task

@login_required
def home(request):
    events = EventCard.objects.all().filter(users__username=request.user.username)
    tasklist = {}
    for event in events:
        tasklist[event.event_name] = event.task_set.all().filter(users__username=request.user.username) 
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
    fields = ['event_name', 'small_description', 'big_description', 'date', 'room']

    def form_valid(self, form):
        self.object = form.save()
        self.object.users.add(self.request.user)
        self.object.save()
        return super().form_valid(form)

class EventUpdateView(LoginRequiredMixin, UpdateView):
    model = EventCard
    fields = ['event_name', 'small_description', 'big_description', 'date', 'room']

    def form_valid(self, form):
        self.object = form.save()
        self.object.users.add(self.request.user)
        self.object.save()
        return super().form_valid(form)

class EventDeleteView(LoginRequiredMixin, DeleteView):
    model = EventCard
    success_url = '/home/events'