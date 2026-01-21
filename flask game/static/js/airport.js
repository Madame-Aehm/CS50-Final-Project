const select = document.querySelector("#table");

select.addEventListener("change", (e) => {
  const label = document.querySelector("label[for='string']");
  const stringInput = document.querySelector("#string");
  if (e.target.value === "flight") {
    label.innerHTML = "Flight Number:";
    stringInput.setAttribute("placeholder", "Flight Number");
  } else {
    label.innerHTML = "Passport Number:";
    stringInput.setAttribute("placeholder", "Passport Number");
  }
})