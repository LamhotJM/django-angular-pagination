from django.shortcuts import render

# Create your views here.
from seTest.models import State
from seTest.serializers import StateSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class StateList(APIView):

    """
    List all state or create a new state
    """

    def get(self, request, format=None):
        pageNum = int(request.GET.get("pageNum"))
        pageSize = int(request.GET.get("pageSize"))
        begin = (int(pageNum) - 1) * pageSize
        end = begin + pageSize
        states = State.objects.all().order_by('title')[begin:end]
        totalStates = State.objects.count()
        serializer = StateSerializer(states, many=True)
        response = {'statesList': serializer.data, 'totalStates': totalStates}
        return Response(response)

    def post(self, request, format=None):
        serializer = StateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
