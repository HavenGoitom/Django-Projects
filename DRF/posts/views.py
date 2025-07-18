from rest_framework.request import Request
from rest_framework.response import Response 
from rest_framework import status,generics,mixins
from rest_framework.decorators import api_view, APIView
from .models import Post
from .serializers import PostSerializer
from django.shortcuts import get_object_or_404

@api_view(["GET", "POST"])
def homepage(request:Request):
    if request.method == "POST":
        data = request.data
        ans = {"message": "this is the homepage!", "data":data}
        return Response(data=ans, status= status.HTTP_201_CREATED)
    ans = {"message": "this is the homepage!"}
    return Response(data=ans, status= status.HTTP_200_OK)

class PostListCreateView(
    generics.GenericAPIView, 
    mixins.ListModelMixin,
    mixins.CreateModelMixin):
    """
        a view for creating and listing posts
    """
    serializer_class = PostSerializer
    queryset = Post.objects.all()
    def get(self, request: Request, *args, **kwargs):
        return self.list(request,*args, **kwargs )
    def post(self, request: Request, *args, **kwargs):
        return self.create(request,*args, **kwargs )


    """serializer_class= PostSerializer
    def get(self, request: Request, *args, **kwargs):
        posts = Post.objects.all()
        serializer = self.serializer_class(instance=posts, many=True)
        return Response(data= serializer.data, status= status.HTTP_200_OK)
    def post(self, request: Request, *args, **kwargs):
        data = request.data
        serializer = self.serializer_class(data = data)
        if serializer.is_valid():
            serializer.save()
            response ={"message": "Post created","data": serializer.data }
            return Response(data =response , status=status.HTTP_201_CREATED)
        return Response(data= serializer.errors, status=status.HTTP_400_BAD_REQUEST)"""
            
class PostRetrieveupdateDeleteView(
    generics.GenericAPIView, 
    mixins.RetrieveModelMixin, 
    mixins.UpdateModelMixin, 
    mixins.DestroyModelMixin):
    """
    A view for getting a post by an id and deleting and
    retrieving a post.
    """
    serializer_class = PostSerializer
    queryset = Post.objects.all()
    def get(self, request: Request, *args, **kwargs):
        return self.retrieve(request,*args, **kwargs )
    def put(self, request: Request, *args, **kwargs):
        return self.update(request,*args, **kwargs )
    def delete(self, request: Request, *args, **kwargs):
        return self.delete(request,*args, **kwargs )
    


    """serializer_class = PostSerializer
    def get(self, request:Request, post_id:int):
        post = get_object_or_404(Post, pk = post_id)
        serializer = self.serializer_class(instance = post)
        return Response(data = serializer.data, status = status.HTTP_200_OK)
    def put(self, request:Request, post_id:int):
        post = get_object_or_404(Post, pk = post_id)
        data = request.data
        serializer = self.serializer_class(instance = post, data = data)
        if serializer.is_valid():
            serializer.save()
            response = {"message": "Post has been updated!", "data": serializer.data}
            return Response(data=response, status=status.HTTP_200_OK)
        return Response(data= serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request:Request, post_id:int):
        post = get_object_or_404(Post, pk = post_id)
        post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)"""
        

