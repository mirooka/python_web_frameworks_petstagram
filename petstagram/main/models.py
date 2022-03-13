import datetime

from django.core.validators import MinLengthValidator
from django.db import models

# Create your models here.
from petstagram.main.validators import validate_only_letters, validate_file_max_size_in_mb, MinDateValidator, \
    MaxDateValidator

'''
Profile
The user must provide the following information in their profile:
 The first name - it should have at least 2 chars, max - 30 chars, and should consist only of letters.
 The last name - it should have at least 2 chars, max - 30 chars, and should consist only of letters.
 Profile picture - the user can link their picture using a URL.

The user may provide the following information in their profile:

© SoftUni – about.softuni.bg. Copyrighted document. Unauthorized copy, reproduction or use is not permitted.
Follow us: Page 3 of 3

 Date of birth: day, month, and year of birth.
 Description - a user can write any description about themselves, no limit of words/chars.
 Email - a user can only write a valid email address.
 Gender - the user can choose one of the following: &quot;Male&quot;, &quot;Female&quot;, and &quot;Do not show&quot;.'''


class Profile(models.Model):
    FIRST_NAME_MIN_LENGTH = 2
    LAST_NAME_MIN_LENGTH = 2

    FIRST_NAME_MAX_LENGTH = 30
    LAST_NAME_MAX_LENGTH = 30

    MALE = 'Male'
    FEMALE = 'Female'
    DO_NOT_SHOW = 'Do not show'

    GENDERS = [(x, x) for x in (MALE, FEMALE, DO_NOT_SHOW)]

    first_name = models.CharField(
        max_length=FIRST_NAME_MAX_LENGTH,
        validators=(
            MinLengthValidator(FIRST_NAME_MIN_LENGTH),
            validate_only_letters,
        )
    )

    last_name = models.CharField(
        max_length=LAST_NAME_MAX_LENGTH,
        validators=(
            MinLengthValidator(FIRST_NAME_MIN_LENGTH),
            validate_only_letters,
        )
    )

    picture = models.URLField()

    date_of_birth = models.DateField(
        null=True,
        blank=True,
    )
    description = models.TextField(
        null=True,
        blank=True,
    )

    email = models.EmailField(
        null=True,
        blank=True,
    )

    gender = models.CharField(
        max_length=max(len(x) for x, _ in GENDERS),
        choices=GENDERS,
        default=DO_NOT_SHOW,
        null=True,
        blank=True,
    )

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Pet(models.Model):
    # Constants
    CAT = 'Cat'
    DOG = 'Dog'
    BUNNY = 'Bunny'
    PARROT = 'Parrot'
    FISH = 'Fish'
    OTHER = 'Other'

    TYPES = [(x, x) for x in (CAT, DOG, BUNNY, PARROT, FISH, OTHER)]
    MIN_DATE = datetime.date(1920, 1, 1)

    NAME_MAX_LENGTH = 30
    # Fields(columns)
    name = models.CharField(
        max_length=NAME_MAX_LENGTH,
    )

    type = models.CharField(
        max_length=max(len(x) for (x, _) in TYPES),
        choices=TYPES,
    )

    date_of_birth = models.DateField(
        null=True,
        blank=True,
        validators=(
           # MinDateValidator(),
           # MaxDateValidator(),
        )
    )
    # One-to-one relations

    # One-to-many relations
    user_profile = models.ForeignKey(
        Profile,
        on_delete=models.CASCADE,
    )

    # Many-to-many relations

    # Properties
    @property
    def age(self):
        return datetime.datetime.now().year - self.date_of_birth.year

    # Methods

    # dunder methods

    # Meta
    class Meta:
        unique_together = ('user_profile', 'name')


class PetPhoto(models.Model):
    photo = models.ImageField(
        validators=(
            # validate_file_max_size_in_mb(5),
        )
    )
    tagged_pets = models.ManyToManyField(
    Pet,
    # validate atleast one pet
    )
    description = models.TextField(
        null=True,
        blank=True,
    )
    publication_date = models.DateTimeField(
        auto_now_add=True,
    )
    likes = models.IntegerField(
        default=0,
    )
