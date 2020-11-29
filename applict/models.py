from django.db import models
from cloudinary.models import CloudinaryField
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.exceptions import ObjectDoesNotExist

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_picture = CloudinaryField('image')
    bio = models.TextField(max_length=700, default="Bio", blank=True)
    name = models.CharField(blank=True, max_length=120)
    location = models.CharField(max_length=60, blank=True)
    contact = models.EmailField(max_length=100, blank=True)

    def __str__(self):
        return f'{self.user.username} profile'


    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)
           

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        try:
            instance.profile.save()
        except ObjectDoesNotExist:
            Profile.objects.create(user=instance)

class Project(models.Model):
    image = CloudinaryField('image')
    project_name = models.CharField(max_length=50,null=True)
    link = models.CharField(max_length=50, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')

    def __str__(self):
        return self.sitename

    def save_project(self):
        self.save()

    def delete_project(self):
        self.delete()        

    @classmethod
    def get_images(cls):
        all_images = cls.objects.all()
        return all_images       

class Rating(models.Model):
    ratings = ((1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'), (6, '6'), (7, '7'), (8, '8'), (9, '9'), (10, '10'))
    post = models.ForeignKey(Project, on_delete=models.CASCADE,)
    pub_date = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE,)
    usability = models.IntegerField(default=0,null=True)
    design = models.IntegerField(default=0, null=True)
    content = models.IntegerField(default=0,null=True)
    review = models.CharField(max_length=200)

    def __str__(self):
        return self.review

    def save_rating(self):
        self.save()

    def delete_rating(self):
        self.delete()       