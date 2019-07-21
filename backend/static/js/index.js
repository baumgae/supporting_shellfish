var currentImage;

function previewFile() {
    var uploadFileButton = document.getElementById('upload-file');
    document.getElementById('bad-type-error').style.display = "none";
    document.getElementById('general-error').style.display = "none";

    var preview = document.getElementById('img_preview');
    var file    = document.querySelector('input[type=file]').files[0];
    var reader  = new FileReader();
    if (file) {
        reader.addEventListener("load", function () {
            currentImage = reader.result;
            preview.src = reader.result;
            uploadFileButton.disabled = false;
        }, false);

        reader.readAsDataURL(file);
    }
}

function uploadFile() {
    var uploadFileButton = document.getElementById('upload-file');
    uploadFileButton.classList.add('is-loading');
    var xhr = new XMLHttpRequest();
    xhr.open('POST', 'http://127.0.0.1:5000/advice');
    xhr.setRequestHeader('Content-Type', 'application/json');
    xhr.onload = function() {
        if (xhr.status === 200) {
            uploadFileButton.classList.remove('is-loading');
            console.log(JSON.parse(xhr.responseText));
            response = JSON.parse(xhr.responseText);
            document.getElementById('shelly').src="./static/images/Shelly_"+response.emotion+".png";
            document.getElementById('p1').innerHTML = "I can see your "+response.emotion+"! Take my advice: ";
            document.getElementById('p2').innerHTML = response.advice;
        }
        else {
            if (xhr.status === 400){

                document.getElementById('bad-type-error').style.display = "block";

            } else {
                document.getElementById('general-error').style.display = "block";
            }
            uploadFileButton.classList.remove('is-loading');
            document.getElementById('shelly').src="./static/images/Shelly_neutral.png";
            document.getElementById('p1').innerHTML = "I'm Shelly, the Supporting Shellfish.";
            document.getElementById('p2').innerHTML = "Please upload a picture of your face.";
        }
    };

    var jsonFile = JSON.stringify({"image": currentImage});
    xhr.send(jsonFile);
}