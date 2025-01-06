import random

from django.shortcuts import render
#
from  rest_framework.response import Response
from  rest_framework.decorators import api_view
from .models import Quiz
from .serializers import QuizSerializer
# Create your views here.
@api_view(['GET'])
def helloApi(request):
    return Response('Hello Api world')

@api_view(['GET'])
def randomQuiz(request, id):
    totalQuizs = Quiz.objects.all()
    randomeQuiz = random.sample(list(totalQuizs), id)
    serializer = QuizSerializer(randomeQuiz, many=True)
    return Response(serializer.data)