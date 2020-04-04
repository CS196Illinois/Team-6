//Display image chosen through the input element in "#img-output".
const plusButton = document.getElementById("img-find-button");
plusButton.onchange = function (event) {
    let image = document.getElementById('img-output');
    image.src = URL.createObjectURL(event.target.files[0]);
} 

//Prevent uploading if no image is chosen and pop up an alert message.
const uploadImg = document.getElementById("img-output");
const form = document.querySelector("form");
form.onsubmit = function (event) {
    if (uploadImg.src === "") {
        event.preventDefault();
        alert("You must choose an image to classify.");
    }
}

//Get a jsonObject from server to extract and display data.
fetch(url).then(function(response) {
    //Return the response as an jsonObject
    return response.json();
}).then(function(json) {
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

    let data = json;
    display(data);
});

//Helper function to display extracted data.
function display(jsonObject) {
    for (info in jsonObject) {
        let newElement = document.createElement("p");
        newElement.textContent = `${info}: ${jsonObject[info]}`;
        dataBox.append(newElement);
    }
}