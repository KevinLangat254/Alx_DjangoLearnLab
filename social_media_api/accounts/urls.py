from django.urls import include, path
from .views import RegisterView, LoginView, ProfileView, UserViewSet
from rest_framework.routers import DefaultRouter

router= DefaultRouter()
router.register(r'users', UserViewSet, basename='user')

urlpatterns = [
    path('register/', RegisterView.as_view(), name="register"),
    path('login/', LoginView.as_view(), name="login"),
    path('profile/', ProfileView.as_view(), name="profile"),
    path('', include(router.urls)), 
    path('follow/<int:pk>/', UserViewSet.as_view({'post': 'follow_user'}), name='follow-user'),
    path('unfollow/<int:pk>/', UserViewSet.as_view({'post': 'unfollow_user'}), name='unfollow-user'), 
]
