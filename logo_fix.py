from PIL import Image
import numpy as np

img = Image.open(r'C:\Users\Usuário\.gemini\antigravity\brain\7b3bb914-0992-4a1e-866a-be9b97adaa40\logo_transparent.png').convert('RGBA')
arr = np.array(img)
result = arr.copy()

r = arr[:,:,0].astype(float)
g = arr[:,:,1].astype(float)
b = arr[:,:,2].astype(float)

# Blueness metric
blueness = b - (r + g) / 2.0

# Brightness metric
brightness = (r + g + b) / 3.0

# The fake transparency checkerboard has white (255) and gray (204) squares.
# They are both grayscale, so blueness is near 0.
# The blue emblem has high blueness.
# We want to remove all pixels that are not distinctly blue and are bright enough to be part of the fake background.
is_fake_bg = (brightness > 180) & (blueness < 40)
result[is_fake_bg, 3] = 0

# Soft transition for anti-aliased edge pixels
semi = (brightness > 150) & (brightness <= 180) & (blueness < 40)
fade = (brightness[semi] - 150) / 30.0
result[semi, 3] = np.clip(result[semi, 3] * (1.0 - fade), 0, 255).astype(np.uint8)

# Remove the ghost reflection at the bottom
result[800:, :, 3] = 0

out = Image.fromarray(result, 'RGBA')
out.save(r'C:\Users\Usuário\Desktop\LaMoreAutomacao\logo-final.png', 'PNG')
print("Done - Fake checkerboard background removed, emblem preserved.")
