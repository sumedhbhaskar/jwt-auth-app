"""
custom users and user managers
"""

from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin




class UserManager(BaseUserManager):
    """create user and super user"""
    def create_user(self,username:str=None,password:str=None, **extra_fields):
        """create new user based on custom user model"""

        is_staff = extra_fields.setdefault("is_staff",False)
        is_superuser = extra_fields.setdefault("is_superuser",False)

        if not username:
            raise ValueError("Username required")
        
        user = self.model(username=username,**extra_fields)
        user.set_password(password)
        user.save()

        return user
    
    def create_superuser(self,username:str=None,password:str=None, **extra_fields):
        """create super user"""

        if not extra_fields['is_staff'] or not extra_fields['is_super_user']:
            raise ValueError("is_staff or is_superuser is False")
        
        if not username:
            raise ValueError("Username required")
        
        user = self.model(username=username,**extra_fields)
        user.set_password(password)
        user.save()

        return user        


class CustomUser(AbstractBaseUser):
    username = models.EmailField("Email ID",unique=True)
    is_staff = models.BooleanField("Is staff?",default=False)
    is_superuser = models.BooleanField("Is super user?",default=False)

    objects = UserManager()

    USERNAME_FIELD = 'username'



