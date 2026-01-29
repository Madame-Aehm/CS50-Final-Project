addModelControllers();
buildClueList();
noteController();
updateAllClueButtons();

function addModelControllers () {
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

function addToClues(button) {
    const category = button.getAttribute("data-category")
    const clue = button.getAttribute("data-clue")
    let list = localStorage.getItem(category);
    if (list) {
        list = JSON.parse(list);
        if (list.find(c => c === clue)) {
            updateClueButtonForClue(category, clue);
            return;
        }
        list.push(clue);
        localStorage.setItem(category, JSON.stringify(list));
    } else {
        localStorage.setItem(category, JSON.stringify([clue]));
    }
    buildClueList();
    updateClueButtonForClue(category, clue);
}

function removeFromClues(category, clue) {
    let list = localStorage.getItem(category);
    if (list) {
        list = JSON.parse(list).filter(e => e !== clue);
        if (list.length === 0) localStorage.removeItem(category);
        else localStorage.setItem(category, JSON.stringify(list));
        buildClueList();
        updateClueButtonForClue(category, clue);
    }
}

function buildClueList() {
    const modelContent = document.querySelector("#db-clues");
    modelContent.innerHTML = `<ul>
                        <li class="pixel-box list-item">
                            <p>
                                The theft took place on July 28, 2024 on Humphrey Street.
                                Maybe start by checking for reports in the police station?
                            </p>
                        </li>
                    </ul>`;
    const categories = Object.keys(localStorage).filter(
        key => key && key !== "user-notes" && key !== "won"
    );
    console.log(categories)
    categories.forEach(cat => {
        const ul = document.createElement("ul");
        const title = document.createElement("h2");
        title.innerHTML = cat;
        const items = JSON.parse(localStorage.getItem(cat));
        const divider = document.createElement("hr");
        items.forEach(i => {
            const li = document.createElement("li");
            li.classList.add("pixel-box", "list-item");
            ul.appendChild(li);
            const p = document.createElement("p");
            p.innerHTML = i;
            const button = document.createElement("button");
            button.classList.add("pixel-box", "button-icon")
            button.title = "Forget clue";
            button.addEventListener("click", () => removeFromClues(cat, i));
            const icon = document.createElement("img");
            icon.src = trashIconGlobalPath;
            icon.alt = "A pixel art image of a trash can";
            button.appendChild(icon);
            li.append(button, p);
        })
        modelContent.append(title, divider, ul);
    })
}


function noteController() {
    const notes = document.querySelector("#user-notes");
    const savedNotes = localStorage.getItem("user-notes");
    if (savedNotes) {
        notes.value = savedNotes;
    }
    notes.addEventListener("keyup", () => {
        localStorage.setItem("user-notes", notes.value);
    });
}

function isClueSaved(category, clue) {
    const list = localStorage.getItem(category);
    if (!list) return false;
    const parsedList = JSON.parse(list);
    return parsedList.find(c => c === clue) !== undefined;
}

function updateClueButtonState(button, category, clue) {
    if (!button || !category || !clue) return;
    const saved = isClueSaved(category, clue);
    const icon = button.querySelector("img");
    if (saved) {
        button.classList.add("clue-button-saved");
        button.title = "Clue already saved";
        icon.src = "/static/assets/icon-search-small.png";
        icon.alt = "A pixel art image of a magnifying glass";
    } else {
        button.classList.remove("clue-button-saved");
        button.title = "Save clue";
        icon.src = "/static/assets/icon-add+.png";
        icon.alt = "A plus symbol"
    }
}

function updateClueButtonForClue(category, clue) {
    const buttons = document.querySelectorAll('[data-category][data-clue]');
    buttons.forEach(button => {
        const buttonCategory = button.getAttribute("data-category");
        const buttonClue = button.getAttribute("data-clue");
        if (buttonCategory === category && buttonClue === clue) {
            updateClueButtonState(button, category, clue);
        }
    });
}

function updateAllClueButtons() {
    const buttons = document.querySelectorAll('[data-category][data-clue]');
    buttons.forEach(button => {
        const category = button.getAttribute("data-category");
        const clue = button.getAttribute("data-clue");
        updateClueButtonState(button, category, clue);
    });
}