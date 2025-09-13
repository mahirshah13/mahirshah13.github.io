#!/usr/bin/env python3
import re

# Read the file
with open('/Users/mahir/Desktop/mahirshah13.github.io/1/index.html', 'r') as f:
    content = f.read()

# Define the pattern to match image pairs
pattern = r'<div class="image-pair">\s*<div>\s*<img src="([^"]+)" alt="([^"]+)">\s*<div class="image-label">Original</div>\s*</div>\s*<div>\s*<img src="([^"]+)" alt="([^"]+)">\s*<div class="image-label">Aligned</div>\s*</div>\s*</div>'

def replace_pair(match):
    original_src = match.group(1)
    original_alt = match.group(2)
    aligned_src = match.group(3)
    aligned_alt = match.group(4)
    
    return f'''<div class="single-image">
                            <img src="{aligned_src}" alt="{aligned_alt}">
                            <div class="image-label">Aligned Result</div>
                        </div>'''

# Replace all occurrences
new_content = re.sub(pattern, replace_pair, content, flags=re.MULTILINE | re.DOTALL)

# Write back to file
with open('/Users/mahir/Desktop/mahirshah13.github.io/1/index.html', 'w') as f:
    f.write(new_content)

print("Replacement complete!")
