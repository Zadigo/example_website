from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views import generic
from dashboard import models
try:
    from accounts import models as accounts_models
except:
    from django.contrib.auth import get_user_model
    USER = get_user_model()

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

class ListUsersView(generic.ListView):
    model = accounts_models.MyUser
    queryset = accounts_models.MyUser.objects.all()
    template_name = 'pages/profiles.html'
    context_object_name = 'users'

class UserDetailsView(generic.DetailView):
    model = accounts_models.MyUser
    queryset = accounts_models.MyUser.objects.all()
    template_name = 'pages/profile.html'
    context_object_name = 'user'

class CreateNewView(generic.View):
    def get(self, request, *args, **kwargs):
        return render(request, 'pages/create.html')

class UpdateItemView(generic.View):
    def get(self, request, *args, **kwargs):
        return render(request, 'pages/create.html')