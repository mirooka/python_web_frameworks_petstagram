from django.core.exceptions import ValidationError
from django.utils.deconstruct import deconstructible


def validate_only_letters(value):
    for ch in value:
        if not ch.isalpha():
            raise ValidationError('Value must contain only letters')


def validate_file_max_size_in_mb(max_size):
    def validate(value):  # add this to some file where you can import it from
        filesize = value.file.size
        if filesize > max_size * 1024 * 1024:
            raise ValidationError('Max file size is %sMB' % str(max_size))
    return validate


@deconstructible
class ValidateFileMaxSizeInMb:
    def __init__(self, max_size):
        self.max_size = max_size

    def __call__(self, value):
        pass


@deconstructible()
class MinDateValidator:
    def __init__(self, min_date):
        self.min_date = min_date

    def __call__(self, value):
        if value < self.min_date:
            raise ValidationError(f'Date must be greater than {self.min_date}')


@deconstructible()
class MaxDateValidator:
    def __init__(self, max_date):
        self.max_date = max_date

    def __call__(self, value):
        if value > self.max_date:
            raise ValidationError(f'Date must be earlier than {self.max_date}')



