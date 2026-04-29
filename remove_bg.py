from PIL import Image

def remove_bg(input_path, output_path):
    try:
        img = Image.open(input_path).convert("RGBA")
        data = img.getdata()
        
        newData = []
        # Reemplazar colores cercanos al blanco (los artefactos del JPG) con transparencia
        for item in data:
            if item[0] > 220 and item[1] > 220 and item[2] > 220:
                newData.append((255, 255, 255, 0)) # Transparente
            else:
                newData.append(item)
                
        img.putdata(newData)
        img.save(output_path, "PNG")
        print("Fondo removido exitosamente.")
    except Exception as e:
        print(f"Error: {e}")

remove_bg('static/img/logo_cropped.jpg', 'static/img/logo.png')
