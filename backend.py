import os
from flask import Flask, request
from transformers import AutoTokenizer
import transformers
import torch
# from dotenv import load_dotenv


# load_dotenv()

app = Flask(__name__)
hf_access_token = os.environ.get('HF_ACCESS_TOKEN')
# hf_access_token = "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"




model = "meta-llama/Llama-2-7b-chat-hf"

tokenizer = AutoTokenizer.from_pretrained(model, token = hf_access_token)
pipeline = transformers.pipeline(
    "text-generation",
    model=model,
    torch_dtype=torch.float16,
    device_map="auto",
    token=hf_access_token
)

@app.route('/test_args', methods=['GET'])
def test_args():
    param2 = request.args.get('top_p')
    param3 = request.args.get('prompt')

    # Use the parameters in your API logic
    result = f"Received parameters: top_p={param2}"
    return param3 + result

@app.route("/test")
def test():
    return "Hello, World!"

@app.route("/enlighten", methods=['GET'])
def enlighten():
    num_return_sequences = request.args.get('num_return_sequences')
    top_k = request.args.get('top_k')
    max_length = request.args.get('max_length')
    prompt = request.args.get('prompt')

    sequences = pipeline(
        prompt,
        do_sample=True,
        top_k=top_k,
        num_return_sequences=num_return_sequences,
        eos_token_id=tokenizer.eos_token_id,
        max_length=max_length,
    )
    return sequences[0]["generated_text"]


if __name__ == "__main__":
    app.run(debug=True, port=40000)
