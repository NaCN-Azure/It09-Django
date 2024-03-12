# application/admin.py
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from .models.user_model import User

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = User
        fields = '__all__'

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('email', 'user_name', 'phone', 'city', 'password1', 'password2', 'type')

class CustomUserAdmin(UserAdmin):
    form = CustomUserChangeForm
    add_form = CustomUserCreationForm
    model = User
    list_display = ('email', 'user_name', 'is_staff', 'is_active', 'type')
    list_filter = ('is_staff', 'is_active', 'type')
    fieldsets = (
        (None, {'fields': ('email', 'password', 'type')}),
        ('Personal info', {'fields': ('user_name', 'phone', 'city')}),
        ('Permissions', {'fields': ('is_staff', 'is_active')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'user_name', 'phone', 'city', 'password1', 'password2', 'type', 'is_active', 'is_staff')}
        ),
    )
    search_fields = ('email', 'user_name')
    ordering = ('email',)

admin.site.register(User, CustomUserAdmin)

