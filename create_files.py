import os
from pathlib import Path

# Define all locations
LOCATIONS = [
    "agra", "aligarh", "ayodhya", "azamgarh", "bareilly", "bhadohi",
    "firozabad", "ghaziabad", "gorakhpur", "greater-noida", "hapur",
    "jaunpur", "jhansi", "kanpur", "lucknow", "mathura", "meerut",
    "mirzapur", "moradabad", "muzaffarnagar", "noida", "prayagraj",
    "rampur", "saharanpur", "shahjahanpur", "vrindavan"
]

EXISTING_SEO = ["agra", "aligarh", "ayodhya", "azamgarh", "bareilly", "bhadohi", "firozabad"]

SERVICES = {
    "SEO": {
        "title_suffix": "SEO Services In",
        "keyword_phrase": "SEO services in",
        "service_name": "SEO",
        "items": [
            ("Keyword Research", "In-depth analysis to find high-intent keywords your target audience is searching for."),
            ("On-Page Optimization", "Optimize your website content, meta tags, and structure for search engines."),
            ("Technical SEO", "Fix technical issues that prevent search engines from crawling and indexing your site."),
            ("Link Building", "Build high-quality backlinks from authoritative websites to boost domain authority."),
            ("Content Strategy", "Create SEO-optimized content that ranks and engages your audience."),
            ("Local SEO", "Dominate local search results in {location} with Google My Business optimization.")
        ],
        "cta_text": "Get Free SEO Audit",
        "cta_final": "Start Your SEO Journey"
    },
}

base_path = Path(".")
for location in LOCATIONS:
    if location not in EXISTING_SEO:
        filename = f"seo-services-{location}.html"
        filepath = base_path / filename
        if not filepath.exists():
            print(f"Would create: {filename}")

print("Total files to create systematically")
