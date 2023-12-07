//const URL = "http://127.0.0.1:5000/"
const URL = "https://rociogc02.pythonanywhere.com/"

document.getElementById('formulario').addEventListener('submit', function (event) {
    event.preventDefault();

    var formData = new FormData();
    formData.append('codigo', document.getElementById('codigo').value);
    formData.append('descripcion', document.getElementById('descripcion').value);
    formData.append('destino', document.getElementById('destino').value);
    formData.append('duracion', document.getElementById('duracion').value);
    formData.append('alojamiento', document.getElementById('alojamiento').value);
    formData.append('transporte', document.getElementById('transporte').value);
    formData.append('actividades', document.getElementById('actividades').value);
    formData.append('precio', document.getElementById('precio').value);
    formData.append('imagen', document.getElementById('imagenPaquete').files[0]);
    formData.append('proveedor', document.getElementById('proveedorPaquete').value);

    fetch(URL + 'paquetes-turisticos', {
        method: 'POST',
        body: formData
    })
    .then(function (response) {
        if (response.ok) {
            return response.json();
        } else {
            throw new Error('Error al agregar el paquete turístico.');
        }
    })
    .then(function (data) {
        // Si se agregó
        alert('Paquete turístico agregado correctamente.');
    })
    .catch(function (error) {
        // Si hubo algún error
        alert('Error al agregar el paquete turístico.');
        console.error('Error:', error);
    })
    .finally(function () {
        // Limpiar el formulario en ambos casos (éxito o error)
        document.getElementById('codigo').value = "";
        document.getElementById('descripcion').value = "";
        document.getElementById('destino').value = "";
        document.getElementById('duracion').value = "";
        document.getElementById('alojamiento').value = "";
        document.getElementById('transporte').value = "";
        document.getElementById('actividades').value = "";
        document.getElementById('precio').value = "";
        document.getElementById('imagenPaquete').value = "";
        document.getElementById('proveedorPaquete').value = "";
    });
});
