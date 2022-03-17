from django.contrib import admin

from Sample_Paper.models import Question,SamplePaper,Test_Record

admin.site.register(Question)
admin.site.register(SamplePaper)
admin.site.register(Test_Record)

# Register your models here.
