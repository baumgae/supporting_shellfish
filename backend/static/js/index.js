
function previewFile() {
    var uploadFileButton = document.getElementById('upload-file');
    var preview = document.getElementById('img_preview');
    var file    = document.querySelector('input[type=file]').files[0];
    var reader  = new FileReader();
    if (file) {
        reader.addEventListener("load", function () {
            console.log('base64'+reader.result);
            preview.src = reader.result;
            uploadFileButton.disabled = false;
        }, false);

        reader.readAsDataURL(file);
    }
}
const uploadFile = async () => {
    const response = await fetch('http://127.0.0.1:5000/advice', {
        method: 'POST',
        body: JSON.stringify({"image": "Its me"}),
        headers: {
            'dataType': 'json'
        }
    });
    const myJson = await response.json(); //extract JSON from the http response
    // do something with myJson
};