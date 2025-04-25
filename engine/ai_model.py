from transformers import AutoTokenizer, AutoModelForCausalLM
import torch

# Load model and tokenizer once
tokenizer = AutoTokenizer.from_pretrained("Salesforce/codegen-2B-multi")
model = AutoModelForCausalLM.from_pretrained("Salesforce/codegen-2B-multi")
model.eval()

# Automatically use GPU if available
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model.to(device)

def suggest_code_improvement(code, prompt, context=[], fast_mode=True):
    # Add memory context from previous history
    memory_context = "\n\n".join(
        [f"# Earlier Task: {p}\n{c}" for c, p in context]
    )
    user_block = f"# Current Task: {prompt}\n{code}"
    full_prompt = f"{memory_context}\n\n{user_block}\n\n# Suggestion:\n"

    inputs = tokenizer(full_prompt, return_tensors="pt", truncation=True).to(device)

    gen_config = {
        "max_new_tokens": 120 if fast_mode else 256,
        "temperature": 0.6,
        "top_k": 50,
        "top_p": 0.95,
        "do_sample": True
    }

    with torch.no_grad():
        outputs = model.generate(**inputs, **gen_config)

    generated = tokenizer.decode(outputs[0], skip_special_tokens=True)
    suggestion = generated.split("# Suggestion:")[-1].strip()

    explanation = "🧚‍♀️ Pixie here! I’ve updated your code based on your request. Let me know if you want more changes!"

    return suggestion, explanation
