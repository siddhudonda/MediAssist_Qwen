from transformers import AutoModelForCausalLM, AutoProcessor
import whisper

def load_qwen_vl():
    return AutoModelForCausalLM.from_pretrained("Qwen/Qwen-VL-Chat", trust_remote_code=True)

def load_qwen_omni():
    return AutoModelForCausalLM.from_pretrained("Qwen/Qwen2.5-Omni", trust_remote_code=True)

def load_whisper():
    return whisper.load_model("base")

def load_medvill():
    return AutoModelForCausalLM.from_pretrained("SuperSupermoon/MedViLL", trust_remote_code=True)
