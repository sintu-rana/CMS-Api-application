from django.urls import path
from .views import UserAPI, PostAPI, LikeAPI


#urls-

urlpatterns = [
    # User URLs
    path('user/', UserAPI.as_view(), name='create_user'),
    path('user/<int:user_id>/', UserAPI.as_view(), name='user'),

    # Post URLs
    path('post/', PostAPI.as_view(), name='create_post'),
    path('all_post/', PostAPI.as_view(), name='all_post'),
    path('post/<int:post_id>/', PostAPI.as_view(), name='post'),
    

    # Like URLs
    path('like/', LikeAPI.as_view(), name='create_like'),
    path('like/<int:like_id>/', LikeAPI.as_view(), name='like'),
    
]
