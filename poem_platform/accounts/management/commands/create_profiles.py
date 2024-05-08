from django.core.management.base import BaseCommand
from accounts.models import CustomUser, Profile

class Command(BaseCommand):
    help = 'Create profiles for existing users'

    def handle(self, *args, **kwargs):
        users = CustomUser.objects.all()
        
        for user in users:
            if not hasattr(user, 'profile'):
                Profile.objects.create(user=user, bio='', avatar='D:\Django\poem_platform\accounts\static\avatar.png')
                self.stdout.write(f"Profile created for user {user.username}")
                
        self.stdout.write(self.style.SUCCESS('All profiles created for existing users'))
