const fs = require('fs');
const path = require('path');

const LOCATIONS = [
    "agra", "aligarh", "ayodhya", "azamgarh", "bareilly", "bhadohi",
    "firozabad", "ghaziabad", "gorakhpur", "greater-noida", "hapur",
    "jaunpur", "jhansi", "kanpur", "lucknow", "mathura", "meerut",
    "mirzapur", "moradabad", "muzaffarnagar", "noida", "prayagraj",
    "rampur", "saharanpur", "shahjahanpur", "vrindavan"
];

const EXISTING_SEO = ["agra", "aligarh", "ayodhya", "azamgarh", "bareilly", "bhadohi", "firozabad", "ghaziabad", "gorakhpur"];

const baseDir = __dirname;
let filesCreated = 0;

// Create placeholder files
console.log("Starting file generation...");

// For each location and service combo
LOCATIONS.forEach((location) => {
    if (!EXISTING_SEO.includes(location)) {
        const filename = path.join(baseDir, `seo-services-${location}.html`);
        console.log(`Would create: ${filename}`);
    }
});

console.log(`Total files to create: ${LOCATIONS.length * 5 + (LOCATIONS.length - EXISTING_SEO.length)}`);
