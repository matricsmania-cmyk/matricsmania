// Modern Website Interactions - Professional Enhancements
// Smooth scroll, stat counters, mobile nav, parallax

// Smooth scrolling for anchor links
document.querySelectorAll('a[href^=\"#\"]').forEach(anchor => {
  anchor.addEventListener('click', function (e) {
    e.preventDefault();
    const target = document.querySelector(this.getAttribute('href'));
    if (target) {
      target.scrollIntoView({ behavior: 'smooth', block: 'start' });
    }
  });
});

// Stat counters with IntersectionObserver
const stats = document.querySelectorAll('.stat-number');
const animateStats = new IntersectionObserver((entries) => {
  entries.forEach(entry => {
    if (entry.isIntersecting) {
      const stat = entry.target;
      const target = parseInt(stat.dataset.target || stat.textContent);
      let current = 0;
      const increment = target / 100;
      const timer = setInterval(() => {
        current += increment;
        if (current >= target) {
          stat.textContent = target + (stat.dataset.suffix || '');
          clearInterval(timer);
        } else {
          stat.textContent = Math.floor(current) + (stat.dataset.suffix || '');
        }
      }, 20);
      animateStats.unobserve(stat);
    }
  });
}, { threshold: 0.5 });

stats.forEach(stat => {
  stat.dataset.target = stat.textContent.replace(/[^0-9]/g, '');
  animateStats.observe(stat);
});

// Mobile Hamburger Menu Toggle
const hamburger = document.getElementById('hamburger');
const navLinks = document.getElementById('navLinks');

if (hamburger && navLinks) {
  hamburger.addEventListener('click', function() {
    hamburger.classList.toggle('active');
    navLinks.classList.toggle('active');
  });

  // Close menu when a link is clicked
  const navItems = navLinks.querySelectorAll('a');
  navItems.forEach(item => {
    item.addEventListener('click', function() {
      hamburger.classList.remove('active');
      navLinks.classList.remove('active');
    });
  });

  // Close menu when clicking outside
  document.addEventListener('click', function(event) {
    const isClickInsideNav = navLinks.contains(event.target);
    const isClickOnHamburger = hamburger.contains(event.target);
    
    if (!isClickInsideNav && !isClickOnHamburger && navLinks.classList.contains('active')) {
      hamburger.classList.remove('active');
      navLinks.classList.remove('active');
    }
  });
}

// Hero parallax effect
window.addEventListener('scroll', () => {
  const scrolled = window.pageYOffset;
  const heroImage = document.querySelector('.hero-image');
  if (heroImage) {
    heroImage.style.transform = `translateY(${scrolled * 0.5}px)`;
  }
});

// Staggered animations on scroll
const observer = new IntersectionObserver((entries) => {
  entries.forEach((entry, index) => {
    if (entry.isIntersecting) {
      entry.target.style.animationDelay = `${index * 0.1}s`;
      entry.target.classList.add('animate-in');
    }
  });
}, { threshold: 0.1 });

document.querySelectorAll('.feature-card, .service-item, .process-item, .industry-card').forEach(el => {
  observer.observe(el);
});

// Client Success Stories Slider - Infinite Loop with Cloned Cards (No Blank Space)
let sliderIndex = 0;
let totalCards = 0;
let originalCardCount = 0;
let autoPlayInterval;
let isTransitioning = false;

function getItemsPerView() {
  if (window.innerWidth <= 768) return 1;
  if (window.innerWidth <= 1024) return 2;
  return 3;
}

function initSuccessStoriesSlider() {
  const sliderTrack = document.getElementById('sliderTrack');
  const sliderDotsContainer = document.getElementById('sliderDots');
  
  if (!sliderTrack) return;

  const originalCards = Array.from(sliderTrack.querySelectorAll('.success-story-card:not(.cloned)'));
  originalCardCount = originalCards.length;

  if (originalCardCount === 0) return;

  // Clone cards for seamless infinite loop
  const itemsPerView = getItemsPerView();
  const clonesToCreate = itemsPerView + 1;
  
  // Remove any existing clones
  document.querySelectorAll('.success-story-card.cloned').forEach(card => card.remove());
  
  // Clone first N cards and append to the end
  for (let i = 0; i < clonesToCreate; i++) {
    const cardToClone = originalCards[i % originalCardCount];
    const clonedCard = cardToClone.cloneNode(true);
    clonedCard.classList.add('cloned');
    sliderTrack.appendChild(clonedCard);
  }

  totalCards = originalCardCount + clonesToCreate;

  // Create dots only for original cards (not clones)
  sliderDotsContainer.innerHTML = '';
  for (let i = 0; i < originalCardCount; i++) {
    const dot = document.createElement('div');
    dot.className = `slider-dot ${i === 0 ? 'active' : ''}`;
    dot.onclick = () => goToSlideInstant(i);
    sliderDotsContainer.appendChild(dot);
  }

  sliderIndex = 0;
  updateSlider();
  startAutoPlay();
}

function moveSlider(direction) {
  if (isTransitioning) return;
  
  sliderIndex += direction;
  updateSliderWithWrap();
  
  // Reset auto-play timer when user interacts
  clearInterval(autoPlayInterval);
  startAutoPlay();
}

function goToSlideInstant(index) {
  sliderIndex = index;
  updateSlider();
  
  // Reset auto-play timer when user interacts
  clearInterval(autoPlayInterval);
  startAutoPlay();
}

