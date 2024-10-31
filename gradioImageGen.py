import os
import io
import requests
from PIL import Image
import base64
from dotenv import load_dotenv, find_dotenv
import gradio as gr

# Load environment variables
load_dotenv(find_dotenv())
hf_api_key = os.environ['HF_API_KEY']

# API URLs
TTI_ENDPOINT = os.environ['HF_API_TTI_BASE']  # Text-to-Image endpoint
API_URL = "https://api-inference.huggingface.co/models/stabilityai/stable-diffusion-3.5-large"
headers = {"Authorization": f"Bearer {hf_api_key}"}

# Function to get image caption
def get_completion(inputs, parameters=None, ENDPOINT_URL=""):
    headers = {
        "Authorization": f"Bearer {hf_api_key}",
        "Content-Type": "application/json"
    }
    data = {"inputs": inputs}
    if parameters is not None:
        data["parameters"] = parameters

    try:
        response = requests.post(ENDPOINT_URL, headers=headers, json=data)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.HTTPError as errh:
        print("HTTP Error:", errh)
    except requests.exceptions.ConnectionError as errc:
        print("Error Connecting:", errc)
    except requests.exceptions.Timeout as errt:
        print("Timeout Error:", errt)
    except requests.exceptions.RequestException as err:
        print("Unexpected Error:", err)
    return None



# Function to generate images
def generate(prompt):
    payload = {"inputs": prompt}
    response = requests.post(API_URL, headers=headers, json=payload)
    if response.status_code == 200:
        image_bytes = response.content
        image = Image.open(io.BytesIO(image_bytes))
        return image
    else:
        print(f"Error: {response.status_code} - {response.text}")
        return None



# Function for captioning images
def captioner(image):
    # Resize the image to a maximum width or height
    max_size = 1024  # Set a maximum size (e.g., 1024x1024)
    image.thumbnail((max_size, max_size), Image.LANCZOS)

    # Convert image to bytes for API upload
    buffered = io.BytesIO()
    image.save(buffered, format="JPEG")  # Use JPEG format for smaller size
    img_str = base64.b64encode(buffered.getvalue()).decode("utf-8")

    # Make API request for image captioning
    data = {
        "inputs": img_str
    }
    response = requests.post(TTI_ENDPOINT, headers=headers, json=data)

    
    if response.status_code == 200:
        try:
            # Parse response
            caption = response.json()[0]["generated_text"]
            return caption
        except (IndexError, KeyError) as e:
            print("Error parsing the response:", e)
            return "Error parsing the response."
    else:
        print(f"Error: {response.status_code} - {response.text}")
        return f"Error: {response.status_code} - {response.text}"




# Gradio app setup
with gr.Blocks() as demo:
    gr.Markdown("# Describe-and-Generate Game")

    with gr.Row():
        # Left column: Input image and caption button
        with gr.Column():
            image_upload = gr.Image(
                label="Your first image",
                type="pil",
                width=500,
                height=400,
            )
            btn_caption = gr.Button("Generate Caption")

        # Right column: Output image and generate button
        with gr.Column():
            image_output = gr.Image(
                label="Generated Image",
                width=400,
                height=400,

            )
            btn_image = gr.Button("Generate Image")

    # Caption textbox spans both columns
    caption = gr.Textbox(label="Generated Caption")

    btn_caption.click(fn=captioner, inputs=[image_upload], outputs=[caption])
    btn_image.click(fn=generate, inputs=[caption], outputs=[image_output])

demo.launch(share=True)
