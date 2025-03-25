//Funcionalidad de ScrollView en habilidades tecnicas en el Index de la página

const skillsList = document.getElementById("skills-list");
const scrollUp = document.querySelector(".fa-chevron-up");
const scrollDown = document.querySelector(".fa-chevron-down");

scrollUp.addEventListener("click", function () {
  skillsList.scrollTop -= 50;
});

scrollDown.addEventListener("click", function () {
  skillsList.scrollTop += 50;
});
