from datetime import date

from django import forms

from petstagram.main.models import Pet
from petstagram.common.helpers import BootstrapFormMixin, DisabledFieldsFormMixin


class CreatePetForm(BootstrapFormMixin, forms.ModelForm):
    def __init__(self, user, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.user = user
        self._init_bootstrap_form_controls()

    def save(self, commit=True):
        pet = super().save(commit=False)
        pet.user = self.user
        if commit:
            pet.save()
        return pet

    class Meta:
        model = Pet
        fields = ('name', 'type', 'date_of_birth')
        widgets = {
            'name': forms.TextInput(
                attrs={
                    'placeholder': 'Enter pet name',
                }
            ),
        }


class EditPetForm(BootstrapFormMixin, forms.ModelForm):
    MIN_DATE_OF_BIRTH = date(1920, 1, 1)
    MAX_DATE_OF_BIRTH = date.today()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._init_bootstrap_form_controls()

    class Meta:
        model = Pet
        exclude = ('user_profile',)


class DeletePetForm(DisabledFieldsFormMixin, BootstrapFormMixin, forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._init_bootstrap_form_controls()
        self._init_disabled_fields()

    class Meta:
        model = Pet
        fields = '__all__'

    def save(self, commit=True):
        self.instance.delete()
        return self.instance
