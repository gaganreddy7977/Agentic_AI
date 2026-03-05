Agentic AI CSV/XLSX → PDF Analyzer

Steps:

1. Install requirements

pip install -r requirements.txt

2. Create .env file

OPENAI_API_KEY=your_key_here

3. Run server

in terminal run > streamlit run app.py 

uvicorn main:app --reload

4. Open browser

http://127.0.0.1:8000/docs

Upload CSV or XLSX file and system will generate AI analysis PDF.