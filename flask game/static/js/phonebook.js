const select = document.querySelector("select");

select.addEventListener("change", (e) => {
  const label = document.querySelector("label[for='query']");
  const queryInput = document.querySelector("#query");
  if (e.target.value === "name") {
    label.innerHTML = "Name:";
    queryInput.setAttribute("placeholder", "Name");
  } else {
    label.innerHTML = "Phone Number:";
    queryInput.setAttribute("placeholder", "Phone Number");
  }
})