function toggleForm(object) {
  if (object.style.display === "block") {
    object.style.display = "none";
  } else {
    object.style.display = "block"
  }
}

function reversToggleForm(object) {
  if (object.style.display === "none") {
    object.style.display = "block";
  } else {
    object.style.display = "none";
  }
}

document.addEventListener("DOMContentLoaded", function () {

  let editUserProfileButton = document.getElementById("editUserProfileButton");
  let cancelUpdateButton = document.getElementById("cancelUpdateButton");
  let editUserProfileForm = document.getElementById("editUserProfileForm");
  let projectsContainer = document.getElementById("projects-container");

  if (
    editUserProfileForm &&
    (
      editUserProfileForm.querySelector('.form-errors') ||
      editUserProfileForm.querySelector('.errorlist')
    )
  ) {
    editUserProfileForm.style.display = "block";
    projectsContainer.style.display = "none";
  }

  editUserProfileButton.addEventListener("click", function () {
    if (editUserProfileForm.style.display === "none"){
      editUserProfileForm.style.display = "block";
      cancelUpdateButton.style.display = "flex";
      projectsContainer.style.display = "none";
    } else {
      editUserProfileForm.style.display = "none";
      cancelUpdateButton.style.display = "none";
      projectsContainer.style.display = "block";
    }
  });
});

