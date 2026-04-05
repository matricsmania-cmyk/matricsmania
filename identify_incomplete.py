import os
import json
from pathlib import Path

workspace = r"c:\Users\OM\Documents\Matrics Mania"

# Get all SEO and social media files
seo_files = sorted([f.name for f in Path(workspace).glob("seo-services-*.html")])
social_media_files = sorted([f.name for f in Path(workspace).glob("social-media-services-*.html")])

# Files with canonical (from grep results)
seo_with_canonical = [
    'seo-services-bare...html', 'seo-services-agra.html', 'seo-services-ghaziabad.html',
    'seo-services-hapur.html', 'seo-services-greater-noida.html', 'seo-services-gorakhpur.html',
    'seo-services-kanpur.html', 'seo-services-firozabad.html', 'seo-services-jhansi.html',
    'seo-services-bhadohi.html', 'seo-services-jaunpur.html', 'seo-services-azamgarh.html',
    'seo-services-ayodhya.html', 'seo-services-aligarh.html'
]

# Files with service-number from grep results  
seo_with_services = [
    'seo-services-bareilly.html', 'seo-services-agra.html', 'seo-services-ghaziabad.html',
    'seo-services-hapur.html', 'seo-services-kanpur.html', 'seo-services-jhansi.html',
    'seo-services-jaunpur.html', 'seo-services-greater-noida.html', 'seo-services-gorakhpur.html',
    'seo-services-aligarh.html', 'seo-services-azamgarh.html', 'seo-services-ayodhya.html'
]

social_with_services = [
    'social-media-services-vrindavan.html', 'social-media-services-shahjahanpur.html',
    'social-media-services-saharanpur.html', 'social-media-services-rampur.html',
    'social-media-services-prayagraj.html', 'social-media-services-noida.html',
    'social-media-services-muzaffarnagar.html', 'social-media-services-moradabad.html',
    'social-media-services-mirzapur.html', 'social-media-services-meerut.html',
    'social-media-services-mathura.html', 'social-media-services-lucknow.html',
    'social-media-services-kanpur.html', 'social-media-services-jhansi.html',
    'social-media-services-jaunpur.html', 'social-media-services-hapur.html',
    'social-media-services-greater-noida.html'
]

incomplete_seo = []
incomplete_social = []

# Find incomplete SEO files
for f in seo_files:
    if f not in seo_with_services:
        file_path = Path(workspace) / f
        size_kb = os.path.getsize(file_path) / 1024
        incomplete_seo.append({'file': f, 'size_kb': round(size_kb, 2)})

# Find incomplete social media files
for f in social_media_files:
    if f not in social_with_services:
        file_path = Path(workspace) / f
        size_kb = os.path.getsize(file_path) / 1024
        incomplete_social.append({'file': f, 'size_kb': round(size_kb, 2)})

print("INCOMPLETE SEO FILES:")
for item in incomplete_seo:
    print(f"  {item['file']} ({item['size_kb']} KB)")

print(f"\nINCOMPLETE SOCIAL MEDIA FILES:")
for item in incomplete_social:
    print(f"  {item['file']} ({item['size_kb']} KB)")

print(f"\n\nSUMMARY:")
print(f"Total files to check: {len(seo_files) + len(social_media_files)}")
print(f"Complete SEO files: {len(seo_with_services)}/26")
print(f"Incomplete SEO files: {len(incomplete_seo)}/26")
print(f"Complete Social Media files: {len(social_with_services)}/26")
print(f"Incomplete Social Media files: {len(incomplete_social)}/26")
print(f"Total incomplete files: {len(incomplete_seo) + len(incomplete_social)}")

# JSON output
json_output = []
for item in incomplete_seo:
    json_output.append({**item, "type": "SEO", "needs_regeneration": True})
for item in incomplete_social:
    json_output.append({**item, "type": "Social Media", "needs_regeneration": True})

print("\n\nJSON OUTPUT:")
print(json.dumps(json_output, indent=2))
