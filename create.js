arrOfInputs = document.querySelectorAll(".cardInput")
newCardBtn = document.getElementById("newCardBtn")
saveCardBtn = document.getElementById("saveCardsBtn")
placeholdingDiv = document.getElementById("placeholdingDiv")
divOfCards = document.getElementById("divOfCards")
title = document.getElementById("title")




let objOfCards = {}
let overCards = {}
let numOfCards = 0


//-----------------------------------------------------------------------------
//Running
makeNewCard()


















//---------------------------------------------------------------------------------
//Functions

function textF(term, def) {

    term.addEventListener("input", () => {
        term.style.height = "auto"
        term.style.height = term.scrollHeight + "px"

        parent = term.parentNode.parentNode.id
        console.log(parent)
        objOfCards[parent]["term"] = term.value
        console.log(objOfCards[parent]["term"])
    })
    def.addEventListener("input", () => {
        def.style.height = "auto"
        def.style.height = def.scrollHeight + "px"

        parent = term.parentNode.parentNode.id
        console.log(parent)
        objOfCards[parent]["def"] = def.value
        console.log(objOfCards[parent]["def"])
    })

}

title.addEventListener("input", () => {

    objOfCards["title"] = title.value
    console.log(title.value)
})


newCardBtn.onclick = () => {
    makeNewCard()
}



function makeNewCard() {
    numOfCards++

    const newDiv = placeholdingDiv.cloneNode(true)
    newDiv.style.display = "flex"
    newDiv.id = "cardDiv" + numOfCards
    input = newDiv.querySelectorAll(".cardInput")
    textF(input[0], input[1])
    const dltBtn = newDiv.querySelector(".dltBtn")

    divOfCards.appendChild(newDiv)

    if (objOfCards["cardDiv" + numOfCards] == null) {
        objOfCards["cardDiv" + numOfCards] = {
            "at": newDiv,
            "term": "",
            "def": ""
        }
    }
    console.log(objOfCards)

    dltBtn.onclick = () => {
        deleteCard(dltBtn)
    }

}

function deleteCard(btn) {
    parent = btn.parentNode
    console.log(parent.id)
    delete objOfCards[parent.id]
    parent.remove()

    console.log(objOfCards)
}

saveCardBtn.onclick = () => {

    saveCards()
}

async function saveCards() {

    res = await fetch("http://127.0.0.1:8000/send", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify(objOfCards)

    });

    const data = await res.json()
    console.log("Message: ", data)

}