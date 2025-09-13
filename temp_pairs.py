#!/usr/bin/env python3
import re

# Read the file
with open('/Users/mahir/Desktop/mahirshah13.github.io/1/index.html', 'r') as f:
    content = f.read()

# Define the pattern to match single images and extract the image info
pattern = r'<div class="single-image">\s*<img src="([^"]+)" alt="([^"]+)">\s*<div class="image-label">Aligned Result</div>\s*</div>'

def replace_single(match):
    aligned_src = match.group(1)
    aligned_alt = match.group(2)
    
    # Convert aligned path to original path
    original_src = aligned_src.replace('_aligned.jpg', '_original.jpg')
    original_alt = aligned_alt.replace(' Aligned', ' Original')
    
    return f'''<div class="image-pair">
                            <div>
                                <img src="{original_src}" alt="{original_alt}">
                                <div class="image-label">Original</div>
                            </div>
                            <div>
                                <img src="{aligned_src}" alt="{aligned_alt}">
                                <div class="image-label">Aligned</div>
                            </div>
                        </div>'''

# Replace all occurrences
new_content = re.sub(pattern, replace_single, content, flags=re.MULTILINE | re.DOTALL)

# Write back to file
with open('/Users/mahir/Desktop/mahirshah13.github.io/1/index.html', 'w') as f:
    f.write(new_content)

print("Replacement complete!")
