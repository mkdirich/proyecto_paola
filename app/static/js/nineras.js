
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
