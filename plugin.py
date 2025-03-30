# inventree_meinplugin/plugin.py
"""
Haupt-Plugin-Klasse für MeinPlugin.
"""

from plugin import InvenTreePlugin
from plugin.mixins import NavigationMixin, UrlsMixin # Mixins für Navigationsleiste und URLs
from django.urls import path, include

# Importiere die Version aus der version.py
from .version import PLUGIN_VERSION
# Importiere die Views, die wir später definieren
from . import views

class MeinPlugin(NavigationMixin, UrlsMixin, InvenTreePlugin): # Erbt von Mixins und Basisklasse
    """
    Ein einfaches Beispiel-Plugin für InvenTree.
    Fügt einen Eintrag zur Navigationsleiste hinzu.
    """

    # Metadaten des Plugins
    NAME = "MeinPlugin"  # Interner Name
    SLUG = "meinplugin"  # Eindeutiger Slug (wird in URLs, etc. verwendet) - nur Kleinbuchstaben/Zahlen/-/_
    TITLE = "Mein Cooles Plugin" # Angezeigter Titel
    DESCRIPTION = "Ein einfaches Beispielplugin, das einen Navigationslink hinzufügt."
    VERSION = PLUGIN_VERSION
    AUTHOR = "Jan Schüler"

    # Definiert den Eintrag in der Navigationsleiste
    def setup_navbar_entries(self):
        """
        Gibt eine Liste von Navigationsleisten-Einträgen zurück.
        Jeder Eintrag ist ein Dictionary.
        """
        return {
            # Eindeutiger Schlüssel für diesen Eintrag
            'meinplugin_index': {
                'name': 'Mein Plugin',  # Text, der in der Navigationsleiste angezeigt wird
                'link': 'plugin:meinplugin:index', # URL-Name (Plugin-Slug:URL-Name aus setup_plugin_urls)
                'icon': 'fas fa-plug', # Optional: FontAwesome Icon-Klasse (stelle sicher, dass FA geladen ist)
            }
        }

    # Definiert die URL-Routen für dieses Plugin
    def setup_plugin_urls(self):
        """
        Gibt eine Liste von URL-Mustern für dieses Plugin zurück.
        Diese werden unter dem Namespace des Plugin-Slugs gemountet.
        z.B. /plugin/meinplugin/
        """
        return [
            # Pfad für die Hauptseite des Plugins
            # '' bedeutet die Basis-URL des Plugins (/plugin/meinplugin/)
            # views.mein_plugin_view ist die Funktion in views.py, die aufgerufen wird
            # name='index' ist der Name dieser URL, verwendet im 'link' oben
            path('', views.mein_plugin_view, name='index'),
            # Hier könntest du weitere URLs für dein Plugin hinzufügen
            # path('andere-seite/', views.andere_ansicht, name='andere_seite'),
        ]