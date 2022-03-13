from django.shortcuts import render

from petstagram.main.models import PetPhoto
from petstagram.main.views.helpers import get_profile


def show_home(request):
    context = {
        'hide_additional_nav_items': True
    }
    return render(request, 'mian/home_page.html', context)


def show_dashboard(request):
    profile = get_profile()

    pet_photos = PetPhoto.objects.prefetch_related('tagged_pets').filter(tagged_pets__user_profile=profile).distinct()

    context = {
        'pet_photos': pet_photos,
    }
    return render(request, 'mian/dashboard.html', context)
