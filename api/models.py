from django.db import models
from random import choices
from string import ascii_letters
from django.conf import settings


class Link(models.Model):
    original_link = models.URLField()
    shortened_link = models.URLField(blank=True, null=True)
    SHIRT_SIZES = (
        ('.su', '.su'),
        ('.ru', '.ru'),
        ('.com', '.com'),
    )
    shortener_link_end = models.CharField(max_length=30, choices=SHIRT_SIZES)
    clicked = models.IntegerField(default=0, help_text="not enter")

    def shortener(self):
        while True:
            random_string = ''.join(choices(ascii_letters, k=6)) + self.shortener_link_end
            new_link = settings.HOST_URL + '/' + random_string

            if not Link.objects.filter(shortened_link=new_link).exists():
                break

        return new_link

    def save(self, *args, **kwargs):
        if not self.shortened_link:
            new_link = self.shortener()
            self.shortened_link = new_link
        return super().save(*args, **kwargs)
