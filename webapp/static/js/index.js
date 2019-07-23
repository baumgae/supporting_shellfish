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

function createSnapShoot() {
    const supported = 'mediaDevices' in navigator;

    var player = document.getElementById('player');
    var createImageButton = document.getElementById('shoot-image'); // Enable PhotoShoot

    const canvas = document.getElementById('canvas');   // Canvas for Stream and Shoot
    const context = canvas.getContext('2d');

    const captureButton = document.getElementById('capture');         // Create SnapShoot
    var preview = document.getElementById('img_preview');             // Look at yourself

    const constraints = {
        video: true,
    };

    createImageButton.addEventListener('click', () => {
        context.disabled = false;
        captureButton.disabled = false;

        captureButton.addEventListener('click', () => {
            // Draw the video frame to the canvas.
            context.drawImage(player, 0, 0, preview.width, preview.height);

            // Create SnapShoot and Upload File
            var file = context;
            var reader  = new FileReader();
            if (file) {
                reader.addEventListener("Capture...", function () {
                currentImage = reader.result;
                preview.src = reader.result;
                uploadFileButton.disabled = false;
            }, false);

            reader.readAsDataURL(file);
        }
        });

        // Attach the video stream to the video element and autoplay.
        navigator.mediaDevices.getUserMedia(constraints)
            .then((stream) => {
              context.srcObject = stream;
            });


    });

}

function uploadFile() {
    var uploadFileButton = document.getElementById('upload-file');
	var openFileButton = document.getElementById('open-filesystem-btn');
    uploadFileButton.classList.add('is-loading');
	openFileButton.classList.add('is-disabled');
	
    var xhr = new XMLHttpRequest();
    xhr.open('POST', 'http://0.0.0.0:4000/advice');
    xhr.setRequestHeader('Content-Type', 'application/json');
    xhr.onload = function() {
        if (xhr.status === 200) {
            uploadFileButton.classList.remove('is-loading');
            console.log(JSON.parse(xhr.responseText));
            response = JSON.parse(xhr.responseText);
            document.getElementById('shelly').src="./static/images/Shelly_"+response.emotion+".png";
            document.getElementById('p1').innerHTML = "I can see your "+response.emotion+"! Take my advice: ";
            document.getElementById('p2').innerHTML = response.advice;
			openFileButton.classList.remove('is-disabled');
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
			openFileButton.classList.remove('is-disabled');
        }
    };

    var jsonFile = JSON.stringify({"image": currentImage});
    xhr.send(jsonFile);
}