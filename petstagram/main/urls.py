from django.urls import path

from petstagram.main.views.generic import DashboardView, HomeView
from petstagram.main.views.pet_photos import show_pet_photo_details, create_pet_photo, edit_pet_photo, like_pet_photo
from petstagram.main.views.pets import CreatePetView, EditPetView, DeletePetView
from petstagram.main.views.profiles import show_profile, create_profile, edit_profile, delete_profile

urlpatterns = (
    path('', HomeView.as_view(), name='index'),
    path('dashboard/', DashboardView.as_view(), name='dashboard'),

    path('profile/', show_profile, name='profile details'),
    path('profile/create/', create_profile, name='create profile'),
    path('profile/edit/', edit_profile, name='edit profile'),
    path('profile/delete/', delete_profile, name='delete profile'),

    path('photo/details/<int:pk>/', show_pet_photo_details, name='pet photo details'),
    path('photo/add/', create_pet_photo, name='create pet photo'),
    path('photo/edit/<int:pk>/', edit_pet_photo, name='edit pet photo'),
    path('photo/like/<int:pk>/', like_pet_photo, name='like pet photo'),

    path('pet/add/', CreatePetView.as_view(), name='create pet'),
    path('pet/edit/<int:pk>/', EditPetView.as_view(), name='edit pet'),
    path('pet/delete/<int:pk>/', DeletePetView.as_view(), name='delete pet'),
)
