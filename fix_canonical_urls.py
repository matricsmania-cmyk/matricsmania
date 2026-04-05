#!/usr/bin/env python3
"""
Regenerate incomplete service pages with proper structure and canonical URLs
"""

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

SERVICES = {
    "social-media": {
        "name": "Social Media Marketing",
        "title": "Social Media Marketing Services In",
        "keyword": "social media marketing services in",
        "description": "Expert {service_name} services in {location} to grow your brand. Matrics Mania offers proven strategies for Instagram, Facebook, LinkedIn, and more.",
        "why_choose": "At Matrics Mania, we deliver {service_name} services in {location} that build brands and engage audiences. Our expert team creates compelling content and manages communities across all platforms. We combine organic strategies with paid advertising to maximize your social media ROI."
    },
    "seo-services": {
        "name": "SEO",
        "title": "SEO Services In",
        "keyword": "SEO services in",
        "description": "Expert SEO services in {location} to boost your search rankings and online visibility. Matrics Mania offers proven SEO strategies for businesses in {location}.",
        "why_choose": "At Matrics Mania, we deliver SEO services in {location} that drive organic traffic and improve search rankings. Our team uses proven strategies including keyword research, on-page optimization, technical SEO, and link building to boost your online visibility and attract qualified customers."
    },
    "ppc-services": {
        "name": "PPC Advertising",
        "title": "PPC Advertising Services In",
        "keyword": "PPC advertising services in",
        "description": "Expert PPC advertising services in {location}. Manage Google Ads, Facebook Ads, and LinkedIn Ads with precision targeting to maximize ROI.",
        "why_choose": "At Matrics Mania, we deliver PPC advertising services in {location} that generate immediate visibility and qualified leads. Our experts manage Google Ads, Facebook Ads, LinkedIn Ads, and Instagram Ads with precision targeting and continuous optimization for maximum ROI."
    }
}

HERO_TEMPLATE = """    <section class="hero">
        <div class="hero-container">
            <div class="hero-content">
                <h1>{title_with_service} in {location}</h1>
                <p>Get expert {service_lower} strategies tailored to boost your business growth in {location}. Expert consultation and proven results.</p>
                <div class="hero-buttons">
                    <a href="contact.html" class="cta-button">Get Free Consultation</a>
                    <a href="services.html" class="cta-button outline">View All Services</a>
                </div>
            </div>
        </div>
    </section>"""

def generate_service_page(service_prefix, location, service_info):
    """Generate a complete service page for a location"""
    
    service_name = service_info["name"]
    title_prefix = service_info["title"]
    keyword_base = service_info["keyword"]
    
    filename = f"{service_prefix}-{location}.html"
    filepath = Path("c:\\Users\\OM\\Documents\\Matrics Mania") / filename
    
    # Format description and why_choose
    description = service_info["description"].format(
        service_name=service_name,
        location=location.replace("-", " ").title()
    )
    why_choose = service_info["why_choose"].format(
        location=location.replace("-", " ").title(),
        service_lower=service_name.lower()
    )
    
    location_display = location.replace("-", " ").title()
    
    # Determine the correct links based on service
    if service_prefix == "social-media":
        other_service_1 = "seo-services"
        other_service_1_text = "SEO Services"
        other_service_2 = "ppc-services"
        other_service_2_text = "PPC Services"
    elif service_prefix == "seo-services":
        other_service_1 = "ppc-services"
        other_service_1_text = "PPC Services"
        other_service_2 = "social-media-services"
        other_service_2_text = "Social Media"
    else:  # ppc-services
        other_service_1 = "seo-services"
        other_service_1_text = "SEO Services"
        other_service_2 = "social-media-services"
        other_service_2_text = "Social Media"
    
    html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title_prefix} {location_display} | Matrics Mania</title>
    <meta name="description" content="{description}">
    <meta name="keywords" content="{keyword_base} {location_display}, {keyword_base} {location_display} company, {keyword_base} {location_display} agency">
    <meta name="author" content="Matric Mania">
    <meta name="robots" content="index, follow">
    
    <meta property="og:title" content="{title_prefix} {location_display} | Matrics Mania">
    <meta property="og:description" content="{description}">
    <meta property="og:type" content="website">
    <meta property="og:locale" content="en_IN">
    
    <link rel="canonical" href="https://matricsmania.com/{filename}">
    
    <script type="application/ld+json">
    {{
      "@context": "https://schema.org",
      "@type": "LocalBusiness",
      "name": "Matric Mania",
      "description": "{service_name} services in {location_display}",
      "address": {{
        "@type": "PostalAddress",
        "addressLocality": "{location_display}",
        "addressRegion": "UP",
        "addressCountry": "IN"
      }},
      "areaServed": "{location_display}",
      "knowsAbout": ["{service_name}"]
    }}
    </script>
    
    <link rel="stylesheet" href="styles.css">
    <script defer src="script.js"></script>
