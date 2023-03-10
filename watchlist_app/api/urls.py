from django.urls import path
# from watchlist_app.api.views import movie_list, movie_details
from watchlist_app.api.views import WatchListAV, WatchDetailsAV, StreamPlatformAV, StreamPlatformDetailAV, ReviewList, ReviewDetail

urlpatterns = [
    path('list/', WatchListAV.as_view(), name='Watch-list'),
    path('stream/', StreamPlatformAV.as_view(), name='Stream-list'),
    path('list/<int:pk>/', WatchDetailsAV.as_view(), name='Watch-details'),
    path('stream/<int:pk>/', StreamPlatformDetailAV.as_view(), name='streamplatform-detail'),
    path('review/', ReviewList.as_view(), name="review-list"),
    path('review/<int:pk>/', ReviewDetail.as_view(), name="review-detail"),
]