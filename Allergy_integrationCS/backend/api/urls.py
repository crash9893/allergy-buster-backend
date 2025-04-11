from django.urls import path
from . import views
from firebase_auth.views import verify_firebase_token  # 🔸 add this import

urlpatterns = [
    path('check_allergies/', views.check_allergies),
    path('verify-token/', verify_firebase_token),       # 🔸 add this line
]
