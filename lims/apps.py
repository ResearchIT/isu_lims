from django.apps import AppConfig
from iastatetheme.apps import IastatethemeConfig, MenuItem

class IsulimsThemeConfig(IastatethemeConfig):
    site_name = 'LIMS'
    menu = [
        MenuItem("Tables", "/", [
            MenuItem("Genera", "/genera"),
            MenuItem("Subgenera", "/subgenera"),
            MenuItem("Genomes", "/genome"),
            MenuItem("Species", "/species"),
            MenuItem("Accessions", "/accession"),
            MenuItem("Plant", "/plant"),
            MenuItem("Seed Packets", "/seedpacket"),
            MenuItem("Projects", "/project"),
            MenuItem("Samples", "/sample"),
            MenuItem("Herbariums", "/herbarium"),
        ]),
        MenuItem("Admin", "/admin"),
    ]
    header_site_links_menu = []
    footer_social_media_menu = []

class LimsConfig(AppConfig):
    name = 'lims'
