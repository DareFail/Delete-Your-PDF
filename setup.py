from setuptools import setup

setup(name='delete-your-pdf',
    version='1.0.0',
    description='Crop, Rotate, and extract text from your PDFs so you can delete them',
    author='James Steinberg',
    author_email='jamespsteinberg@gmail.com',
    url='https://github.com/DareFail/delete-your-pdf',
    packages=['deleteYourPDF'],
    install_requires=['pypdfium2', 'pillow'],
)