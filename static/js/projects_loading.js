document.addEventListener('DOMContentLoaded', () => {
  let page = 2;
  let loading = false;

  const projectsContainer = document.getElementById('projects-container');
  const loadingIndicator = document.getElementById('loading-indicator');

  if (!projectsContainer) return;


  let hasNext = projectsContainer.dataset.hasNext?.toLowerCase() === 'true';

  document.addEventListener('projectsFilterChanged', () => {
    page = 2;
    hasNext = true;
    loading = false;
  });

  function scrollHandler() {
    if (loading || !hasNext) return;

    const scrollBottom = window.innerHeight + window.scrollY >= document.body.offsetHeight - 300;
    if (!scrollBottom) return;

    loading = true;
    if (loadingIndicator) loadingIndicator.style.display = 'block';

    const params = new URLSearchParams(window.location.search);
    params.set('page', page);

    const fetchUrl = `${window.location.pathname}?${params.toString()}`;

    fetch(fetchUrl, {
      headers: {
        'X-Requested-With': 'XMLHttpRequest'
      }
    })
    .then(response => response.json())
    .then(data => {
      if (data.html && data.html.trim() !== '') {
        projectsContainer.insertAdjacentHTML('beforeend', data.html);
        if (window.htmx) htmx.process(projectsContainer);

        page += 1;
        hasNext = data.has_next;
      } else {
        hasNext = false;
      }
    })
    .catch(error => {
      console.error('Ошибка при подгрузке:', error);
    })
    .finally(() => {
      loading = false;
      if (loadingIndicator) loadingIndicator.style.display = 'none';
    });
  }

  window.addEventListener('scroll', scrollHandler);
});
