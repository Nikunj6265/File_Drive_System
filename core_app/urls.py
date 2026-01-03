from django.urls import path
from .views import RegisterView, LoginView, FolderViewSet, FileViewSet, FileDownloadView

urlpatterns = [
    path("auth/register/", RegisterView.as_view()),
    path("auth/login/", LoginView.as_view()),

    path("folders/", FolderViewSet.as_view({"get": "list", "post": "create"})),
    path("files/", FileViewSet.as_view({"get": "list", "post": "create"})),
    path("files/<int:pk>/download/", FileDownloadView.as_view()),
]
