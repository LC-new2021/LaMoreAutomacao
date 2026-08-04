from PIL import Image
import numpy as np

# Open the ORIGINAL logo_transparent.png - THE ONE THE USER APPROVED
img = Image.open(r'C:\Users\Usuário\.gemini\antigravity\brain\7b3bb914-0992-4a1e-866a-be9b97adaa40\logo_transparent.png').convert('RGBA')
w, h = img.size
arr = np.array(img)

# Work on a copy - do NOT touch the emblem, only the text
result = arr.copy()

# The text "La More Eventos" is located at rows ~690-780
# Its color is dark navy blue: R ~10-80, G ~30-120, B ~80-180
# Alpha > 30 (not transparent)
# Importantly, it is NOT in the top part of image (the 3D blue emblem)

text_rows = (np.arange(h) >= 685) & (np.arange(h) <= 790)
text_row_mask = np.zeros((h, w), dtype=bool)
text_row_mask[685:790, :] = True

r = result[:,:,0].astype(float)
g = result[:,:,1].astype(float)
b = result[:,:,2].astype(float)
a = result[:,:,3].astype(float)

# Text pixels: in the text row region, non-transparent, dark navy blue color
# Dark navy: R < 100, G < 140, B < 200, and NOT very bright
is_text = (
    text_row_mask &
    (a > 30) &
    (r < 120) &
    (g < 150) &
    (b < 200)
)

# Change ONLY text pixels to pure white
result[is_text, 0] = 255
result[is_text, 1] = 255
result[is_text, 2] = 255
result[is_text, 3] = 255

out = Image.fromarray(result, 'RGBA')
out.save(r'C:\Users\Usuário\Desktop\LaMoreAutomacao\logo-final.png', 'PNG')
print(f"Done! Changed {is_text.sum()} text pixels to white. Saved to logo-final.png")
