addEventControllers();
buildClueList();

function addEventControllers () {
    const clueControl = document.querySelector("#clue-control");
    const closeModelButton = document.querySelector("#close-model");
    const clueModel = document.querySelector("#clue-model");
    const modelBody = clueModel.querySelector(".model-body");

    clueControl.addEventListener("click", () => {
        clueModel.classList.remove("hidden");
        clueControl.classList.add("hidden");
    });

    function closeModel() {
        clueModel.classList.add("hidden");
        clueControl.classList.remove("hidden");
    }
    closeModelButton.addEventListener("click", closeModel);
    clueModel.addEventListener("click", closeModel);
    
    modelBody.addEventListener("click", (e) => e.stopPropagation())
}

function addToClues(category, clue) {
    let list = localStorage.getItem(category);
    if (list) {
        list = JSON.parse(list);
        if (list.find(c => c === clue)) return alert("clue already saved");
        list.push(clue);
        localStorage.setItem(category, JSON.stringify(list));
    } else {
        localStorage.setItem(category, JSON.stringify([clue]));
    }
    buildClueList();
    alert("clue added");
}

function removeFromClues(category, clue) {
    let list = localStorage.getItem(category);
    if (list) {
        list = JSON.parse(list).filter(e => e !== clue);
        localStorage.setItem(category, JSON.stringify(list));
        buildClueList();
    } else alert("Problem removing clue..");
}

function buildClueList() {
    const modelContent = document.querySelector(".model-content");
    modelContent.innerHTML = `<ul id="clue-list">
                        <li>
                            The theft took place on July 28, 2024 and that it took place on Humphrey Street.
                            Maybe start by checking for reports in the police station?
                        </li>
                    </ul>`;
    const categories = Object.keys(localStorage);
    categories.forEach(cat => {
        const ul = document.createElement("ul");
        const title = document.createElement("h3");
        title.innerHTML = cat;
        const items = JSON.parse(localStorage.getItem(cat));
        items.forEach(i => {
            const li = document.createElement("li");
            const clue = document.createElement("span");
            clue.innerHTML = i + "   ";
            const button = document.createElement("button");
            button.innerHTML = "x";
            button.title = "Remove from clues";
            button.addEventListener("click", () => removeFromClues(cat, i));
            li.append(clue, button);
            ul.appendChild(li);
        })
        modelContent.append(title, ul);
    })
}