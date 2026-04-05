#!/usr/bin/env python3
"""Generate all service pages for Matrics Mania"""
import os

LOCATIONS = [
    "agra", "aligarh", "ayodhya", "azamgarh", "bareilly", "bhadohi",
    "firozabad", "ghaziabad", "gorakhpur", "greater-noida", "hapur",
    "jaunpur", "jhansi", "kanpur", "lucknow", "mathura", "meerut",
    "mirzapur", "moradabad", "muzaffarnagar", "noida", "prayagraj",
    "rampur", "saharanpur", "shahjahanpur", "vrindavan"
]

EXISTING_SEO = ["agra", "aligarh", "ayodhya", "azamgarh", "bareilly", "bhadohi", "firozabad", "ghaziabad"]

SERVICES_DATA = {
    "SEO": {
        "items": [
            ("Keyword Research", "In-depth analysis to find high-intent keywords y target audience is searching for."),
            ("On-Page Optimization", "Optimize your website content, meta tags, and structure for search engines."),
            ("Technical SEO", "Fix technical issues that prevent search engines from crawling and indexing your site."),
            ("Link Building", "Build high-quality backlinks from authoritative websites to boost domain authority."),
            ("Content Strategy", "Create SEO-optimized content that ranks and engages your audience."),
            ("Local SEO", "Dominate local search results with Google My Business optimization.")
        ]
    },
    "PPC": {
        "items": [
            ("Keyword Bidding Strategy", "Strategic keyword selection and intelligent bid management to maximize your ad visibility."),
            ("Ad Copywriting & Design", "Compelling ad copy and visuals that attract clicks and drive conversions."),
            ("Landing Page Optimization", "High-converting landing pages designed to turn clicks into customers."),
            ("Conversion Tracking & ROI", "Detailed tracking and reporting to measure every click's impact on your business."),
            ("Budget Management & Optimization", "Smart budget allocation ensuring maximum ROI on every advertising dollar spent."),
            ("Remarketing Campaigns", "Re-engage interested visitors with targeted remarketing advertisements.")
        ]
    },
    "Social Media": {
        "items": [
            ("Content Creation & Planning", "Strategic content calendars and engaging posts that resonate with your audience."),
            ("Community Management", "Active engagement and relationship building with your followers on all platforms."),
            ("Influencer Outreach", "Connect with relevant influencers to amplify your brand message."),
            ("Paid Social Ads", "Targeted social media advertising that reaches the right audience at the right time."),
            ("Analytics & Reporting", "In-depth performance metrics and actionable insights to improve your social presence."),
            ("Social Media Strategy", "Comprehensive strategies tailored to your business goals and target market.")
        ]
    },
    "Content Marketing": {
        "items": [
            ("Blog Writing & SEO", "SEO-optimized blog posts that attract organic traffic and establish authority."),
            ("Video Content Creation", "Engaging video content that tells your story and drives viewer engagement."),
            ("Infographic Design", "Visual infographics that simplify complex information and boost shareability."),
            ("Whitepapers & E-books", "In-depth resources that generate leads and position your business as an industry leader."),
            ("Case Studies", "Compelling case studies showcasing your results and building trust with prospects."),
            ("Newsletter Marketing", "Regular newsletters that keep your audience engaged and informed.")
        ]
    },
    "Web Development": {
        "items": [
            ("Responsive Design", "Websites that look perfect on every device - desktop, tablet, and mobile."),
            ("UX/UI Design", "User-centered design that improves navigation and maximizes conversions."),
            ("Site Speed Optimization", "Lightning-fast websites that provide excellent user experience and better SEO rankings."),
            ("Security Implementation", "Secure websites with SSL certificates and protection against cyber threats."),
            ("CMS Setup", "Easy-to-manage content management systems like WordPress, Shopify, and more."),
            ("Mobile Optimization", "Fully optimized mobile experiences for the growing mobile-first audience.")
        ]
    },
    "Brand Development": {
        "items": [
            ("Logo Design", "Unique, memorable logos that represent your brand identity and values."),
            ("Brand Identity Development", "Comprehensive brand systems including colors, fonts, and visual guidelines."),
            ("Brand Messaging Strategy", "Clear, compelling messaging that communicates your unique value to customers."),
            ("Visual Design Standards", "Consistent visual identity across all marketing channels and touchpoints."),
            ("Brand Guidelines Document", "Detailed brand guidelines ensuring consistency in every brand application."),
            ("Brand Positioning Strategy", "Strategic positioning that differentiates your brand in a competitive market.")
        ]
    }
}

