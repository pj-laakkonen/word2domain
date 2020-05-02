from django.db import models


class WordCollectionEN(models.Model):
    word = models.CharField(max_length=100)

    def __str__(self):
        """A string representation of the model."""
        return self.word
