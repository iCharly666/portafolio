// Calculadora de edpi en projects.html
function calcularEdpi() {
  var dpi = document.getElementById("dpiInput").value;
  var sensibilidad = document.getElementById("sensibilidadInput").value;
  var resultadoDiv = document.getElementById("resultado");

  if (dpi && sensibilidad) {
    var edpi = dpi * sensibilidad;
    resultadoDiv.innerHTML = "eDPI: " + edpi;
    resultadoDiv.classList.remove("d-none");
  } else {
    resultadoDiv.innerHTML = "Por favor, ingrese los valores de DPI y sensibilidad.";
    resultadoDiv.classList.remove("d-none");
  }
}

function mostrarEdpiInfo() {
  var edpiInfoDiv = document.getElementById("edpiInfo");
  edpiInfoDiv.classList.toggle("d-none");
}


// Sensitivity calculator
function convertirSensibilidad() {
  var juegoA = document.getElementById("juegoAInput").value;
  var sensibilidadJuegoA = document.getElementById("sensibilidadJuegoAInput").value;
  var juegoB = document.getElementById("juegoBInput").value;
  var resultadoDiv = document.getElementById("resultadoConversor");

  var sensibilidades = {
    csgo: 1,
    apex: 1,
    quake: 1,
    tf2: 1,
    titanfall2: 1,
    eft: 0.1760,
    cod: 3.333,
    fortnite: 0.038495,
    overwatch: 3.333333,
    valorant: 0.3145,
    paladins: 2.4
  };

  if (sensibilidadJuegoA && sensibilidades[juegoA] && sensibilidades[juegoB]) {
    var sensibilidadJuegoB = (sensibilidadJuegoA * sensibilidades[juegoA]) / sensibilidades[juegoB];
    resultadoDiv.innerHTML = "Sensibilidad en " + juegoB.toUpperCase() + ": " + sensibilidadJuegoB.toFixed(2);
    resultadoDiv.classList.remove("d-none");
  } else {
    resultadoDiv.innerHTML = "Por favor, ingrese los valores de sensibilidad y seleccione los juegos.";
    resultadoDiv.classList.remove("d-none");
  }
}
