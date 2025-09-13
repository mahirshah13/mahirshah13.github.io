#!/usr/bin/env python3
import re

# Read the file
with open('/Users/mahir/Desktop/mahirshah13.github.io/1/index.html', 'r') as f:
    content = f.read()

# Define the pattern to match slider containers
pattern = r'<div class="slider-container">\s*<img src="([^"]+)" alt="([^"]+)" class="slider-image aligned">\s*<img src="([^"]+)" alt="([^"]+)" class="slider-image original">\s*<div class="slider-overlay">\s*<span class="slider-label">Original</span>\s*<input[^>]+>\s*<span class="slider-label">Aligned</span>\s*</div>\s*</div>'

def replace_slider(match):
    aligned_src = match.group(1)
    aligned_alt = match.group(2)
    original_src = match.group(3)
    original_alt = match.group(4)
    
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
new_content = re.sub(pattern, replace_slider, content, flags=re.MULTILINE | re.DOTALL)

# Write back to file
with open('/Users/mahir/Desktop/mahirshah13.github.io/1/index.html', 'w') as f:
    f.write(new_content)

print("Replacement complete!")
