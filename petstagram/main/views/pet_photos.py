from django.contrib.auth import mixins as auth_mixin
from django.urls import reverse_lazy
from django.views import generic as views
from django.shortcuts import redirect

from petstagram.main.models import PetPhoto


# def show_pet_photo_details(request, pk):
#     pet_photo = PetPhoto.objects.\
#         prefetch_related('tagged_pets').\
#         get(pk=pk)
#
#     context = {
#         'pet_photo': pet_photo,
#     }
#
#     return render(request, 'mian/photo_details.html', context)


class PetPhotoDetailsView(auth_mixin.LoginRequiredMixin, views.DetailView):
    model = PetPhoto
    template_name = 'mian/photo_details.html'
    context_object_name = 'pet_photo'

    def dispatch(self, request, *args, **kwargs):
        response = super().dispatch(request, *args, **kwargs)

        viewed_pet_photos = request.session.get('last_viewed_pet_photos_ids', [])

        viewed_pet_photos.insert(0, self.kwargs['pk'])
        request.session['last_viewed_pet_photos_ids'] = viewed_pet_photos[:4]

        return response

    def get_queryset(self):
        return super()\
            .get_queryset()\
            .prefetch_related('tagged_pets')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['is_owner'] = self.object.user == self.request.user
        return context


class CreatePetPhotoView(auth_mixin.LoginRequiredMixin, views.CreateView):
    model = PetPhoto
    template_name = 'mian/photo_create.html'
    fields = ('photo', 'description', 'tagged_pets')

    success_url = reverse_lazy('dashboard')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


def like_pet_photo(pk):
    # Like the pet with pk
    pet_photo = PetPhoto.objects.get(pk=pk)
    pet_photo.likes += 1
    pet_photo.save()
    return redirect('pet photo details', pk)


# def create_pet_photo(request):
#     return render(request, 'mian/photo_create.html')

class EditPetPhotoView(views.UpdateView):
    model = PetPhoto
    template_name = 'mian/photo_edit.html'
    fields = ('description',)

    def get_success_url(self):
        return reverse_lazy('pet photo details', kwargs={'pk': self.object.id})
