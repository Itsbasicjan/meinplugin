# inventree_meinplugin/views.py
"""
Views für das MeinPlugin Plugin.
"""

from django.shortcuts import render
from django.http import HttpRequest, HttpResponse

def mein_plugin_view(request: HttpRequest) -> HttpResponse:
    """
    Rendert die Hauptseite für das MeinPlugin.
    """
    # Kontextdaten, die an das Template übergeben werden
    context = {
        'page_title': 'Mein Plugin Seite',
        'message': 'Willkommen auf der Seite meines InvenTree Plugins!',
    }
    # Rendert das HTML-Template und übergibt den Kontext
    # Wichtig: Verwende den Namespace des Templates ('meinplugin/')
    return render(request, 'meinplugin/mein_plugin_seite.html', context)

# Hier könntest du weitere View-Funktionen definieren
# def andere_ansicht(request: HttpRequest) -> HttpResponse:
#     ...