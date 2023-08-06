from django.shortcuts import render
from .models import User, Post, Like
from .serializers import UserSerializer, PostSerializer, LikeSerializer
from django.http import HttpResponse
from rest_framework import status
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from .models import User




class UserAPI(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"data": serializer.data, "msg": "User created successfully"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, user_id):
        user = get_object_or_404(User, pk=user_id)
        serializer = UserSerializer(user)
        return Response({"data": serializer.data, "msg": "User created successfully"})

    def put(self, request, user_id):
        user = get_object_or_404(User, pk=user_id)
        serializer = UserSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"data": serializer.data, "msg": "User created successfully"})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, user_id):
        user = get_object_or_404(User, pk=user_id)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class PostAPI(APIView):
    def post(self, request):
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"data": serializer.data, "msg": "Post is created successfully"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def get(self, request, post_id=None):  
        print(request.user)
        if post_id is not None:
            # If post_id is provided, get a single post by post_id
            post = get_object_or_404(Post, pk=post_id)
            serializer = PostSerializer(post)
            return Response({"data": serializer.data, "msg": "Post View successfully"})
        else:
            # If post_id is not provided, get all posts
            posts = Post.objects.all()
            serializer = PostSerializer(posts, many=True)
            return Response(serializer.data)


    
    def put(self, request, post_id):
        post = get_object_or_404(Post, pk=post_id)
        if request.data['author'] == post.author:
            serializer = PostSerializer(post, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({"data": serializer.data, "msg": "Post Updated successfully"})
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, post_id):
        post = get_object_or_404(Post, pk=post_id)
        post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class LikeAPI(APIView):
    def post(self, request):
        serializer = LikeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"data": serializer.data, "msg": "Like is created successfully"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, like_id):
        like = get_object_or_404(Like, pk=like_id)
        serializer = LikeSerializer(like)
        return Response({"data": serializer.data, "msg": "Like is viewed successfully"})

    def put(self, request, like_id):
        like = get_object_or_404(Like, pk=like_id)
        serializer = LikeSerializer(like, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"data": serializer.data, "msg": "Like is Updated successfully"})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, like_id):
        like = get_object_or_404(Like, pk=like_id)
        like.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)