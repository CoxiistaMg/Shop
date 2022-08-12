from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Review
from .forms import ReviewForm
from .forms import UserForm, UserChangeAdminForm


@admin.register(User)
class User(UserAdmin):
    model = User
    add_form = UserForm
    form = UserChangeAdminForm
    query = User.objects.all()
    list_display = ['email', 'nome_completo']
    search_fields = ['email', 'nome_completo']
    fieldsets = (
        ("Informações pessoais", {"fields": ("email", "password",'nome_completo')}),
        (
            "Permissions",
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                ),
            },
        ),
        ("Important dates", {"fields": ("last_login", "date_joined")}),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("email", "password1", "password2"),
            },
        ),
    )
    ordering = ['id']


    def get_queryset(self, request):
        return self.query


@admin.register(Review)
class Review(admin.ModelAdmin):
    form = ReviewForm
    
    def get_form(self, request, obj, **kwargs):
        form = ReviewForm
        form.usuario = request.user
        return form
