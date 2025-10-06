# Neural Caption Generator

A dual-mode application that uses Google Vision API and Google's Gemini AI to generate creative social media captions from images. Can be used as a command-line tool or web application.

## Features

- 🖼️ **Image Upload**: Drag & drop or click to upload images (web mode)
- 🔍 **Text Detection**: Automatically extracts text from images using Google Vision API
- 🏷️ **Label Detection**: Identifies objects and themes in images
- 🤖 **AI Caption Generation**: Creates 3 unique social media captions using Gemini AI
- 💻 **Modern Web Interface**: Beautiful, responsive design with real-time feedback
- 🖥️ **Command Line Mode**: Process images directly from terminal

## Setup

1. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

2. **Configure Google APIs**:
   - Ensure your `neuralcaption-4873593c7bc4.json` service account key is in the project directory
   - API key is already configured in the code

## Usage

### Command Line Mode
```bash
python test.py
```
This will process the `1.png` file and display results in the terminal.

### Web Mode
```bash
python web_interface.py
```
Then open your browser and go to `http://localhost:5001`

### Web Interface Usage
1. Upload an image (PNG, JPG, JPEG, GIF, BMP, WEBP - Max 16MB)
2. Click "Generate Captions"
3. View the detected text, image labels, and AI-generated captions
4. Copy the captions for your social media posts!

## File Structure

- `test.py` - Core caption generation functions (CLI mode)
- `web_interface.py` - Web application with Flask routes
- `templates/index.html` - Web interface template
- `requirements.txt` - Python dependencies
- `neuralcaption-4873593c7bc4.json` - Google Cloud service account key
- `1.png` - Sample image for testing

## API Endpoints (Web Mode)

- `GET /` - Main web interface
- `POST /upload` - Upload and process images
- `GET /health` - Health check endpoint

## Technologies Used

- **Backend**: Flask (Python)
- **AI Services**: Google Vision API, Google Gemini AI
- **Frontend**: HTML5, CSS3, JavaScript
- **File Handling**: Werkzeug secure file uploads
