from django import forms
from .models import Event, Comment

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = [
            'name',
            'description',
            'location',
            'event_date',
            'price',
            'photo_url'
        ]
        labels = {
            'name': 'Nome',
            'description': 'Descrição',
            'location': 'Local',
            'event_date': 'Data do Evento',
            'price': 'Valor do Ingresso',
            'photo_url': 'URL da foto'
        }

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = [
            'text',
        ]
        labels = {
            'text': 'Comentário',
        }
