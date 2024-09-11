# Delete-Your-PDF

Delete your PDF is a set of tools to export information from your PDFs so you can delete them.

Image files can be taken in as both base64 strings or BytesIO objects

## Live Demo

**Live Demo:** [https://pdf.darefail.com](https://pdf.darefail.com)

**Demo Opensource Repo:** [https://github.com/DareFail/AI-Video-Boilerplate-Pro](https://github.com/DareFail/AI-Video-Boilerplate-Pro)


### Installation

```sh
pip install delete-your-pdf
```

## How to use

**countPdfPages**: Counts the number of pages in a PDF and returns an int
```sh
from deleteYourPDF import countPdfPages

numberOfPages = countPdfPages(file="PDF_FILE_HERE")
```

**pdfToImagePages**: Convert PDF to a list of pages that are PNG images as a base64 strings
```sh
from deleteYourPDF import pdfToImagePages

# Return a list containing all pages in order as images
listOfImagePages = pdfToImagePages(file="PDF_FILE_HERE")

# Return a list containing only an image of page 7
listOfImagePages = pdfToImagePages(file="PDF_FILE_HERE", page_number=7)
```

**imageWidthHeight**: get the width and height of an image as a dictionary in pixels {width: 100, height: 100}
```sh
from deleteYourPDF import imageWidthHeight

image_dimensions = imageWidthHeight(file="IMAGE_FILE_HERE")

width = image_dimensions["width"]
height = image_dimensions["height"]
```

**cropRotateImage**: Crop and rotate an image and return a PNG image as a base64 string
```sh
from deleteYourPDF import cropRotateImage

# Returns an image of the top left 100x100 square from an image and rotates it 90 degrees to the right, the new image dimensions will match the rotation
croppedAndRotatedImage = cropRotateImage(file="IMAGE_FILE_HERE", x=0, y=0, width=100, height=100, rotation_degrees=90)

# Returns an image of the top left 100x100 square from an image and keep the original image dimensions
croppedAndRotatedImage = cropRotateImage(file="IMAGE_FILE_HERE", x=0, y=0, width=100, height=100, rotation_degrees=30, expand_for_rotation=False)
```

**imageToText_Roboflow**: Convert image to text with Roboflow OCR and returns a string
```sh
from deleteYourPDF import imageToText_Roboflow

# Returns the text from a local image file
text = imageToText_Roboflow(file="IMAGE_FILE_HERE", api_key="ROBOFLOW_API_KEY_HERE")
```

## Example 1: Convert the top 100 pixels of all pages of a PDF to a list of text
```sh
from deleteYourPDF import countPdfPages, pdfToImagePages, imageToText_Roboflow, cropRotateImage, imageWidthHeight

listOfText = []

listOfImagePages = pdfToImagePages(file="PDF_FILE_HERE")

for imagePage in listOfImagePages:
    image_dimensions = imageWidthHeight(file=imagePage)

    width = image_dimensions["width"]
    height = image_dimensions["height"]

    croppedAndRotatedImage = cropRotateImage(file=imagePage, x=0, y=0, width=width, height=100)
    listOfText.append(imageToText_Roboflow(file=croppedAndRotatedImage, api_key="ROBOFLOW_API_KEY_HERE"))

return listOfText
```

## Example 2: Rotate a 100x100 box in the center of page 7 90 degrees to the right on a PDF and print the text
```sh
from deleteYourPDF import countPdfPages, pdfToImagePages, imageToText_Roboflow, cropRotateImage

if countPdfPages(file="PDF_FILE_HERE") > 7:
    imagePage = pdfToImagePages(file="PDF_FILE_HERE", page_number=7)
    image_dimensions = imageWidthHeight(file=imagePage)

    width = image_dimensions["width"]
    height = image_dimensions["height"]
    x = (width - 100)/2
    y = (height - 100)/2

    croppedAndRotatedImage = cropRotateImage(file=imagePage, x=x, y=y, width=100, height=100, rotation_degrees=90)
    return imageToText_Roboflow(file=croppedAndRotatedImage, api_key="ROBOFLOW_API_KEY_HERE")
```

## Acknowledgements

Thanks to Roboflow for sponsoring this project. Get your free API key at: [Roboflow](https://roboflow.com/)

## License

Distributed under the APACHE 2.0 License. See `LICENSE` for more information.

## Contact

Twitter: [@darefailed](https://twitter.com/darefailed)

Youtube: [How to Video coming soon](https://www.youtube.com/@darefail)

Project Link: [https://github.com/darefail/Delete-Your-PDF](https://github.com/darefail/Delete-Your-PDF)


## Update Package
```sh
python3 -m build
python3 -m twine upload dist/*
```