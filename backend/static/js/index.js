var currentImage;

function previewFile() {
    var uploadFileButton = document.getElementById('upload-file');
    var preview = document.getElementById('img_preview');
    var file    = document.querySelector('input[type=file]').files[0];
    var reader  = new FileReader();
    if (file) {
        reader.addEventListener("load", function () {
            console.log('base64'+reader.result);
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
      //var image = JSON.parse(xhr.responseText);
			//What to do with response
			uploadFileButton.classList.remove('is-loading');
    }
		else {
			uploadFileButton.classList.remove('is-loading');
			//display error message
		}};

    var jsonFile = JSON.stringify({"image": currentImage});
	console.log(jsonFile);
	xhr.send(JSON.stringify(jsonFile));
}
