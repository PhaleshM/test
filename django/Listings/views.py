from rest_framework.generics import CreateAPIView ,RetrieveUpdateDestroyAPIView,DestroyAPIView,ListAPIView,RetrieveAPIView
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, FormParser
from .models import Listing
from django.shortcuts import get_object_or_404
from .serializers import ListingSerializers
from rest_framework.permissions import SAFE_METHODS, IsAuthenticated, IsAuthenticatedOrReadOnly, BasePermission, IsAdminUser, DjangoModelPermissions, AllowAny



class ListingCreateView(CreateAPIView):
    parser_class = [MultiPartParser, FormParser]
    serializer_class = ListingSerializers

class ListingListView(ListAPIView):
    permission_classes = []
    # queryset = Post.postobjects.all()
    serializer_class = ListingSerializers
    
    queryset=Listing.listsobjects.all()

class ListingDetailView(RetrieveAPIView):
    permission_classes = []
    serializer_class = ListingSerializers

    def get_object(self, queryset=None, **kwargs):
        item = self.kwargs.get('pk')
        return get_object_or_404(Listing, id=item)

class ListingUpdateView(RetrieveUpdateDestroyAPIView):
    permission_classes=[]
    queryset=Listing.objects.all()
    serializer_class = ListingSerializers

class ListingDeleteView(DestroyAPIView):
    permission_classes=[]
    queryset=Listing.objects.all()
    serializer_class=ListingSerializers

# def get_queryset(self):
    #     user=self.request.user
    #     return Post.objects.filter(author=user)

# class UserRegistrationView(CreateAPIView):
#   renderer_classes = [UserRenderer]
#   serializer_class = ListingSerializers
#   def post(self, request, format=None):
#     serializer = UserRegistrationSerializer(data=request.data)
#     serializer.is_valid(raise_exception=True)
#     user = serializer.save()
#     token = get_tokens_for_user(user)
#     return Response({'token':token, 'msg':'Registration Successful'}, status=status.HTTP_201_CREATED)