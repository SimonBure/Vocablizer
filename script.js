function lancerTraining() {

    let score = 0
    let checkedRadioButton = document.querySelector('input[type="radio"]:checked');
    let i = 0;
    let motUtilisateur;
    initPopupPartage();
    
    console.log(checkedRadioButton)
    let databaseChoisis = choisirLangue(checkedRadioButton.value)
    afficherProposition(i, databaseChoisis)


    document.querySelectorAll("input[name='optionLangue']").forEach((btn) => {btn.addEventListener("change", (event) => {
        console.log(event)
        checkedRadioButton = document.querySelector('input[type="radio"]:checked');
        databaseChoisis = choisirLangue(checkedRadioButton.value);
        afficherProposition(i, databaseChoisis)

        });
    });


    let boutonVallider = document.getElementById("btnValliderMot")
    boutonVallider.addEventListener("click", () => {
        motUtilisateur = document.getElementById("inputEcriture").value
        score = updateScore(motUtilisateur, databaseChoisis[i], score);
        afficherResultat(score, databaseChoisis);
        i++;
        afficherProposition(i, databaseChoisis)
        if (i >= databaseChoisis.length) {
            boutonVallider.disabled = true
        };
        textZoneSaisie = document.getElementById("inputEcriture").value = "";
    });

    let boutonPartager = document.querySelector("form")
    boutonPartager.addEventListener("submit", (event) => {
        event.preventDefault();
        let nom = document.getElementById("nom").value;
        let email = document.getElementById("email").value;
        if (verifierForm(nom, email) === true) {
            afficherEmail(nom, email, score)
            console.log("Email envoyé")
        } else {
            console.log("Erreur lors de l'envoi de l'email")
        }
    });
};

function gererFormulaire() {
    pass
}


function verifierForm(nom, email) {
    isNomValide = verifierNom(nom);
    isEmailValide = verifierEmail(email);
    console.log(isNomValide);
    console.log(isEmailValide);
    return (isNomValide && isEmailValide);
}


function verifierNom(nom) {
    if (nom.trim().length < 3) {
        alert("Nom trop court.");
        return false;
    } else {
        return true;
    }
};

function verifierEmail(email) {
    const regexEmailCommand = /^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$/;
    let regexEmail = new RegExp(regexEmailCommand);
    let testEmailRegex = regexEmail.test(email);
    if (testEmailRegex === false) {
        alert("Mauvais format d'email.");
        return false;
    } else {
        return true;
    }
}


function afficherEmail(nom, email, score) {
    let mailto = `mailto:${email}?subject=Partage du score Azertype&body=Salut, je suis ${nom} et je viens de réaliser le score ${score} sur le site d'Azertype !`
    location.href = mailto;
};

function updateScore(wordWriten, wordToFind, score) {
    if (wordWriten === wordToFind) {
        console.log("GG")
        score++
    } else {
        console.log("Faute de frappe. Lost.")
    }
    return score;
}

function afficherProposition(index, database) {
    motAfficher = document.querySelector(".zoneProposition span")
    if (index < database.length) {
        motAfficher.innerText = database[index]
    } else {
        motAfficher.innerText = "Fin du training."
    }
}

function choisirLangue(langue) {
    console.log(langue)
    if (langue === "fr") {
        console.log("Langue : Français")
        database = database_fr
    }
    else {
        console.log("Langue : Anglais")
        database = database_en
    }
    return database
}

function afficherResultat(score, database) {
    let scoreText = document.querySelector(".zoneResultat span")
    scoreText.innerText = `${score}/${database.length}`
}
//pop up
{
    function afficherPopup() {
        let popup = document.querySelector(".popupBackground")
        popup.classList.add("active")
        console.log("afficher")    
    };

    function cacherPopup() {
        let popup = document.querySelector(".popupBackground")
        popup.classList.remove("active")
        console.log("fermer")
    }

    function initPopupPartage() {
        let btnPartager = document.querySelector(".zonePartage button")
        btnPartager.addEventListener("click", afficherPopup)
        let popupPartage = document.getElementById("btnEnvoyerMail")
        popupPartage.addEventListener("click", cacherPopup)

    }
}
