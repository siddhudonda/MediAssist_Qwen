from fastapi import FastAPI, UploadFile
from pipelines.orchestrator import run_full_pipeline

app = FastAPI()

@app.post("/process/")
async def process(image: UploadFile, audio: UploadFile = None):
    img = await image.read()
    audio_path = None
    if audio:
        audio_path = f"/tmp/{audio.filename}"
        open(audio_path, "wb").write(await audio.read())
    return run_full_pipeline({"image_bytes": img, "audio_path": audio_path})
