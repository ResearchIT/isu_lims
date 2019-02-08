from django.db import models

###########
# Theme wide settings like site title
###########
class SiteTheme(models.Model):
    site_name = models.CharField(max_length=50)

    def __str__(self):
        return self.site_name
