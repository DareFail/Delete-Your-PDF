from setuptools import setup

# read the contents of your README file
from pathlib import Path
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setup(name='delete-your-pdf',
    version='1.0.3',
    description='Crop, Rotate, and extract text from your PDFs so you can delete them',
    author='James Steinberg',
    author_email='jamespsteinberg@gmail.com',
    url='https://github.com/DareFail/delete-your-pdf',
    packages=['deleteYourPDF'],
    install_requires=['pypdfium2', 'pillow'],
    long_description=long_description,
    long_description_content_type='text/markdown',
)