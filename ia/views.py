import json
import google.generativeai as genai
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view # type: ignore
from rest_framework import status
import requests


@api_view(['POST'])
def chatia(request):
    API_KEY = "AIzaSyByHrrbBQsnRt3WUZqxV7dTLAcHKiEM8GI"
    genai.configure(api_key = API_KEY)
    model = genai.GenerativeModel(
        model_name = "gemini-2.0-flash"
    )
    contexto = "responde como vegeta :"
    data = json.loads(request.body)
    pregunta = data.get("pregunta")
    response = model.generate_content(contexto + pregunta)
    return Response(response.text)

#prueba