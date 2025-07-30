document.addEventListener("DOMContentLoaded", () => {
  const modal = document.getElementById("project-modal-container");
  const modalContent = document.getElementById("project-modal-content");

  function openModal(url, roomId, push = true) {
    fetch(url, {
      headers: { "X-Requested-With": "XMLHttpRequest" },
    })
      .then((response) => response.text())
      .then((html) => {
        if (html.includes('Planning')) {
          modalContent.innerHTML = html;
        } else {
          modalContent.innerHTML = "<h1 class='project-no-plannings'>No results</h1>";
        }
        modal.classList.add("show");
        modalContent.classList.add("show");
        document.body.classList.add("modal-no-scroll");
        console.log(html);

        if (push && roomId) {
          const newUrl = new URL(window.location);
          newUrl.searchParams.set("room_id", roomId);
          history.pushState(null, "", newUrl.toString());
        }

        const canvas = modalContent.querySelector("#project-plan-canvas");
        if (canvas) {
          new Swiper(canvas, {
            loop: true,
            slidesPerView: 1,
            speed: 300,
            slideToClickedSlide: true,
            simulateTouch: true,
            observer: true,
            observeParents: true,
          });
        }
      })
      .catch((err) => {
        console.error("Помилка завантаження модального вікна:", err);
      });
  }

  document.addEventListener("click", function (event) {
    const link = event.target.closest(".project-card-link");
    if (!link) return;

    event.preventDefault();

    const url = link.dataset.url;
    const roomId = new URL(link.href).searchParams.get("room_id");

    if (url && roomId) {
      openModal(url, roomId, true);
    }
  });

  modal.addEventListener("click", (event) => {
    if (
      !event.target.closest(".project-modal-content") ||
      event.target.closest(".button-modal-close")
    ) {
      modal.classList.remove("show");
      modalContent.classList.remove("show");
      document.body.classList.remove("modal-no-scroll");

      const newUrl = new URL(window.location);
      newUrl.searchParams.delete("room_id");
      history.pushState(null, "", newUrl.pathname + newUrl.search);
    }
  });

  const params = new URLSearchParams(window.location.search);
  const roomId = params.get("room_id");
  if (roomId) {
    const slug = window.location.pathname.split("/")[1];
    const roomsCount = window.location.pathname.split("/")[2];
    const fetchUrl = `/${slug}/${roomsCount}/${roomId}/`;

    openModal(fetchUrl, roomId, false); 
  }

  window.addEventListener("popstate", () => {
    const params = new URLSearchParams(window.location.search);
    const roomId = params.get("room_id");

    if (roomId) {
      const slug = window.location.pathname.split("/")[1];
      const roomsCount = window.location.pathname.split("/")[2];
      const fetchUrl = `/${slug}/${roomsCount}/${roomId}/`;
      openModal(fetchUrl, roomId, false);
    } else {
      modal.classList.remove("show");
      modalContent.classList.remove("show");
      document.body.classList.remove("modal-no-scroll");
    }
  });
});
