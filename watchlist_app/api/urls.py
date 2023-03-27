from django.urls import path, include
# from watchlist_app.api.views import movie_list, movie_details
from watchlist_app.api.views import (WatchListAV, WatchDetailsAV, StreamPlatformAV, 
                                     StreamPlatformDetailAV, ReviewList, ReviewDetail,
                                     ReviewCreate, StreamPlatformVS)
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('stream', StreamPlatformVS, basename='streamplatform')

urlpatterns = [
    path('list/', WatchListAV.as_view(), name='Watch-list'),
    # path('stream/', StreamPlatformAV.as_view(), name='Stream-list'),
    path('list/<int:pk>/', WatchDetailsAV.as_view(), name='Watch-details'),
    path('', include(router.urls)),
    path('<int:pk>/', StreamPlatformDetailAV.as_view(), name='streamplatform-detail'),
    path('<int:pk>/review-create/', ReviewCreate.as_view(), name="review-create"),
    path('<int:pk>/reviews/', ReviewList.as_view(), name="review-list"),
    path('review/<int:pk>/', ReviewDetail.as_view(), name="review-detail"),
]