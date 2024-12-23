document.getElementById('id_photo').addEventListener('change', function() {
    let file = this.files[0];
    let reader = new FileReader();

    reader.onload = function(e) {
        document.getElementById('project-image').src = e.target.result;
    };

    reader.readAsDataURL(file);
});