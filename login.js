var accion = "nuevo";
var idUsuario = 0;

document.addEventListener("DOMContentLoaded", event => {
    frmUsuarios.addEventListener("submit", e => {
        e.preventDefault();
        guardarUsuario();
    });
    obtenerUsuarios();
});

async function guardarUsuario() {
    let datos = {
        accion,
        idUsuario,
        tipo: "usuario",
        usuario: txtUsuario.value,
        clave: txtClave.value,
        nombre: txtNombre.value,
        direccion: txtDireccion.value,
        telefono: txtTelefono.value
    };

    let response = await fetch("/usuarios", {
        method: "POST",
        body: JSON.stringify(datos),
    });

    let respuesta = await response.json();

    if (respuesta.msg != "ok") {
        alert(`Error al procesar usuario: ${respuesta.msg}`);
        return;
    }

    limpiarFormulario();
    obtenerUsuarios();
}

function limpiarFormulario() {
    accion = "nuevo";
    idUsuario = 0;
    txtUsuario.value = "";
    txtClave.value = "";
    txtNombre.value = "";
    txtDireccion.value = "";
    txtTelefono.value = "";
}

async function obtenerUsuarios() {
    let response = await fetch("/usuarios");
    let usuarios = await response.json();
    mostrarDatosUsuarios(usuarios);
}

function mostrarDatosUsuarios(usuarios) {
    let filas = "";
    usuarios.forEach(usuario => {
        filas += `
            <tr onclick='mostrarUsuario(${JSON.stringify(usuario)})'>
                <td>${usuario.usuario}</td>
                <td>${usuario.nombre}</td>
                <td>${usuario.direccion}</td>
                <td>${usuario.telefono}</td>
                <td><button onclick='eliminarUsuario(${JSON.stringify(usuario)}, event)' class="btn btn-danger btn-sm">ELIMINAR</button></td>
            </tr>
        `;
    });
    tblUsuarios.innerHTML = filas;
}

function mostrarUsuario(usuario) {
    accion = "modificar";
    idUsuario = usuario.idUsuario;
    txtUsuario.value = usuario.usuario;
    txtClave.value = usuario.clave;
    txtNombre.value = usuario.nombre;
    txtDireccion.value = usuario.direccion;
    txtTelefono.value = usuario.telefono;
}

function eliminarUsuario(usuario, event) {
    event.preventDefault();
    if (confirm(`¿Seguro de eliminar a ${usuario.nombre}?`)) {
        idUsuario = usuario.idUsuario;
        accion = "eliminar";
        guardarUsuario();
    }
}
