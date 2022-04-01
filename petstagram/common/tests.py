from django import test as django_test
from django.core.exceptions import ValidationError
from django.core.files import File
from django.core.files.uploadedfile import SimpleUploadedFile

from petstagram.common.validators import MaxFileSizeInMbValidator


class FakeFile:
    size = 5


class FakeImage:
    file = FakeFile()


class MaxFileSizeInMbValidatorTests(django_test.TestCase):
    def test_when_file_is_bigger__expect_to_raise(self):
        validator = MaxFileSizeInMbValidator(0.000001)
        file = FakeImage()
        with self.assertRaises(ValidationError) as context:
            validator(file)
        self.assertIsNotNone(context.exception)

    def test_when_file_size_is_correct_expect_to_do_nothing(self):
        validator = MaxFileSizeInMbValidator(1)

        file = FakeImage

        validator(file)
