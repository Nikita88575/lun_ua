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

  let editNBBtn = document.getElementById("editNBBtn");
  let editNBForm = document.getElementById("editNBForm");
  let deleteNBForm = document.getElementById("deleteNBForm");
  let deleteNBBtn = document.getElementById("deleteNBBtn");
  let NBDetail = document.getElementById("NBDetail");

  if (
    editNBForm &&
    (
      editNBForm.querySelector('.form-errors') ||
      editNBForm.querySelector('.errorlist')
    )
  ) {
    editNBForm.style.display = "block";
    NBDetail.style.display = "none";
    deleteNBForm.style.display = "none";
  }

  if (editNBBtn && deleteNBBtn) {
    editNBBtn.addEventListener("click", function (){
      if (editNBForm.style.display === "none"){
        editNBForm.style.display = "block";
        NBDetail.style.display = "none";
        deleteNBForm.style.display = "none";
      } else {
        editNBForm.style.display = "none";
        NBDetail.style.display = "block";
        deleteNBForm.style.display = "none";
      }
    });

    deleteNBBtn.addEventListener("click", function () {
      if (deleteNBForm.style.display === "none"){
        deleteNBForm.style.display = "block";
        NBDetail.style.display = "none";
        editNBForm.style.display = "none";
      } else {
        editNBForm.style.display = "none";
        NBDetail.style.display = "block";
        deleteNBForm.style.display = "none";
      }
    });
  }
});

