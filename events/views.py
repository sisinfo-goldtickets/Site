from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Event
from django.shortcuts import render, get_object_or_404
from .forms import EventForm 
from django.views import generic
from django.urls import reverse_lazy

class EventListView(generic.ListView):
    model = Event
    template_name = 'events/index.html'

class EventDetailView(generic.DetailView):
    model = Event
    template_name = 'events/detail.html'

class EventCreateView(generic.CreateView):
    model = Event
    fields = ["name","description","location","event_date","price","photo_url"]
    template_name = 'events/create.html'
    success_url = reverse_lazy('events:index')

class EventUpdateView(generic.UpdateView):
    model = Event
    fields = ["name","description","location","event_date","price"]
    template_name = 'events/update.html'
    success_url = reverse_lazy('events:index')

class EventDeleteView(generic.DeleteView):
    model = Event
    fields = ["name","description","location","event_date","price"]
    template_name = 'events/delete.html'
    success_url = reverse_lazy('events:index')

def search_events(request):
    context = {}
    if request.GET.get('query', False):
        search_term = request.GET['query'].lower()
        event_list = Event.objects.filter(name__icontains=search_term)
        context = {"event_list": event_list}
    return render(request, 'events/search.html', context)