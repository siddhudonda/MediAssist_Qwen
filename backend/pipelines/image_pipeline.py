def process_image(image_bytes):
    model = load_qwen_vl()
    inputs = processor(images=image_bytes, return_tensors="pt")
    return model.generate(**inputs)