</head>
<body>
    <!-- Navigation -->
    <nav>
        <div class="nav-container">
            <div class="logo"><img src="images/matrics_logo.png" alt="Matric Mania Logo"></div>
            <ul class="nav-links" id="navLinks">
                <li><a href="index.html">Home</a></li>
                <li><a href="about.html">About</a></li>
                <li class="nav-item"><a href="services.html">Services <span class="dropdown-arrow">▼</span></a></li>
                <li><a href="blog.html">Blog</a></li>
                <li><a href="contact.html">Contact</a></li>
            </ul>
            <div class="hamburger" id="hamburger"><span></span><span></span><span></span></div>
        </div>
    </nav>

    <section class="hero">
        <div class="hero-container">
            <div class="hero-content">
                <h1>{title_prefix} <span>{service_name}</span> in {location_display}</h1>
                <p>Expert {service_name.lower()} strategies tailored to boost your business growth in {location_display}. Get proven results with our experienced team.</p>
                <div class="hero-buttons">
                    <a href="contact.html" class="cta-button">Get Free Consultation</a>
                    <a href="services.html" class="cta-button outline">View All Services</a>
                </div>
            </div>
        </div>
    </section>

    <section class="section">
        <h2 class="section-title">{service_name} in {location_display}</h2>
        <p style="text-align: center; max-width: 900px; margin: 0 auto 3rem; color: #666; font-size: 1rem; line-height: 1.8;">
            {why_choose}
        </p>
        
        <div class="services-grid">
            <div class="service-item">
                <div class="service-number">01</div>
                <h3>Strategy Development</h3>
                <p>Custom strategies designed specifically for {location_display} businesses to achieve your marketing goals.</p>
            </div>
            <div class="service-item">
                <div class="service-number">02</div>
                <h3>Expert Execution</h3>
                <p>Our experienced team implements proven tactics that deliver measurable results and ROI for your campaigns.</p>
            </div>
            <div class="service-item">
                <div class="service-number">03</div>
                <h3>Continuous Optimization</h3>
                <p>We monitor performance metrics and continuously refine strategies to improve results and reduce costs.</p>
            </div>
            <div class="service-item">
                <div class="service-number">04</div>
                <h3>Transparent Reporting</h3>
                <p>Detailed monthly reports keep you informed on campaign performance, insights, and ROI.</p>
            </div>
            <div class="service-item">
                <div class="service-number">05</div>
                <h3>Local Expertise</h3>
                <p>Deep understanding of {location_display}'s market dynamics and local audience preferences.</p>
            </div>
            <div class="service-item">
                <div class="service-number">06</div>
                <h3>24/7 Support</h3>
                <p>Our support team is always available to answer questions and address your campaign needs.</p>
            </div>
        </div>
    </section>

    <!-- Services and Locations Section -->
    <section class="section services-locations-section">
        <div class="services-locations-container">
            <h2 class="section-title">{title_prefix} All Locations</h2>
            
            <div class="location-category-card">
                <div class="category-header">
                    <h3><span class="category-icon">🎯</span>Uttar Pradesh Cities</h3>
                    <span class="category-count">26 Cities</span>
                </div>
                <div class="locations-list">
                    <div class="location-item"><span class="location-bullet">◆</span><a href="{service_prefix}-agra.html">Agra</a></div>
                    <div class="location-item"><span class="location-bullet">◆</span><a href="{service_prefix}-aligarh.html">Aligarh</a></div>
                    <div class="location-item"><span class="location-bullet">◆</span><a href="{service_prefix}-ayodhya.html">Ayodhya</a></div>
                    <div class="location-item"><span class="location-bullet">◆</span><a href="{service_prefix}-azamgarh.html">Azamgarh</a></div>
                    <div class="location-item"><span class="location-bullet">◆</span><a href="{service_prefix}-bareilly.html">Bareilly</a></div>
                    <div class="location-item"><span class="location-bullet">◆</span><a href="{service_prefix}-bhadohi.html">Bhadohi</a></div>
                    <div class="location-item"><span class="location-bullet">◆</span><a href="{service_prefix}-firozabad.html">Firozabad</a></div>
                    <div class="location-item"><span class="location-bullet">◆</span><a href="{service_prefix}-ghaziabad.html">Ghaziabad</a></div>
                    <div class="location-item"><span class="location-bullet">◆</span><a href="{service_prefix}-gorakhpur.html">Gorakhpur</a></div>
                    <div class="location-item"><span class="location-bullet">◆</span><a href="{service_prefix}-greater-noida.html">Greater Noida</a></div>
                    <div class="location-item"><span class="location-bullet">◆</span><a href="{service_prefix}-hapur.html">Hapur</a></div>
                    <div class="location-item"><span class="location-bullet">◆</span><a href="{service_prefix}-jaunpur.html">Jaunpur</a></div>
                    <div class="location-item"><span class="location-bullet">◆</span><a href="{service_prefix}-jhansi.html">Jhansi</a></div>
                    <div class="location-item"><span class="location-bullet">◆</span><a href="{service_prefix}-kanpur.html">Kanpur</a></div>
                    <div class="location-item"><span class="location-bullet">◆</span><a href="{service_prefix}-lucknow.html">Lucknow</a></div>
                    <div class="location-item"><span class="location-bullet">◆</span><a href="{service_prefix}-mathura.html">Mathura</a></div>
                    <div class="location-item"><span class="location-bullet">◆</span><a href="{service_prefix}-meerut.html">Meerut</a></div>
                    <div class="location-item"><span class="location-bullet">◆</span><a href="{service_prefix}-mirzapur.html">Mirzapur</a></div>
                    <div class="location-item"><span class="location-bullet">◆</span><a href="{service_prefix}-moradabad.html">Moradabad</a></div>
                    <div class="location-item"><span class="location-bullet">◆</span><a href="{service_prefix}-muzaffarnagar.html">Muzaffarnagar</a></div>
                    <div class="location-item"><span class="location-bullet">◆</span><a href="{service_prefix}-noida.html">Noida</a></div>
                    <div class="location-item"><span class="location-bullet">◆</span><a href="{service_prefix}-prayagraj.html">Prayagraj</a></div>
                    <div class="location-item"><span class="location-bullet">◆</span><a href="{service_prefix}-rampur.html">Rampur</a></div>
                    <div class="location-item"><span class="location-bullet">◆</span><a href="{service_prefix}-saharanpur.html">Saharanpur</a></div>
                    <div class="location-item"><span class="location-bullet">◆</span><a href="{service_prefix}-shahjahanpur.html">Shahjahanpur</a></div>
                    <div class="location-item"><span class="location-bullet">◆</span><a href="{service_prefix}-vrindavan.html">Vrindavan</a></div>
                </div>
            </div>
            
            <div class="services-list">
                <div class="services-list-title">Explore Our Other Services</div>
                <div class="services-grid">
                    <div class="service-link-item">
                        <a href="seo-optimization.html">SEO Optimization</a>
                    </div>
                    <div class="service-link-item">
                        <a href="social-media-marketing.html">Social Media Marketing</a>
                    </div>
                    <div class="service-link-item">
                        <a href="ppc-advertising.html">PPC Advertising</a>
                    </div>
                    <div class="service-link-item">
                        <a href="content-marketing.html">Content Marketing</a>
                    </div>
                    <div class="service-link-item">
                        <a href="brand-development.html">Brand Development</a>
                    </div>
                    <div class="service-link-item">
                        <a href="analytics-reporting.html">Analytics & Reporting</a>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- Footer -->
    <footer>
        <div class="footer-wrapper">
            <div class="footer-col">
                <h3>Matric Mania</h3>
                <p>Your trusted partner in digital marketing success. We deliver strategies that drive growth and transform businesses in {location_display}.</p>
            </div>
            <div class="footer-col">
                <h3>Quick Links</h3>
                <a href="index.html">Home</a>
                <a href="services.html">Services</a>
                <a href="about.html">About Us</a>
                <a href="contact.html">Contact</a>
            </div>
            <div class="footer-col">
                <h3>Services</h3>
                <a href="{other_service_1}-{location}.html">{other_service_1_text}</a>
                <a href="{service_prefix}-{location}.html">{service_name}</a>
                <a href="{other_service_2}-{location}.html">{other_service_2_text}</a>
            </div>
            <div class="footer-col">
                <h3>Connect</h3>
                <a href="#">Facebook</a>
                <a href="#">Twitter</a>
                <a href="#">LinkedIn</a>
                <a href="#">Instagram</a>
            </div>
        </div>
        <div class="footer-bottom">
            <p>&copy; 2026 Matric Mania Digital Marketing Agency in {location_display}. All rights reserved.</p>
        </div>
    </footer>
</body>
</html>"""
    
    return html_content


def main():
    base_path = Path("c:\\Users\\OM\\Documents\\Matrics Mania")
    
    total_generated = 0
    for service_prefix, service_info in SERVICES.items():
        for location in LOCATIONS:
            filename = f"{service_prefix}-{location}.html"
            filepath = base_path / filename
            
            # Only regenerate if file exists and is likely incomplete
            if filepath.exists():
                with open(filepath, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                # Check if it's incomplete (missing canonical or very short)
                if 'rel="canonical"' not in content or len(content) < 2000:
                    print(f"Regenerating: {filename}")
                    html_content = generate_service_page(service_prefix, location, service_info)
                    with open(filepath, 'w', encoding='utf-8') as f:
                        f.write(html_content)
                    total_generated += 1
                else:
                    print(f"Skipping (complete): {filename}")
            else:
                print(f"File not found: {filename}")
    
    print(f"\n✓ Regenerated {total_generated} incomplete files")


if __name__ == "__main__":
    main()
