from django.db import models


class Restaurant(models.Model):
    name = models.CharField(max_length=50)
    street_addr = models.CharField(max_length=256)
    bunji_addr = models.CharField(max_length=256)
    avg_rating = models.DecimalField(max_digits=3, decimal_places=2)
    lat = models.FloatField()
    lng = models.FloatField()
    operation_hr = models.CharField(max_length=512)
    main_img = models.URLField()
