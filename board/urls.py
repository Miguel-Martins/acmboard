from django.urls import path
from .views import EventListView, EventDetailView, EventCreateView, EventUpdateView, EventDeleteView
from . import views as board_views
from users import views as user_views
from django.conf.urls import url

urlpatterns = [
    path('', board_views.home, name = 'home'),
    path('events/', EventListView.as_view(), name = 'events'),
    path('profile/', user_views.profile, name = 'profile'),
    path('event/new/', EventCreateView.as_view(), name='event-create'),
    path('event/<pk>/update', EventUpdateView.as_view(), name='event-update'),
    path('event/<pk>/', EventDetailView.as_view(), name='event-detail'),
    path('event/<pk>/delete', EventDeleteView.as_view(), name='event-delete'),
]