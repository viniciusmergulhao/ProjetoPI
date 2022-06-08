'use strict'

let photo = document.getElementById('img-photo');
let file = document.getElementById('fileimg');

photo.addEventListener('click', () => {
    file.click();
});