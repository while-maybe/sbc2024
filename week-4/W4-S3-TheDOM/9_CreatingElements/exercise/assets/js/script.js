// TODO: Add 2 new items to the sidebar called "Register" and "Help".
const ulEl = document.querySelector(".sidebar ul");
// console.log(sidebarEl);
const newEl01 = document.createElement("li");
newEl01.textContent  = "Register";
ulEl.appendChild(newEl01);

const newEl02 = document.createElement("li");
newEl02.textContent  = "Help";
ulEl.appendChild(newEl02);

// TODO: MEGA CHALLENGE: can you add the Help link between Reports and Settings?
ulEl.insertBefore(newEl02, ulEl.children[3]);
