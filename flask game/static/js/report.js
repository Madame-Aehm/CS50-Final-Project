function replaceForm() {
  const won = localStorage.getItem("won");
  if (won === "true") {
    const form = document.querySelector("form");
    form.classList.add("hidden")
    const pageContainer = document.querySelector(".page-container");
    const h1 = document.createElement("h1");
    h1.innerHTML = "🎉🎊 Congratulations, you solved the mystery!"
    const h2 = document.createElement("h2");
    h2.innerHTML = "You correctly identified the thief as Bruce, the city as New York, and the accomplice as Robin!";
    pageContainer.append(h1, h2);
  }
}

replaceForm();