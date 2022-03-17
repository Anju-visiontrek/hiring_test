from django.db import models
import uuid
from uuid import uuid4

from Product_owner_role.models import *
from Sample_Paper.models import SamplePaper


class Company_Profile(models.Model):
    company_Name = models.CharField(max_length=255)
    company_address = models.CharField(max_length=255, null=True, blank=True)
    company_phone_no = models.CharField(max_length=12, null=True, blank=True)
    company_email = models.EmailField()
    company_Password = models.CharField(max_length=255)
    company_state = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    added_on = models.DateField(auto_now_add=True)







class IntervieweeDetail(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(blank=False)
    github = models.CharField(max_length=255,blank=True,default="")
    phone_no = models.CharField(max_length=12, null=True, blank=True)
    cv = models.FileField()
    interviewed_on = models.DateField(auto_now_add=True)
    language = models.CharField(max_length=255,default="")
    level = models.CharField(max_length=255,default="")
    interviwee_key = models.UUIDField(default=uuid.uuid4)

    #
    # def __str__(self):
    #     return f"{self.email}"

    # extract the username and text field from the data


class IntervieweeTestDetails(models.Model):
    interviewer=models.ForeignKey('Product_owner_role.User',on_delete=models.DO_NOTHING,null=True,blank=True)
    interviewee = models.ForeignKey(IntervieweeDetail,on_delete=models.DO_NOTHING,null=True,blank=True)
    started_at = models.DateTimeField(null=True,blank=True)
    is_completed = models.BooleanField(default=False)
    completed_at = models.DateTimeField(null=True,blank=True)
    test=models.ForeignKey(SamplePaper,on_delete=models.DO_NOTHING,null=True,blank=True)
    is_completed_by_computer = models.BooleanField(default=False)
    remarks = models.TextField(default="")
    #
    #
    # def __str__(self):
    #     return f"{self.interviewer}"





