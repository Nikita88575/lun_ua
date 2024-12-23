let slideIndex = 0;
let slides = document.querySelectorAll(".slider-item");

function moveSlide(step) {
    slideIndex += step;

    if (slideIndex < 0) {
        slideIndex = slides.length - 1;
    } else if (slideIndex >= slides.length) {
        slideIndex = 0;
    }

    updateSlides();
}

function updateSlides() {
    slides.forEach((slide) => {
        slide.style.display = "none";
    });

    slides[slideIndex].style.display = "block";
}

updateSlides();