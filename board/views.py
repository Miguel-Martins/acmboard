from django.shortcuts import render,get_object_or_404, redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import EventCard, Task, Board, Attachment

from .forms import TaskForm, EventCardForm, EventJoinForm, TaskJoinForm
from bootstrap_modal_forms.generic import BSModalCreateView, BSModalUpdateView, BSModalDeleteView


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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['boards'] = Board.objects.all()
        return context

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

class JoinEventView(LoginRequiredMixin, BSModalUpdateView):
    model = EventCard
    template_name = 'board/confirm.html'
    form_class = EventJoinForm
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        if not form.instance.users.all().filter(pk = self.request.user.id):
            form.instance.users.add(self.request.user)
        return super().form_valid(form)

class LeaveEventView(LoginRequiredMixin, BSModalUpdateView):
    model = EventCard
    template_name = 'board/confirm.html'
    form_class = EventJoinForm
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        if form.instance.users.all().filter(pk = self.request.user.id):
            tasks = form.instance.task_set.all().filter(pk = form.instance.id)
            for task in tasks:
                task.users.remove(self.request.user.id)
            form.instance.users.remove(self.request.user)
        form.instance.save()
        return super().form_valid(form)

class JoinTaskView(LoginRequiredMixin, BSModalUpdateView):
    model = Task
    template_name = 'board/confirm.html'
    form_class = TaskJoinForm
    submitBtn = ".join-task"
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        if not form.instance.users.all().filter(pk = self.request.user.id):
            form.instance.event.users.add(self.request.user)
            form.instance.users.add(self.request.user)
        form.instance.save()
        return super().form_valid(form)

class LeaveTaskView(LoginRequiredMixin, BSModalUpdateView):
    model = Task
    template_name = 'board/confirm.html'
    form_class = TaskJoinForm
    submitBtn = ".leave-task"
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        if form.instance.users.all().filter(pk = self.request.user.id):
            form.instance.isCompleted = True
            form.instance.users.remove(self.request.user)
            form.instance.save()
        return super().form_valid(form)

class BoardCreateView(LoginRequiredMixin, CreateView):
    model = Board
    fields = ['name', 'image']
    
    success_url=reverse_lazy('home')

class AddEventToBoard(LoginRequiredMixin, UpdateView):
    model = EventCard
    template_name='board/add_event_board.html'
    fields=[]
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form.instance.board = get_object_or_404(Board,pk=self.kwargs['board'])
        return super().form_valid(form)

class CreateAttachment(LoginRequiredMixin, CreateView):
    model = Attachment
    fields=['file']
    template_name = 'board/create_attachment.html'
    success_url = reverse_lazy('events')

    def form_valid(self, form):
        form.instance.event = get_object_or_404(EventCard, pk=self.kwargs['pk'])
        return super().form_valid(form)
