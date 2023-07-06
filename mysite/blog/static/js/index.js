//Funcionalidad Para ScrollView en el Index de la página

const skillsList = document.getElementById("skills-list");
const scrollUp = document.querySelector(".scroll-icon:not(.down)");
const scrollDown = document.querySelector(".scroll-icon.down");

scrollUp.addEventListener("click", function () {
    skillsList.scrollTop -= 50;
});

scrollDown.addEventListener("click", function () {
    skillsList.scrollTop += 50;
});