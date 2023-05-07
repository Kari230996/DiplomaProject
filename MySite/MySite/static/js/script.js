function showImage(imgSrc) {
    var modal = document.getElementById('modal');
    var modalImg = document.getElementById('modal-img');
    modal.style.display = 'block';
    modalImg.src = imgSrc;
}

function hideImage() {
    var modal = document.getElementById('modal');
    modal.style.display = 'none';
}