⚡ ClipDrop

Instantly share text & files between any devices using a 6-character code.
No login. No account. No BS. Auto-deletes in 10 minutes.

🌐 Live Demo: clipdrop2026.netlify.app

🎯 The Problem
Ever been on a college lab PC and needed to get a file or some text to your phone?
You'd have to log into email, WhatsApp Web, or Google Drive — on a public computer.
That's slow, annoying, and a privacy risk.
ClipDrop fixes this in seconds.

✨ How It Works

Open ClipDrop on any device
Paste text or drop a file → click Generate Code
Get a 6-character code like X9K2A3
Open ClipDrop on your other device → click Receive → enter the code
Done. Your content appears instantly ⚡

No login. No account. Everything auto-deletes in 10 minutes.

🖥️ Demo
SendReceivePaste text or drop a fileEnter the 6-char codeGet a code + QR instantlyContent appears in secondsTimer shows when it expiresCopy text or download file

🛠️ Tech Stack
LayerTechFrontendHTML, CSS, Vanilla JSBackendPython, FlaskHosting (Frontend)NetlifyHosting (Backend)RenderData storageIn-memory (auto-expiry)

📁 Project Structure
ClipDrop/
├── backend/
│   ├── app.py              ← Flask API server
│   ├── requirements.txt    ← Python dependencies
│   └── Procfile            ← Render deployment config
└── frontend/
    └── index.html          ← Complete frontend (single file)

🚀 Run Locally
Backend:
bashcd backend
pip install -r requirements.txt
python app.py
# Runs on http://localhost:5000
Frontend:
Open frontend/index.html in your browser.
Change the API URL in index.html to http://localhost:5000

🔌 API Reference
MethodEndpointDescriptionPOST/api/pushUpload text or file, get a codeGET/api/pull/:codeRetrieve content by codeGET/api/pingHealth check
Push text example:
jsonPOST /api/push
{
  "type": "text",
  "content": "Hello from my lab PC!"
}
Response:
json{
  "code": "X9K2A3",
  "expires_in": 600
}

🔧 Features

✅ Share text between any devices
✅ Share files up to 7MB
✅ QR code for easy mobile access
✅ 6-character short code
✅ Auto-delete after 10 minutes
✅ No login or account needed
✅ Works on any browser, any device

🗺️ Roadmap

 End-to-end encryption
 Password-protected codes
 Custom expiry times
 PWA — installable on phone
 Paste history (local storage)
 Larger file support (Pro tier)


👤 Author
Pranesh — CSE Year 1(19-04-2026)
Built this to solve a real problem faced every day in college computer labs.
