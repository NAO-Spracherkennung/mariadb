# NAO Developer Center mit Downloads und API Reference
https://www.aldebaran.com/developer-center/index.html

## Choregraphe installieren (Mac)
- Neueste Choregraphe Mac Binaries herunterladen (2.8.6 hat funktioniert)
- in recovery mode von mac ins terminal gehen und ```csrutil disable``` ausführen
- computer neustarten
- Choregraphe aus der Binaries zip mit ```./choregraphe``` öffnen
- Choregraphe nutzen

### Troubleshooting
- Wenn eine Meldung kommt, dass QtCore.framework beschädigt ist, dann muss in recovery mode terminal ```csrutil disable``` gemacht werden
- Wenn eine Meldung kommt, ...nicht verifizierte Entwickler... dann ```sudo spctl --master-disable``` in normalem Terminal

## Deployment und Starten des Backends

Voraussetzungen:
- Docker ist installiert und läuft
- python3 ist installiert und kann mit python3 aufgerufen werden\
\
Setup und Start wird mit folgender Kommandozeile durchgeführt:\
`./local_build_and_start.sh

## Nach dem Projekt (Mac)
- ```csrutil enable``` in recovery mode ausführen, um wieder mehr Sicherheit im Mac zu schaffen
