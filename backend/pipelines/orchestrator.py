def run_full_pipeline(inputs):
    img = inputs.get("image_bytes")
    aud = inputs.get("audio_path")
    findings = process_image(img)
    ocr_text = ocr_handwriting(img)
    transcript = transcribe_audio(aud) if aud else ""
    summary = medical_reasoning(transcript + ocr_text, findings)
    return {"findings": findings, "ocr": ocr_text, "transcript":transcript, "summary":summary}
