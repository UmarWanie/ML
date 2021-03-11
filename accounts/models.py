from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver




GENDER_CHOICES = (
    (1, 'Male'),
    (0, 'Female'),
    (2, 'Gender'),
)

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    age  = models.IntegerField( null=True, blank=True)
    gender = models.IntegerField(choices=GENDER_CHOICES,default=2)


    def __str__(self):
    	return f'{self.user.username}'
    	pass


    
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):



    if created:
        Profile.objects.create(user=instance)

    instance.profile.save()



class Prediction(models.Model):

    VAL_CHOICES = (
        (1, 'Yes'),
        (0, 'No'),
        (2, 'Select'),
    )
    patient = models.ForeignKey(User, null=True, on_delete= models.SET_NULL)
    Gender = models.IntegerField(choices = GENDER_CHOICES,default=2)
    Polyuria = models.IntegerField(choices=VAL_CHOICES,default=2)
    
    Polydipsia = models.IntegerField(choices=VAL_CHOICES,default=2)
    Sudden_weight_loss = models.IntegerField(choices=VAL_CHOICES,default=2)
    Partial_paresis = models.IntegerField(choices=VAL_CHOICES,default=2)
    Polyphagia = models.IntegerField(choices=VAL_CHOICES,default=2)
    Irritability = models.IntegerField(choices=VAL_CHOICES,default=2)
    Alopecia = models.IntegerField(choices=VAL_CHOICES,default=2)
    Visual_blurring = models.IntegerField(choices=VAL_CHOICES,default=2)
    Weakness = models.IntegerField(choices=VAL_CHOICES,default=2)
    Prediction = models.CharField(max_length=3, null=True)























class Prediction2(models.Model):

    VAL_CHOICES = (
        (1, 'Yes'),
        (0, 'No'),
        (2, 'Select'),
    )
    username = models.CharField(max_length=20)
    Gender = models.IntegerField(choices = GENDER_CHOICES,default=2)
    Polyuria = models.IntegerField(choices=VAL_CHOICES,default=2)
    
    Polydipsia = models.IntegerField(choices=VAL_CHOICES,default=2)
    Sudden_weight_loss = models.IntegerField(choices=VAL_CHOICES,default=2)
    Partial_paresis = models.IntegerField(choices=VAL_CHOICES,default=2)
    Polyphagia = models.IntegerField(choices=VAL_CHOICES,default=2)
    Irritability = models.IntegerField(choices=VAL_CHOICES,default=2)
    Alopecia = models.IntegerField(choices=VAL_CHOICES,default=2)
    Visual_blurring = models.IntegerField(choices=VAL_CHOICES,default=2)
    Weakness = models.IntegerField(choices=VAL_CHOICES,default=2)
    Prediction = models.CharField(max_length=3, null=True)



	   