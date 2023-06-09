from PIL import Image

import config
import os

files = sorted(os.listdir(f"telegram-bot-api/bin/{config.TOKEN}/photos/"), key=lambda x: int(x[5:-4]))

images = [Image.open(f"telegram-bot-api/bin/{config.TOKEN}/photos/{files[-1]}")]

pdf_path = "data/doc.pdf"

images[0].save(pdf_path, "PDF", resolution=100.0, save_all=True, append_images=images[1:])
