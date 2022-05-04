from django.db import models
from accounts.models import City, CaseType, User


# Create your models here.

class Criminal(models.Model):
    name = models.CharField(
        max_length=100,
        verbose_name='Full Name',
    )
    house_name = models.CharField(
        max_length=100,
        verbose_name='House Name'
    )
    city = models.ForeignKey(
        to=City,
        on_delete=models.CASCADE
    )
    aadhar_no = models.BigIntegerField(
        verbose_name='Aadhar Number'
    )
    casr_type = models.ForeignKey(
        to=CaseType,
        on_delete=models.CASCADE
    )
    image = models.FileField(
        upload_to='Images',
        max_length=300,
        verbose_name='Image'
    )
    case_file = models.FileField(
        upload_to='CaseFile',
        verbose_name='Case File',
        max_length=300
    )
    person_id = models.IntegerField(
        default=0,
        verbose_name='Criminal Number'
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=0, null=True, blank=True)

    def __str__(self):
        return self.name

class ImageSearch(models.Model):
    image = models.FileField(
        upload_to='Temp',
        verbose_name='Choose an Image',
        max_length=300,
    )
    user = models.ForeignKey(
        to=User,
        on_delete=models.CASCADE
    )

