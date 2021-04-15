from django.db import models

# Create your models here.


class Certificate(models.Model):
    sr_no = models.AutoField(primary_key=True)
    h2_tag = models.CharField(max_length=200)
    img = models.ImageField(upload_to="images/certificate", height_field=None, width_field=None)

    def __str__(self):
        return self.h2_tag
    

