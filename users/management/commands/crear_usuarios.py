# users/management/commands/crear_usuarios.py

from django.core.management.base import BaseCommand
from users.models import Usuario

class Command(BaseCommand):
    help = "Crear usuarios iniciales"

    def handle(self, *args, **kwargs):
        usuarios = [
            {
                "correo": "vice@correo.com",
                "nombre": "Vicerrector",
                "password": "vice123",
                "rol": "Vicerrector"
            },
            {
                "correo": "coordinador@correo.com",
                "nombre": "Coordinador",
                "password": "coord123",
                "rol": "Coordinador"
            },
            {
                "correo": "nuevo@correo.com",
                "nombre": "Nuevo Coordinador",
                "password": "nuevo123",
                "rol": "Coordinador"
            }
        ]

        for u in usuarios:
            if not Usuario.objects.filter(correo=u["correo"]).exists():
                user = Usuario.objects.create_user(
                    correo=u["correo"],
                    nombre=u["nombre"],
                    password=u["password"],
                    rol=u["rol"]
                )
                self.stdout.write(self.style.SUCCESS(f"Usuario '{u['correo']}' creado"))
            else:
                self.stdout.write(self.style.WARNING(f"Usuario '{u['correo']}' ya existe"))

