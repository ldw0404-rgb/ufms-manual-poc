from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(title="UFMS Manual POC")

class SummaryResponse(BaseModel):
    manufacturer: str
    model: str
    summary: str

class DownloadResponse(BaseModel):
    manufacturer: str
    model: str
    url: str

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/maintenance/summary", response_model=SummaryResponse)
def maintenance_summary(manufacturer: str, model: str):
    if not manufacturer or not model:
        raise HTTPException(status_code=400, detail="manufacturer and model are required")
    return SummaryResponse(
        manufacturer=manufacturer,
        model=model,
        summary=f"[MOCK] Summary for {manufacturer} {model}. (Next: Bedrock)"
    )

@app.get("/maintenance/manual/download", response_model=DownloadResponse)
def manual_download(manufacturer: str, model: str):
    if not manufacturer or not model:
        raise HTTPException(status_code=400, detail="manufacturer and model are required")
    return DownloadResponse(
        manufacturer=manufacturer,
        model=model,
        url="[MOCK] presigned-url-will-be-here"
    )
