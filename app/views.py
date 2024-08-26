from rest_framework.decorators import api_view
from rest_framework.response import Response 
from rest_framework import status
from .models import *
from .serializers import *


# Create your views here.
@api_view(["GET","POST"])
def foodView(request,category):
    if request.method == "GET":
        if category == "food":
            items = Food.objects.all()
        else:
            items = Food.objects.filter(category=category)
        serializer = FoodSerializer(items,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    elif request.method == "POST":
        try:
            serializer = FoodSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data,status=status.HTTP_201_CREATED)
            else:
                return Response(serializer.data,status=status.HTTP_403_FORBIDDEN)
        except Exception:
            return Response(serializer.data,status=status.HTTP_403_FORBIDDEN)