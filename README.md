# PhotoStamp Organizer

PhotoStamp Organizer es una herramienta en Python diseñada para **estampar información contextual directamente sobre fotografías** y **organizarlas automáticamente en carpetas**, utilizando datos EXIF o, en su defecto, la fecha de modificación del archivo.

Es especialmente útil para **documentación de obras**, **inspecciones técnicas**, **seguimiento de proyectos** o cualquier flujo de trabajo donde la trazabilidad visual sea crítica.

---

## 🚀 Características principales

- 📅 Obtiene automáticamente la **fecha y hora real** desde:
  - EXIF (`DateTimeOriginal`)
  - Fecha de modificación del archivo (fallback automático)
- 🖼️ Estampa sobre la imagen:
  - Nombre del proyecto
  - Autor
  - Día y hora
- 🎨 Texto legible con:
  - Fondo semi-transparente
  - Borde (stroke) para máxima visibilidad
- 📁 Organización automática en carpetas:
  - Detecta códigos en el nombre del archivo mediante **expresiones regulares**
  - Crea carpetas de destino de forma inteligente
- 💾 Conserva calidad alta en la imagen final (`quality=95`)
- ⚙️ Ejecución simple: procesa todas las imágenes de la carpeta actual

---

## 🧠 Funcionamiento general

1. El script analiza cada imagen (`.jpg`, `.jpeg`, `.png`) del directorio actual.
2. Extrae un **código identificador** del nombre del archivo para crear la carpeta destino.
3. Obtiene la fecha:
   - Primero desde EXIF
   - Si no existe, desde la fecha de modificación
4. Estampa el bloque de información en la esquina inferior izquierda.
5. Guarda la imagen procesada en su carpeta correspondiente.

---

## 📂 Ejemplo de estructura generada

/proyecto

│

├── AB-2021-0045+003/

│ ├── AB-2021-0045+003_foto1_barrionuevo.jpg

│ └── AB-2021-0045+003_foto2_barrionuevo.jpg

│

├── CD-2021-0099+012/

│ └── CD-2021-0099+012_foto1_barrionuevo.jpg

---

## 🛠️ Requisitos

- Python 3.9+
- Librerías:
  - Pillow
  - piexif

Instalación rápida:

```bash
pip install pillow piexif
```
---

## ▶️ Uso
Coloca el script en la carpeta que contiene las imágenes.

Ejecuta:

```bash
python main.py
```

El script procesará automáticamente todas las imágenes compatibles.

---

## ⚙️ Configuración rápida
Puedes modificar fácilmente:

```python
COLOR_TEXTO = "white"
BORDE_TEXTO = "black"
TAMANO_FUENTE = 22
```
Y el bloque de texto estampado:

```python
texto = (
    "Obras de Paso - Campaña 2021\n"
    "Rubén J. Barrionuevo Jiménez\n"
    f"Día: {dia}\n"
    f"Hora: {hora}"
)
```

---

## 🧩 Casos de uso ideales

Documentación fotográfica de obras
Inspecciones técnicas y peritajes
Seguimiento temporal de proyectos
Archivos históricos con trazabilidad visual
Automatización de flujos fotográficos profesionales

---

## 📄 Licencia
Este proyecto se distribuye bajo licencia MIT.
Puedes usarlo, modificarlo y adaptarlo libremente.

---

## ✍️ Autor
Desarrollado por Rubén J. Barrionuevo Jiménez







