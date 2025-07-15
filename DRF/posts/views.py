from rest_framework.request import Request
from rest_framework.response import Response 
from rest_framework import status
from rest_framework.decorators import api_view

@api_view(http_method_names= ["GET"])
def homepage(request:Request):
    ans = {"message": "heyyy haven"}
    return Response(data=ans, status= status.HTTP_200_OK)
