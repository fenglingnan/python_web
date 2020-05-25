from django.db import models

# Create your models here.

# create table book(
#     name varchar(20),
#     price float(4,2)
# )

class UserInfo(models.Model):

    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=16)
    age=models.IntegerField()
    current_data=models.DateField()
class run(models.Model):

    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=16)
    age=models.IntegerField()
    current_data=models.DateField()