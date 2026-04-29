import sys
import subprocess

def install_and_import(package):
    try:
        __import__(package)
    except ImportError:
        subprocess.check_call([sys.executable, "-m", "pip", "install", package])

install_and_import('PIL')
from PIL import Image, ImageChops

def trim(im):
    # Asume que el color de la esquina superior izquierda es el color de fondo (blanco)
    bg = Image.new(im.mode, im.size, im.getpixel((0,0)))
    diff = ImageChops.difference(im, bg)
    diff = ImageChops.add(diff, diff, 2.0, -100)
    bbox = diff.getbbox()
    if bbox:
        return im.crop(bbox)
    return im

try:
    im = Image.open('static/img/logo.jpg')
    # Convertir a RGB por si acaso
    im = im.convert('RGB')
    im_cropped = trim(im)
    im_cropped.save('static/img/logo_cropped.jpg')
    print("Logo recortado exitosamente.")
except Exception as e:
    print(f"Error: {e}")
