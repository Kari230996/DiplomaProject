function showImage(imgSrc, title, content, url) {
    let modal = document.getElementById('myModal');
    let modalImg = document.getElementById('modal-img');
    modal.style.display = 'block';
    let captionText = document.getElementById('caption');
    modalImg.src = imgSrc;
    captionText.innerHTML = '<h4>' + title + '</h4>' + '<p>' + content + '</p>';
}

function hideImage() {
    var modal = document.getElementById('modal');
    modal.style.display = 'none';
}