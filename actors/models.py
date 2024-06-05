from django.db import models


NATIONALITY_CHOICES = (
    ('EUA', 'Estados Unidos'),
    ('BR', 'Brasil'),
    ('OUTROS', 'Outros'),
)


class Actor(models.Model):
    name = models.CharField(max_length=200)
    birthday = models.DateField(null=True, blank=True)
    nationality = models.CharField(max_length=100, null=True, blank=True, choices=NATIONALITY_CHOICES)

    def __str__(self):
        return self.name
