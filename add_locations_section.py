#!/usr/bin/env python3
import os
import re
from pathlib import Path

# Define all locations (capitalized versions)
LOCATIONS = [
    ("agra", "Agra"),
    ("aligarh", "Aligarh"),
    ("ayodhya", "Ayodhya"),
    ("azamgarh", "Azamgarh"),
    ("bareilly", "Bareilly"),
    ("bhadohi", "Bhadohi"),
    ("firozabad", "Firozabad"),
    ("ghaziabad", "Ghaziabad"),
    ("gorakhpur", "Gorakhpur"),
    ("greater-noida", "Greater Noida"),
    ("hapur", "Hapur"),
    ("jaunpur", "Jaunpur"),
    ("jhansi", "Jhansi"),
    ("kanpur", "Kanpur"),
    ("lucknow", "Lucknow"),
    ("mathura", "Mathura"),
    ("meerut", "Meerut"),
    ("mirzapur", "Mirzapur"),
    ("moradabad", "Moradabad"),
    ("muzaffarnagar", "Muzaffarnagar"),
    ("noida", "Noida"),
    ("prayagraj", "Prayagraj"),
    ("rampur", "Rampur"),
    ("saharanpur", "Saharanpur"),
    ("shahjahanpur", "Shahjahanpur"),
    ("vrindavan", "Vrindavan")
]

ALL_SERVICES = [
    "seo-optimization",
    "social-media-marketing",
    "ppc-advertising",
    "content-marketing",
    "brand-development",
    "analytics-reporting",
    "email-marketing",
    "web-development",
    "marketing-strategy"
]

def get_location_button_html(service_type, current_location):
    """Generate location buttons for a specific service type"""
    buttons_html = ""
    for location_slug, location_name in LOCATIONS:
        buttons_html += f'                <a href="{service_type}-services-{location_slug}.html" class="location-btn">{location_name}</a>\n'
    return buttons_html

def get_services_html():
    """Generate the services list HTML"""
    services_list = {
        "seo-optimization": "SEO Optimization",
        "social-media-marketing": "Social Media Marketing",
        "ppc-advertising": "PPC Advertising",
        "content-marketing": "Content Marketing",
        "brand-development": "Brand Development",
        "analytics-reporting": "Analytics & Reporting",
        "email-marketing": "Email Marketing",
        "web-development": "Web Development",
        "marketing-strategy": "Marketing Strategy"
    }
    
    services_html = ""
    for service_slug, service_name in services_list.items():
        services_html += f'''                <div class="service-link-item">
                    <a href="{service_slug}.html">{service_name}</a>
                </div>
'''
    return services_html.rstrip()

def get_services_locations_section(service_type, service_title):
    """Generate the complete services-locations section"""
    location_buttons = get_location_button_html(service_type, None)
    services_list = get_services_html()
    
    section_html = f'''    <section class="section services-locations-section">
        <div class="services-locations-container">
            <h2 class="section-title">View Our {service_title} Services in Other Locations</h2>
            <div class="locations-grid">
{location_buttons}            </div>
            
            <h2 class="section-title" style="margin-top: 4rem;">Explore Our Other Services</h2>
            <div class="services-list">
{services_list}            </div>
        </div>
    </section>
'''
    return section_html

def add_section_to_file(file_path, service_type, service_title):
    """Add the services-locations section to an HTML file"""
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Check if section already exists
    if 'services-locations-section' in content:
        print(f"  ✓ Section already exists in {file_path}")
        return
    
    # Find the footer and insert section before it
    footer_pattern = r'(\s*<footer>)'
    
    if not re.search(footer_pattern, content):
        print(f"  ✗ No footer found in {file_path}")
        return
    
    section_html = get_services_locations_section(service_type, service_title)
    
    # Replace the footer with section + footer
    new_content = re.sub(footer_pattern, section_html + r'\1', content)
    
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(new_content)
    
    print(f"  ✓ Added to {file_path}")

