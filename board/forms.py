from .models import Task, EventCard
from bootstrap_modal_forms.forms import BSModalForm

class TaskForm(BSModalForm):
    class Meta:
        model = Task
        fields = ['description']

class EventCardForm(BSModalForm):
    class Meta:
        model = EventCard
        fields = ['event_name', 'small_description', 'big_description', 'date', 'room']