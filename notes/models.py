from django.db import models

class Tag(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

class Note(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    tags = models.ManyToManyField(Tag, related_name='notes')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class Relationship(models.Model):
    note_a = models.ForeignKey(Note, on_delete=models.CASCADE, related_name='related_from')
    note_b = models.ForeignKey(Note, on_delete=models.CASCADE, related_name='related_to')
    similarity_score = models.FloatField(default=0)
