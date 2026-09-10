from django.urls import path
from .views import SignatureFormPageView, SignatureResultPageView
from django.views.generic import RedirectView

urlpatterns = [
    path(
        "",
        RedirectView.as_view(
            url="/signature/",
            permanent=False,
        ),
        name="home",
    ),
    path("signature/", SignatureFormPageView.as_view(), name="signature_form"),
    path(
        "signature/result/", SignatureResultPageView.as_view(), name="signature_result"
    ),
]
