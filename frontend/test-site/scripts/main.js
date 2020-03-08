// "Get Information" button.
// It nows can redirect users to "second-page.html".
// What about fetching information about the car? Should we do that in the javascript for "second-page.html"?
let getInfoButton = document.querySelector('button');
getInfoButton.onclick = function () {
    location.href = "frontend/test-site/second-page.html"
}

