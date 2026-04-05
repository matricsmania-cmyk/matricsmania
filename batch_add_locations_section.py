#!/usr/bin/env python3
"""
Batch add services-locations sections to all location-based HTML files
Run this script to automatically update remaining location pages
"""
import os
import re
from pathlib import Path

LOCATIONS = [
    ("agra", "Agra"), ("aligarh", "Aligarh"), ("ayodhya", "Ayodhya"),
    ("azamgarh", "Azamgarh"), ("bareilly", "Bareilly"), ("bhadohi", "Bhadohi"),
    ("firozabad", "Firozabad"), ("ghaziabad", "Ghaziabad"), ("gorakhpur", "Gorakhpur"),
    ("greater-noida", "Greater Noida"), ("hapur", "Hapur"), ("jaunpur", "Jaunpur"),
    ("jhansi", "Jhansi"), ("kanpur", "Kanpur"), ("lucknow", "Lucknow"),
    ("mathura", "Mathura"), ("meerut", "Meerut"), ("mirzapur", "Mirzapur"),
    ("moradabad", "Moradabad"), ("muzaffarnagar", "Muzaffarnagar"), ("noida", "Noida"),
    ("prayagraj", "Prayagraj"), ("rampur", "Rampur"), ("saharanpur", "Saharanpur"),
    ("shahjahanpur", "Shahjahanpur"), ("vrindavan", "Vrindavan")
]

def create_location_buttons(prefix):
    buttons = ""
    for slug, name in LOCATIONS:
        buttons += f'                <a href="{prefix}-services-{slug}.html" class="location-btn">{name}</a>\n'
    return buttons.rstrip()

def create_services_list():
    services = {
        "ppc-advertising": "PPC Advertising",
        "seo-optimization": "SEO Optimization",
        "social-media-marketing": "Social Media Marketing",
        "content-marketing": "Content Marketing",
        "brand-development": "Brand Development",
        "analytics-reporting": "Analytics & Reporting",
        "email-marketing": "Email Marketing",
    }
    html = ""
    for slug, name in services.items():
        html += f'                <div class="service-link-item">\n                    <a href="{slug}.html">{name}</a>\n                </div>\n'
    return html.rstrip()

def process_file(filepath, service_display):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    if 'services-locations-section' in content:
        return False
    
    # Get service prefix from filename
    if 'ppc-services-' in filepath:
        prefix = 'ppc-services'
        display = 'PPC Advertising'
    elif 'seo-services-' in filepath:
        prefix = 'seo-services'
        display = 'SEO'
    elif 'social-media-services-' in filepath:
        prefix = 'social-media-services'
        display = 'Social Media Marketing'
    else:
        return False
    
    buttons = create_location_buttons(prefix)
    services = create_services_list()
    
    section = f'''    <!-- Services & Locations Section -->
    <section class="section services-locations-section">
        <div class="services-locations-container">
            <h2 class="section-title">View Our {display} Services in Other Locations</h2>
            <div class="locations-grid">
{buttons}            </div>
            
            <h2 class="section-title" style="margin-top: 4rem;">Explore Our Other Services</h2>
            <div class="services-list">
{services}            </div>
        </div>
    </section>
'''
    
    # Insert before footer
    new_content = re.sub(r'(\s*<footer>)', section + r'\1', content)
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(new_content)
    return True

# Run
if __name__ == '__main__':
    workspace = Path.cwd()
    updated = 0
    skipped = 0
    
    patterns = [
        ('ppc-services-*.html', 'PPC'),
        ('seo-services-*.html', 'SEO'),
        ('social-media-services-*.html', 'Social Media'),
    ]
    
    for pattern, service_name in patterns:
        print(f"\n📍 Processing {service_name} location files...")
        for filepath in sorted(workspace.glob(pattern)):
            if process_file(str(filepath), service_name):
                print(f"  ✓ {filepath.name}")
                updated += 1
            else:
                print(f"  - {filepath.name} (skipped)")
                skipped += 1
    
    print(f"\n✅ Added sections to {updated} files ({skipped} skipped)")
