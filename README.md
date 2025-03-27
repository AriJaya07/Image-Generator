# Image Generator using Hugging Face and Python

## 📌 Overview
This project is an **AI-based Image Generator** that utilizes **Hugging Face's models** and **Python** to generate images from text prompts. It provides an easy-to-use interface for creating AI-generated images.

## ✨ Features
✅ Generate images from text prompts using Hugging Face models  
✅ Save generated images as PNG or JPG files  
✅ Customize image resolution and model parameters  
✅ Simple Python script with minimal dependencies  

## 🛠️ Prerequisites
Before running the project, ensure you have the following installed:
- **Python 3.x**

## 🚀 Installation
Follow these steps to set up and run the Image Generator:

### 1️⃣ Clone the Repository
```sh
git clone https://github.com/your-username/image-generator.git
cd image-generator
```

### 2️⃣ Install Dependencies
```sh
pip install -r requirements.txt
```

## 🎯 Usage
### Running the Script
To generate an image, run the following command:
```sh
python generate_image.py
```

### Example Usage in Python
#### Generating an Image from a Text Prompt
```python
from diffusers import StableDiffusionPipeline
import torch

def generate_image(prompt, filename="generated_image.png"):
    model_id = "runwayml/stable-diffusion-v1-5"
    pipe = StableDiffusionPipeline.from_pretrained(model_id, torch_dtype=torch.float16)
    pipe = pipe.to("cuda" if torch.cuda.is_available() else "cpu")
    
    image = pipe(prompt).images[0]
    image.save(filename)
    print(f"✅ Image saved as {filename}")

# Example
generate_image("A futuristic city skyline at sunset")
```

## 🎨 Customization
You can customize the image generation by modifying:
- **Prompt**: Change the input text to generate different images
- **Model Parameters**: Adjust the diffusion settings for different outputs
- **Image Size**: Some models allow specifying different resolutions

## 📷 Output Example
When you run the script, it generates an image and saves it as a file (e.g., `generated_image.png`).

## 📜 License
This project is open-source and available under the **MIT License**.

## 🤝 Contributing
Feel free to contribute by submitting a pull request or reporting issues!

## 📬 Contact
For questions or suggestions, reach out via:
- **GitHub Issues**
