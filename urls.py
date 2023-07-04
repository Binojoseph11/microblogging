from django.urls import path
from .views import UserView, UserDetailsView, PostView, PostDetailsView, UserTimelineView

app_name = 'api'

urlpatterns = [
    path('users/', UserView.as_view(), name='user_list'),
    path('users/<int:user_id>/', UserDetailsView.as_view(), name='user_details'),
    path('posts/', PostView.as_view(), name='post_list'),
    path('posts/<int:post_id>/', PostDetailsView.as_view(), name='post_details'),
    path('users/<int:user_id>/timeline/', UserTimelineView.as_view(), name='user_timeline'),
]
