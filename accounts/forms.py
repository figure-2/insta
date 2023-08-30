from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import User
from django.contrib.auth import get_user_model

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        # 유지 보수를 위해서는 아래보다는 위에 코드가 관리하기 편하다.
        # model = User
        fields = ('username', 'profile_image',)

class CustomAuthenticationForm(AuthenticationForm):
    pass