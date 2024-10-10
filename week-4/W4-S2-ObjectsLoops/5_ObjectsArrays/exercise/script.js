// create your coffee object array here
const orders = [
    {
        type: "latte",
        milk: true,
        customer: "Jim"
    },
    {
        type: "flat white",
        milk: true,
        customer: "Tom"
    },
    {
        type: "cortado",
        milk: false,
        customer: "Anna"
    }
];

// creat your print order function here
function printOrders(orders) {
    // for (let i = 0; i < orders.length; i++ ) {
    //     console.log(`Customer: ${orders[i].customer}, Coffee: ${orders[i].type}, Milk: ${orders[i].milk ? "Yes" : "No"}`);
    // };

    // using the array method .forEach() does it all in one line...
    orders.forEach(order => console.log(`Customer: ${order.customer}, Coffee: ${order.type}, Milk: ${order.milk ? "Yes" : "No"}`));
}

printOrders(orders);
