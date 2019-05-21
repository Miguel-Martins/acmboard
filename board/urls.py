from django.urls import path
from .views import EventListView, EventDetailView, EventCreateView
from . import views as board_views
from users import views as user_views
from django.conf.urls import url

urlpatterns = [
    path('', board_views.home, name = 'home'),
    path('events/', EventListView.as_view(), name = 'events'),
    path('home/<int:pk>/update-profile/', user_views.UserProfileUpdateView.as_view(), name='user_profile_update'),
    path('home/<int:pk>/update/', user_views.UserUpdateView.as_view(), name='user_update'),
    path('event/new/', EventCreateView.as_view(), name='event-create'),
    path('event/<int:pk>/', EventDetailView.as_view(), name='event-detail'),
    path('event/<int:pk>/update_event/', board_views.ModalEventEditView.as_view(), name='update_event'),
    path('event/<int:pk>/delete_event/', board_views.ModalEventDeleteView.as_view(), name='delete_event'),
    path('event/<int:pk>/create_task/', board_views.TaskCreateView.as_view(), name='create_task'),
    path('event/<int:pk/delete_task/<int:pk>/', board_views.TaskDeleteView.as_view(), name='delete_task'),
    path('event/<int:pk>/join_event/', board_views.JoinEventView.as_view(), name='join_event'),
    path('event/<int:pk>/leave_event/', board_views.LeaveEventView.as_view(), name='leave_event'),
    path('event/<int:pk>/join_task/', board_views.JoinTaskView.as_view(), name='join_task'),
    path('event/<int:pk>/leave_task/', board_views.LeaveTaskView.as_view(), name='leave_task'),
    path('event/<int:pk>/<board>/join/', board_views.AddEventToBoard.as_view(), name='event-to-board'),
    path('event/<int:pk>/<board>/leave/', board_views.RemoveEventFromBoard.as_view(), name='event-away-board'),
    path('event/<int:pk>/add_attachment/', board_views.CreateAttachment.as_view(), name='add_attachment'),
    path('event/board/new/', board_views.BoardCreateView.as_view(), name='board-create'),
    path('event/board/delete/<int:pk>/', board_views.BoardDeleteView.as_view(), name='delete_board'),
    path('event/<int:pk>/delete_attachment/', board_views.AttachmentDeleteView.as_view(), name='delete_attachment'),

]