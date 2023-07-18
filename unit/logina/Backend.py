from django.contrib.auth.backends import ModelBackend,UserModel
from django.contrib.auth.models import User
from django.db.models import Q
from django.core.exceptions import MultipleObjectsReturned


#we will use 2 available function and make override on them
class profile_idBackend(ModelBackend):
    #
    def authenticate(self, request,username=None, password=None, **kwargs):
        # for if user recorded or not
        try:
            user=User.objects.get(
                    Q(username__iexact=username) |
                    Q(userprofile__NationalId=username)
            )
        except User.DoesNotExist:
            pass
        except MultipleObjectsReturned:
            return User.objects.filter(userprofile__NationalId=username).order_by(id).first()
        else:
            if user.check_password(password)and self.user_can_authenticate(user):
             return user