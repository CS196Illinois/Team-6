//Display image chosen through the input element in "#img-output".
const plusButton = document.getElementById("img-find-button");
plusButton.onchange = function () {
    let uploadImg = document.getElementById('img-output');
    var file = this.files[0];
    var reader = new FileReader();
    reader.onload = function() {
        uploadImg.src = reader.result;
    }
    reader.readAsDataURL(file);
} 

// Pop up an alert and prevent sending the request if no image is chosen
const classifyButton = document.getElementById("classify-button");
const uploadImg = document.getElementById("img-output");
classifyButton.onclick = function () {
    if (uploadImg.src === "") {
        event.preventDefault();
        alert("You must choose an image to classify.");
        return;
    }
}
// // Send a post request
// const classifyButton = document.getElementById("classify-button");
// classifyButton.onclick = function() {
//     // Pop up an alert if no image is chosen.
//     const uploadImg = document.getElementById("img-output");
//     if (uploadImg.src === "") {
//         alert("You must choose an image to classify.");
//         return;
//     }

//     var xhr = new XMLHttpRequest();
//     // url ??????
//     xhr.open('POST', url, true);
//     xhr.responseType = 'json';
//     xhr.onload = function() {
//         // if the operation is completed
//         if (this.readyState === xhr.DONE) {
//             var dataAsJson = xhr.response;
//             // Display JsonObject in a readable way
//             display(dataAsJson);
//         }
//     }

//     // Get the file of the selected image
//     var image = plusButton.files[0];
//     // Convert the image into URL
//     var reader = new FileReader();
//     reader.onload = function() {
//         var imageURL = reader.result;
//         fileData.append('file', imageURL)
//     }
//     reader.readAsDataURL(image);
//     // Send the selected image to server
//     var fileData = new FormData();
//     xhr.send(fileData);
// }

//Helper function to display extracted data.
function display(jsonObject) {
    //Make "description" and "pictureDropBox" disaapear.
    const description = document.getElementById("description");
    description.style.display = "none";
    const pictureDropBox = document.getElementById("pictureDropBox");
    pictureDropBox.style.display = "none";

    //Create a new "div" for displaying data extracted from jsonObject
    const dataBox = document.createElement("div");
    dataBox.setAttribute("id", "dataBox");
    const parent = document.querySelector("main");
    parent.append(dataBox);

    for (info in jsonObject) {
        let newElement = document.createElement("p");
        newElement.textContent = `${info}: ${jsonObject[info]}`;
        dataBox.append(newElement);
    }
}