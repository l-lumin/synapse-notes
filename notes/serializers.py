import spacy
from rest_framework import serializers

from notes.models import Note, Tag

nlp = spacy.load("en_core_web_sm")


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = "__all__"


class NoteSerializer(serializers.ModelSerializer):
    tags = TagSerializer(many=True, read_only=True)

    class Meta:
        model = Note
        fields = "__all__"

    def create(self, validated_data):
        tags_data = validated_data.pop("tags")
        note = Note.objects.create(**validated_data)

        doc = nlp(note.content)
        for ent in doc.ents:
            tag, _ = Tag.objects.get_or_create(name=ent.text)
            note.tags.add(tag)

        for tag_data in tags_data:
            tag, _ = Tag.objects.get_or_create(name=tag_data["name"])
            note.tags.add(tag)
        return note
