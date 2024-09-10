from packaging import requirements
from setuptools import setup, find_packages

# Leitura do conteúdo do README.md para usar como long_description
with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="image_processing",  # Nome do seu pacote
    version="0.1.0",  # Versão inicial do seu pacote
    author="Beatriz Gomes",  # Nome do autor
    author_email="beatrizgomesxx@gmail.com",  # E-mail do autor
    description="A simple image processing package",  # Descrição curta
    long_description=long_description,  # Descrição longa do projeto
    long_description_content_type="text/markdown",  # Tipo do long_description (Markdown)
    url="https://github.com/beatrizgomees/image_processing",  # URL do repositório do projeto
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",  # Linguagem de programação suportada
        "License :: OSI Approved :: MIT License",  # Tipo de licença (pode ser alterado)
        "Operating System :: OS Independent",  # Sistema operacional
    ],
    python_requires='>=3.6',
    install_requires=[
        "Pillow",
        "numpy",
    ],
    entry_points={
        'console_scripts': [
            'image-process=image_processing.main:main',  # Comando de linha de comando (ajuste conforme seu projeto)
        ],
    },
)
