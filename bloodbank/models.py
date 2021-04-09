from django.db import models

# Create your models here.

class Bloodbank(models.Model):
    category=models.CharField(max_length=5)
    amount=models.IntegerField()
    def __str__(self):
        return self.category


class Contact(models.Model):
    firstName=models.CharField(max_length=122)
    lastName=models.CharField(max_length=122)
    email=models.CharField(max_length=50)
    address=models.TextField()
    city=models.CharField(max_length=20)
    state=models.CharField(max_length=30)
    pincode=models.CharField(max_length=6)
    phoneNumber=models.CharField(max_length=13)

    def is_valid(self):
        if len(self.firstName) and len(self.lastName) and len(self.email) and len(self.address) and len(self.city) and len(self.state) and len(self.pincode) and len(self.phoneNumber):
            return 1
        return 0
      
