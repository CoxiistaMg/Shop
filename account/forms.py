from django.forms import ModelForm
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from django.core.exceptions import ValidationError
from .models import User, Review


class UserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('email', 'nome_completo')


class UserChangeForm(UserChangeForm):
    class Meta:
        model = User
        fields = ['nome_completo', 'email']


class UserChangeAdminForm(UserChangeForm):
    class Meta:
        model = User
        fields = ['nome_completo', 'email', 'is_staff', 'is_superuser']


class ReviewForm(ModelForm):  
    class Meta:
        model = Review
        fields = '__all__'
    
    def save(self, commit=False, *args, **kwargs):
        self.instance.usuario_id = self.usuario.id
        return super().save(commit)

