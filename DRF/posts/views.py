from rest_framework.request import Request
from rest_framework.response import Response 
from rest_framework import status
from rest_framework.decorators import api_view

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
    return Response(data=posts, status= status.HTTP_200_OK)
@api_view(["GET"])
def post_detail(request:Request, post_index:int):
    post = posts[post_index]
    if post:
        return Response(data=post, status= status.HTTP_200_OK)
    return Response(data={"error":"Post not found"}, status= status.HTTP_404_NOT_FOUND)
posts = [
  {
    "id": 1,
    "title": "Why is it difficult to learn Programming?",
    "content": "This is to give reasons why it is hard"
  },
  {
    "id": 2,
    "title": "Learn JavaScript",
    "content": "This is a course on JS"
  },
  {
    "id": 3,
    "title": "Python for Beginners",
    "content": "This post covers the basics of Python programming."
  }
]
