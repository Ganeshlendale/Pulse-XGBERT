import base64
import zlib
import urllib.request
import urllib.error

mermaid_code = """
sequenceDiagram
    actor User as User
    participant Browser as Client Browser
    participant Django as Django Web Server
    participant DB as SQLite / PostgreSQL
    participant ML as ML Inference Engine (XGB/BERT)

    User->>Browser: Access Application
    Browser->>Django: GET /dashboard/
    Django-->>Browser: Redirect to Login (Unauthenticated)
    
    User->>Browser: Submit Login Credentials
    Browser->>Django: POST /login/
    Django->>DB: Validate Credentials
    DB-->>Django: Auth Success
    Django-->>Browser: Set Session Cookie

    User->>Browser: Paste & Submit SMS text
    Browser->>Django: POST /predict/
    
    Django->>ML: Forward text for classification
    Note over ML: 1. Text Preproc (NLTK)<br/>2. TF-IDF & Tokenize
    Note over ML: 3. Dual Inference<br/>4. Threshold Aggregation
    ML-->>Django: Return Verdict & Score

    Django->>DB: Log Prediction Record
    DB-->>Django: Record Saved

    Django-->>Browser: Render Dashboard with Verdict
    Browser-->>User: Display Security Classification

    opt Active Learning Feedback
        User->>Browser: Click Report Misclassification
        Browser->>Django: POST /feedback/
        Django->>DB: Update Record
        DB-->>Django: Update Confirmed
        Django-->>Browser: Render Success
        Browser-->>User: Visual Confirmation
    end
"""

compressed = zlib.compress(mermaid_code.encode('utf-8'))
encoded = base64.urlsafe_b64encode(compressed).decode('ascii')
url = f"https://kroki.io/mermaid/png/{encoded}"

print(f"Downloading from: {url}")

req = urllib.request.Request(
    url, 
    headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'}
)

try:
    with urllib.request.urlopen(req) as response:
        with open("System_Flowchart.png", "wb") as out_file:
            out_file.write(response.read())
    print("Saved System_Flowchart.png successfully!")
except urllib.error.HTTPError as e:
    print(f"HTTP Error: {e.code} - {e.reason}")
except Exception as e:
    print(f"Error: {e}")
