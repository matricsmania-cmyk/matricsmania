#!/usr/bin/env python3
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

# SEO services that already exist
EXISTING_SEO = ["agra", "aligarh", "ayodhya", "azamgarh", "bareilly", "bhadohi", "firozabad"]

# Define services with their specific content
SERVICES = {
    "SEO": {
        "title_suffix": "SEO Services In",
        "keyword_phrase": "SEO services in",
        "service_name": "SEO",
        "items": [
            {"num": "01", "title": "Keyword Research", "desc": "In-depth analysis to find high-intent keywords your target audience is searching for."},
            {"num": "02", "title": "On-Page Optimization", "desc": "Optimize your website content, meta tags, and structure for search engines."},
            {"num": "03", "title": "Technical SEO", "desc": "Fix technical issues that prevent search engines from crawling and indexing your site."},
            {"num": "04", "title": "Link Building", "desc": "Build high-quality backlinks from authoritative websites to boost domain authority."},
            {"num": "05", "title": "Content Strategy", "desc": "Create SEO-optimized content that ranks and engages your audience."},
            {"num": "06", "title": "Local SEO", "desc": "Dominate local search results in {location} with Google My Business optimization."}
        ],
        "why_choose": "At Matrics Mania, we deliver SEO services in {location} that drive real results. Our team of certified SEO experts understands the local market and uses proven strategies to increase your online visibility. From keyword research to link building, we handle every aspect of SEO to get your website ranking on the first page of Google.",
        "cta_text": "Get Free SEO Audit",
        "cta_final": "Start Your SEO Journey"
    },
    "PPC": {
        "title_suffix": "PPC Advertising Services In",
        "keyword_phrase": "PPC advertising services in",
        "service_name": "PPC",
        "items": [
            {"num": "01", "title": "Keyword Bidding Strategy", "desc": "Strategic keyword selection and intelligent bid management to maximize your ad visibility."},
            {"num": "02", "title": "Ad Copywriting & Design", "desc": "Compelling ad copy and visuals that attract clicks and drive conversions."},
            {"num": "03", "title": "Landing Page Optimization", "desc": "High-converting landing pages designed to turn clicks into customers."},
            {"num": "04", "title": "Conversion Tracking & ROI", "desc": "Detailed tracking and reporting to measure every click's impact on your business."},
            {"num": "05", "title": "Budget Management & Optimization", "desc": "Smart budget allocation ensuring maximum ROI on every advertising dollar spent."},
            {"num": "06", "title": "Remarketing Campaigns", "desc": "Re-engage interested visitors in {location} with targeted remarketing advertisements."}
        ],
        "why_choose": "At Matrics Mania, we deliver PPC advertising services in {location} that drive immediate results. Our certified Google Ads specialists create campaigns that attract qualified leads and boost your revenue. From keyword research to bid optimization, we ensure every advertising dollar works hard for your business.",
        "cta_text": "Get Free PPC Audit",
        "cta_final": "Launch Your PPC Campaign"
    },
    "Social Media": {
        "title_suffix": "Social Media Marketing Services In",
        "keyword_phrase": "social media marketing services in",
        "service_name": "Social Media Marketing",
        "items": [
            {"num": "01", "title": "Content Creation & Planning", "desc": "Strategic content calendars and engaging posts that resonate with your audience."},
            {"num": "02", "title": "Community Management", "desc": "Active engagement and relationship building with your followers on all platforms."},
            {"num": "03", "title": "Influencer Outreach", "desc": "Connect with relevant influencers in {location} to amplify your brand message."},
            {"num": "04", "title": "Paid Social Ads", "desc": "Targeted social media advertising that reaches the right audience at the right time."},
            {"num": "05", "title": "Analytics & Reporting", "desc": "In-depth performance metrics and actionable insights to improve your social presence."},
            {"num": "06", "title": "Social Media Strategy", "desc": "Comprehensive strategies tailored to your business goals and target market in {location}."}
        ],
        "why_choose": "At Matrics Mania, we deliver social media marketing services in {location} that build brands and engage audiences. Our expert team creates compelling content and manages communities across all platforms. We combine organic strategies with paid advertising to maximize your social media ROI.",
        "cta_text": "Get Free Social Media Audit",
        "cta_final": "Boost Your Social Presence"
    },
    "Content Marketing": {
        "title_suffix": "Content Marketing Services In",
        "keyword_phrase": "content marketing services in",
        "service_name": "Content Marketing",
        "items": [
            {"num": "01", "title": "Blog Writing & SEO", "desc": "SEO-optimized blog posts that attract organic traffic and establish authority."},
            {"num": "02", "title": "Video Content Creation", "desc": "Engaging video content that tells your story and drives viewer engagement."},
            {"num": "03", "title": "Infographic Design", "desc": "Visual infographics that simplify complex information and boost shareability."},
            {"num": "04", "title": "Whitepapers & E-books", "desc": "In-depth resources that generate leads and position your business as an industry leader."},
            {"num": "05", "title": "Case Studies", "desc": "Compelling case studies showcasing your results and building trust with prospects."},
            {"num": "06", "title": "Newsletter Marketing", "desc": "Regular newsletters that keep your {location} audience engaged and informed."}
        ],
        "why_choose": "At Matrics Mania, we deliver content marketing services in {location} that attract, engage, and convert. Our expert writers and designers create valuable content across all formats. We build content strategies that establish your authority and drive sustainable business growth.",
        "cta_text": "Get Free Content Strategy",
        "cta_final": "Start Your Content Journey"
    },
    "Web Development": {
        "title_suffix": "Web Development Services In",
        "keyword_phrase": "web development services in",
        "service_name": "Web Development",
        "items": [
            {"num": "01", "title": "Responsive Design", "desc": "Websites that look perfect on every device - desktop, tablet, and mobile."},
            {"num": "02", "title": "UX/UI Design", "desc": "User-centered design that improves navigation and maximizes conversions."},
            {"num": "03", "title": "Site Speed Optimization", "desc": "Lightning-fast websites that provide excellent user experience and better SEO rankings."},
            {"num": "04", "title": "Security Implementation", "desc": "Secure websites with SSL certificates and protection against cyber threats."},
            {"num": "05", "title": "CMS Setup", "desc": "Easy-to-manage content management systems like WordPress, Shopify, and more."},
            {"num": "06", "title": "Mobile Optimization", "desc": "Fully optimized mobile experiences for the growing {location} mobile-first audience."}
        ],
        "why_choose": "At Matrics Mania, we deliver web development services in {location} that drive business results. Our expert developers build modern, fast, and secure websites optimized for conversion. From design to launch, we ensure your web presence represents your brand effectively.",
        "cta_text": "Get Free Website Audit",
        "cta_final": "Build Your Perfect Website"
    },
    "Brand Development": {
        "title_suffix": "Brand Development Services In",
        "keyword_phrase": "brand development services in",
        "service_name": "Brand Development",
        "items": [
            {"num": "01", "title": "Logo Design", "desc": "Unique, memorable logos that represent your brand identity and values."},
            {"num": "02", "title": "Brand Identity Development", "desc": "Comprehensive brand systems including colors, fonts, and visual guidelines."},
            {"num": "03", "title": "Brand Messaging Strategy", "desc": "Clear, compelling messaging that communicates your unique value to {location} customers."},
            {"num": "04", "title": "Visual Design Standards", "desc": "Consistent visual identity across all marketing channels and touchpoints."},
            {"num": "05", "title": "Brand Guidelines Document", "desc": "Detailed brand guidelines ensuring consistency in every brand application."},
            {"num": "06", "title": "Brand Positioning Strategy", "desc": "Strategic positioning that differentiates your brand in a competitive {location} market."}
        ],
        "why_choose": "At Matrics Mania, we deliver brand development services in {location} that create lasting impressions. Our creative team builds strong, recognizable brands that connect emotionally with your audience. We ensure your brand stands out and represents your business effectively.",
        "cta_text": "Get Free Brand Consultation",
        "cta_final": "Develop Your Brand Legacy"
    }
}

