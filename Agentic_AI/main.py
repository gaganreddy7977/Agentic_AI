from fastapi import FastAPI, UploadFile, File
import shutil
import os
from agents.orchestrator import OrchestratorAgent

app = FastAPI()

orch = OrchestratorAgent()

os.makedirs("uploads", exist_ok=True)

@app.get("/")
def root():
    return {"message":"Agentic AI CSV/XLSX Analyzer Running"}


@app.post("/upload")
async def upload_file(file: UploadFile = File(...)):

    file_path = f"uploads/{file.filename}"

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    pdf = orch.run_file_pipeline(file_path)

    return {
        "message":"PDF generated",
        "pdf_path": pdf
    }