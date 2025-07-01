def medical_reasoning(text, img_report):
    omni = load_qwen_omni()
    med = load_medvill()
    prompt = f"Findings: {img_report}\nNotes: {text}\nSummarize and recommend next steps."
    interim = omni.generate(prompt)
    return med.generate("Refine: " + interim)
