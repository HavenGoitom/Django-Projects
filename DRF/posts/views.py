from rest_framework.request import Request
from rest_framework.response import Response 
from rest_framework import status
from rest_framework.decorators import api_view
from .models import Post
from .serializers import PostSerializer
@api_view(["GET", "POST"])
def homepage(request:Request):
    if request.method == "POST":
        data = request.data
        ans = {"message": "heyyy haven", "data":data}
        return Response(data=ans, status= status.HTTP_201_CREATED)
    ans = {"message": "heyyy haven"}
    return Response(data=ans, status= status.HTTP_200_OK)
@api_view(["GET"])
def list_posts(request:Request):
    posts = Post.objects.all()
    
    serializer= PostSerializer(instance=posts, many=True)
    response={
        "message":"posts",
        "data": serializer.data
    }
    return Response(data=response, status= status.HTTP_200_OK)
@api_view(["GET"])
def post_detail(request:Request, post_index:int):
    post = Post[post_index]
    if post:
        return Response(data=post, status= status.HTTP_200_OK)
    return Response(data={"error":"Post not found"}, status= status.HTTP_404_NOT_FOUND)


