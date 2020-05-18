from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views import generic
from dashboard import models

class IndexView(generic.View):
    def get(self, request, *args, **kwargs):
        context = {
            'total_likes': models.DashboardSetting\
                                .dashboard_manager.sum_of_likes()['likes__sum']
        }
        return render(request, 'index.html', context)

class ListItemsView(generic.ListView):
    model = models.DashboardSetting
    queryset = models.DashboardSetting.objects.all()
    template_name = 'pages/list.html'
    context_object_name = 'celebrities'

class ItemDetailsView(generic.DetailView):
    model = models.DashboardSetting
    queryset = models.DashboardSetting.objects.all()
    template_name = 'pages/details.html'
    context_object_name = 'celebrity'
