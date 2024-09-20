from django.db import models

# Create your models here.
class homepage(models.Model):
    name=models.CharField(max_length=250)
    course=models.CharField(max_length=250)
    hallticketno=models.IntegerField()
    email=models.EmailField(max_length=250)
    password=models.IntegerField()
    mobile=models.IntegerField()
    
    def __str__(self):
        return self.name
    
    
class thomepage(models.Model):
    firstname=models.CharField(max_length=250)
    lastname=models.CharField(max_length=250)
    email=models.EmailField(max_length=250)
    password=models.IntegerField()
    mobile=models.IntegerField()
    
    def __str__(self):
        return self.firstname
    
class studetails(models.Model):
    studentname=models.CharField(max_length=250)
    studenthallticketno=models.IntegerField()
    mlmarks=models.DecimalField(max_digits=5,decimal_places=2)
    iotmarks=models.DecimalField(max_digits=5,decimal_places=2)
    webmarks=models.DecimalField(max_digits=5,decimal_places=2)
    cnsmarks=models.DecimalField(max_digits=5,decimal_places=2)
    spmmarks=models.DecimalField(max_digits=5,decimal_places=2)
    
    def __str__(self):
        return self.studentname
    
    def totalmarks(self):
        return self.mlmarks + self.iotmarks + self.webmarks + self.cnsmarks + self.spmmarks
    
    def grade(self):
        total=self.totalmarks()
        if total >= 450:
            return 'A'
        elif total >= 400:
            return 'B'
        elif total >= 350:
            return 'C'
        elif total >= 300:
            return 'D'
        else:
            return 'Fail'
    
    