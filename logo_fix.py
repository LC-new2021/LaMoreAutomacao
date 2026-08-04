from PIL import Image
import numpy as np

# Load original - DO NOT TOUCH the emblem or the text
img = Image.open(r'C:\Users\Usuário\.gemini\antigravity\brain\7b3bb914-0992-4a1e-866a-be9b97adaa40\logo_transparent.png').convert('RGBA')
arr = np.array(img)
result = arr.copy()

# The original image is 874 x 1024 pixels.
# The blue emblem + dark blue text "La More Eventos" spans rows 0-790.
# The ghost white reflection/shadow is BELOW row 790.
# ONLY action: set alpha=0 for rows 790 and below.
result[790:, :, 3] = 0

out = Image.fromarray(result, 'RGBA')
out.save(r'C:\Users\Usuário\Desktop\LaMoreAutomacao\logo-final.png', 'PNG')
print("Done. Only removed rows 790+ (the ghost reflection). Nothing else changed.")
print(f"Output size: {out.size}")
