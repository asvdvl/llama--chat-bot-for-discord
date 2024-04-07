from transformers import AutoTokenizer, AutoModelForCausalLM

model_id = "sambanovasystems/SambaLingo-Russian-Chat"
tokenizer = AutoTokenizer.from_pretrained(model_id)
model = AutoModelForCausalLM.from_pretrained(model_id)
#model.eval()

chat = [
    {"role": "user", "content": "привет, раскажи о себе что нибуть"},
]

def next_generate():
    token_id = tokenizer.apply_chat_template(chat, tokenize=True, add_generation_prompt=True, return_tensors="pt")
    print(token_id.shape)
    output = model.generate(token_id, max_new_tokens=50) #,max_length=50
    print(output.shape)
    print(tokenizer.decode(output[0],skip_special_tokens=True))

next_generate()