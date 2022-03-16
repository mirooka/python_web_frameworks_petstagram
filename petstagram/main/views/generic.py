from django.views import generic as views
from django.shortcuts import render, redirect

from petstagram.common.view_mixins import RedirectToDashboard
from petstagram.main.models import PetPhoto


# def show_home(request):
#     context = {
#         'hide_additional_nav_items': True
#     }
#     return render(request, 'mian/home_page.html', context)


class HomeView(RedirectToDashboard, views.TemplateView):
    template_name = 'mian/home_page.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['hide_additional_nav_items'] = True
        return context


class DashboardView(views.ListView):
    model = PetPhoto
    template_name = 'mian/dashboard.html'
    context_object_name = 'pet_photos'

# def show_dashboard(request):
#     profile = get_profile()
#
#     pet_photos = PetPhoto.objects.prefetch_related('tagged_pets').filter(tagged_pets__user_profile=profile).distinct()
#
#     context = {
#         'pet_photos': pet_photos,
#     }
#     return render(request, 'mian/dashboard.html', context)
