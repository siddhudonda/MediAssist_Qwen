import gradio as gr
from pipelines.orchestrator import run_full_pipeline

def infer(image, audio):
    return run_full_pipeline({"image_bytes": image.tobytes(), "audio_path": audio.name if audio else None})

gr.Interface(
    fn=infer,
    inputs=[gr.Image(type="pil"), gr.Audio(source="upload", type="file")],
    outputs=["text","text","text","text"],
).launch()
