import base64
import os
import re

html_path = "index.html"
with open(html_path, "r", encoding="utf-8") as f:
    html_content = f.read()

images = [
    "/Users/cauamendes/.gemini/antigravity/brain/bac8656c-fdbe-456a-837a-75dd80c4679e/media__1776973484426.jpg",
    "/Users/cauamendes/.gemini/antigravity/brain/bac8656c-fdbe-456a-837a-75dd80c4679e/media__1776973494452.jpg",
    "/Users/cauamendes/.gemini/antigravity/brain/bac8656c-fdbe-456a-837a-75dd80c4679e/media__1776973506856.jpg",
    "/Users/cauamendes/.gemini/antigravity/brain/bac8656c-fdbe-456a-837a-75dd80c4679e/media__1776973526440.jpg",
    "/Users/cauamendes/.gemini/antigravity/brain/bac8656c-fdbe-456a-837a-75dd80c4679e/media__1776973563003.jpg"
]

slides_html = ""
existing_slides = re.findall(r'<div class="slide".*?>', html_content)
start_idx = len(existing_slides)

for idx, img_path in enumerate(images):
    with open(img_path, "rb") as bf:
        b64_str = base64.b64encode(bf.read()).decode()
    
    slide = f'<div class="slide" onclick="openLightbox({start_idx + idx})"><img src="data:image/jpeg;base64,{b64_str}" alt="Tattoo Portfolio Image" loading="lazy"><div class="slide-overlay"><span>Black &amp; Grey Realism</span></div></div>'
    slides_html += slide

last_slide_match = list(re.finditer(r'<div class=\"slide\"[^>]*>.*?</div>\s*</div>', html_content, re.DOTALL))
if last_slide_match:
    insert_pos = last_slide_match[-1].end()
    new_html = html_content[:insert_pos] + slides_html + html_content[insert_pos:]
    with open(html_path, "w", encoding="utf-8") as f:
        f.write(new_html)
    print(f"Appended {len(images)} slides successfully! New HTML length: {len(new_html)} bytes")
else:
    print("Could not find the last slide.")
