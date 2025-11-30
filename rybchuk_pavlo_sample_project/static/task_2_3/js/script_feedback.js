"use strict";

document.addEventListener("DOMContentLoaded", function () {
  const stars = document.querySelectorAll(".star");
  const ratingInput = document.querySelector("#rating_input");

  const starSVG = `
        <svg viewBox="0 0 24 24">
          <path d="M12 .587l3.668 7.431 8.2 1.192-5.934 5.789 1.402 8.174L12 18.897 4.664 23.173l1.402-8.174L.132 9.21l8.2-1.192z"/>
        </svg>
      `;

  stars.forEach((star) => (star.innerHTML = starSVG));

  let rating = 0;

  function updateStars() {
    stars.forEach((s, i) => {
      s.classList.toggle("filled", i < rating);
    });
  }

  stars.forEach((star, index) => {
    star.addEventListener("mouseenter", () => {
      stars.forEach((s, i) => s.classList.toggle("preview", i <= index));
    });

    star.addEventListener("mouseleave", () => {
      stars.forEach((s) => s.classList.remove("preview"));
    });

    star.addEventListener("click", () => {
      rating = index + 1;
      ratingInput.value = rating;
      updateStars();
    });
  });

  updateStars();
});
