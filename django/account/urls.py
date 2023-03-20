from django.urls import path
from account.views import SendPasswordResetEmailView, UserChangePasswordView, UserLoginView, UserProfileView, UserRegistrationView, UserPasswordResetView
from Listings.views import ListingCreateView,ListingDeleteView,ListingUpdateView,ListingListView,ListingDetailView
urlpatterns = [
    path('register/', UserRegistrationView.as_view(), name='register'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('profile/', UserProfileView.as_view(), name='profile'),
    path('changepassword/', UserChangePasswordView.as_view(), name='changepassword'),
    path('send-reset-password-email/', SendPasswordResetEmailView.as_view(), name='send-reset-password-email'),
    path('reset-password/<uid>/<token>/', UserPasswordResetView.as_view(), name='reset-password'),
    path("listings/", ListingListView.as_view(), name="listings"),
    path("listings/<int:pk>", ListingDetailView.as_view(), name="listings-desc"),
    path("listings/create/", ListingCreateView.as_view(), name="listings-create"),
    path("listings/update/<int:pk>", ListingUpdateView.as_view(), name="listings-update"),
    path("listings/delete/<int:pk>", ListingDeleteView.as_view(), name="listings-delete"),

]