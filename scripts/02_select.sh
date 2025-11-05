#mit "bash 02_select.sh" im terminal ausführen

# In das Projektverzeichnis wechseln
cd "$(dirname "$0")/.."  # eine Ebene über dem scripts-Ordner
cd data-lake

find . -type f ! '(' -name '*sz.html' -o -name '*zeit.html' -o -name '*faz.html' -o -name '*tagesspiegel.html' -o -name '*taz.html' -o -name '*abendblatt.html' -o -name '*berliner.html' -o -name '*welt.html' -o -name '*esslinger.html' -o -name '*handelsblatt.html' -o -name '*ntv.html' -o -name '*pioneer.html' -o -name '*suedwest.html' -o -name '*stuttgarter.html' -o -name '*dlf.html' -o -name '*dw-de.html' -o -name '*spiegel.html' -o -name '*mm.html' -o -name '*stern.html' -o -name '*tagesschau.html' -o -name '*wiwo.html' -o -name '*watson-de.html' -o -name '*.csv' ')' -exec rm -f {} +