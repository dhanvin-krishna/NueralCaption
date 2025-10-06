
import os
import google.generativeai as genai

# Configure Google AI
credentials_json = os.environ.get("GOOGLE_APPLICATION_CREDENTIALS_JSON")
if credentials_json:
    creds_dict = json.loads(credentials_json)
    creds = service_account.Credentials.from_service_account_info(creds_dict)
    client = vision.ImageAnnotatorClient(credentials=creds)
else:
    client = vision.ImageAnnotatorClient()



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
    A user uploaded a poster/image.

    The image text says:
    "{text}"

    The image seems to be about: {", ".join(labels)}

    Based on this, write 3 creative and catchy social media captions.
    Use emojis and relevant hashtags.
    Make each caption unique with different styles:
    1. First caption: Excited and direct with full details
    2. Second caption: Question-based and intriguing
    3. Third caption: Short, punchy with bullet points
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
