// static/js/main.js — Custom JavaScript for the Library site

// Visible confirmation that this JS file loaded
console.log("✅ main.js loaded successfully!");

// Highlight the active nav link based on the current URL
document.addEventListener("DOMContentLoaded", function () {
    const currentPath = window.location.pathname;
    const navLinks = document.querySelectorAll(".navbar-nav .nav-link");

    navLinks.forEach(function (link) {
        // If the link's href matches the current page, mark it active
        if (link.getAttribute("href") === currentPath) {
            link.classList.add("active");
        }
    });
});
