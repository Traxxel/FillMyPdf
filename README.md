# FillMyPdf 📄✨

Ein intelligentes PDF-Formular-Ausfüll-Tool, das OpenAI nutzt, um automatisch Formulare basierend auf Eingabedokumenten zu befüllen.

## 🎯 Überblick

FillMyPdf ist ein Python-basierter Service, der PDF-Formulare automatisch ausfüllt, indem er:
1. Text aus Eingabe-PDFs extrahiert
2. Die Formularfelder der Ziel-PDF analysiert
3. OpenAI's KI nutzt, um die passenden Informationen zu finden und zuzuordnen
4. Das ausgefüllte Formular generiert

**Das Besondere:** Sie müssen den Code nicht anpassen - die KI erkennt automatisch Ihre Formularfelder und füllt sie intelligent aus!

## ✨ Features

- 🤖 **KI-gesteuerte Feldzuordnung** - OpenAI analysiert und ordnet Daten automatisch zu
- 📝 **Flexible Formularfelder** - Funktioniert mit beliebigen PDF-Formularfeldern
- 🔧 **Keine Code-Anpassung nötig** - Einfach neue Formulare verwenden
- 🌐 **REST API** - Einfache Integration in andere Anwendungen
- 🛠️ **Robuste PDF-Verarbeitung** - Behandelt auch beschädigte PDFs mit NullObjects
- 📦 **Einfaches Setup** - Schnell einsatzbereit

## 🚀 Schnellstart

### Voraussetzungen

- Python 3.14+ (oder 3.10+)
- OpenAI API Key
- macOS, Linux oder Windows

### Installation

1. **Repository klonen:**
```bash
git clone https://github.com/Traxxel/FillMyPdf.git
cd FillMyPdf
```

2. **Virtual Environment erstellen:**
```bash
cd python
python3 -m venv venv
source venv/bin/activate  # Auf Windows: venv\Scripts\activate
```

3. **Dependencies installieren:**
```bash
pip install -r requirements.txt
```

4. **Umgebungsvariablen konfigurieren:**
```bash
cp .env.example .env
# Bearbeiten Sie .env und fügen Sie Ihren OpenAI API Key hinzu
```

### Verwendung

#### 1. Server starten

Aus dem Hauptverzeichnis:
```bash
./start.sh
```

Der Server läuft dann auf `http://localhost:5003`

#### 2. Test-Script verwenden

**Standard-Test:**
```bash
python/venv/bin/python test.py
```

**Mit eigenen Dateien:**
```bash
python/venv/bin/python test.py -in=input/MeinDokument.pdf -out=Ausgabe.pdf
```

**Hilfe anzeigen:**
```bash
python/venv/bin/python test.py --help
```

#### 3. API direkt nutzen

**Endpoint:** `POST /process`

**Request:**
```json
{
    "input_files": ["/pfad/zu/eingabe.pdf"],
    "form_file": "/pfad/zu/formular.pdf",
    "output_file": "/pfad/zu/ausgabe.pdf"
}
```

**Response:**
```json
{
    "status": "success",
    "output_file": "/pfad/zu/ausgabe.pdf",
    "metadata": {
        "Feldname1": "Wert1",
        "Feldname2": "Wert2"
    }
}
```

## 📁 Projektstruktur

```
FillMyPdf/
├── python/
│   ├── src/
│   │   ├── app.py           # Flask API Server
│   │   ├── ai_service.py    # OpenAI Integration
│   │   └── pdf_utils.py     # PDF-Verarbeitung
│   ├── requirements.txt     # Python Dependencies
│   ├── .env.example         # Beispiel-Konfiguration
│   └── README.md           # Python-spezifische Dokumentation
├── input/                   # Eingabe-PDFs
├── output/                  # Ausgabe-PDFs
├── start.sh                # Startup-Script
├── test.py                 # Test-Script
└── .gitignore              # Git-Ausschlüsse
```

## 🔧 Konfiguration

### Umgebungsvariablen (.env)

```env
OPENAI_API_KEY=sk-your-api-key-here
```

### Port ändern

In `python/src/app.py` (Zeile 66):
```python
app.run(host='0.0.0.0', port=5003, debug=True)
```

## 💡 Beispiele

### Beispiel 1: Märchen-Formular

**Eingabe:** `input/Haensel.pdf` (Märchentext)  
**Formular:** Felder wie "Hauptdarsteller", "Handlungsort", "Ertrag"  
**Ergebnis:** KI extrahiert automatisch "Hänsel und Gretel", "großer Wald", "Gold und Edelsteine"

### Beispiel 2: Rechnungsformular

**Eingabe:** Beliebige Rechnung als PDF  
**Formular:** Felder wie "Kunde", "Betrag", "Datum", "Rechnungsnummer"  
**Ergebnis:** KI füllt die Felder basierend auf dem Rechnungsinhalt

## 🛠️ Technologie-Stack

- **Backend:** Python 3.14, Flask 3.0
- **PDF-Verarbeitung:** pypdf 3.17
- **KI:** OpenAI API (GPT-4)
- **Umgebungsvariablen:** python-dotenv

## 🐛 Troubleshooting

### Port 5000 bereits belegt

**Problem:** `Address already in use`  
**Lösung:** Deaktivieren Sie AirPlay Receiver in den Systemeinstellungen oder ändern Sie den Port

### Keine Felder gefunden

**Problem:** `No fields found in form PDF`  
**Lösung:** Stellen Sie sicher, dass Ihr PDF tatsächlich Formularfelder enthält (nicht nur Text)

### OpenAI API Fehler

**Problem:** API-Fehler oder fehlender Key  
**Lösung:** Überprüfen Sie Ihren API-Key in der `.env` Datei

## 🤝 Beitragen

Contributions sind willkommen! Bitte:

1. Forken Sie das Repository
2. Erstellen Sie einen Feature-Branch (`git checkout -b feature/AmazingFeature`)
3. Committen Sie Ihre Änderungen (`git commit -m 'Add some AmazingFeature'`)
4. Pushen Sie zum Branch (`git push origin feature/AmazingFeature`)
5. Öffnen Sie einen Pull Request

## 📝 Lizenz

Dieses Projekt ist Open Source und frei verfügbar.

## 👤 Autor

**Traxxel**
- GitHub: [@Traxxel](https://github.com/Traxxel)

## 🙏 Danksagungen

- OpenAI für die leistungsstarke API
- pypdf für die robuste PDF-Verarbeitung
- Flask für das einfache Web-Framework

---

**Hinweis:** Stellen Sie sicher, dass Sie Ihren OpenAI API-Key niemals in öffentlichen Repositories committen!
