# WWW.blazor - FillMyPdf Frontend

Ein modernes Blazor Server Frontend mit Neobrutalism-Design für die FillMyPdf API.

## 🎨 Features

- **Neobrutalism Design** - Mutiges, farbenfrohes UI mit dicken Rahmen und Schatten
- **Projektverwaltung** - Erstellen und verwalten Sie PDF-Verarbeitungsprojekte
- **Multi-File Upload** - Laden Sie mehrere Input-PDFs hoch
- **Echtzeit-Verarbeitung** - Sehen Sie den Fortschritt der PDF-Verarbeitung
- **Responsive Design** - Funktioniert auf Desktop und Tablet

## 🚀 Schnellstart

### Voraussetzungen

- .NET 8.0 SDK
- Python API muss laufen (siehe Hauptprojekt README)

### Installation & Start

1. **Zum Blazor-Verzeichnis wechseln:**
```bash
cd WWW.blazor
```

2. **Anwendung starten:**
```bash
dotnet run
```

Die Anwendung läuft dann auf `https://localhost:5001` oder `http://localhost:5000`

## 📖 Verwendung

### 1. Projekt erstellen

- Klicken Sie auf "+ New Project"
- Geben Sie einen Namen und Beschreibung ein
- Klicken Sie auf "Create"

### 2. Dateien hochladen

- Klicken Sie auf ein Projekt
- Laden Sie Input-PDFs hoch (die Daten enthalten)
- Laden Sie eine Form Template PDF hoch (das Formular, das ausgefüllt werden soll)

### 3. Verarbeiten

- Klicken Sie auf "🚀 Analyze & Fill"
- Warten Sie, bis die Verarbeitung abgeschlossen ist
- Das ausgefüllte PDF wird angezeigt

## 🎨 Design System

Das Projekt verwendet ein **Neobrutalism Design System** mit:

- **Farben:** Gelb, Pink, Blau, Grün, Lila, Orange
- **Typografie:** Space Grotesk (Google Fonts)
- **Schatten:** 6px-8px dicke schwarze Schatten
- **Rahmen:** 4px dicke schwarze Rahmen
- **Animationen:** Hover-Effekte mit Transform

## 📁 Projektstruktur

```
WWW.blazor/
├── Components/
│   ├── Pages/
│   │   ├── Home.razor           # Projektliste
│   │   └── ProjectDetails.razor # Projektdetails & Upload
│   └── Layout/
│       └── MainLayout.razor     # Haupt-Layout
├── Models/
│   └── Project.cs               # Datenmodelle
├── Services/
│   ├── ProjectService.cs        # Projektverwaltung
│   └── PdfApiService.cs         # API-Integration
└── wwwroot/
    └── css/
        └── neobrutalism.css     # Design System
```

## 🔧 Konfiguration

### API-URL ändern

In `Services/PdfApiService.cs`:
```csharp
private readonly string _apiBaseUrl = "http://localhost:5003";
```

### Port ändern

In `Properties/launchSettings.json` oder via:
```bash
dotnet run --urls "http://localhost:8080"
```

## 🛠️ Entwicklung

### Build
```bash
dotnet build
```

### Watch Mode (Auto-Reload)
```bash
dotnet watch
```

### Publish
```bash
dotnet publish -c Release
```

## 🎯 Roadmap

- [ ] Benutzer-Authentifizierung
- [ ] Projekt-Export/Import
- [ ] PDF-Vorschau
- [ ] Batch-Verarbeitung
- [ ] Verlauf/History

## 🤝 Beitragen

Contributions sind willkommen! Siehe Haupt-README für Details.

## 📝 Lizenz

Open Source - siehe Haupt-Repository
