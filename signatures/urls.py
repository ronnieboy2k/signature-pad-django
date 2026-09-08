from django.urls import path
from .views import SignatureFormPageView, SignatureResultPageView

urlpatterns = [
    path("signature/", SignatureFormPageView.as_view(), name="signature_form"),
    path(
        "signature/result/", SignatureResultPageView.as_view(), name="signature_result"
    ),
]
