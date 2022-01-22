from rest_framework import mixins
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import GenericViewSet

from .models import Post
from .serializers import PostSerializer


class PostViewSet(mixins.CreateModelMixin, GenericViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (IsAuthenticated, )

    @action(detail=True, methods=['post'])
    def like(self, request, pk=None):
        pass

    @like.mapping.delete
    def unlike(self, request, pk=None):
        pass
