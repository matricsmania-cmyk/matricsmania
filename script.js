const themeToggle = document.querySelector(".theme-toggle");
const themeStorageKey = "matricsmania-theme";
const themeColor = document.querySelector('meta[name="theme-color"]');

let savedTheme = null;
try {
  savedTheme = localStorage.getItem(themeStorageKey);
} catch (error) {
  console.warn("Could not read the saved theme preference.", error);
}

const initialTheme = savedTheme === "dark" ? "dark" : "light";
document.documentElement.dataset.theme = initialTheme;

function updateThemeControls(theme) {
  if (!(themeToggle instanceof HTMLButtonElement)) return;

  const isDark = theme === "dark";
  themeToggle.setAttribute("aria-label", `Switch to ${isDark ? "light" : "dark"} theme`);
  themeToggle.setAttribute("aria-pressed", String(isDark));
  const icon = themeToggle.querySelector("span");
  if (icon) icon.textContent = isDark ? "☀" : "☾";
  if (themeColor instanceof HTMLMetaElement) {
    themeColor.content = isDark ? "#111321" : "#fbfaff";
  }
}

updateThemeControls(initialTheme);

if (window.location.protocol === "file:") {
  const servicePageSlugs = [
    "search-engine-optimisation",
    "social-media-marketing",
    "website-development",
    "meta-ads",
    "google-ads",
    "performance-marketing",
    "seo-agency-in-varanasi",
    "social-media-marketing-agency-in-varanasi",
    "website-development-company-in-varanasi",
    "meta-ads-agency-in-varanasi",
    "google-ads-agency-in-varanasi",
    "performance-marketing-agency-in-varanasi"
  ];

  document.querySelectorAll('a[href^="/"]').forEach((link) => {
    const slug = link.getAttribute("href").replace(/^\/|\/$/g, "");
    if (servicePageSlugs.includes(slug)) {
      link.href = `${slug}.html`;
    }
  });
}

if (themeToggle instanceof HTMLButtonElement) {
  themeToggle.addEventListener("click", () => {
    const nextTheme = document.documentElement.dataset.theme === "dark" ? "light" : "dark";
    document.documentElement.dataset.theme = nextTheme;
    updateThemeControls(nextTheme);

    try {
      localStorage.setItem(themeStorageKey, nextTheme);
    } catch (error) {
      console.warn("Could not save the theme preference.", error);
    }
  });
}

const menuToggle = document.querySelector(".menu-toggle");
const primaryNav = document.querySelector(".primary-nav");

if (menuToggle && primaryNav) {
  menuToggle.addEventListener("click", () => {
    const isExpanded = menuToggle.getAttribute("aria-expanded") === "true";
    menuToggle.setAttribute("aria-expanded", String(!isExpanded));
    menuToggle.setAttribute("aria-label", isExpanded ? "Open navigation" : "Close navigation");
    primaryNav.classList.toggle("is-open", !isExpanded);
  });

  primaryNav.addEventListener("click", (event) => {
    if (event.target instanceof Element && event.target.closest("a")) {
      menuToggle.setAttribute("aria-expanded", "false");
      menuToggle.setAttribute("aria-label", "Open navigation");
      primaryNav.classList.remove("is-open");
    }
  });
}

document.querySelectorAll("[data-year]").forEach((element) => {
  element.textContent = String(new Date().getFullYear());
});

const contactForm = document.querySelector("[data-contact-form]");
const formStatus = document.querySelector("[data-form-status]");
const serviceSelect = document.querySelector("#service");

if (serviceSelect instanceof HTMLSelectElement) {
  const requestedService = new URLSearchParams(window.location.search).get("service");
  if (requestedService && Array.from(serviceSelect.options).some((option) => option.value === requestedService)) {
    serviceSelect.value = requestedService;
  }
}

if (contactForm instanceof HTMLFormElement && formStatus instanceof HTMLElement) {
  contactForm.addEventListener("submit", (event) => {
    event.preventDefault();
    formStatus.textContent = "This demo form does not send or store messages yet. Connect it to your email or a form service before publishing.";
    formStatus.classList.add("is-notice");
  });
}
