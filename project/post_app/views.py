from rest_framework import mixins
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.status import HTTP_201_CREATED, HTTP_204_NO_CONTENT
from rest_framework.viewsets import GenericViewSet

from .models import Post
from .serializers import PostSerializer


class PostViewSet(mixins.CreateModelMixin, GenericViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (IsAuthenticated,)

    @action(detail=True, methods=['post'])
    def like(self, request, pk=None):
        post = self.get_object()
        post.likes.add(self.request.user)
        return Response(status=HTTP_201_CREATED)

    @like.mapping.delete
    def unlike(self, request, pk=None):
        post = self.get_object()
        post.likes.remove(self.request.user)
        return Response(status=HTTP_204_NO_CONTENT)
