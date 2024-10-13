const liEls = document.querySelectorAll("li");
for (element of liEls) {
    element.style.color = "blue";
}

const h2El = document.querySelector(".widget h2");
if (h2El) {
    h2El.textContent = "Reports";
}

const pEls = document.querySelectorAll(".widget p");
if (pEls.length >= 3) {
    pEls[2].textContent = "Optimise performance metrics here";
}
