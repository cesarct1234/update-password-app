from django.core.management.base import BaseCommand
from users.models import Usuario

class Command(BaseCommand):
    help = 'Elimina un superusuario específico por correo'

    def add_arguments(self, parser):
        parser.add_argument('correo', type=str, help='Correo del superusuario a eliminar')

    def handle(self, *args, **kwargs):
        correo = kwargs['correo']
        try:
            user = Usuario.objects.get(correo=correo, is_superuser=True)
            user.delete()
            self.stdout.write(self.style.SUCCESS(f"Superusuario '{correo}' eliminado correctamente."))
        except Usuario.DoesNotExist:
            self.stdout.write(self.style.ERROR(f"No se encontró un superusuario con el correo '{correo}'."))
