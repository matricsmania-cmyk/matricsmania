#!/usr/bin/env python3
"""
Generate a comprehensive sitemap.xml with all pages in the workspace
"""

from pathlib import Path
from datetime import datetime

def generate_sitemap():
    base_path = Path("c:\\Users\\OM\\Documents\\Matrics Mania")
    
    # Define all pages with priorities
    pages = []
    
    # Main pages (priority 1.0, 0.9, etc.)
    main_pages = [
        ("index.html", 1.0, "weekly"),
        ("services.html", 0.9, "weekly"),
        ("about.html", 0.9, "monthly"),
        ("blog.html", 0.8, "weekly"),
        ("contact.html", 0.7, "monthly"),
    ]
    
    # Service pages
    service_pages = [
        "ppc-advertising.html",
        "seo-optimization.html",
        "social-media-marketing.html",
        "content-marketing.html",
        "brand-development.html",
        "analytics-reporting.html",
        "email-marketing.html",
        "marketing-strategy.html",
        "web-development.html",
    ]
    
    # All locations
    locations = [
        "agra", "aligarh", "ayodhya", "azamgarh", "bareilly", "bhadohi",
        "firozabad", "ghaziabad", "gorakhpur", "greater-noida", "hapur",
        "jaunpur", "jhansi", "kanpur", "lucknow", "mathura", "meerut",
        "mirzapur", "moradabad", "muzaffarnagar", "noida", "prayagraj",
        "rampur", "saharanpur", "shahjahanpur", "vrindavan"
    ]
    
    service_types = [
        ("ppc-services", "ppc-services-*.html"),
        ("seo-services", "seo-services-*.html"),
        ("social-media-services", "social-media-services-*.html"),
    ]
    
    # Add main pages
    for page, priority, freq in main_pages:
        filepath = base_path / page
        if filepath.exists():
            pages.append({
                "url": f"https://matricsmania.com/{page}",
                "priority": priority,
                "changefreq": freq,
                "category": "Main"
            })
    
    # Add service pages
    for page in service_pages:
        filepath = base_path / page
        if filepath.exists():
            pages.append({
                "url": f"https://matricsmania.com/{page}",
                "priority": 0.8,
                "changefreq": "weekly",
                "category": "Service"
            })
    
    # Add location pages
    for location in locations:
        filepath = base_path / "locations" / f"{location}.html"
        if filepath.exists():
            pages.append({
                "url": f"https://matricsmania.com/locations/{location}.html",
                "priority": 0.7,
                "changefreq": "monthly",
                "category": "Location"
            })
    
    # Add service-location pages (PPC, SEO, Social Media)
    for location in locations:
        # PPC Services
        ppc_file = base_path / f"ppc-services-{location}.html"
        if ppc_file.exists():
            pages.append({
                "url": f"https://matricsmania.com/ppc-services-{location}.html",
                "priority": 0.7,
                "changefreq": "monthly",
                "category": "PPC Service"
            })
        
        # SEO Services
        seo_file = base_path / f"seo-services-{location}.html"
        if seo_file.exists():
            pages.append({
                "url": f"https://matricsmania.com/seo-services-{location}.html",
                "priority": 0.7,
                "changefreq": "monthly",
                "category": "SEO Service"
            })
        
        # Social Media Services
        sm_file = base_path / f"social-media-services-{location}.html"
        if sm_file.exists():
            pages.append({
                "url": f"https://matricsmania.com/social-media-services-{location}.html",
                "priority": 0.7,
                "changefreq": "monthly",
                "category": "Social Media Service"
            })
    
    # Generate XML
    today = datetime.now().strftime("%Y-%m-%d")
    xml_content = '<?xml version="1.0" encoding="UTF-8"?>\n'
    xml_content += '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
    
    # Organize by category for readability
    current_category = None
    for page in pages:
        if page["category"] != current_category:
            if current_category:
                xml_content += "\n"
            xml_content += f"  <!-- {page['category']} Pages -->\n"
            current_category = page["category"]
        
        xml_content += "  <url>\n"
        xml_content += f"    <loc>{page['url']}</loc>\n"
        xml_content += f"    <lastmod>{today}</lastmod>\n"
        xml_content += f"    <changefreq>{page['changefreq']}</changefreq>\n"
        xml_content += f"    <priority>{page['priority']}</priority>\n"
        xml_content += "  </url>\n"
    
    xml_content += "</urlset>\n"
    
    # Write to file
    sitemap_path = base_path / "sitemap.xml"
    with open(sitemap_path, 'w', encoding='utf-8') as f:
        f.write(xml_content)
    
    # Print statistics
    print(f"✓ Sitemap generated successfully!")
    print(f"✓ Total URLs: {len(pages)}")
    
    # Count by category
    categories = {}
    for page in pages:
        cat = page["category"]
        categories[cat] = categories.get(cat, 0) + 1
    
    print(f"\nBreakdown:")
    for cat, count in sorted(categories.items()):
        print(f"  - {cat}: {count} pages")
    
    print(f"\nSitemap saved to: {sitemap_path}")


if __name__ == "__main__":
    generate_sitemap()
