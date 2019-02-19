function avisoContacto()
    {
    alert("EN BREVE NOS PONDREMOS EN CONTACTO CON USTED");
}

function avisoRegistro()
    {
    alert("PROCESANDO EL REGISTRO EN EL SISTEMA");
}


function borrarFormulario(formulario) {

    var elements = formulario.elements;  
    formulario.reset();
  
    for(i=0; i<elements.length; i++) { 
      
      
        tipo = elements[i].tipo.toLowerCase();
  
      switch(tipo) {
        case "nombre":
        case "email":
        case "mensaje":        
          elements[i].value = "";
        default:
          break;
      }
    }
  }