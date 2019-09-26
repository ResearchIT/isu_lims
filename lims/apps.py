from django.apps import AppConfig
from iastatetheme.apps import IastatethemeConfig

class IsulimsThemeConfig(IastatethemeConfig):
    site_name = 'LIMS'

class LimsConfig(AppConfig):
    name = 'lims'
