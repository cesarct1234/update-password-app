from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.contrib.auth.hashers import check_password
from rest_framework import status

class CambiarContrasenaView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        user = request.user
        current_password = request.data.get('currentPassword')
        new_password = request.data.get('newPassword')

        if not check_password(current_password, user.password):
            return Response({'error': 'La contraseña actual es incorrecta.'}, status=400)

        user.set_password(new_password)
        user.save()
        return Response({'message': 'Contraseña actualizada correctamente'}, status=200)
