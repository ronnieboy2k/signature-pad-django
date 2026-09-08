from django.shortcuts import render
from django.views.generic import TemplateView


class SignatureFormPageView(TemplateView):
    template_name = "signatures/signature_form.html"

    def get_context_date(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
