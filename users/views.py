from django.contrib.auth.models import User
from django.contrib.auth.hashers import check_password, make_password
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def update_password(request):
    user = request.user
    current_password = request.data.get('currentPassword')
    new_password = request.data.get('newPassword')
    confirm_password = request.data.get('confirmPassword')

    if not current_password or not new_password or not confirm_password:
        return Response({'error': 'Todos los campos son obligatorios'}, status=400)

    if not check_password(current_password, user.password):
        return Response({'error': 'La contraseña actual es incorrecta'}, status=400)

    if new_password != confirm_password:
        return Response({'error': 'Las nuevas contraseñas no coinciden'}, status=400)

    user.password = make_password(new_password)
    user.save()
    return Response({'message': 'Contraseña actualizada correctamente'})
