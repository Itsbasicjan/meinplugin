# inventree_meinplugin/plugin.py
"""
Haupt-Plugin-Klasse für MeinPlugin mit Navigation und Panel.
"""

from plugin import InvenTreePlugin
# Benötigte Mixins importieren
from plugin.mixins import NavigationMixin, PanelMixin, UrlsMixin
# Die Ansicht importieren, zu der wir ein Panel hinzufügen wollen (z.B. Teiledetails)
from part.views import PartDetail
from django.urls import path
from .version import PLUGIN_VERSION
from . import views # Import für unsere eigene Plugin-Seite

# PanelMixin zur Vererbung hinzufügen
class MeinPlugin(PanelMixin, NavigationMixin, UrlsMixin, InvenTreePlugin):
    """
    Ein Beispielplugin mit Navigationslink (via Konstante) und Panel.
    """

    # --- Metadaten ---
    NAME = "MeinPlugin"
    SLUG = "meinplugin"
    TITLE = "Mein Cooles Plugin"
    DESCRIPTION = "Ein Beispielplugin mit Navigationslink und Panel." # Beschreibung aktualisiert
    VERSION = PLUGIN_VERSION
    AUTHOR = "Jan Schüler"

    # --- Navigation via Konstante ---
    # Explizit die Navigation für dieses Plugin aktivieren (gute Praxis)
    NAVIGATION_ENABLED = True
    # Definiere die Navigationslinks als Liste von Dictionaries
    NAVIGATION = [
        {
            'name': 'Coole Plugin Seite', # Name leicht geändert zum Testen
            'link': 'plugin:meinplugin:index', # Muss mit URL 'name' übereinstimmen
            'icon': 'fas fa-star', # Anderes Icon zum Testen
        },
        # Hier könnten weitere Links für dieses Plugin stehen
        # {'name': 'Zweiter Link', 'link': 'plugin:meinplugin:other', 'icon': '...'},
    ]
    # Optional: Ein gemeinsamer Reiter für die Links dieses Plugins
    # NAVIGATION_TAB_NAME = "Meine Tools"
    # NAVIGATION_TAB_ICON = 'fas fa-tools'


    # --- Panel Implementation ---
    # Diese Methode wird von InvenTree aufgerufen, um Panels für die aktuelle Ansicht zu erhalten
    def get_custom_panels(self, view, request):
        panels = [] # Eine Liste, da man mehrere Panels hinzufügen könnte

        # Prüfen: Sind wir auf der Detailansicht eines Teils (PartDetail)?
        if isinstance(view, PartDetail):
            # Ja! Holen wir uns das spezifische Teil-Objekt, das gerade angezeigt wird
            part = view.get_object()

            # Erstelle die Definition für unser Panel
            panels.append({
                'title': 'Mein Teil-Panel', # Titel des Panels
                'icon': 'fas fa-info-circle', # Icon für das Panel
                # --- Inhalt Option 1: Direkter HTML-Code ---
                'content': f'<h3>Panel von MeinPlugin</h3><p>Dieses Panel wird für das Teil <strong>{part.name}</strong> (PK: {part.pk}) angezeigt.</p><hr><p>Hier könnte spezifische Info oder Aktionen für dieses Teil stehen.</p>',

                # --- Inhalt Option 2: Template verwenden (besser für komplexere Inhalte) ---
                # 'content_template': 'meinplugin/mein_panel_inhalt.html', # Pfad zur Template-Datei
                # 'context': { # Daten, die an das Template übergeben werden sollen
                #     'anzeige_teil': part,
                #     'plugin_version': self.VERSION
                # }
            })

        # Hier könnte man auf andere Views prüfen:
        # elif isinstance(view, PurchaseOrderDetail):
        #     panels.append({...}) # Panel für Bestell-Details

        return panels # Gib die Liste der Panels für diese Ansicht zurück


    # --- URLs für die eigene Plugin-Seite ---
    # Diese Methode definiert die URL für die Seite, auf die der Navigationslink zeigt
    def setup_plugin_urls(self):
        return [
            path('', views.mein_plugin_view, name='index'),
            # path('other/', views.andere_ansicht, name='other'), # Falls zweiter Nav-Link genutzt wird
        ]

    # Die Methode setup_navbar_entries wird nicht mehr benötigt, wenn NAVIGATION verwendet wird!