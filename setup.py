from setuptools import setup, find_packages

setup(
    name="img_to_pdf_converter",
    version="1.0.0",
    description="Un outil simple pour convertir des images en PDF",
    author="Clémence Fernandez",
    author_email="clemencefrz@gmail.com",
    packages=find_packages(),
    install_requires=[
        "img2pdf",
    ],
    entry_points={
        'console_scripts': [
            'img_to_pdf=main:main',
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
)
