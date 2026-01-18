const select = document.querySelector("#table");

select.addEventListener("change", (e) => {
  const label = document.querySelector("label[for='string']");
  const stringInput = document.querySelector("#string");
  const dateInput = document.querySelector("#date-input");
  dateInput.classList.remove("hidden")
  if (e.target.value === "interviews") {
    label.innerHTML = "Keyword:";
    stringInput.setAttribute("placeholder", "Keyword");
  } else if (e.target.value === "lp_lookup") {
    label.innerHTML = "License Plate:";
    stringInput.setAttribute("placeholder", "License Plate");
    dateInput.classList.add("hidden")
  } else {
    label.innerHTML = "Street:";
    stringInput.setAttribute("placeholder", "Street");
  }
})