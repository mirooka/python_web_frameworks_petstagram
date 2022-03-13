from django.shortcuts import render, redirect

from petstagram.main.models import PetPhoto


def show_pet_photo_details(request, pk):
    pet_photo = PetPhoto.objects.prefetch_related('tagged_pets').get(pk=pk)
    context = {
        'pet_photo': pet_photo,
    }
    return render(request, 'mian/photo_details.html', context)


def like_pet_photo(request, pk):
    # Like the pet with pk
    pet_photo = PetPhoto.objects.get(pk=pk)
    pet_photo.likes += 1
    pet_photo.save()
    return redirect('pet photo details', pk)


def create_pet_photo(request):
    return render(request, 'mian/photo_create.html')


def edit_pet_photo(request):
    return render(request, 'mian/photo_edit.html')

