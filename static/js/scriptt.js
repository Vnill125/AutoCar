function showPassword() {
    var x = document.getElementById("myInput");
    if (x.type === "password") {
      x.type = "text";
    } else {
      x.type = "password";
    }
  } 

  function toggleDescription() {
    var shortDescription = document.getElementById("shortDescription");
    var fullDescription = document.getElementById("fullDescription");
    var button = document.getElementById("showMoreButton");

    if (shortDescription.style.display === "none" || shortDescription.style.display === "") {
        shortDescription.style.display = "block";
        fullDescription.style.display = "none";
        button.innerHTML = "Show more";
    } else {
        shortDescription.style.display = "none";
        fullDescription.style.display = "block";
        button.innerHTML = "Show less";
    }
}

let currentSlide = 1;

function changeSlide(n) {
  showSlides(currentSlide += n);
}

function showSlides(n) {
  let slides = $('.car_left img');

  if (n > slides.length) {
    currentSlide = 1;
  }

  if (n < 1) {
    currentSlide = slides.length;
  }

  slides.removeClass('active');
  slides.eq(currentSlide - 1).addClass('active');
}