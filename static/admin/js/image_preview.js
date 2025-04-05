document.addEventListener("DOMContentLoaded", function() {
    var input = document.querySelector("#id_image");  // Rasm yuklash input elementi
    var preview = document.querySelector("#image-preview");  // Oldindan ko‘rish rasm elementi

    input.addEventListener("change", function(event) {
        var reader = new FileReader();
        reader.onload = function(){
            preview.src = reader.result;
            preview.style.display = 'block';
        };
        reader.readAsDataURL(event.target.files[0]);
    });
});
