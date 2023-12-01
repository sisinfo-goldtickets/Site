from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Event, Comment, Category
from django.shortcuts import render, get_object_or_404
from .forms import EventForm 
from django.views import generic
from django.urls import reverse_lazy
from .forms import CommentForm

class EventListView(generic.ListView):
    model = Event
    template_name = 'events/index.html'

class EventDetailView(generic.DetailView):
    model = Event
    template_name = 'events/detail.html'

class EventCreateView(generic.CreateView):
    model = Event
    template_name = 'events/create.html'
    success_url = reverse_lazy('events:index')
    form_class = EventForm

class EventUpdateView(generic.UpdateView):
    model = Event
    template_name = 'events/update.html'
    success_url = reverse_lazy('events:index')
    form_class = EventForm

class EventDeleteView(generic.DeleteView):
    model = Event
    template_name = 'events/delete.html'
    success_url = reverse_lazy('events:index')
    form_class = EventForm

def search_events(request):
    context = {}
    if request.GET.get('query', False):
        search_term = request.GET['query'].lower()
        event_list = Event.objects.filter(name__icontains=search_term)
        context = {"event_list": event_list}
    return render(request, 'events/search.html', context)

def create_comment(request, event_id):
    event = get_object_or_404(Event, pk=event_id)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            review_author = request.user # modificar esta linha

class CategoryListView(generic.ListView):
    model = Category
    template_name = 'events/categories.html' 

class CategoryDetailView(generic.DetailView):
    model = Category
    template_name = 'events/detail_category.html'