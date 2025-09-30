var accion = "nuevo",
    idProfesor = 0;

document.addEventListener("DOMContentLoaded", event => { 
    frmProfesores.addEventListener("submit", e => {
        e.preventDefault();
        guardarProfesores();
    });
    obtenerProfesores();
});

async function guardarProfesores(){
    let datos = {
        accion,
        idProfesor,
        codigo: txtCodigoProfesor.value,
        nombre: txtNombreProfesor.value,
        dui: txtDuiProfesor.value,
        telefono: txtTelefonoProfesor.value,
        direccion: txtDireccionProfesor.value,
        correo: txtCorreoProfesor.value
    };

    let response = await fetch("/profesores", {
        method: "POST",
        body: JSON.stringify(datos),
    }), 
    respuesta = await response.json();

    if(respuesta.msg != "ok"){
        alertify.error(`Error al procesar profesor: ${respuesta}`);
        return;
    }
    limpiarFormulario();
    obtenerProfesores();
}

function limpiarFormulario(){
    accion = "nuevo";
    idProfesor = 0;
    txtCodigoProfesor.value = "";
    txtNombreProfesor.value = "";
    txtDuiProfesor.value = "";
    txtTelefonoProfesor.value = "";
    txtDireccionProfesor.value = "";
    txtCorreoProfesor.value = "";
}

async function obtenerProfesores(){
    let response = await fetch("/profesores"), 
        respuesta = await response.json();
    mostrarDatosProfesores(respuesta);
}

function mostrarDatosProfesores(profesores){
    let filas = "";
    profesores.forEach(profesor => {
        filas += `
            <tr onClick='mostrarProfesor(${ JSON.stringify(profesor) })'>
                <td>${profesor.codigo}</td>
                <td>${profesor.nombre}</td>
                <td>${profesor.dui}</td>
                <td>${profesor.telefono}</td>
                <td>${profesor.direccion}</td>
                <td>${profesor.correo}</td>
                <td>
                    <button onClick='eliminarProfesor(${ JSON.stringify(profesor) }, event)' class="btn btn-danger btn-sm">ELIMINAR</button>
                </td>
            </tr>
        `;
    });
    tblProfesores.innerHTML = filas;
}

function mostrarProfesor(profesor){
    accion = "modificar";
    idProfesor = profesor.idProfesor;
    txtCodigoProfesor.value = profesor.codigo;
    txtNombreProfesor.value = profesor.nombre;
    txtDuiProfesor.value = profesor.dui;
    txtTelefonoProfesor.value = profesor.telefono;
    txtDireccionProfesor.value = profesor.direccion;
    txtCorreoProfesor.value = profesor.correo;
}

function eliminarProfesor(profesor, event){
    event.preventDefault();

    if(confirm(`¿Está seguro de eliminar a ${profesor.nombre}?`)){
        idProfesor = profesor.idProfesor;
        accion = "eliminar";
        guardarProfesores();
    }
}
