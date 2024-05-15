from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from .views import register, index, user_login, profile
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', index, name="index"),
    path('register/', register, name="register"),
    path('login/', user_login, name="login"),
    path('profile/<int:id>/', profile, name="profile"),
    path("logout/", LogoutView.as_view(next_page = "index"), name = "logout")
]
urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)