# inventree_meinplugin/__init__.py
"""
Plugin Paket für MeinPlugin.
"""

# Importiere die Plugin-Klasse, damit sie von InvenTree entdeckt wird
from .inventree_meinplugin.plugin import MeinPlugin

# Optional: Definiere Metadaten für das Paket
__version__ = "0.1.0"
__author__ = "Jan Schüler"

# Stelle sicher, dass die Plugin-Klasse verfügbar ist
__all__ = [
    'MeinPlugin',
]