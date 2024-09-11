import pypdfium2 as pdfium
import base64
import requests
from io import BytesIO
from PIL import Image


def countPdfPages(file: str) -> int:
    pdf = pdfium.PdfDocument(file)
    return len(pdf)


def pdfToImagePages(file: str, page_number: int = None) -> list:
    imagePages = []
    pdf = pdfium.PdfDocument(file)

    if page_number:
        page = pdf[page_number - 1]
        image = page.render(scale=4).to_pil()
        buffer = BytesIO()
        image.save(buffer, format="PNG")
        img_str = base64.b64encode(buffer.getvalue()).decode()
        img_str = f"data:image/png;base64,{img_str}"
        imagePages.append(img_str)
    else:
        for i in range(len(pdf)):
            page = pdf[i]
            image = page.render(scale=4).to_pil()
            buffer = BytesIO()
            image.save(buffer, format="PNG")
            img_str = base64.b64encode(buffer.getvalue()).decode()
            img_str = f"data:image/png;base64,{img_str}"
            imagePages.append(img_str)

    return imagePages


def cropRotateImage(file, x: int, y: int, width: int, height: int, rotation_degrees: int = 0, expand_for_rotation: bool = True) -> str:

    if isinstance(file, str):
        base64_data = file.split(",")[1]
        image_data = base64.b64decode(base64_data)
        image = Image.open(BytesIO(image_data))
        
    elif isinstance(file, BytesIO):
        image = Image.open(file)
    
    cropped_image = image.crop((x, y, x+width, y+height))

    rotation_degrees = (360 - rotation_degrees) % 360
    
    rotated_image = cropped_image.rotate(rotation_degrees, expand=expand_for_rotation)

    buffered = BytesIO()
    rotated_image.save(buffered, format = "PNG")
    
    img_str = base64.b64encode(buffered.getvalue()).decode()

    img_str = f"data:image/png;base64,{img_str}"

    return img_str


def imageWidthHeight(file) -> list:

    if isinstance(file, str):
        base64_data = file.split(",")[1]
        image_data = base64.b64decode(base64_data)
        image = Image.open(BytesIO(image_data))
        
    elif isinstance(file, BytesIO):
        image = Image.open(file)
    
    widthHeight = image.size

    return {
        "width": widthHeight[0],
        "height": widthHeight[1],
    }



def imageToText_Roboflow(file, api_key: str) -> str:

    if isinstance(file, str):
        base64_data = file.split(",")[1]
        image_data = base64.b64decode(base64_data)
        image = Image.open(BytesIO(image_data))
        
    elif isinstance(file, BytesIO):
        image = Image.open(file)

    if image.mode == 'RGBA':
        rgb_image = image.convert('RGB')
    else:
        rgb_image = image

    byte_arr = BytesIO()
    rgb_image.save(byte_arr, format='PNG')
    encoded_image = base64.encodebytes(byte_arr.getvalue()).decode('ascii')

    data = {
        "image": {
            "type": "base64", 
            "value": encoded_image
        }
    }

    ocr_results = requests.post("https://infer.roboflow.com/doctr/ocr?api_key=" + api_key, json=data).json()

    return ocr_results["result"]
