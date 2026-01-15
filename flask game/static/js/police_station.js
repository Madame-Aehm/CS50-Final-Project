const select = document.querySelector("#table");

select.addEventListener("change", (e) => {
  const label = document.querySelector("label[for='string']");
  const input = document.querySelector("#string");
  if (e.target.value === "interviews") {
    label.innerHTML = "Keyword:";
    input.setAttribute("placeholder", "Keyword");
  } else {
    label.innerHTML = "Street:";
    input.setAttribute("placeholder", "Street");
  }
})