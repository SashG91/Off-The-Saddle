from django.shortcuts import render
from django.views import generic
from .models import Climb
from django.views.generic import ListView
from django.views.generic import DetailView
from django.views.generic import UpdateView
from django.views.generic import DeleteView
from django.views.generic import CreateView
from django.views.generic import TemplateView


class ClimbList(generic.ListView):
    """
    Climb List View
    """
    model = Climb
    queryset = Climb.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'
    paginate_by = 6


class ClimbDetail(DetailView):
    """
    Climb Detail View
    """
    model = Climb
    template_name = 'climb_detail.html'

    def get_context_data(self, **kwargs):
        context['ride_times'] = RideTime.objects.filter(
            climb=pk).order_by('-time')

class AddClimbTime(CreateView): 
    """
    Create Climb Time View
    """
    model = RideTime 
    template_name = 'add_climb.html'
    path('<slug:slug>/add_time', views.AddClimbTime.as_view(), name='add_time')
    
