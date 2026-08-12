function updateCounter() {
    const el = document.getElementById('slide-counter');
    const idx = window.shower.activeSlideIndex;
    el.textContent = idx >= 0 ? `${idx + 1}/${window.shower.slides.length}` : '';
}

window.shower.addEventListener('start', () => {
    document.querySelector('.shower').focus();
    updateCounter();
});

window.shower.addEventListener('slidechange', updateCounter);

window.shower.addEventListener('modechange', () => {
    if (window.shower.isFullMode && !window.shower.activeSlide) window.shower.first();
    document.documentElement.classList.toggle('slides-full', window.shower.isFullMode);
});
