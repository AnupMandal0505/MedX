let openShopping = document.querySelector(".shopping");
let closeShopping = document.querySelector(".closeShopping");
let list = document.querySelector(".list");
let listCard = document.querySelector(".listCard");
let body = document.querySelector("body");
let total = document.querySelector(".total");
let quantity = document.querySelector(".quantity");

openShopping.addEventListener("click", () => {
  body.classList.add("active");
});
closeShopping.addEventListener("click", () => {
  body.classList.remove("active");
});

let products = [
  {
    id: 1,
    name: "Face Mist Ultra Sheer SPF 40",
    price: 404,
  },
  {
    id: 2,
    name: "Photostable Gold Gel Spf 55",
    price: 700,
  },
  {
    id: 3,
    name: "La Shield SPF 40 PA+++",
    price: 632,
  },
  {
    id: 4,
    name: "1% Hyaluronic Aqua Gel",
    price: 439,
  },
  {
    id: 5,
    name: "Sunmate Gel SPF 30+ PA+++",
    price: 679,
  },
  {
    id: 6,
    name: "ADEL 78 Dercut Ointment",
    price: 445,
  },
  {
    id: 7,
    name: "SBL Curoplus Ointment",
    price: 108,
  },
  {
    id: 8,
    name: "VLCC Matte Look SPF 30",
    price: 297,
  },
  {
    id: 9,
    name: "Lotus Herbals Safe Matte Gel PA+++ SPF 50",
    price: 449,
  },
  {
    id: 10,
    name: "Lacto Calamine Activated Kaolin Clay",
    price: 173,
  },
  {
    id: 11,
    name: "Fougera Hydrocortisone Cream",
    price: 796,
  },
  {
    id: 12,
    name: "Perrigo Triamcinolone Acetonide Cream",
    price: 1599,
  },
  {
    id: 13,
    name: "Pirox Gel 30 Gm",
    price: 50,
  },
  {
    id: 14,
    name: "Actiza Paraffin",
    price: 560,
  },
  {
    id: 15,
    name: "Triluma Cream RD",
    price: 645,
  },
  {
    id: 16,
    name: "Curenext Gel",
    price: 150,
  },
  {
    id: 17,
    name: "A Ret Tretinoin 0.05% Gel",
    price: 115,
  },
  {
    id: 18,
    name: "Desowen Desonide Cream",
    price: 240,
  },
  {
    id: 19,
    name: "La Shield Fisico SPF 50+ & PA+++",
    price: 650,
  },
  {
    id: 20,
    name: "Light Gel with SPF 50 PA++++",
    price: 448,
  },
];
let listCards = [];
function addToCard(key) {
  if (listCards[key] == null) {
    // copy product form list to list card
    listCards[key] = JSON.parse(JSON.stringify(products[key]));
    listCards[key].quantity = 1;
  }
  reloadCard();
}
function reloadCard() {
  listCard.innerHTML = "";
  let count = 0;
  let totalPrice = 0;
  listCards.forEach((value, key) => {
    totalPrice = totalPrice + value.price;
    count = count + value.quantity;
    if (value != null) {
      let newDiv = document.createElement("li");
      newDiv.innerHTML = `
                <div>${value.name}</div>
                <div>${value.price.toLocaleString()}</div>
                <div>
                    <button onclick="changeQuantity(${key}, ${
        value.quantity - 1
      })">-</button>
                    <div class="count">${value.quantity}</div>
                    <button onclick="changeQuantity(${key}, ${
        value.quantity + 1
      })">+</button>
                </div>`;
      listCard.appendChild(newDiv);
    }
  });
  total.innerText = totalPrice.toLocaleString();
  quantity.innerText = count;
}
function changeQuantity(key, quantity) {
  if (quantity == 0) {
    delete listCards[key];
  } else {
    listCards[key].quantity = quantity;
    listCards[key].price = quantity * products[key].price;
  }
  reloadCard();
}
