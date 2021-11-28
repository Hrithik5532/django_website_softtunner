from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from datetime import datetime
# Create your models here.

class Blogpost(models.Model):
    thumbnail = models.ImageField(upload_to ='upload/')
    Post_date = models.DateTimeField(default=datetime.today())
    writer_name= models.CharField(max_length=20, default='')
    heading= models.CharField(max_length=30)
    description = models.CharField(max_length=50, null=True)
    blog_link = models.CharField(max_length=500, default='')
    def __str__(self) :
        return self.heading 

# STATUS = (
#        (1,'website development'),
#        (2,'Digital Marketing'),
#        (3,'UI/UX Design'),
#        (4,'Other')
#    )
# BUDGET=(
#         (1,'less to 5000'),
#         (2,'5000 to 10000'),
#         (3,'10,000 to 25,000'),
#         (4,"25000 to more")

#    )

class Contact(models.Model):
    new = models.AutoField(primary_key=True, default='')
    fname= models.CharField(max_length=100)
    email = models.EmailField(max_length=250)
    phone = models.CharField(max_length=10,null=False, blank=False, unique=True)
    time = models.CharField( max_length=20)
    file = models.ImageField(upload_to ='upload/contact_files/', blank=True)

    service = models.CharField(
       max_length=32,
  
   )
    budget= models.CharField(
       max_length=32,
   )
    message= models.CharField(max_length=100, null=True)
    def __str__(self) :
        return self.fname 
     

class portfolio(models.Model):
    cpic = models.ImageField(upload_to ='upload/')
    descrip= models.CharField(max_length=100)

      

        

