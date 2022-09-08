const starRating = document.querySelectorAll('.rating-stars');


    starRating.forEach(rating => {
        const ratingValue = parseInt(rating.getAttribute('data-value'));
        const fullStar = ratingValue;
        const emptyStar = 5 - fullStar;
        let stars = '';

        for (let i = 1; i < 6; i++) {
            if (i <= fullStar) {
                stars += `<i class="fas fa-star"></i>`;
            }
            else {
                stars += `<i class="far fa-star"></i>`;
            }
        }
        rating.innerHTML = stars;
    });