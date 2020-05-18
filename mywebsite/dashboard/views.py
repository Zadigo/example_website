from django.shortcuts import render
from django.views import generic


class IndexView(generic.View):
    def get(self, request, *args, **kwargs):
        return render(request, 'index.html', {})

class ListItemsView(generic.ListView):
    model = None
    queryset = None
    template_name = 'pages/list.html'
    context_object_name = None

class ItemDetailsView(generic.DetailView):
    model = None
    queryset = None
    template_name = 'pages/details.html'
    context_object_name = 'product'