def generate_html(service, location):
    """Generate HTML content for a service page"""
    service_config = SERVICES[service]
    location_title = location.replace("-", " ").title()
    
    # Generate service items HTML
    services_html = ""
    for item in service_config["items"]:
        desc = item["desc"].format(location=location_title)
        services_html += f"""            <div class="service-item">
                <div class="service-number">{item["num"]}</div>
                <h3>{item["title"]}</h3>
                <p>{desc}</p>
            </div>
"""
    
    why_choose_desc = service_config["why_choose"].format(location=location_title)
    
    # Generate the full HTML
    html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{service_config["title_suffix"]} {location_title} | Matrics Mania</title>
    <meta name="description" content="Expert {service_config['keyword_phrase']} {location_title} to boost your online presence. Matrics Mania offers proven strategies for businesses in {location_title}.">
    <meta name="keywords" content="{service_config['keyword_phrase']} {location_title}, {service} company {location_title}, {service} agency {location_title}">
    <meta name="author" content="Matric Mania">
    <meta name="robots" content="index, follow">
    
    <meta property="og:title" content="{service_config['title_suffix']} {location_title} | Matrics Mania">
    <meta property="og:description" content="Expert {service_config['keyword_phrase']} {location_title} to boost your online presence.">
    <meta property="og:type" content="website">
    <meta property="og:locale" content="en_IN">
    
    <link rel="canonical" href="https://matricsmania.com/{service.lower().replace(' ', '-')}-services-{location}.html">
    
    <script type="application/ld+json">
    {{
      "@context": "https://schema.org",
      "@type": "LocalBusiness",
      "name": "Matric Mania",
      "description": "{service} services in {location_title}",
      "address": {{
        "@type": "PostalAddress",
        "addressLocality": "{location_title}",
        "addressRegion": "UP",
        "addressCountry": "IN"
      }},
      "areaServed": "{location_title}",
      "knowsAbout": ["{service}", "{service_config['service_name']}"]
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
                <li class="nav-item">
                    <a href="services.html">Services <span class="dropdown-arrow">▼</span></a>
                </li>
                <li><a href="blog.html">Blog</a></li>
                <li><a href="contact.html">Contact</a></li>
            </ul>
            <div class="hamburger" id="hamburger">
                <span></span>
                <span></span>
                <span></span>
            </div>
        </div>
    </nav>

    <!-- Hero Section -->
    <section class="hero">
        <div class="hero-container">
            <div class="hero-content">
                <h1>{service_config['title_suffix']} {location_title} - <span>Matrics Mania</span></h1>
                <p>Boost your online presence with expert <span class="keyword">{service_config['keyword_phrase']} {location_title}</span>. Our data-driven strategies help {location_title} businesses succeed online.</p>
                <div class="hero-buttons">
                    <a href="contact.html" class="cta-button">{service_config['cta_text']}</a>
                    <a href="services.html" class="cta-button outline">Explore Services</a>
                </div>
            </div>
            <div class="hero-image">
                <img src="images/hero-section.jpg" alt="{service_config['title_suffix']} {location_title} - Matrics Mania">
            </div>
        </div>
    </section>

    <!-- Why Choose Us Section -->
    <section class="section why-choose-us-section">
        <h2 class="section-title">Why Choose Our {service} Services</h2>
        <div class="why-choose-content">
            <h3>Professional {service} Solutions for {location_title} Businesses</h3>
            <p>{why_choose_desc}</p>
        </div>
    </section>

    <!-- Services Section -->
    <section class="section services-section">
        <h2 class="section-title">Our {service} Services</h2>
        <div class="services-grid">
{services_html}        </div>
    </section>

    <!-- Results Section -->
    <section class="section">
        <h2 class="section-title">Results We Deliver</h2>
        <div class="stats">
            <div class="stat">
                <div class="stat-number">500+</div>
                <div class="stat-label">Satisfied Clients</div>
            </div>
            <div class="stat">
                <div class="stat-number">350%</div>
                <div class="stat-label">Average ROI Growth</div>
            </div>
            <div class="stat">
                <div class="stat-number">$50M+</div>
                <div class="stat-label">Client Revenue Generated</div>
            </div>
        </div>
    </section>

    <!-- CTA Section -->
    <section class="section" style="text-align: center;">
        <h2 class="section-title">Ready to Get Started?</h2>
        <p class="section-subtitle">Let's create a {service_config['keyword_phrase']} {location_title} strategy that drives real results.</p>
        <a href="contact.html" class="cta-button">{service_config['cta_final']}</a>
    </section>

    <!-- Footer -->
    <footer>
        <div class="footer-wrapper">
            <div class="footer-col">
                <h3>Matric Mania</h3>
                <p>Your trusted digital marketing partner in {location_title}.</p>
            </div>
            <div class="footer-col">
                <h3>Quick Links</h3>
                <a href="index.html">Home</a>
                <a href="services.html">Services</a>
                <a href="contact.html">Contact</a>
            </div>
            <div class="footer-col">
                <h3>Services</h3>
                <a href="seo-services-{location}.html">SEO Services</a>
                <a href="ppc-services-{location}.html">PPC Services</a>
                <a href="social-media-services-{location}.html">Social Media</a>
            </div>
        </div>
    </footer>
</body>
</html>"""
    return html_content

def main():
    base_path = Path(".")
    created_files = []
    
    # Create SEO files for remaining locations
    print("Creating SEO service pages...")
    for location in LOCATIONS:
        if location not in EXISTING_SEO:
            filename = f"seo-services-{location}.html"
            filepath = base_path / filename
            html = generate_html("SEO", location)
            filepath.write_text(html)
            created_files.append(filename)
            print(f"  Created: {filename}")
    
    # Create PPC files for all locations
    print("\nCreating PPC service pages...")
    for location in LOCATIONS:
        filename = f"ppc-services-{location}.html"
        filepath = base_path / filename
        html = generate_html("PPC", location)
        filepath.write_text(html)
        created_files.append(filename)
        print(f"  Created: {filename}")
    
    # Create Social Media files for all locations
    print("\nCreating Social Media service pages...")
    for location in LOCATIONS:
        filename = f"social-media-services-{location}.html"
        filepath = base_path / filename
        html = generate_html("Social Media", location)
        filepath.write_text(html)
        created_files.append(filename)
        print(f"  Created: {filename}")
    
    # Create Content Marketing files for all locations
    print("\nCreating Content Marketing service pages...")
    for location in LOCATIONS:
        filename = f"content-marketing-services-{location}.html"
        filepath = base_path / filename
        html = generate_html("Content Marketing", location)
        filepath.write_text(html)
        created_files.append(filename)
        print(f"  Created: {filename}")
    
    # Create Web Development files for all locations
    print("\nCreating Web Development service pages...")
    for location in LOCATIONS:
        filename = f"web-development-services-{location}.html"
        filepath = base_path / filename
        html = generate_html("Web Development", location)
        filepath.write_text(html)
        created_files.append(filename)
        print(f"  Created: {filename}")
    
    # Create Brand Development files for all locations
    print("\nCreating Brand Development service pages...")
    for location in LOCATIONS:
        filename = f"brand-development-services-{location}.html"
        filepath = base_path / filename
        html = generate_html("Brand Development", location)
        filepath.write_text(html)
        created_files.append(filename)
        print(f"  Created: {filename}")
    
    print(f"\n✅ Successfully created {len(created_files)} files!")
    return created_files

if __name__ == "__main__":
    files = main()
    print("\n" + "="*60)
    print("FILES CREATED:")
    print("="*60)
    for f in sorted(files):
        print(f)
