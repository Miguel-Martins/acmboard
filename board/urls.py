from django.urls import path
from .views import EventListView, EventDetailView, EventCreateView
from . import views as board_views
from users import views as user_views
from django.conf.urls import url

urlpatterns = [
    path('', board_views.home, name = 'home'),
    path('events/', EventListView.as_view(), name = 'events'),
    path('profile/', user_views.profile, name = 'profile'),
    path('event/new/', EventCreateView.as_view(), name='event-create'),
    path('event/<int:pk>/', EventDetailView.as_view(), name='event-detail'),
    path('event/<int:pk>/update_event/', board_views.ModalEventEditView.as_view(), name='update_event'),
    path('event/<int:pk>/delete_event/', board_views.ModalEventDeleteView.as_view(), name='delete_event'),
    path('event/<int:pk>/create_task/', board_views.TaskCreateView.as_view(), name='create_task'),
    path('event/<int:pk/delete_task/<int:pk>', board_views.TaskDeleteView.as_view(), name='delete_task'),
]