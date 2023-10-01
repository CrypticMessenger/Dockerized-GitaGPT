import os
from flask import Flask, request
from transformers import AutoTokenizer
import transformers
import torch

app = Flask(__name__)
hf_access_token = os.environ.get('HF_ACCESS_TOKEN')


# checks if model is in .cache, if not, downloads it from HuggingFace (about 13 GB)
model = "meta-llama/Llama-2-7b-chat-hf"

tokenizer = AutoTokenizer.from_pretrained(model, token = hf_access_token)
pipeline = transformers.pipeline(
    "text-generation",
    model=model,
    torch_dtype=torch.float16,
    device_map="auto",
    token=hf_access_token
)

# Use this api to test if the server is running, by sending some args
@app.route('/test_args', methods=['GET'])
def test_args():
    param1 = request.args.get('top_p')
    param2 = request.args.get('prompt')

    result = f"Received parameters: {param1} top_p={param2}"
    return result

# Use this api to test if the server is running
@app.route("/test")
def test():
    return "Hello, World!"

# Use this api to make inference
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


# start the flask app, allow remote connections
if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0', port=40000)
