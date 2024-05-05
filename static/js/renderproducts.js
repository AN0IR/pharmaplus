let products = [
    {
        name: "lactoflorence",
        heading: "Лактофлоренс таблетки",
        price: 1950,
        img: "/static//assets/products/lactoflorence.png",
    },
    {
        name: "mucoplant",
        heading: "Эвкалипт Мукоплант",
        price: 1630,
        img: "/static//assets/products/mucoplant.png",
    },
    {
        name: "cream_vitc",
        heading: "Крем Витамин-С",
        price: 980,
        img: "/static//assets/products/cream_vitc.png",
    },
    {
        name: "lacalut",
        heading: "Зубная паста Lacalut",
        price: 980,
        img: "/static//assets/products/lacalut.png",
    },
    {
        name: "ambro",
        heading: "Сироп от кашля ambro",
        price: 980,
        img: "/static//assets/products/ambro.png",
    },
    {
        name: "magne",
        heading: "Таблетки Magne B6",
        price: 4175,
        img: "/static//assets/products/magne.png",
    },
    {
        name: "rengalin",
        heading: "Таблетки rengalin",
        price: 2350,
        img: "/static//assets/products/rengalin.png",
    },
    {
        name: "anaferon",
        heading: "Таблетки Анаферон детский",
        price: 1680,
        img: "/static//assets/products/anaferon.png",
    },
    {
        name: "lazolvan",
        heading: "Сироп от кашля Лазолван",
        price: 2150,
        img: "/static//assets/products/lazolvan.png",
    },
    {
        name: "magne_premium",
        heading: "Таблетки Magne B6 premium",
        price: 5190,
        img: "/static//assets/products/magne_premium.png",
    },
    {
        name: "zodak",
        heading: "Таблетки Zodak противоалергенные",
        price: 1300,
        img: "/static//assets/products/zodak.png",
    },
    {
        name: "smekta",
        heading: "Smekta растворимый",
        price: 2500,
        img: "/static//assets/products/smekta.png",
    },
    {
        name: "quickset",
        heading: "MEDTRONIC Система инфузионная стерильная",
        price: 4820,
        img: "/static//assets/products/quickset.png",
    },
    {
        name: "omez",
        heading: "Омез №30 капс Омепразол",
        price: 1900,
        img: "/static//assets/products/omez.png",
    },
    {
        name: "reservoir",
        heading: "MEDTRONIC Резервуар стерильный",
        price: 1020,
        img: "/static//assets/products/reservoir.png",
    },
];

let fullPathname = document.URL
let pathnameParts = fullPathname.split('/');
let lastPart = pathnameParts[pathnameParts.length - 1];

if (lastPart==="about"){
    const grid = document.querySelector(".productsgrid");

    const productsGrid = products.map( (product) => {
        const card = document.createElement("div");
        const cardImage = document.createElement("img");
        const cardName = document.createElement("h3");
        const cardPrice = document.createElement("p");
        const addButton = document.createElement("button");


        card.classList.add("product")
        card.appendChild(cardImage)
        card.appendChild(cardName)
        card.appendChild(cardPrice)
        card.appendChild(addButton)


        addButton.classList.add("add-to-cart");
        addButton.innerHTML = "Добавить"
        addButton.setAttribute("type", "button");
        addButton.setAttribute("onclick", `addToCart("${product.heading}", "${product.price}", "${product.img}");`);

        cardImage.setAttribute("src", product.img);
        cardName.innerHTML = product.heading;
        cardPrice.innerHTML = `${product.price} тг`;

        grid.appendChild(card)
    })


    console.log(products);
} else if(lastPart===""){
   const grid = document.querySelector(".carousel");
   console.log(grid)

   const productsGrid = products.map( (product) => {
       let card = document.createElement("div");
       grid.appendChild(card)
       card.innerHTML = `
                        <div class="slide product">
                            <a href="./about"><img src=${product.img}></a>
                            <h3>${product.heading}</h3>
                            <p>${product.price} тг</p>
                        </div>
                        `;
    })
}