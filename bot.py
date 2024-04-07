import torch

if not torch.cuda.is_available():
    print("no cuda!")
    exit()

from transformers import AutoTokenizer, AutoModelForCausalLM
model_id = "sambanovasystems/SambaLingo-Russian-Chat"
tokenizer = AutoTokenizer.from_pretrained(model_id)
model = AutoModelForCausalLM.from_pretrained(model_id, device_map="auto", torch_dtype="auto")
#model.eval()

chat = [
    {"role": "user", "content": "привет, раскажи о себе что нибуть"},
]

def next_generate():
    token_id = tokenizer.apply_chat_template(chat, tokenize=True, add_generation_prompt=True, return_tensors="pt").to("cuda")
    print(len(token_id[0]))
    output = model.generate(token_id, max_new_tokens=50) #,max_length=50
    print(len(output[0]))
    print(tokenizer.decode(output[0],skip_special_tokens=True))

next_generate()