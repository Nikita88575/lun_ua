const slider = document.getElementById('areaSlider');
const fromSpan = document.getElementById('areaFromValue');
const toSpan = document.getElementById('areaToValue');
const projectsContainer = document.getElementById('projectsContainer');
const loadingIndicator = document.getElementById('loading');

const params = new URLSearchParams(window.location.search);
const areaMin = parseFloat(slider.dataset.min);
const areaMax = parseFloat(slider.dataset.max);
const areaFrom = parseFloat(slider.dataset.from);
const areaTo = parseFloat(slider.dataset.to);


noUiSlider.create(slider, {
  start: [areaFrom, areaTo],
  connect: true,
  step: 1,
  range: {
    min: areaMin,
    max: areaMax
  },
  format: {
    to: value => Math.round(value),
    from: value => Number(value)
  },
  tooltips: [true, true]
});

slider.noUiSlider.on('update', function(values) {
  fromSpan.innerText = values[0];
  toSpan.innerText = values[1];
});

slider.noUiSlider.on('change', function(values) {
  const [from, to] = values;
  const params = new URLSearchParams(window.location.search);
  params.set('area_from', Math.round(from));
  params.set('area_to', Math.round(to));
  params.delete('page');

  const url = `${window.location.pathname}?${params.toString()}`;

  loadingIndicator.style.display = "block";

  fetch(url, {
    headers: { 'X-Requested-With': 'XMLHttpRequest' }
  })
  .then(response => response.json()) 
  .then(data => {
    projectsContainer.innerHTML = data.html;
    loadingIndicator.style.display = "none";
    window.history.replaceState(null, '', url);
    document.dispatchEvent(new CustomEvent('projectsFilterChanged'));
  })
  .catch(error => {
    loadingIndicator.style.display = "none";
    console.error('Ошибка при фильтрации:', error);
  });
});

