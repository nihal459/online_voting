from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    is_election = models.BooleanField('is election', default=False)
    is_staff = models.BooleanField('is staff', default=False)
    is_party = models.BooleanField('is party', default=False)
    is_user = models.BooleanField('is user', default=False)
    is_verified = models.BooleanField(default=False)

    name = models.CharField(max_length=100, default='User')
    mobile_number = models.CharField(max_length=20, default='Nil')
    district = models.CharField(max_length=100, default='Nil')
    state = models.CharField(max_length=100, default='Nil')
    pincode = models.CharField(max_length=20, default='Nil')
    address = models.TextField()

    profile_pic = models.ImageField(upload_to='Photos', blank=True, null=True)
    aadhaar_front = models.ImageField(upload_to='Aadhaar Cards', blank=True, null=True)
    aadhaar_back = models.ImageField(upload_to='Aadhaar Cards', blank=True, null=True)
    voterid_front = models.ImageField(upload_to='VoterId Cards', blank=True, null=True)
    voterid_back = models.ImageField(upload_to='VoterId Cards', blank=True, null=True)
 