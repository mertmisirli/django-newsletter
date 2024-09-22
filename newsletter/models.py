from django.db import models

class NewsletterCategory(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title  # Kategori adı burada gösterilecek



class Newsletter(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    category = models.ForeignKey(NewsletterCategory, on_delete=models.CASCADE, related_name='newsletters')

    def __str__(self):
        return self.title  # Bülten adı burada gösterilecek
