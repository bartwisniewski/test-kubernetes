from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView, DeleteView, UpdateView, FormView
from django.urls import reverse_lazy
from django.contrib import messages

from clientapp.forms import ClientForm
from clientapp.serializers import ClientSerializer
from clientapp.api_logic import calculate

# Create your views here.
class ClientFormView(FormView):
    template_name = "clientapp/client.html"
    form_class = ClientForm
    success_url = reverse_lazy("client-form")

    def form_valid(self, form):
        result = calculate(form)
        if result:
            self.success_url = reverse_lazy(
                "client-result", kwargs={"result": result}
            )
        else:
            messages.warning(self.request, "api did not respond correctly")
        return super().form_valid(form)


class ClientResultView(TemplateView):
    template_name = "clientapp/client_result.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["result"] = self.kwargs.get("result", None)
        return context
