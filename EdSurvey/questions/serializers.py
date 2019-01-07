# questions.api
from rest_framework import serializers

from .models import Question


class QuestionSerializer(serializers.ModelSerializer):
    """
    Serializing all the Question
    """
    class Meta:
        model = Question
        # fields = ('id', 'name', 'description', 'qtype', 'public', 'owner', 'active', 'arcived',)
        fields = ('id', 'name',)