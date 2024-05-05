function addToCart(product, price, image) {

    // Retrieve the cart items from local storage or initialize an empty array
    let cartItems = JSON.parse(localStorage.getItem('cartItems')) || [];

    // Create a new cart item object
    const newItem = {
      product: product,
      price: price,
      image: image,
    };

    // Add the new item to the cart
    cartItems.push(newItem);

    // Store the updated cart items in local storage
    localStorage.setItem('cartItems', JSON.stringify(cartItems));

    // Calculate the total price
    let totalPrice = 0;
    for (let i = 0; i < cartItems.length; i++) {
      totalPrice += cartItems[i].price;
    }

    // Return the total price
    return totalPrice;
  }



$(document).ready(function(){
    $('.carousel').slick({
        slidesToShow: 7,
        slidesToScroll: 1,
        autoplay: true,
        autoplaySpeed: 1800,
        arrows: false,
        dots: false,
        pauseOnHover: false,
        responsive: [{
            breakpoint: 768,
            settings: {
                slidesToShow: 4
            }
        }, {
            breakpoint: 520,
            settings: {
                slidesToShow: 3
            }
        }]
    });
});

console.log(localStorage.getItem('cartItems'))