SERVICE_TITLES = {
    "SEO": "SEO Services In",
    "PPC": "PPC Advertising Services In",
    "Social Media": "Social Media Marketing Services In",
    "Content Marketing": "Content Marketing Services In",
    "Web Development": "Web Development Services In",
    "Brand Development": "Brand Development Services In"
}

SERVICE_KEYWORDS = {
    "SEO": "SEO services in",
    "PPC": "PPC advertising services in",
    "Social Media": "social media marketing services in",
    "Content Marketing": "content marketing services in",
    "Web Development": "web development services in",
    "Brand Development": "brand development services in"
}

CTA_TEXT = {
    "SEO": ("Get Free SEO Audit", "Start Your SEO Journey"),
    "PPC": ("Get Free PPC Audit", "Launch Your PPC Campaign"),
    "Social Media": ("Get Free Social Media Audit", "Boost Your Social Presence"),
    "Content Marketing": ("Get Free Content Strategy", "Start Your Content Journey"),
    "Web Development": ("Get Free Website Audit", "Build Your Perfect Website"),
    "Brand Development": ("Get Free Brand Consultation", "Develop Your Brand Legacy")
}

WHY_CHOOSE = {
    "SEO": "At Matrics Mania, we deliver SEO services in {loc} that drive real results. Our team of certified SEO experts understands the local market and uses proven strategies to increase your online visibility. From keyword research to link building, we handle every aspect of SEO to get your website ranking on the first page of Google.",
    "PPC": "At Matrics Mania, we deliver PPC advertising services in {loc} that drive immediate results. Our certified Google Ads specialists create campaigns that attract qualified leads and boost your revenue. From keyword research to bid optimization, we ensure every advertising dollar works hard for your business.",
    "Social Media": "At Matrics Mania, we deliver social media marketing services in {loc} that build brands and engage audiences. Our expert team creates compelling content and manages communities across all platforms. We combine organic strategies with paid advertising to maximize your social media ROI.",
    "Content Marketing": "At Matrics Mania, we deliver content marketing services in {loc} that attract, engage, and convert. Our expert writers and designers create valuable content across all formats. We build content strategies that establish your authority and drive sustainable business growth.",
    "Web Development": "At Matrics Mania, we deliver web development services in {loc} that drive business results. Our expert developers build modern, fast, and secure websites optimized for conversion. From design to launch, we ensure your web presence represents your brand effectively.",
    "Brand Development": "At Matrics Mania, we deliver brand development services in {loc} that create lasting impressions. Our creative team builds strong, recognizable brands that connect emotionally with your audience. We ensure your brand stands out and represents your business effectively."
}

def generate_html(service, location):
    location_title = location.replace("-", " ").title()
    
    items_html = ""
    for i, (title, desc) in enumerate(SERVICES_DATA[service]["items"], 1):
        items_html += f'            <div class="service-item"><div class="service-number">{i:02d}</div><h3>{title}</h3><p>{desc}</p></div>\n'
    
    why_choose_text = WHY_CHOOSE[service].format(loc=location_title)
    cta_btn1, cta_btn2 = CTA_TEXT[service]
    
    return f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{SERVICE_TITLES[service]} {location_title} | Matrics Mania</title>
    <meta name="description" content="Expert {SERVICE_KEYWORDS[service]} {location_title} to boost your online presence. Matrics Mania offers proven strategies for businesses in {location_title}.">
    <meta name="keywords" content="{SERVICE_KEYWORDS[service]} {location_title}, {service} company {location_title}, {service} agency {location_title}">
    <meta name="author" content="Matric Mania">
    <meta name="robots" content="index, follow">
    <meta property="og:title" content="{SERVICE_TITLES[service]} {location_title} | Matrics Mania">
    <meta property="og:description" content="Expert {SERVICE_KEYWORDS[service]} {location_title} to boost your online presence.">
    <meta property="og:type" content="website">
    <meta property="og:locale" content="en_IN">
    <link rel="canonical" href="https://matricsmania.com/{service.lower().replace(" ", "-")}-services-{location}.html">
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
      "knowsAbout": ["{service}"]
    }}
    </script>
    <link rel="stylesheet" href="styles.css">
    <script defer src="script.js"></script>
