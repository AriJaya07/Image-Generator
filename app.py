import gradio as gr
import requests
import io
import json
import os
from dotenv import load_dotenv
from PIL import Image

load_dotenv()

# Hugging Face API endpoint for Stable Diffusion
API_URL = os.getenv("API_URL")
API_KEY = os.getenv("API_KEY")

# Ensure API key is set
if not API_KEY or not API_URL:
    raise ValueError("Missing API_KEY or API_URL in environment variables.")

# Replace with your actual Hugging Face API key
HEADERS = {"Authorization": f"Bearer {API_KEY}"}

def query(payload):
    response = requests.post(API_URL, headers=HEADERS, json=payload)

    # Debugging: Print response status and headers
    print("Status Code:", response.status_code)
    print("Response Headers:", response.headers)

    # Check if the response contains an image
    if response.status_code == 200 and "image" in response.headers.get("Content-Type", ""):
        return response.content

    # Print and return error message if not an image
    try:
        error_message = response.json()
        print("API Error Response:", json.dumps(error_message, indent=2))
        return None
    except json.JSONDecodeError:
        print("Unknown error: Response is not JSON or an image.")
        return None

def generate_image(prompt):
    payload = {
        "inputs": prompt,
        "parameters": {
            "num_inference_steps": 50,  # Increase for better quality (default: 30-50)
            "guidance_scale": 7.5,      # Higher value = more prompt adherence (default: 7.5)
            "negative_prompt": "blurry, distorted, low resolution, ugly"  # Avoid unwanted outputs
        }
    }
    
    image_bytes = query(payload)
    
    if image_bytes:
        return Image.open(io.BytesIO(image_bytes))
    else:
        return "Failed to generate image. Check API settings or model availability."

# Create the Gradio interface
demo = gr.Interface(
    fn=generate_image,
    inputs="text",
    outputs="image",
    title="Stable Diffusion Image Generator",
    description="Enter a prompt to generate an image using Stable Diffusion."
)

# Launch with public sharing enabled
demo.launch(share=True)
