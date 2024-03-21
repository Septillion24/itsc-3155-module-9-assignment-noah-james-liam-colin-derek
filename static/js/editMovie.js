
    // Add event listener to each star element to update the rating input value and refresh the star display.
    document.addEventListener('DOMContentLoaded', (event)=>{
        let stars = document.querySelectorAll('.star');
        stars.forEach((star,index) => {
            star.addEventListener('click', (e) => {
                document.getElementById('ratingInput').value = star.getAttribute('data-value');
                updateStars(index+1);
            });
        });

    
    // Update the stars displayed based on the given rating value.
    function updateStars(rating){
        stars.forEach((star, index) => {
            if(index < rating){
                star.innerHTML = '★';
            } else {
                star.innerHTML = '☆';
            }
        });
    }
    });
