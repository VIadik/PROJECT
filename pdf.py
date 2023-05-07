from PIL import Image

images = [Image.open("photos/" + f) for f in ["file_53.jpg"]]

pdf_path = "documents/pdf.pdf"

images[0].save(pdf_path, "PDF", resolution=100.0, save_all=True, append_images=images[1:])
