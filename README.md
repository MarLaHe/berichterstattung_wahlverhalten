# Projektübersicht
Vergleich der Trends von Medienpräsenz und Umfragewerten deutscher Parteien


## Fragestellungen
Inwiefern spiegelt die mediale Präsenz der Parteien, gemessen anhand des Vorkommens ihrer Bezeichnungen (wordcounts) in digitalen deutschen Zeitungen 
sich in den Umfragewerten der Sonntagsfrage (abgerufen von wahlrecht.de) wieder? 
Folgen einer hohen medialen Präsenz hohe Umfragewerte?

## Medienpräsenz
Daten aus dem Scraping folgender Zeitungen werden als Grundlage für die wordcounts genutzt:
Süddeutsche Zeitung  
Die Zeit  
Frankfurter Allgemeine  
Der Tagesspiegel  
Die Tageszeitung  
Hamburger Abendblatt  
Berliner Zeitung  
Welt  
Eßlinger Zeitung  
Handelsblatt  
ntv  
The Pioneer  
Südwest Presse  
Stuttgarter Nachrichten  
Deutschlandfunk  
Deutsche Welle  
Spiegel Online  
Manager Magazin  
Stern  
Tagesschau  
Wirtschaftswoche  
Watson  

Es wird in den jeweiligen Medien zwischen April 2021 bis November 2024 nach den Partei-Bezeichnungen CDU, CDU/CSU, Grünen, SPD, FDP, AfD gesucht.  
Es wird der wordcount pro Tag auf Monate aufsummiert und sowohl als Gesamtvorkommen als auch im Verlauf der Jahre dargestellt. Es wird zusätzlich pro Monat der jeweilige prozentuale Anteil der einzelnen Parteien am monatlichen Gesamt-Wordcount berechnet.

## Umfragewerte
Es werden von wahlrecht.de die Umfrageergebnisse zur Sonntagsfrage in einer Excel zusammengefasst und in Dataframes geladen. Es werden zwischen April 2021 bis November 2024 die monatlichen Mittelwerte der Umfrageergebnisse (als Prozent-Angabe) von den Umfrageinstituten 
Allensbach,  
Verian,  
Forsa,  
Forschungsgruppe Wahlen,  
infratest dimap,  
INSA,  
yougov  
gebildet. 

## Vergleich von wordcounts und Umfragewerten
Die Datensätze (prozentuale Wordcounts und prozentuale Umfrageergebnisse) werden in der Analyse vergleichend in einer Grafik pro Partei zusammengeführt.
Um ähnliche Tendenzen besser zu erkennen, wird hierzu jeweils auch ein Trend über die dritte Polynomfunktion modelliert und die durchschnittliche Differenz der Trends berechnet.

## Ausführung des Projekts
1. Als Grundlage dienen die .tar-Dateien aus einem Webscraper von April 2021 bis November 2024. Diese werden im Projektordner in einen Unterordner "tageszeitungen_gesamt" gespeichert und über das Skript 01_extract.py entpackt.
2. Das Skript 02_select.sh wählt nur die HTML von bestimmten Zeitungen aus und löscht alle anderen.
3. Im Notebook 03_build_dwh.ipynb werden die HTML eingelesen, Wörter bestimmt und gezählt und in eine Datenbank geschrieben.
4. Im Notebook 04_analyse_dwh.ipynb werden die Analysen vorgenommen
5. Die Dokumentation findet mithilfe von Sphinx statt.
6. Es wird ein Report, eine PowerPointPräsentation und ein Screencast erstellt.


Für begleitende Ausarbeitung bitte in den docs-Ordner schauen.


### Lizenz
Dieses Projekt steht unter der [Creative Commons Namensnennung – Nicht-kommerziell 4.0 International Lizenz (CC BY-NC 4.0)](https://creativecommons.org/licenses/by-nc/4.0/deed.de).  
Eine Nutzung ist nur mit Namensnennung und nicht-kommerziell gestattet.
