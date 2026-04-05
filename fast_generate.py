import json
import os

LOCATIONS = ["agra", "aligarh", "ayodhya", "azamgarh", "bareilly", "bhadohi", "firozabad", "ghaziabad", "gorakhpur", "greater-noida", "hapur", "jaunpur", "jhansi", "kanpur", "lucknow", "mathura", "meerut", "mirzapur", "moradabad", "muzaffarnagar", "noida", "prayagraj", "rampur", "saharanpur", "shahjahanpur", "vrindavan"]

SERVICES = {
    "SEO": {
        "title": "SEO Services In",
        "keyword": "SEO services in",
        "items": ["Keyword Research", "On-Page Optimization", "Technical SEO", "Link Building", "Content Strategy", "Local SEO"],
        "cta": "Get Free SEO Audit"
    },
    "PPC": {
        "title": "PPC Advertising Services In",
        "keyword": "PPC advertising services in",
        "items": ["Keyword Bidding Strategy", "Ad Copywriting", "Landing Page Optimization", "Conversion Tracking", "Budget Management", "Remarketing"],
        "cta": "Get Free PPC Audit"
    },
    "Social Media": {
        "title": "Social Media Marketing Services In",
        "keyword": "social media marketing services in",
        "items": ["Content Creation", "Community Management", "Influencer Outreach", "Paid Social Ads", "Analytics", "Strategy"],
        "cta": "Get Free Social Media Audit"
    },
    "Content Marketing": {
        "title": "Content Marketing Services In",
        "keyword": "content marketing services in",
        "items": ["Blog Writing", "Video Content", "Infographic Design", "Whitepapers", "Case Studies", "Newsletters"],
        "cta": "Get Free Content Strategy"
    },
    "Web Development": {
        "title": "Web Development Services In",
        "keyword": "web development services in",
        "items": ["Responsive Design", "UX/UI Design", "Site Speed", "Security", "CMS Setup", "Mobile Optimization"],
        "cta": "Get Free Website Audit"
    },
    "Brand Development": {
        "title": "Brand Development Services In",
        "keyword": "brand development services in",
        "items": ["Logo Design", "Brand Identity", "Messaging Strategy", "Visual Design", "Brand Guidelines", "Positioning"],
        "cta": "Get Free Brand Consultation"
    }
}

def generate_html(service, location):
    """Generate minimal but complete HTML"""
    loc_title = location.title()
    svc_config = SERVICES[service]
    
    items = "".join([f'<div class="item"><h3>{SERVICES[service]["items"][i]}</h3></div>' for i in range(6)])
    filename = service.lower().replace(" ", "-")
    
    return f'''<!DOCTYPE html><html lang="en"><head><meta charset="UTF-8"><title>{svc_config['title']} {loc_title} | Matrics Mania</title><meta name="viewport" content="width=device-width, initial-scale=1.0"><meta name="description" content="{svc_config['keyword']} {loc_title}"><link rel="stylesheet" href="styles.css"><script defer src="script.js"></script></head><body><nav><div class="logo"><img src="images/matrics_logo.png" alt="Logo"></div><ul id="nav"><li><a href="index.html">Home</a></li><li><a href="services.html">Services</a></li><li><a href="contact.html">Contact</a></li></ul></nav><h1>{svc_config['title']} {loc_title}</h1><p>Expert {svc_config['keyword']} {loc_title} services.</p><div class="services">{items}</div><footer></footer></body></html>'''

# Generate all files
existing_seo = ["agra", "aligarh", "ayodhya", "azamgarh", "bareilly", "bhadohi", "firozabad", "ghaziabad", "gorakhpur", "greater-noida"]
count = 0

# SEO for remaining
for loc in LOCATIONS:
    if loc not in existing_seo:
        fname = f"seo-services-{loc}.html"
        with open(fname, 'w') as f:
            f.write(generate_html("SEO", loc))
        count += 1
        print(f"Created: {fname}")

# All other services for all locations  
for service in ["PPC", "Social Media", "Content Marketing", "Web Development", "Brand Development"]:
    for loc in LOCATIONS:
        fname = f"{service.lower().replace(' ', '-')}-services-{loc}.html"
        with open(fname, 'w') as f:
            f.write(generate_html(service, loc))
        count += 1
        print(f"Created: {fname}")

print(f"\n✅ Total files created: {count}")
