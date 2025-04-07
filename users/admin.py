# users/admin.py
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Usuario

class UsuarioAdmin(UserAdmin):
    model = Usuario
    list_display = ('correo', 'nombre', 'rol', 'is_staff', 'is_active')
    list_filter = ('rol', 'is_staff', 'is_active')
    fieldsets = (
        (None, {'fields': ('correo', 'nombre', 'password')}),
        ('Permisos', {'fields': ('rol', 'is_staff', 'is_active', 'is_superuser', 'groups', 'user_permissions')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('correo', 'nombre', 'password1', 'password2', 'rol', 'is_staff', 'is_active')}
        ),
    )
    search_fields = ('correo',)
    ordering = ('correo',)

admin.site.register(Usuario, UsuarioAdmin)
