# Agentic AI CSV/XLSX → PDF Analyzer

An intelligent data analysis tool that uses AI agents to process CSV and Excel files, generating comprehensive PDF reports with insights, trends, and anomalies.

## Features

- **File Upload**: Supports CSV and XLSX file formats
- **AI-Powered Analysis**: Leverages OpenAI's GPT models for data insights
- **Automated Reporting**: Generates detailed PDF reports automatically
- **Web Interface**: User-friendly Streamlit interface for easy interaction
- **API Access**: FastAPI backend for programmatic integration

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/gaganreddy7977/Agentic_AI.git
   cd Agentic_AI/Agentic_AI
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Set up environment variables:
   Create a `.env` file in the project root:
   ```
   OPENAI_API_KEY=your_openai_api_key_here
   ```

## Usage

### Streamlit Web App

Run the interactive web application:

```bash
streamlit run app.py
```

Open your browser to `http://localhost:8501` and upload your CSV or Excel file to generate a PDF report.

### FastAPI Server

For API access, run the FastAPI server:

```bash
uvicorn main:app --reload
```

Access the API documentation at `http://127.0.0.1:8000/docs`.

#### API Endpoint

- **POST /upload**: Upload a file and generate a PDF report
  - Parameters: `file` (UploadFile)
  - Returns: JSON with message and PDF path

## Project Structure

```
Agentic_AI/
├── app.py                 # Streamlit web application
├── main.py                # FastAPI server
├── requirements.txt       # Python dependencies
├── .env                   # Environment variables (not committed)
├── agents/
│   ├── base_agent.py      # Base agent class
│   ├── file_agent.py      # File loading agent
│   ├── analysis_agent.py  # Data analysis agent
│   ├── pdf_agent.py       # PDF generation agent
│   └── orchestrator.py    # Main orchestrator
└── uploads/               # Temporary upload directory
```

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## License

This project is licensed under the MIT License.