import torch
from transformers import AutoTokenizer, AutoModelForCausalLM
from transformers import pipeline

class LMMModel():
    def __init__(self):
        model = AutoModelForCausalLM.from_pretrained("TinyLlama/TinyLlama-1.1B-Chat-v1.0",
                                                    load_in_4bit=False,
                                                    torch_dtype="auto",)

        tokenizer = AutoTokenizer.from_pretrained("TinyLlama/TinyLlama-1.1B-Chat-v1.0",
                                                torch_dtype="auto")

        self.pipe = pipeline("text-generation",
                        model=model,
                        tokenizer=tokenizer,
                        torch_dtype=torch.bfloat16,
                        device_map="auto")
    
    def query(self, user_query):
        messages = [
        {
            "role": "system",
            "content": "You are an experienced professor who enjoy sharing his knowledge with others.",
        },
        {"role": "user", "content": user_query},
        ]

        prompt = self.pipe.tokenizer.apply_chat_template(messages,
                                                    tokenize=False,
                                                    add_generation_prompt=True)

        outputs = self.pipe(prompt,
                    max_new_tokens=256,
                    do_sample=True,
                    temperature=0.7,
                    top_k=50,
                    top_p=0.95)

        generated_text = outputs[0]["generated_text"]
        start_i = generated_text.find("<|assistant|>") + 14
        end_i = generated_text.rfind("\n")

        return generated_text[start_i: end_i]