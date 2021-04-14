from django.db import models

# Create your models here.
class Pic(models.Model):
    name = models.CharField("Название", max_length=50)
    descr = models.CharField("Описание", max_length=200)
    pic = models.ImageField("Изображение", upload_to="images")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Изображение"
        verbose_name_plural = "Изображения"