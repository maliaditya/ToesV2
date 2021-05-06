from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser, AbstractUser
)
import datetime

''' For Storing Basic User Information '''


class User(AbstractUser):
    dob = models.CharField(max_length=255)
    phone = models.CharField(max_length=255, unique=True, blank=False)
    is_admin = models.BooleanField(default=False)
    isblocked = models.BooleanField(default=False)
    gender = models.CharField(max_length=255)
    counter = models.IntegerField(default=0, blank=True, null=True)
    address = models.TextField(blank=False)
    smartphone = models.BooleanField(default=True)
    aadhar_no = models.CharField(max_length=255, default=None)

    REQUIRED_FIELDS = ['counter', 'isblocked', 'is_superuser', 'is_admin', 'first_name', 'last_name', 'username',
                       'password',
                       'dob', 'gender', 'aadhar_no', 'address', 'smartphone']

    USERNAME_FIELD = 'phone'

    def __str__(self):
        if self.first_name is None:
            return "ERROR-CUSTOMER NAME IS NULL"
        else:
            return f'{self.first_name} {self.last_name}'

    def get_username(self):
        return self.phone


class ProfileImage(models.Model):
    profile_image = models.ImageField(null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


''' Storing Worker Details like Categories, Visiting Charges, Experience '''


class WorkerDetails(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    city = models.CharField(max_length=255, blank=True)
    category_1 = models.CharField(max_length=255, blank=True)
    category_1_vc = models.CharField(max_length=255, blank=True)
    category_1_exp = models.IntegerField(blank=True)
    category_2 = models.CharField(max_length=255, blank=True)
    category_2_vc = models.CharField(max_length=255, blank=True)
    category_2_exp = models.IntegerField(blank=True)
    category_3 = models.CharField(max_length=255, blank=True)
    category_3_vc = models.CharField(max_length=255, blank=True)
    category_3_exp = models.IntegerField(blank=True)


''' Request Status

    id - Status_Name

     1 - Pending
     2 - Accepted
     3 - Rejected
     4 - Applied
'''


class StatusMaster(models.Model):
    status_name = models.CharField(max_length=255)


''' When recruiter creates post it is stored in JobDetails 
    the post data will be provided from JobDetails
    Status Default == pending
'''


class JobDetails(models.Model):
    job_title = models.CharField(max_length=255)
    job_description = models.CharField(max_length=300)
    recruiter = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.IntegerField(default=1)

    def __str__(self):
        return self.job_title


''' 
When Worker sends request to Recruiter
In Recruiters requests tab the data from RecruitersRequests will be provided

'''


class RecruitersRequests(models.Model):
    job_detail = models.ForeignKey(JobDetails, on_delete=models.CASCADE)
    worker = models.ForeignKey(User, on_delete=models.CASCADE)
    recruiter = models.IntegerField()
    amount = models.IntegerField()
    status = models.IntegerField(default=1)

    def __str__(self):
        return self.job_detail


''' 
When Recruiter hits the hire button a request is send to the worker 
In workers requests tab the data from this table will be provided

'''


class WorkersRequests(models.Model):
    job_detail = models.ForeignKey(JobDetails, on_delete=models.CASCADE)
    worker = models.ForeignKey(User, on_delete=models.CASCADE)
    recruiter = models.IntegerField()
    status = models.IntegerField(default=1)

    def __str__(self):
        return self.job_detail


''' All the work categories data will be stored in this table '''


class Categories(models.Model):
    categories = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.categories


class EmergencyDetails(models.Model):
    contact_no = models.CharField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.first_name


class Inbox(models.Model):
    sender_id = models.ForeignKey(User, on_delete=models.CASCADE)
    receiver_id = models.IntegerField()
    last_msg = models.CharField(max_length=255)
    seen = models.BooleanField(default=False)
    unseen = models.IntegerField()

    def __str__(self):
        return self.sender_id


class Chat(models.Model):
    sender_id = models.ForeignKey(User, on_delete=models.CASCADE)
    receiver_id = models.IntegerField()
    msg = models.CharField(max_length=500)

    def __str__(self):
        return self.sender_id
