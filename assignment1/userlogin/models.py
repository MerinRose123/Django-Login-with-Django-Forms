from django.db import models

class userlogin(models.Model):

   firstname = models.CharField(max_length=50)
   lastname = models.CharField(max_length = 50)
   username = models.CharField(max_length = 30,null=True)
   mail = models.EmailField(max_length = 50, primary_key=True)
   phonenumber = models.BigIntegerField(null=True)
   address = models.TextField(max_length = 80)
   password = models.CharField(max_length = 20,null=True)

   class Meta:
      db_table = "userlogin"