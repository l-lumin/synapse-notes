from django.urls import path
from notes.views import NoteListCreateView, NoteDetailView, TagListCreateView

urlpatterns = [
    path('notes/', NoteListCreateView.as_view(), name='note-list-create'),
    path('notes/<int:pk>/', NoteDetailView.as_view(), name='note-detail'),
    path('tags/', TagListCreateView.as_view(), name='tag-list-create'),
]