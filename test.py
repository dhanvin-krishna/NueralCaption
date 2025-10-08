
import os
import google.generativeai as genai
from dotenv import load_dotenv

# Configure Google AI

load_dotenv('.env')
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = os.getenv("GOOGLE_APPLICATION_CREDENTIALS")



def detect_text(path):
    from google.cloud import vision

    client = vision.ImageAnnotatorClient()
    textlist = []

    with open(path, "rb") as image_file:
        content = image_file.read()

    image = vision.Image(content=content)

    response = client.text_detection(image=image)
    texts = response.text_annotations

    for text in texts:
        textlist.append(text.description)

    if response.error.message:
        raise Exception(
            "{}\nFor more info on error messages, check: "
            "https://cloud.google.com/apis/design/errors".format(response.error.message)
        )
    return textlist

def detect_labels(path):
    """Detects labels in the file."""
    from google.cloud import vision

    client = vision.ImageAnnotatorClient()

    with open(path, "rb") as image_file:
        content = image_file.read()

    image = vision.Image(content=content)

    response = client.label_detection(image=image)
    labels = response.label_annotations
    lab_ls =[]

    for label in labels:
        lab_ls.append(label.description)

    if response.error.message:
        raise Exception(
            "{}\nFor more info on error messages, check: "
            "https://cloud.google.com/apis/design/errors".format(response.error.message)
        )
    return lab_ls

def generate_captions(text, labels):
    """Generate social media captions using Gemini AI"""
    model = genai.GenerativeModel("gemini-pro-latest")
    
    prompt = f"""
    A user uploaded a poster.

    Poster text: "{text}"
    Detected themes: {', '.join(labels)}

   Write 3 engaging Instagram captions based on this poster.
    Each caption should:
    - Be 2–4 sentences long.
    - Have a warm, emotional, or energetic tone (depending on the poster content).
    - Include 2–4 relevant emojis.
    - Include 4–8 relevant hashtags.
    - Start with "Caption 1:", "Caption 2:", "Caption 3:".
    - Do not include any explanations, introductions, or extra text. Only output the captions.
"""
    
    response = model.generate_content(prompt)
    return response.text

# Command line execution (for testing with 1.png)
if __name__ == '__main__':
    text = detect_text("1.png")
    label = detect_labels("1.png")
    captions = generate_captions(text[0] if text else "No text detected", label)
    print("Detected Text:", text[0] if text else "No text detected")
    print("Labels:", label)
    print("Generated Captions:")
    print(captions)