function updateSliderWithWrap() {
  const sliderTrack = document.getElementById('sliderTrack');
  
  if (!sliderTrack) return;

  const itemsPerView = getItemsPerView();
  const cardWidth = 100 / itemsPerView;
  const translateValue = -(sliderIndex * cardWidth);
  
  sliderTrack.style.transition = 'transform 0.6s cubic-bezier(0.175, 0.885, 0.32, 1.275)';
  sliderTrack.style.transform = `translateX(${translateValue}%)`;

  // Update dots - show position in original cards (loop back)
  const dotIndex = sliderIndex % originalCardCount;
  updateDots(dotIndex);

  // When we reach the cloned section, smoothly jump back to beginning
  setTimeout(() => {
    if (sliderIndex >= originalCardCount) {
      sliderTrack.style.transition = 'none';
      sliderIndex = sliderIndex % originalCardCount;
      const newTranslateValue = -(sliderIndex * cardWidth);
      sliderTrack.style.transform = `translateX(${newTranslateValue}%)`;
    }
  }, 600);
}

function updateSlider() {
  const sliderTrack = document.getElementById('sliderTrack');
  
  if (!sliderTrack) return;

  const itemsPerView = getItemsPerView();
  const cardWidth = 100 / itemsPerView;
  const translateValue = -(sliderIndex * cardWidth);
  
  sliderTrack.style.transition = 'none';
  sliderTrack.style.transform = `translateX(${translateValue}%)`;

  // Update dots
  const dotIndex = sliderIndex % originalCardCount;
  updateDots(dotIndex);
}

function updateDots(dotIndex) {
  const sliderDots = document.querySelectorAll('.slider-dot');
  sliderDots.forEach((dot, idx) => {
    dot.classList.toggle('active', idx === dotIndex);
  });
}

function startAutoPlay() {
  autoPlayInterval = setInterval(() => {
    sliderIndex += 1;
    updateSliderWithWrap();
  }, 5000); // Move to next card every 5 seconds
}

// Stop auto-play on hover, resume on mouse leave
function addHoverControl() {
  const sliderWrapper = document.querySelector('.slider-wrapper');
  if (sliderWrapper) {
    sliderWrapper.addEventListener('mouseenter', () => {
      clearInterval(autoPlayInterval);
    });
    sliderWrapper.addEventListener('mouseleave', () => {
      startAutoPlay();
    });
  }
}

// Keyboard navigation support
function addKeyboardControl() {
  document.addEventListener('keydown', (e) => {
    const sliderWrapper = document.querySelector('.slider-wrapper');
    if (!sliderWrapper || !sliderWrapper.parentElement) return;
    
    // Only if slider is in viewport
    const rect = sliderWrapper.getBoundingClientRect();
    if (rect.top > window.innerHeight || rect.bottom < 0) return;

    if (e.key === 'ArrowLeft') {
      moveSlider(-1);
    } else if (e.key === 'ArrowRight') {
      moveSlider(1);
    }
  });
}

let heroSlideIndex = 0;
let heroSlides = [];
let heroDots = [];
let heroAutoPlay = null;

function initHeroSlider() {
  heroSlides = Array.from(document.querySelectorAll('.hero-slide'));
  const heroDotsContainer = document.getElementById('heroDots');
  const prevButton = document.querySelector('.hero-prev');
  const nextButton = document.querySelector('.hero-next');

  if (!heroSlides.length || !heroDotsContainer) return;

  heroDotsContainer.innerHTML = '';
  heroSlides.forEach((slide, idx) => {
    const dot = document.createElement('button');
    dot.type = 'button';
    dot.className = `hero-dot${idx === 0 ? ' active' : ''}`;
    dot.addEventListener('click', () => goToHeroSlide(idx));
    heroDotsContainer.appendChild(dot);
  });

  heroDots = Array.from(heroDotsContainer.children);
  heroSlideIndex = 0;
  updateHeroSlide();

  if (prevButton) prevButton.addEventListener('click', () => { prevHeroSlide(); resetHeroAutoplay(); });
  if (nextButton) nextButton.addEventListener('click', () => { nextHeroSlide(); resetHeroAutoplay(); });

  const heroSlider = document.getElementById('heroSlider');
  if (heroSlider) {
    heroSlider.addEventListener('mouseenter', () => clearInterval(heroAutoPlay));
    heroSlider.addEventListener('mouseleave', () => startHeroAutoplay());
  }

  startHeroAutoplay();
}

function updateHeroSlide() {
  heroSlides.forEach((slide, idx) => slide.classList.toggle('active', idx === heroSlideIndex));
  heroDots.forEach((dot, idx) => dot.classList.toggle('active', idx === heroSlideIndex));
}

function goToHeroSlide(index) {
  heroSlideIndex = index;
  updateHeroSlide();
}

function nextHeroSlide() {
  heroSlideIndex = (heroSlideIndex + 1) % heroSlides.length;
  updateHeroSlide();
}

function prevHeroSlide() {
  heroSlideIndex = (heroSlideIndex - 1 + heroSlides.length) % heroSlides.length;
  updateHeroSlide();
}

function startHeroAutoplay() {
  clearInterval(heroAutoPlay);
  heroAutoPlay = setInterval(() => {
    nextHeroSlide();
  }, 6000);
}

function resetHeroAutoplay() {
  clearInterval(heroAutoPlay);
  startHeroAutoplay();
}

// Initialize on DOM ready
if (document.readyState === 'loading') {
  document.addEventListener('DOMContentLoaded', () => {
    initSuccessStoriesSlider();
    addHoverControl();
    addKeyboardControl();
    initHeroSlider();
  });
} else {
  initSuccessStoriesSlider();
  addHoverControl();
  addKeyboardControl();
  initHeroSlider();
}

// Track window resize for responsive slider
let resizeTimer;
window.addEventListener('resize', () => {
  clearTimeout(resizeTimer);
  resizeTimer = setTimeout(() => {
    initSuccessStoriesSlider();
  }, 250);
});