</head>
<body>
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
                <h1>{SERVICE_TITLES[service]} {location_title} - <span>Matrics Mania</span></h1>
                <p>Boost your online presence with expert <span class="keyword">{SERVICE_KEYWORDS[service]} {location_title}</span>. Our data-driven strategies help {location_title} businesses succeed online.</p>
                <div class="hero-buttons">
                    <a href="contact.html" class="cta-button">{cta_btn1}</a>
                    <a href="services.html" class="cta-button outline">Explore Services</a>
                </div>
            </div>
            <div class="hero-image"><img src="images/hero-section.jpg" alt="{SERVICE_TITLES[service]} {location_title} - Matrics Mania"></div>
        </div>
    </section>
    <section class="section why-choose-us-section">
        <h2 class="section-title">Why Choose Our {service} Services</h2>
        <div class="why-choose-content">
            <h3>Professional {service} Solutions for {location_title} Businesses</h3>
            <p>{why_choose_text}</p>
        </div>
    </section>
    <section class="section services-section">
        <h2 class="section-title">Our {service} Services</h2>
        <div class="services-grid">
{items_html}        </div>
    </section>
    <section class="section"><h2 class="section-title">Results We Deliver</h2><div class="stats"><div class="stat"><div class="stat-number">500+</div><div class="stat-label">Satisfied Clients</div></div><div class="stat"><div class="stat-number">350%</div><div class="stat-label">Average ROI Growth</div></div><div class="stat"><div class="stat-number">$50M+</div><div class="stat-label">Client Revenue Generated</div></div></div></section>
    <section class="section" style="text-align: center;"><h2 class="section-title">Ready to Get Started?</h2><p class="section-subtitle">Let's create a {SERVICE_KEYWORDS[service]} {location_title} strategy that drives real results.</p><a href="contact.html" class="cta-button">{cta_btn2}</a></section>
    <footer><div class="footer-wrapper"><div class="footer-col"><h3>Matric Mania</h3><p>Your trusted digital marketing partner in {location_title}.</p></div><div class="footer-col"><h3>Quick Links</h3><a href="index.html">Home</a><a href="services.html">Services</a><a href="contact.html">Contact</a></div><div class="footer-col"><h3>Services</h3><a href="seo-services-{location}.html">SEO Services</a><a href="ppc-services-{location}.html">PPC Services</a><a href="social-media-services-{location}.html">Social Media</a></div></div></footer>
</body>
</html>'''

def main():
    created = []
    
    # SEO services for remaining locations
    print("Generating SEO files...")
    for loc in LOCATIONS:
        if loc not in EXISTING_SEO:
            filename = f"seo-services-{loc}.html"
            if not os.path.exists(filename):
                html = generate_html("SEO", loc)
                with open(filename, 'w') as f:
                    f.write(html)
                created.append(filename)
                print(f"  Created: {filename}")
    
    # PPC, Social Media, Content Marketing, Web Development, Brand Development for all
    services = ["PPC", "Social Media", "Content Marketing", "Web Development", "Brand Development"]
    for service in services:
        print(f"\nGenerating {service} files...")
        for loc in LOCATIONS:
            svc_name = service.lower().replace(" ", "-")
            filename = f"{svc_name}-services-{loc}.html"
            if not os.path.exists(filename):
                html = generate_html(service, loc)
                with open(filename, 'w') as f:
                    f.write(html)
                created.append(filename)
    print(f"\nGenerating {service} files... (100%)")
    
    print(f"\n✅ Successfully created {len(created)} files!")
    return created

if __name__ == "__main__":
    files = main()
