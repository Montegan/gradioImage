# GenAI Game on Gradio

A creative AI-powered game that combines image captioning and generation capabilities in an interactive web interface. Upload an image, get an AI-generated caption, and watch as the system creates a new image based on that description!

## 🎮 [Live Demo](Your-deployment-link-here)

## 📊 [Detailed Project Presentation](https://docs.google.com/presentation/d/11cjat3jfK_sJ84Oy-sIILJhBqA2TibBrRRn50nOv2pE/edit?usp=sharing)

## 🌟 Features

- **Image Captioning**: Automatically generates descriptive captions for uploaded images
- **Text-to-Image Generation**: Creates new images based on generated captions
- **User-Friendly Interface**: Clean, intuitive design with a single-window layout
- **Consistent Image Handling**: Maintains 200x200 dimensions for optimal performance

## 🛠️ Technologies Used

- Python
- Gradio
- Vision-Language Model for captioning
- Diffusion Model for image generation
- PIL (Python Imaging Library)

## 🚀 Getting Started

### Prerequisites

```bash
python 3.8+
pip
```

### Installation

1. Clone the repository

```bash
git clone [https://github.com/Montegan/gradioImage]
cd genai-game
```

2. Install dependencies

```bash
pip install -r requirements.txt
```

3. Run the application

```bash
python app.py
```

4. Open your browser and navigate to `http://localhost:7860`

## 📝 Usage

1. **Upload an Image**

   - Click on the left image box to upload your image
   - Images will be automatically resized to 200x200

2. **Generate Caption**

   - Click "Generate Caption" to create a description of your image
   - The caption will appear in the text box below

3. **Create New Image**
   - Click "Generate Image" to create a new image based on the caption
   - The generated image will appear in the right image box

## ⚙️ Configuration

You can modify the following parameters in `config.py`:

- Image dimensions (default: 200x200)
- Model parameters
- Interface layout

## 🤝 Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📜 License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## 🙏 Acknowledgments

- Thanks to Gradio team for the fantastic framework
- Vision-Language Model community
- Diffusion Model developers

## 📞 Contact

Simon Fasil - [fasilsimon8@gmail.com]

Project Link: [https://github.com/Montegan/gradioImage]

## 🎓 Learn More

For a detailed technical overview of the project, check out our [presentation](https://docs.google.com/presentation/d/11cjat3jfK_sJ84Oy-sIILJhBqA2TibBrRRn50nOv2pE/edit?usp=sharing).