def process_location_files():
    """Process all location-based service files"""
    workspace_dir = Path(os.getcwd())
    
    # Process SEO location files
    print("\n📍 Processing SEO location pages...")
    for location_slug, location_name in LOCATIONS:
        file_path = workspace_dir / f"seo-services-{location_slug}.html"
        if file_path.exists():
            add_section_to_file(str(file_path), "seo-services", "SEO")
    
    # Process PPC location files
    print("\n📍 Processing PPC location pages...")
    for location_slug, location_name in LOCATIONS:
        file_path = workspace_dir / f"ppc-services-{location_slug}.html"
        if file_path.exists():
            add_section_to_file(str(file_path), "ppc-services", "PPC Advertising")
    
    # Process Social Media location files
    print("\n📍 Processing Social Media location pages...")
    for location_slug, location_name in LOCATIONS:
        file_path = workspace_dir / f"social-media-services-{location_slug}.html"
        if file_path.exists():
            add_section_to_file(str(file_path), "social-media-services", "Social Media Marketing")

def process_main_service_files():
    """Process main service pages"""
    print("\n🔧 Processing main service pages...")
    workspace_dir = Path(os.getcwd())
    
    service_files = {
        "seo-optimization.html": "SEO",
        "ppc-advertising.html": "PPC Advertising",
        "social-media-marketing.html": "Social Media Marketing",
        "content-marketing.html": "Content Marketing",
        "brand-development.html": "Brand Development",
        "analytics-reporting.html": "Analytics & Reporting",
        "email-marketing.html": "Email Marketing",
        "web-development.html": "Web Development",
        "marketing-strategy.html": "Marketing Strategy"
    }
    
    for file_name, service_title in service_files.items():
        file_path = workspace_dir / file_name
        if file_path.exists():
            add_section_to_file(str(file_path), "", service_title)
        else:
            print(f"  ! {file_name} not found")

def get_all_services_html_for_general_pages():
    """Generate services HTML for general pages (index, services, etc.)"""
    services_list = {
        "seo-optimization": "SEO Optimization",
        "social-media-marketing": "Social Media Marketing",
        "ppc-advertising": "PPC Advertising",
        "content-marketing": "Content Marketing",
        "brand-development": "Brand Development",
        "analytics-reporting": "Analytics & Reporting",
        "email-marketing": "Email Marketing",
        "web-development": "Web Development",
        "marketing-strategy": "Marketing Strategy"
    }
    
    section_content = f'''    <section class="section services-locations-section">
        <div class="services-locations-container">
            <h2 class="section-title">Our Digital Marketing Services</h2>
            <p class="section-subtitle">Comprehensive digital marketing solutions available in multiple locations across Uttar Pradesh</p>
            
            <h3 style="margin-top: 3rem; margin-bottom: 2rem; text-align: center; font-size: 1.3rem; color: var(--navy-dark);">Available Services</h3>
            <div class="services-list">
'''
    
    for service_slug, service_name in services_list.items():
        section_content += f'''                <div class="service-link-item">
                    <a href="{service_slug}.html">{service_name}</a>
                </div>
'''
    
    section_content += '''            </div>
            
            <h3 style="margin-top: 3rem; margin-bottom: 2rem; text-align: center; font-size: 1.3rem; color: var(--navy-dark);">Service Locations</h3>
            <div class="locations-grid">
'''
    
    for location_slug, location_name in LOCATIONS:
        section_content += f'                <a href="#" class="location-btn">{location_name}</a>\n'
    
    section_content += '''            </div>
        </div>
    </section>
'''
    
    return section_content

def process_general_pages():
    """Process general pages like index.html, services.html, etc."""
    print("\n📄 Processing general pages...")
    workspace_dir = Path(os.getcwd())
    
    general_pages = ["index.html", "services.html", "about.html", "contact.html"]
    
    for file_name in general_pages:
        file_path = workspace_dir / file_name
        if file_path.exists():
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            if 'services-locations-section' not in content:
                section_html = get_all_services_html_for_general_pages()
                new_content = re.sub(r'(\s*<footer>)', section_html + r'\1', content)
                
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                
                print(f"  ✓ Added to {file_name}")
            else:
                print(f"  ✓ Section already exists in {file_name}")
        else:
            print(f"  ! {file_name} not found")

if __name__ == "__main__":
    print("🚀 Adding Services & Locations Section to all pages...\n")
    
    try:
        process_location_files()
        process_main_service_files()
        process_general_pages()
        
        print("\n✅ Successfully added services-locations section to all pages!")
        print("📊 Don't forget to test the pages in your browser.")
    except Exception as e:
        print(f"\n❌ Error occurred: {e}")
        import traceback
        traceback.print_exc()
