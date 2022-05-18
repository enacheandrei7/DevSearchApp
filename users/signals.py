from django.db.models.signals import post_save, post_delete
# post_save is triggered after a model is saved
# post_delete is triggered after a model is deleted
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import Profile


# @receiver(post_save, sender=Profile)
def createProfile(sender, instance, created, **kwargs):
    if created:
        user = instance
        profile = Profile.objects.create(
            user = user,
            username = user.username,
            email = user.email,
            name = user.first_name,
        )

def deleteUser(sender, instance, **kwargs):
    user = instance.user
    user.delete()
    

# If a new User is created --> a new Profile is created (sender = User --> receiver = createProfile)
post_save.connect(createProfile, sender=User)

# For post_delete we don't need to put the sender = User, because when we set the field ' user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)' in the profile we've put the settings 'on_delete = models.CASCADE', which tells Django that when the User is deleted, it's corresponding children (in our case from 'Profiles') are deleted --> But if we delete a Profile, the User still remains, so we need to trigger the deletion when the Profile is erased
post_delete.connect(deleteUser, sender=Profile)