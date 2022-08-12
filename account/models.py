from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.utils import timezone
from shop.models import Produto


class ManagerUser(BaseUserManager):
    def _create_user(self, email, password, nome_completo, **extra_fields):
        email = self.normalize_email(email)
        user = self.model(
            email=email,
            nome_completo=nome_completo,
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_user(self, email, password, nome_completo, **extra_fields):
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        return self._create_user(email, password, nome_completo, **extra_fields)

    def create_superuser(self, email, password, nome_completo, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self._create_user(email, password, nome_completo, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    username_validator = UnicodeUsernameValidator()
    nome_completo = models.CharField('Nome e Sobrenome', max_length=256)
    is_active = models.BooleanField(default=True)
    email = models.EmailField('E-mail', max_length=256, unique=True)
    date_joined = models.DateTimeField("Data de registro", default=timezone.now)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['nome_completo']

    objects = ManagerUser()

    is_staff = models.BooleanField(
        "staff status",
        default=False,
        help_text=("O usuário pode acessar o admin do site"),
    )
    is_superuser = models.BooleanField("staff status",
        default=False,
        help_text=("O usuário pode acessar tem super permissões para acessar o admin"),
    )
    email_verificado = models.BooleanField(default=False)
    def receber_nome(self):
        partes = self.nome_completo.split()
        return f'{partes[0]} {partes[1]}'


class Review(models.Model):
    titulo = models.CharField('Título',max_length=100)
    nota = models.IntegerField(choices=[(1, 'muito ruim'), (2, 'ruim'), (3, 'padrão'), (4, 'bom'), (5, 'muito bom')])
    usuario = models.ForeignKey(verbose_name='Usuário',to=User, on_delete=models.CASCADE, editable=False)
    produto = models.ForeignKey(verbose_name='Produto',to=Produto, on_delete=models.CASCADE)
    comentario = models.TextField(verbose_name='Comentários')

    def __str__(self):
        return f'{self.usuario}|| {self.produto}'
