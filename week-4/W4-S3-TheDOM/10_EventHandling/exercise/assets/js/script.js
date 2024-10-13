// 1. use document.getElementById to select the searchTerm Button
const searchTermEl = document.getElementById("searchTerm");
// 2. use document.getElementById to select the searchButton Button
const searchButtonEl = document.getElementById("searchButton");

// 3. add an event listener to the searchButton that calls the search function when clicked
searchButtonEl.addEventListener("click", () => {
  // 4. use the value property of the searchInput to get the search term
  const term = searchTermEl.value;
  // 5. select the searches div using document.getElementById
  const searchesEl = document.getElementById("searches");
  // 6. create a new li element using document.createElement
  const newEntryEl = document.createElement("li");
  // 7. set the innerHTML of the new paragraph to the search term
  newEntryEl.innerHTML = term;
  // 8. append the new paragraph to the searches div
  searchesEl.appendChild(newEntryEl);
  searchTermEl.value = "";
});
