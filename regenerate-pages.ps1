$cities = @(
    "Agra", "Aligarh", "Ayodhya", "Azamgarh", "Bareilly", "Bhadohi",
    "Firozabad", "Ghaziabad", "Gorakhpur", "Greater Noida", "Hapur",
    "Jaunpur", "Jhansi", "Kanpur", "Lucknow", "Mathura", "Meerut",
    "Mirzapur", "Moradabad", "Muzaffarnagar", "Noida", "Prayagraj",
    "Rampur", "Saharanpur", "Shahjahanpur", "Vrindavan"
)

$services = @(
    @{"name"="SEO"; "type"="seo"; "full"="SEO Optimization"; "url"="seo-optimization.html"},
    @{"name"="PPC"; "type"="ppc"; "full"="PPC Advertising"; "url"="ppc-advertising.html"},
    @{"name"="Social Media"; "type"="social-media"; "full"="Social Media Marketing"; "url"="social-media-marketing.html"}
)

$baseDir = "c:\Users\OM\Documents\Matrics Mania"
Set-Location $baseDir

function Generate-ServicePage {
    param(
        [string]$serviceName,
        [string]$serviceType,
        [string]$serviceFull,
        [string]$serviceUrl,
        [string]$city
    )
    
    $cityLower = $city.ToLower().Replace(" ", "-")
    $filename = "$serviceType-services-$cityLower.html"
    
    $html = @"
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>$serviceName Services In $city | Matrics Mania</title>
    <meta name="description" content="Expert $($serviceName.ToLower()) services in $city. Matrics Mania offers proven $($serviceName.ToLower()) strategies for businesses in $city.">
    <meta name="keywords" content="$($serviceName.ToLower()) services $city, $($serviceName.ToLower()) company $city">
    <meta name="author" content="Matric Mania">
    <meta name="robots" content="index, follow">
    <meta property="og:title" content="$serviceName Services In $city | Matrics Mania">
    <meta property="og:type" content="website">
    <link rel="canonical" href="https://matricsmania.com/$filename">
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
                <h1>$serviceName Services In $city - <span>Matrics Mania</span></h1>
                <p>Professional $($serviceName.ToLower()) services to boost your business visibility in $city.</p>
                <div class="hero-buttons">
                    <a href="contact.html" class="cta-button">Get Free $serviceName Audit</a>
                    <a href="services.html" class="cta-button outline">Explore Services</a>
                </div>
            </div>
        </div>
    </section>
    
    <section class="section">
        <h2 class="section-title">Our $serviceName Services In $city</h2>
        <div class="services-grid">
            <div class="service-item">
                <div class="service-number">01</div>
                <h3>Strategy Development</h3>
                <p>Customized $($serviceName.ToLower()) strategies tailored for $city market.</p>
            </div>
            <div class="service-item">
                <div class="service-number">02</div>
                <h3>Campaign Management</h3>
                <p>Expert management and optimization of your $($serviceName.ToLower()) campaigns.</p>
            </div>
            <div class="service-item">
                <div class="service-number">03</div>
                <h3>Analytics & Reporting</h3>
                <p>Detailed reporting and insights on campaign performance.</p>
            </div>
            <div class="service-item">
                <div class="service-number">04</div>
                <h3>Lead Generation</h3>
                <p>Proven techniques to generate quality leads for your business.</p>
            </div>
            <div class="service-item">
                <div class="service-number">05</div>
                <h3>ROI Optimization</h3>
                <p>Continuous optimization to maximize your return on investment.</p>
            </div>
            <div class="service-item">
                <div class="service-number">06</div>
                <h3>Conversion Tracking</h3>
                <p>Implementation and tracking of conversions and business results.</p>
            </div>
        </div>
    </section>
    
    <section class="section" style="text-align: center;">
        <h2 class="section-title">Ready to Grow Your Business?</h2>
        <p class="section-subtitle">Let Matrics Mania handle your $($serviceName.ToLower()) strategy in $city. Start with a free consultation.</p>
        <a href="contact.html" class="cta-button">Get Free Consultation</a>
    </section>
    
    <footer>
        <div class="footer-wrapper">
            <div class="footer-col">
                <h3>Matric Mania</h3>
                <p>Your trusted partner in digital marketing success. We deliver strategies that drive growth and transform businesses in $city.</p>
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
                <a href="$serviceUrl">$serviceFull</a>
                <a href="seo-optimization.html">SEO Optimization</a>
                <a href="social-media-marketing.html">Social Media Marketing</a>
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
            <p>&copy; 2026 Matric Mania Digital Marketing Agency in $city. All rights reserved.</p>
        </div>
    </footer>
</body>
</html>
"@
    
    $html | Out-File -FilePath $filename -Encoding UTF8 -Force
    return $filename
}

$count = 0
foreach ($service in $services) {
    foreach ($city in $cities) {
        $file = Generate-ServicePage -serviceName $service.name -serviceType $service.type -serviceFull $service.full -serviceUrl $service.url -city $city
        $count++
        Write-Host "✓ Generated: $file"
    }
}

Write-Host "`n✓ All $count service pages regenerated with proper canonical URLs and metadata!"
