from django.shortcuts import render
from django.views.generic import TemplateView
from .services.signature import save_signature_image
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent


class SignatureFormPageView(TemplateView):
    template_name = "signatures/signature_form.html"

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)
        return context


class SignatureResultPageView(TemplateView):
    template_name = "signatures/signature_result.html"

    def post(self, request, *args, **kwargs):
        name = request.POST.get("name")
        signature = request.POST.get("signature")

        save_signature_image(signature)

        image_path = BASE_DIR / "signatures" / "static" / "images" / "signature.png"

        context = {
            "name": name,
            "signature_exists": image_path.exists(),
        }

        return self.render_to_response(context)
