from django.contrib import admin
from .models import EventCard, Task, Attachment, Board
# Register your models here.

admin.site.register(EventCard)
admin.site.register(Task)
admin.site.register(Attachment)
admin.site.register(Board)