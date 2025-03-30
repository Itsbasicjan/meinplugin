# setup.py
# -*- coding: utf-8 -*-

import setuptools
import os

# Lese die Plugin-Version dynamisch aus der version.py-Datei
# Stellt sicher, dass die Version nur an einer Stelle definiert ist.
try:
    from inventree_meinplugin.version import PLUGIN_VERSION
except ModuleNotFoundError:
    # Fallback, falls etwas beim Import schiefgeht oder die Datei fehlt
    # Sollte aber nicht passieren bei korrekter Struktur
    print("WARNUNG: Konnte PLUGIN_VERSION nicht aus inventree_meinplugin.version importieren.")
    PLUGIN_VERSION = "0.0.0" # Standard-Fallback

# Lese die README.md für die lange Beschreibung
# Stellt sicher, dass die Beschreibung auf PyPI etc. gut aussieht.
try:
    with open('README.md', encoding='utf-8') as f:
        long_description = f.read()
except FileNotFoundError:
    long_description = "Ein Beispielplugin für InvenTree mit Navigation und Panel." # Fallback

setuptools.setup(
    # Name des Pakets, wie er auf PyPI oder bei pip install erscheint
    name="inventree-meinplugin",

    # Version des Pakets, dynamisch aus version.py gelesen
    version=PLUGIN_VERSION,

    # Autor-Informationen
    author="Jan Schüler", # Dein Name
    author_email="deine-email@example.com", # Füge deine E-Mail hinzu

    # Kurze Beschreibung
    description="Ein Beispielplugin für InvenTree mit Navigation und Panel.",

    # Lange Beschreibung aus der README.md
    long_description=long_description,
    long_description_content_type='text/markdown',

    # Schlüsselwörter zur einfacheren Suche
    keywords="inventree meinplugin custom panel navigation",

    # URL zum Repository oder zur Projekt-Homepage
    url="https://github.com/Itsbasicjan/meinplugin", # Dein Repository

    # Lizenz des Plugins
    license="MIT", # Oder deine gewählte Lizenz

    # Pakete, die im Projekt enthalten sind.
    # find_packages() sucht automatisch nach allen Verzeichnissen mit einer __init__.py
    # include=["inventree_meinplugin*"] stellt sicher, dass nur dein Plugin-Paket gefunden wird.
    packages=setuptools.find_packages(where=".", include=["inventree_meinplugin*"]),

    # Abhängigkeiten, die dein Plugin ZUSÄTZLICH zu InvenTree benötigt.
    # Für unser einfaches Beispiel brauchen wir erstmal keine.
    install_requires=[],

    # Abhängigkeiten, die nur für den Build-Prozess benötigt werden (selten nötig für einfache Plugins)
    # setup_requires=[
    #     "wheel",
    # ],

    # Benötigte Python-Version (an InvenTree anpassen)
    python_requires=">=3.8",

    # Der entscheidende Teil: Entry Point für InvenTree Plugin Entdeckung
    entry_points={
        "inventree_plugins": [
            # Format: EinName = pfad.zum.modul:KlassenName
            # Hierdurch kann InvenTree das Plugin finden, auch wenn es nicht aktiviert ist.
            "MeinPlugin = inventree_meinplugin.plugin:MeinPlugin"
        ]
    },

    # Wichtig, damit Nicht-Code-Dateien (wie Templates) mitinstalliert werden!
    include_package_data=True,

    # Alternativ oder zusätzlich zu include_package_data, falls spezifischer nötig:
    # package_data={
    #     'inventree_meinplugin': ['templates/meinplugin/*.html'],
    # },

    # Weitere Metadaten zur Klassifizierung
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Framework :: Django",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
)
