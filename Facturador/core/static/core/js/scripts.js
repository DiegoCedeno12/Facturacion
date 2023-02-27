window.addEventListener("load", () => {
    const contenedor_loader = document.querySelector(".contenedor_loader")
    contenedor_loader.style.opacity = 0
    contenedor_loader.style.visibility = "hidden"
})
/* API Token
 Pm5qbQfVT4oPPrm3W1F7OL4b5m2YBbknl3xZL1Q3 */
class modulo {
    getMod11(num) {
        const arr = num.split('');
        let array = JSON.parse(`[${arr}]`);
        var sum = 0;
        var factor = 3;
        for (var i = 0; i < array.length; i++) {
            sum += (array[i] * factor);
            if (factor == 2) {
                factor = 7;
            } else {
                factor--;
            }
        }
        var dv = 11 - (sum % 11);
        if (dv == 10) {
            return 1;
        }
        if (dv == 11) {
            return 0;
        }
        return dv;
    }
}
var fechacreada = null;
let date = new Date()
let day = date.getDate()
let month = date.getMonth() + 1
let year = date.getFullYear()


fechacreada = `0${day}${month}${year}`

document.getElementById('FechaEmision').value = obtenerFechaEcuador();
function obtenerFechaEcuador() {
    // Obtener la fecha y hora actual en UTC
    let fechaUTC = new Date();

    // Obtener la diferencia horaria en minutos entre UTC y Ecuador
    let diferenciaHoraria = -300; // UTC-5 (horario de Ecuador)
    let diferenciaMinutos = fechaUTC.getTimezoneOffset() + diferenciaHoraria;

    // Crear un nuevo objeto Date con la hora y fecha actual en Ecuador
    let fechaEcuador = new Date(fechaUTC.getTime() + diferenciaMinutos * 60000);

    let dia = fechaEcuador.getDate().toString().padStart(2, '0');
    let mes = (fechaEcuador.getMonth() + 1).toString().padStart(2, '0');
    let anio = fechaEcuador.getFullYear().toString();
    fechacreada = `${dia}${mes}${anio}`;
    // Devolver la fecha y hora en formato legible
    return fechaEcuador.toISOString().slice(0, 10);
}

dig = new modulo();
let inputTipoComprobantes = document.getElementById('inputTipoComprobantes');
let inputTipoAmbiente = document.getElementById('inputTipoAmbiente');
let inputRuc = document.getElementById('inputRuc');
let inputSerie = document.getElementById('inputSerie');
let inputNumComprobante = document.getElementById('inputNumComprobante');
let inputCodigoNumerico = document.getElementById('inputCodigoNumerico');
let inputTipoEmision = document.getElementById('inputTipoEmision');

var autorizacion = null;
console.log(inputTipoComprobantes.value);
inputSerie.oninput = function () {
    if (inputSerie.value.length == 6) {
        console.log(inputTipoAmbiente.value);
        inputNumComprobante.oninput = function () {
            if (inputNumComprobante.value.length == 9) {
                inputCodigoNumerico.oninput = function () {
                    if (inputCodigoNumerico.value.length == 8) {
                        autorizacion = `${fechacreada}0${inputTipoComprobantes.value}${inputRuc.value}${inputTipoAmbiente.value}${inputSerie.value}${inputNumComprobante.value}${inputCodigoNumerico.value}${inputTipoEmision.value}`
                        console.log(dig.getMod11(autorizacion))
                        autorizacion += `${dig.getMod11(autorizacion)}`
                        document.getElementById('inputDigitoVerificador').value = autorizacion;
                    }
                }
            }
        }
    }
}