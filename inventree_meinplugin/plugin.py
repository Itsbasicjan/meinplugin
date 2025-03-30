# inventree_meinplugin/plugin.py
"""
Einfaches Plugin mit Navigation und Panel für Lagerorte (Stock Locations).
Stellt sicher, dass normale Leerzeichen für die Einrückung verwendet werden!
"""
from plugin import InvenTreePlugin
from plugin.mixins import NavigationMixin, PanelMixin, UrlsMixin
# View für Lagerort-Details importieren
from stock.views import StockLocationDetail
from django.urls import path
from .version import PLUGIN_VERSION
from . import views # Für die eigene Plugin-Seite (views.py)

class MeinPlugin(PanelMixin, NavigationMixin, UrlsMixin, InvenTreePlugin):
    """
    Fügt Navigationslink hinzu und zeigt ein Panel auf Lagerort-Detailseiten.
    """
    # --- Metadaten ---
    NAME = "MeinPlugin"
    SLUG = "meinplugin"
    TITLE = "Mein Cooles Plugin"
    DESCRIPTION = "Plugin mit Nav-Link und Stock Location Panel."
    VERSION = PLUGIN_VERSION # Stellt sicher, dass version.py existiert und die Variable definiert
    AUTHOR = "Jan Schüler"

    # --- Navigation (über Konstante) ---
    NAVIGATION_ENABLED = True # Sicherstellen, dass Navigation an ist
    NAVIGATION = [
        {
            'name': 'Plugin Hauptseite', # Angezeigter Text im Menü
            'link': 'plugin:meinplugin:index', # Interner URL-Name
            'icon': 'fas fa-plug', # Icon
        },
    ]

    # --- Panel für Lagerort-Details ---
    def get_custom_panels(self, view, request):
        panels = [] # Liste für Panels, die auf dieser Seite angezeigt werden sollen

        # Prüfen: Ist die aktuelle Ansicht die Detailansicht eines Lagerortes?
        if isinstance(view, StockLocationDetail):
            # Ja -> Das Lagerort-Objekt aus der Ansicht holen
            location = view.get_object()

            # Panel-Definition erstellen und zur Liste hinzufügen
            panels.append({
                'title': 'Lagerort Info Panel', # Titel des Panels in der Seitenleiste
                'icon': 'fas fa-info-circle', # Icon in der Seitenleiste
                'content': f'<h3>Zusatzinfos für Lagerort "{location.name}"</h3><p>ID: {location.pk}</p><p>Pfad: {location.pathstring}</p><hr><p><em>Dieses Panel wurde von MeinPlugin hinzugefügt.</em></p>', # Der HTML-Inhalt des Panels
                # 'content_template': 'meinplugin/mein_lagerort_panel.html', # Alternative: Template-Datei
                # 'context': {'lagerort': location}, # Daten für das Template
            })
        # Gib die Liste der Panels zurück (kann leer sein, wenn wir nicht auf der richtigen Seite sind)
        return panels

    # --- URL für die eigene Seite des Plugins ---
    # Definiert, was unter /plugin/meinplugin/ erreichbar ist
    def setup_plugin_urls(self):
        return [
            # Leerer Pfad ('') unter /plugin/meinplugin/ ruft die Funktion 'mein_plugin_view'
            # aus der views.py auf. Der Name 'index' wird für den Navigationslink verwendet.
            path('', views.mein_plugin_view, name='index'),
        ]