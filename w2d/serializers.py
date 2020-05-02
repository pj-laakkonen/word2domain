from rest_framework import serializers
from . import models


class WordCollectionENSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
                'id',
                'word',
        )
        model = models.WordCollectionEN
