import os
from PIL import Image, ImageDraw, ImageFont
import piexif
import re
from datetime import datetime

# --------------------------------------------
# CONFIGURACIÓN GENERAL
# --------------------------------------------
COLOR_TEXTO = "white"
BORDE_TEXTO = "black"
TAMANO_FUENTE = 22

# --------------------------------------------
# FUNCIONES
# --------------------------------------------

def obtener_carpeta_destino(nombre_archivo: str) -> str:
    patron = r"^([0-9A-Za-z]{2}-\d{4}-\d{4}\+\d{3}(?:-(?!BD$|BI$|bi$|bd$)[A-Za-z]+)?)-"
    m = re.match(patron, nombre_archivo, re.IGNORECASE)
    if m:
        return m.group(1)
    else:
        return os.path.splitext(nombre_archivo)[0]


def obtener_fecha_exif_o_modificacion(imagen_ruta: str, img: Image.Image) -> tuple[str, str]:
    try:
        exif = img.info.get("exif", b"")
        if exif:
            exif_dict = piexif.load(exif)
            fecha = exif_dict["Exif"].get(piexif.ExifIFD.DateTimeOriginal, None)
            if fecha:
                fecha = fecha.decode("utf-8")
                dia, hora = fecha.split(" ")
                return dia, hora
    except:
        pass

    ts = os.path.getmtime(imagen_ruta)
    fecha_mod = datetime.fromtimestamp(ts).strftime("%Y:%m:%d %H:%M:%S")
    dia, hora = fecha_mod.split(" ")
    print(f"[SIN EXIF] Usando fecha de modificación: {os.path.basename(imagen_ruta)}")
    return dia, hora


def estampar_fecha(imagen_ruta: str, carpeta_destino: str):
    try:
        img = Image.open(imagen_ruta).convert("RGB")
    except Exception as e:
        print(f"[ERROR] No se pudo abrir {os.path.basename(imagen_ruta)} -> {e}")
        return

    dia, hora = obtener_fecha_exif_o_modificacion(imagen_ruta, img)

    texto = (
        "Title\n"
        "Subtitle\n"
        f"Day: {dia}\n"
        f"Hour: {hora}"
    )

    draw = ImageDraw.Draw(img)
    try:
        font = ImageFont.truetype("arial.ttf", TAMANO_FUENTE)
    except:
        font = ImageFont.load_default()

    # Obtener tamaño del texto
    bbox = draw.multiline_textbbox((0,0), texto, font=font, spacing=10)
    text_width = bbox[2] - bbox[0]
    text_height = bbox[3] - bbox[1]

    # Posición inferior izquierda con margen
    margin = 20
    x = margin
    y = img.height - text_height - margin

    # Fondo semi-transparente
    fondo_color = (0, 0, 0, 150)  # negro semi-transparente
    fondo = Image.new("RGBA", (text_width + 20, text_height + 30), fondo_color)
    img.paste(fondo, (x-10, y-10), fondo)

    # Texto con borde usando stroke
    draw.multiline_text(
        (x, y),
        texto,
        font=font,
        fill=COLOR_TEXTO,
        spacing=10,
        stroke_width=2,
        stroke_fill=BORDE_TEXTO
    )

    # Crear carpeta si no existe
    os.makedirs(carpeta_destino, exist_ok=True)

    base = os.path.splitext(os.path.basename(imagen_ruta))[0]
    salida_path = os.path.join(carpeta_destino, f"{base}_signed.jpg")

    try:
        img.save(salida_path, quality=95)
        print(f"[OK] {os.path.basename(salida_path)} guardada en {carpeta_destino}")
    except Exception as e:
        print(f"[ERROR] No se pudo guardar {salida_path} -> {e}")

# --------------------------------------------
# PROCESAMIENTO PRINCIPAL
# --------------------------------------------

def main():
    carpeta_actual = os.getcwd()

    for archivo in os.listdir(carpeta_actual):
        if not archivo.lower().endswith((".jpg", ".jpeg", ".png")):
            continue

        ruta_imagen = os.path.join(carpeta_actual, archivo)
        codigo_carpeta = obtener_carpeta_destino(archivo)
        carpeta_destino = os.path.join(carpeta_actual, codigo_carpeta)

        estampar_fecha(ruta_imagen, carpeta_destino)

    print("\n--- PROCESO COMPLETADO ---")


# --------------------------------------------
# EJECUCIÓN
# --------------------------------------------
if __name__ == "__main__":
    main()
