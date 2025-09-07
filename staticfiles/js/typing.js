document.addEventListener("DOMContentLoaded", function () {
    const h1 = document.querySelector("h1");
    const text = h1.textContent.trim(); 
    h1.textContent = ""; 

    let index = 0;

    function typeLetter() {
        if (index < text.length) {
            const span = document.createElement("span");
            span.textContent = text[index] === " " ? " " : text[index];
            span.style.opacity = 0;
            h1.appendChild(span);

            setTimeout(() => {
                span.style.transition = "opacity 0.4s ease";
                span.style.opacity = 1;
            }, 50);

            index++;
            setTimeout(typeLetter, 100);
        }
    }

    typeLetter();
});
