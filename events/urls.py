from django.urls import path

from . import views

app_name = 'events'
urlpatterns = [
    path('', views.EventListView.as_view(), name='index'),  # edite esta linha
    path('<int:pk>/', views.EventDetailView.as_view(), name='detail'), # adicione esta linha
    path('search/', views.search_events, name='search'), # adicione esta linha
    path('create/', views.EventCreateView.as_view(), name='create'), # adicione esta linha
    path('update/<int:pk>/', views.EventUpdateView.as_view(), name='update'),
    path('delete/<int:pk>/', views.EventDeleteView.as_view(), name='delete'),
    path('<int:post_id>/comment/', views.create_comment, name='comment'),
    path('categories/', views.CategoryListView.as_view(), name='categories'),
    path('categories<int:pk>', views.CategoryDetailView.as_view(), name='detail-category'),
]