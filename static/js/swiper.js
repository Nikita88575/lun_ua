document.addEventListener('DOMContentLoaded', () => {
  const canvas = document.querySelector('#project-plan-canvas');
  if (!canvas) return;
  new Swiper(canvas, {
    loop: true,
    grabCursor: true,
    slidesPerView: 1,
    speed: 400,
    centeredSlides: true,
    slideToClickedSlide: true,
    simulateTouch: true,
    resistanceRatio: 0.85,
    observer: true,
    observeParents: true,
  });
});
