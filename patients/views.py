from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .models import Patient
from .serializers import PatientSerializer


@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def patients(request):

    if request.method == 'GET':

        patients = Patient.objects.filter(created_by=request.user)

        serializer = PatientSerializer(patients, many=True)

        return Response(serializer.data)


    if request.method == 'POST':

        serializer = PatientSerializer(data=request.data)

        if serializer.is_valid():

            serializer.save(created_by=request.user)

            return Response(serializer.data)

        return Response(serializer.errors)
