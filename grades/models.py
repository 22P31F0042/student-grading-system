from django.db import models

# Create your models here.
class gradesystem(models.Model):
    s_name=models.CharField(max_length=250)
    course=models.CharField(max_length=200)
    ML_marks=models.IntegerField()
    WEB_marks=models.IntegerField()
    IOT_marks=models.IntegerField()
    CNS_marks=models.IntegerField()
    SPM_marks=models.IntegerField()
    def __str__(self):
        return self.s_name