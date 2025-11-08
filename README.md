HeyPico.ai Technical Test Submission
by Anya Manggar
Email: anyamanggar@gmail.com
Date: 2025-11-08

------------------------------------------------------------
PROJECT OVERVIEW
------------------------------------------------------------
This project contains my submission for the HeyPico.ai technical test.
It includes two main components:

1. backend_maps/ — a Flask API that securely connects to Google Maps Places API
2. frontend_maps/ — a Gradio-based interface to query and display map results

------------------------------------------------------------
FEATURES
------------------------------------------------------------
Backend (Flask)
- Secure API key handling using .env
- Rate limiting (10 requests/minute/IP)
- Lightweight cache to reduce API calls
- Error handling for API and network requests

Frontend (Gradio)
- Simple text input for natural queries
- Markdown output with clickable Google Maps links
- Connects directly to local Flask backend

------------------------------------------------------------
SETUP GUIDE
------------------------------------------------------------
1. Clone the repository:
   git clone https://github.com/<your-username>/heypico-technical-test.git
   cd heypico-technical-test

2. Create virtual environment:
   python3 -m venv venv
   source venv/bin/activate

3. Install dependencies:
   pip install -r requirements.txt

4. Add your Google Maps API key:
   Create .env inside backend_maps/ folder:
   GOOGLE_MAPS_API_KEY=your_api_key_here

5. Run backend:
   cd backend_maps
   python3 app.py

6. Run frontend (new terminal):
   cd frontend_maps
   python3 run_gradio.py

------------------------------------------------------------
EXAMPLE QUERY
------------------------------------------------------------
Input:  cafe in Jakarta
Output: [Starbucks SCBD](https://www.google.com/maps/search/?api=1&query=Starbucks+SCBD) - Jakarta Selatan

------------------------------------------------------------
SECURITY
------------------------------------------------------------
- API key hidden via .env
- Rate limiting via flask-limiter
- Dependencies isolated in venv
- Clean folder structure for easy deployment

------------------------------------------------------------
CONTACT
------------------------------------------------------------
Name: Anya Manggar
Email: anyamanggar@gmail.com
Portfolio: https://amangrdesign.github.io
