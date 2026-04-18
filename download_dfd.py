import base64
import zlib
import urllib.request
import urllib.error

mermaid_code = """
graph TD
    User((User Browser))
    Django[Django Web Server]
    ML[AI Models: XGBoost & DistilBERT]
    DB[(SQLite Database)]

    User -- "1. Submit SMS Text" --> Django
    
    Django -- "2. Extract Features" --> ML
    ML -- "3. Spam/Ham Prediction" --> Django
    
    Django -- "4. Store Prediction" --> DB
    Django -- "5. Render Dashboard UI" --> User
    
    User -. "6. Feedback (e.g., False Alarm)" .-> Django
    Django -. "7. Update Learning Data" .-> DB
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
        with open("Dataflow_Diagram_Simple.png", "wb") as out_file:
            out_file.write(response.read())
    print("Saved Dataflow_Diagram_Simple.png successfully!")
except urllib.error.HTTPError as e:
    print(f"HTTP Error: {e.code} - {e.reason}")
except Exception as e:
    print(f"Error: {e}")
