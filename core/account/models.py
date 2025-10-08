from django.db import models
from django.core.validators import RegexValidator
from .util.helper import validate_national_id


# Create your models here.
class UserInfo(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    national_id = models.CharField(unique=True, error_messages={'unique': "کاربر با این شماره ملی قبلا ثبت شده است."},
                                   max_length=11, validators=[validate_national_id], null=True, blank=True,
                                   default=None)
    cellphone = models.CharField(max_length=16, validators=[RegexValidator(r'^\+\d{9,15}$')], unique=True, null=True,
                                 error_messages={'unique': "This mobile number is already registered."})
    birth_date = models.DateField(blank=True, null=True, default=None)
    created_at = models.DateTimeField(auto_now_add=True, editable=False, db_index=True, null=True)
    
    def __str__(self):
        return self.national_id