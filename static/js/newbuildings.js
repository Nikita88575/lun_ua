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

  let deleteNBForm = document.getElementById("deleteNBForm");
  let deleteNBBtn = document.getElementById("deleteNBBtn");
  let NBDetail = document.getElementById("NBDetail");

    // Delete offer button form
    deleteNBBtn.addEventListener("click", function() {
      if (deleteNBForm.style.display === "none"){
        deleteNBForm.style.display = "block";
        NBDetail.style.display = "none";
      } else {
        NBDetail.style.display = "block";
        deleteNBForm.style.display = "none";
      }
    });
});