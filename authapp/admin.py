from django.contrib import admin
from .models import (User, WorkerDetails, JobDetails, Categories, RecruitersRequests, WorkersRequests, EmergencyDetails,
                     Inbox, ProfileImage, Chat)


# Register your models here.

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'dob', 'gender', 'phone', 'isblocked', 'aadhar_no',)


@admin.register(Chat)
class ChatAdmin(admin.ModelAdmin):
    list_display = ('receiver_id', 'sender_id', 'msg')




@admin.register(Inbox)
class InboxAdmin(admin.ModelAdmin):
    list_display = ('sender', 'receiver_id',  'last_msg', 'seen', 'unseen')

    def sender(self, instance):
        return instance.user.first_name


@admin.register(WorkerDetails)
class WorkersAdmin(admin.ModelAdmin):
    list_display = ('name', 'city', 'category_1', 'category_1_vc', 'category_1_exp', 'category_2', 'category_2_vc',
                    'category_2_exp', 'category_3', 'category_3_vc', 'category_3_exp')
    list_filter = ('category_1', 'city')

    def name(self, instance):
        return instance.user.first_name


@admin.register(JobDetails)
class JobDetailsAdmin(admin.ModelAdmin):
    list_display = ('job_title', 'job_description', 'recruiter', 'job_status')

    list_filter = ('status',)

    def recruiter(self, instance):
        return f'{instance.recruiter.first_name}, {instance.recruiter.last_name}'

    def job_status(self, instance):
        if instance.status == 1:
            return 'Pending'
        elif instance.status == 2:
            return 'Accepted'
        else:
            return 'Rejected'


@admin.register(RecruitersRequests)
class RecruitersRequestsAdmin(admin.ModelAdmin):
    list_display = ('job_detail', 'worker', 'recruiters', 'amount', 'job_status',)

    def recruiters(self, instance):
        obj = User.objects.get(pk=instance.recruiter)
        return obj.first_name

    def job_status(self, instance):
        if instance.status == 1:
            return 'Pending'
        elif instance.status == 2:
            return 'Accepted'
        else:
            return 'Rejected'


@admin.register(WorkersRequests)
class WorkersRequestsAdmin(admin.ModelAdmin):
    list_display = ('job_detail', 'worker', 'recruiters', 'job_status',)

    def recruiters(self, instance):
        obj = User.objects.get(pk=instance.recruiter)
        return obj.first_name

    def job_status(self, instance):
        if instance.status == 1:
            return 'Pending'
        elif instance.status == 2:
            return 'Accepted'
        else:
            return 'Rejected'


admin.site.register(Categories)
admin.site.register(ProfileImage)


@admin.register(EmergencyDetails)
class EmergencyDetailsAdmin(admin.ModelAdmin):
    list_display = ('user', 'contact_no')
