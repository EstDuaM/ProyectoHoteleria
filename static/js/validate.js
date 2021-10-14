


let boton = document.getElementById("boton");

boton.addEventListener('click', tareaBoton);


function tareaBoton(){
    let caja = document.getElementById("caja");
    let valorCaja = caja.value;
    let sw =  /^[a-zA-Z0-9.!#$%&'*+/=?^_`{|}~-]+@[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)*$/g.test(valorCaja);
    
    if(sw==false){

        alert("Correo no valido");

    }
    else{
        

    }
   
}




let boton2 = document.getElementById("boton2");

boton2.addEventListener('click', tareaBoton2);


function tareaBoton2(){
    let caja2 = document.getElementById("caja2");
    let valorCaja2 = caja2.value;
    let sw =  /^[a-zA-Z0-9.!#$%&'*+/=?^_`{|}~-]+@[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)*$/g.test(valorCaja2);
    
    if(sw==false){

        alert("Correo no valido");

    }
    else{
        

    }
   
}