# Artwork Database

Dieses Projekt verwaltet KI-generierte Kunstwerke für die automatisierte Erstellung von Print-on-Demand-Produkten.

## Voraussetzungen

- Python 3.8 oder höher
- Virtuelle Umgebung (empfohlen)
- Abhängigkeiten in `requirements.txt` (siehe unten)
- AWS-Zugangsdaten für S3-Integration

## Installation

1. **Repository klonen**:
   ```bash
   git clone <repository-url>
   cd artwork_database
   ```

2. **Virtuelle Umgebung erstellen und aktivieren**:
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # Für Linux/Mac
   venv\Scripts\activate     # Für Windows
   ```

3. **Abhängigkeiten installieren**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Umgebungsvariablen konfigurieren**:
   Erstellen Sie eine `.env`-Datei im Projektverzeichnis und fügen Sie die folgenden Variablen hinzu:
   ```
   DATABASE_URI=sqlite:///artwork.db
   AWS_ACCESS_KEY_ID=<Ihr AWS Access Key>
   AWS_SECRET_ACCESS_KEY=<Ihr AWS Secret Key>
   AWS_REGION=us-east-1
   S3_BUCKET_NAME=<Ihr S3-Bucket-Name>
   ```

## Nutzung

1. **Datenbank initialisieren**:
   Die Datenbank wird automatisch erstellt, wenn die App gestartet wird.

2. **App starten**:
   ```bash
   python app.py
   ```

3. **API-Endpunkte**:
   Die API ist unter `/api` verfügbar. Weitere Details finden Sie in der Datei `routes/image_routes.py`.

## S3-Integration

Die App verwendet AWS S3, um Dateien zu speichern. Stellen Sie sicher, dass Ihre AWS-Zugangsdaten korrekt sind und der S3-Bucket existiert.

## Demo-Daten

Beim ersten Start der App werden automatisch Demo-Daten in die Datenbank eingefügt.

## Lizenz

Dieses Projekt steht unter der MIT-Lizenz. Weitere Informationen finden Sie in der Datei `LICENSE`.