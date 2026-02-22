
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Mapping
from .serializers import MappingSerializer

@api_view(['GET','POST'])
def mappings(request):
    if request.method == 'GET':
        return Response(MappingSerializer(Mapping.objects.all(),many=True).data)
    if request.method == 'POST':
        serializer = MappingSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
