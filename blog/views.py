from .serializers import ArticleSerializers
from rest_framework import generics
from .models import Article
from .permissions import IsOwnerOrReadOnly
from rest_framework.permissions import IsAuthenticated, IsAdminUser

class ArticleCreateView(generics.CreateAPIView):
    serializer_class = ArticleSerializers

class ArticleListView(generics.ListAPIView):
    serializer_class = ArticleSerializers
    queryset = Article.objects.all()
    permission_classes = (IsAdminUser, )

class ArticleRetriveView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ArticleSerializers
    queryset = Article.objects.all()
    permission_classes = (IsOwnerOrReadOnly, )
