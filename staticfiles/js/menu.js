document.addEventListener("DOMContentLoaded", function () {
    const menuBtn = document.querySelector(".menu-toggle");
    const navMenu = document.querySelector("nav ul");

    menuBtn.addEventListener("click", () => {
        navMenu.classList.toggle("show");
    });

    navMenu.querySelectorAll("a").forEach(link => {
        link.addEventListener("click", () => {
            navMenu.classList.remove("show");
        });
    });
});
