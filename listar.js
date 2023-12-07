//const URL = "http://127.0.0.1:5000/"
const URL = "https://rociogc02.pythonanywhere.com/"

// Realizamos la solicitud GET al servidor para obtener todos los paquetes turísticos
fetch(URL + 'paquetes-turisticos')
    .then(function (response) {
        if (response.ok) {
            return response.json();
        } else {
            // Si hubo un error, lanzar explícitamente una excepción
            // para ser "catcheada" más adelante
            throw new Error('Error al obtener los paquetes turísticos.');
        }
    })
    .then(function (data) {
        let tablaPaquetesTuristicos = document.getElementById('tablaPaquetesTuristicos');

        // Iteramos sobre los paquetes turísticos y agregamos filas a la tabla
        for (let paqueteTuristico of data) {
            let fila = document.createElement('tr');
            fila.innerHTML = '<td>' + paqueteTuristico.codigo + '</td>' +
                             '<td>' + paqueteTuristico.descripcion + '</td>' +
                             '<td>' + paqueteTuristico.destino + '</td>' +
                             '<td>' + paqueteTuristico.duracion + '</td>' +
                             '<td>' + paqueteTuristico.alojamiento + '</td>' +
                             '<td>' + paqueteTuristico.transporte + '</td>' +
                             '<td>' + paqueteTuristico.actividades + '</td>' +
                             '<td>' + paqueteTuristico.precio + '</td>' +
                             // Mostrar miniatura de la imagen
                             '<td><img src="https://www.pythonanywhere.com/user/rociogc02/files/home/rociogc02/mysite/img/' + paqueteTuristico.imagen_url + '" alt="Imagen del paquete turístico" style="width: 100px;"></td>' +
                             '<td>' + paqueteTuristico.proveedor + '</td>';

            // Una vez que se crea la fila con el contenido del paquete turístico,
            // se agrega a la tabla utilizando el método appendChild del elemento tablaPaquetesTuristicos.
            tablaPaquetesTuristicos.appendChild(fila);
        }
    })
    .catch(function (error) {
        // En caso de error
        alert('Error al obtener los paquetes turísticos.');
        console.error('Error:', error);
    });
