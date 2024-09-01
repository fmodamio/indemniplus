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
