function encender(color) {
    const colores = ['rojo', 'amarillo', 'verde'];
    colores.forEach(c => {
         const boton = document.querySelector(`.${c}`);
        if (c === color) {
            boton.style.opacity = '1';
            boton.classList.add('encendido');
        } else {
            boton.style.opacity = '0.3';
            boton.classList.remove('encendido');
        }
    });
}

const delay = ms => new Promise(res => setTimeout(res, ms));

const redirigir = async(url,color) =>{
    encender(color);
    await delay(1000);
    window.location.href = url;
}

document.getElementById('id_aceptar_terminos').oninvalid = function(event) {
    event.target.setCustomValidity('Debes aceptar el tratamiento de datos personales para poder enviar tu caso.');
};

document.getElementById('id_aceptar_terminos').oninput = function(event) {
    event.target.setCustomValidity('');  // Restablecer el mensaje de validación personalizado si el usuario marca el checkbox
};
