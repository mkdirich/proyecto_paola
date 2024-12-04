
// Referencias a botones y la tabla
    const btnMostrar = document.getElementById('mostrar');
    const btnOcultar = document.getElementById('ocultar');
    const tablaRegistros = document.getElementById('registros-tabla');

// Mostrar registros
    btnMostrar.addEventListener('click', () => {
        if (tablaRegistros) {
            tablaRegistros.style.display = 'block';
        }
    });
// Ocultar registros
    btnOcultar.addEventListener('click', () => {
        if (tablaRegistros) {
            tablaRegistros.style.display = 'none';
        }
    });

// Botón para añadir registro (funcionalidad pendiente)
    document.getElementById('anadir').addEventListener('click', () => {
        alert('Funcionalidad para añadir registro pendiente.');
    });

// Botón para borrar registros (funcionalidad pendiente)
    document.getElementById('borrar').addEventListener('click', () => {
        alert('Funcionalidad para borrar registros pendiente.');
    });


document.getElementById("anadir").addEventListener("click", function () {
    document.getElementById("form-agregar").style.display = "block";
});
document.getElementById("borrar").addEventListener("click", function () {
    document.getElementById("form-agregar").style.display = "none";
});



$('#form-nuevo-registro').submit(function(event) {
    event.preventDefault();

    // Obtener los datos del formulario
    var formData = $(this).serialize();

    // Enviar la solicitud AJAX
    $.ajax({
        url: $(this).attr('action'),
        type: 'POST',
        data: formData,
        success: function(response) {
            // Mostrar mensaje de éxito
            $('#mensaje').text(response.mensaje);

            // Recargar la tabla de registros sin redirigir
            $('#registros-tabla').load(location.href + " #registros-tabla");
        },
        error: function(error) {
            // Mostrar mensaje de error
            $('#mensaje').text(error.responseJSON.mensaje);
        }
    });
});