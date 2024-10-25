from django.urls import path
from .views import AutorAPIView, AutorReadUpdateDeleteView, LivroAutorAPIView

urlpatterns = [
    path('autor/', AutorAPIView.as_view()),
    path('autor/<int:pk>/', AutorReadUpdateDeleteView.as_view()),

    path('livro/autor/', LivroAutorAPIView.as_view()),


 

]