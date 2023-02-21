from django.db import models
from django.conf import settings
from django.urls import reverse
from django.utils import timezone
from django_extensions.db.fields import AutoSlugField


class Category(models.Model):
    """Categorie utilisée pour classer les astuces."""

    name = models.CharField('tip category', max_length=150)
    slug = AutoSlugField(
        "tip slug",
        populate_from=['name'],
        unique=True,
    )

    class Meta:
        verbose_name_plural = "categories"

    def __str__(self):
        return self.name


class Tip(models.Model):
    """Astuce publiée par PlacePython."""

    title = models.CharField("tip title", max_length=255)
    slug = AutoSlugField(
        "tip slug",
        populate_from=['title'],
        unique=True,
    )
    summary = models.TextField("tip summary", blank=True)
    body = models.TextField("tip body text", blank=True)
    categories = models.ManyToManyField("Category", related_name="tips")
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="tips"
    )
    image = models.ImageField("tip image", upload_to="tips/images/")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        """Retourne l'url vers la vue détaillée de l'astuce."""
        return reverse('tips:detail', kwargs={'slug': self.slug})
