
from django.db import models

from company_role.models import *

class Question_Type(models.Model):
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    added_on = models.DateField(auto_now_add=True)

class Question(models.Model):
    language = models.ForeignKey('Product_owner_role.TaskLanguage',on_delete=models.DO_NOTHING,null=True,blank=True)
    level = models.ForeignKey('Product_owner_role.TaskLevel', on_delete=models.DO_NOTHING,null=True,blank=True)
    ques_type = models.ForeignKey('Question_Type', on_delete=models.CASCADE, null=True, blank=True)
    ques=models.TextField()
    ans=models.TextField()
    is_active = models.BooleanField(default=True)
    added_on = models.DateField(auto_now_add=True)
    user = models.ForeignKey('Product_owner_role.User', on_delete=models.CASCADE, null=True, blank=True)





class SamplePaper(models.Model):
    language = models.ForeignKey('Product_owner_role.TaskLanguage', on_delete=models.CASCADE,null=True,blank=True)
    level = models.ForeignKey('Product_owner_role.TaskLevel', on_delete=models.CASCADE,null=True,blank=True)
    ques_type = models.ForeignKey('Question_Type',on_delete=models.CASCADE,null=True,blank=True)
    question=models.ManyToManyField(Question)
    title=models.CharField(max_length=255)
    duration = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    added_on = models.DateField(auto_now_add=True)
    user = models.ForeignKey('Product_owner_role.User', on_delete=models.CASCADE, null=True, blank=True)


class Test_Record(models.Model):
    sample_paper = models.ForeignKey(SamplePaper,on_delete=models.CASCADE,null=True,blank=True)
    interviewee_TestDetails = models.ForeignKey('company_role.IntervieweeTestDetails',on_delete=models.CASCADE,null=True,blank=True)
    question=models.ForeignKey(Question,on_delete=models.CASCADE,null=True,blank=True)
    answer=models.TextField(null=True,blank=True)
