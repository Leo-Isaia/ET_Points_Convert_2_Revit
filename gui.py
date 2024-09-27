from pathlib import Path
from tkinter import Tk, Canvas, PhotoImage, Text, Scrollbar, filedialog, messagebox
from PIL import Image, ImageTk

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\Lynke\Mega\Pruebas Python\AppConvert\build\assets\frame0")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


def create_transparent_rectangle(width, height, opacity=0.8):
    """Crear una imagen con un rectángulo semi-transparente."""
    img = Image.new("RGBA", (width, height), (255, 255, 255, 0))
    rect_color = (119, 119, 119, int(255 * opacity))  # Gris con opacidad
    for x in range(width):
        for y in range(height):
            img.putpixel((x, y), rect_color if y < height else (255, 255, 255, 0))
    return img


def process_csv(content):
    lines = content.splitlines()
    processed_lines = []
    processed_lines.append(lines[0])
    for line in lines[1:]:
        if line[0].isdigit():
            parts = line.split(',')
            processed_lines.append(','.join(parts[1:]))
    return '\n'.join(processed_lines)


def process_txt(content):
    lines = content.splitlines()
    processed_lines = []
    for line in lines:
        if line[0].isdigit():
            processed_lines.append(line)
    return '\n'.join(processed_lines)


def open_file():
    file_path = filedialog.askopenfilename(
        title="Seleccionar archivo", 
        filetypes=[("CSV files", "*.csv"), ("TXT files", "*.txt")]
    )

    if file_path:
        try:
            with open(file_path, "r") as file:
                content = file.read()
            if file_path.endswith('.csv'):
                processed_content = process_csv(content)
            else:
                processed_content = process_txt(content)

            entry_1.config(state='normal')
            entry_1.delete(1.0, "end")
            entry_1.insert("end", processed_content)
            entry_1.config(state='disabled')
            entry_1.file_path = file_path
        except Exception as e:
            entry_1.config(state='normal')
            entry_1.delete(1.0, "end")
            entry_1.insert("end", f"Error al leer el archivo: {e}")
            entry_1.config(state='disabled')


def save_as_txt(content, save_path):
    output_file = Path(save_path) / "Puntos Listos para Revit.txt"
    try:
        with open(output_file, "w") as file:
            file.write(content)
        messagebox.showinfo("Puntos exportados con éxito", f"Archivo guardado como: {output_file}")
        window.quit()
    except Exception as e:
        messagebox.showerror("Error al exportar el archivo", f"No se pudo guardar el archivo: {e}")


def button_1_click(event):
    open_file()


def button_2_click(event):
    content = entry_1.get(1.0, "end-1c")
    save_path = filedialog.askdirectory(title="Seleccionar carpeta para guardar el TXT")
    if save_path:
        save_as_txt(content, save_path)


# Iniciar la ventana de Tkinter
window = Tk()
window.title("Conversor de Puntos para REVIT")

# Redimensionar el icono
icon_path = relative_to_assets("icon.ico")
icon_image = Image.open(icon_path)
icon_image = icon_image.resize((32, 32))  # Cambia el tamaño aquí
icon_photo = ImageTk.PhotoImage(icon_image)

window.iconphoto(False, icon_photo)
window.geometry("800x600")
window.configure(bg="#FFFFFF")

# Crear el canvas
canvas = Canvas(
    window,
    bg="#FFFFFF",
    height=600,
    width=800,
    bd=0,
    highlightthickness=0,
    relief="ridge"
)

canvas.place(x=0, y=0)

# Cargar las imágenes
image_image_1 = PhotoImage(file=relative_to_assets("image_1.png"))
canvas.create_image(300.0, 400.0, image=image_image_1)

# Crear imágenes semi-transparentes y dibujarlas en el canvas
top_rect = create_transparent_rectangle(800, 103, opacity=0.8)
bottom_rect = create_transparent_rectangle(800, 76, opacity=0.8)

# Convertir las imágenes a formato PhotoImage
top_rect_tk = ImageTk.PhotoImage(top_rect)
bottom_rect_tk = ImageTk.PhotoImage(bottom_rect)

# Dibujar las imágenes en el canvas
canvas.create_image(0, 0, image=top_rect_tk, anchor="nw")
canvas.create_image(0, 524, image=bottom_rect_tk, anchor="nw")

canvas.create_text(168.0, 35.0, anchor="nw", text="Convertir Puntos de Estación Total para REVIT", fill="#FFFFFF", font=("Roboto", 24 * -1))

# Crear el primer botón usando el canvas
button_image_1 = PhotoImage(file=relative_to_assets("button_1.png"))
button_1 = canvas.create_image(223.0, 468.0, image=button_image_1)
canvas.tag_bind(button_1, "<Button-1>", button_1_click)

# Crear el segundo botón usando el canvas
button_image_2 = PhotoImage(file=relative_to_assets("button_2.png"))
button_2 = canvas.create_image(571.0, 468.0, image=button_image_2)
canvas.tag_bind(button_2, "<Button-1>", button_2_click)

# Crear la entrada de texto
entry_1 = Text(window, bd=0, bg="#FFFFFF", fg="#000716", highlightthickness=0, state='disabled')
entry_1.place(x=97.0, y=143.0, width=600.0, height=276.0)

# Crear la barra de desplazamiento
scrollbar = Scrollbar(window, command=entry_1.yview)
scrollbar.place(x=703, y=143, height=276)

entry_1.config(yscrollcommand=scrollbar.set)  # Vincular scrollbar al Text

image_image_2 = PhotoImage(
    file=relative_to_assets("image_2.png"))
canvas.create_image(
    130.0, 54.0,
    image=image_image_2
)

image_image_3 = PhotoImage(
    file=relative_to_assets("image_3.png"))
canvas.create_image(
    223.0, 561.0,
    image=image_image_3
)

canvas.create_text(258.0, 542.0, anchor="nw", text="Aplicación desarrollada por Leonardo Daniel ISAIA\nhttps://github.com/Leo-Isaia", fill="#FFFFFF", font=("Roboto", 14 * -1))

window.resizable(False, False)
window.mainloop()
