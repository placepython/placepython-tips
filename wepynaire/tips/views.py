from django.views.generic import ListView, DetailView
from .models import Tip, Category


class TipListView(ListView):
    model = Tip
    context_object_name = "tips"
    template_name = "tips/home.html"

    def get_queryset(self):
        qs = super().get_queryset()
        category = self.request.GET.get("category")
        if category is not None:
            qs = qs.filter(categories__slug=category)
        return qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["categories"] = Category.objects.all()
        return context


home = TipListView.as_view()


class TipDetailView(DetailView):
    model = Tip
    context_object_name = "tip"
    template_name = "tips/detail.html"


detail_view = TipDetailView.as_view()
