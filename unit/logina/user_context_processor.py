from .models import LoginUser


def get_LoginUser(request):
    if request.user.is_authenticated:
        loginUser = LoginUser.objects.get(user=request.user)
        return {'login_User': loginUser}
    else:
        return {

        }
