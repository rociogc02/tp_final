//const URL = "http://127.0.0.1:5000/"
const URL = "https://rociogc02.pythonanywhere.com/"

const app = Vue.createApp({
    data() {
        return {
            codigo: '',
            descripcion: '',
            destino: '',
            duracion: '',
            alojamiento: '',
            transporte: '',
            actividades: '',
            precio: '',
            proveedor: '',
            imagen_url: '',
            imagenSeleccionada: null,
            imagenUrlTemp: null,
            mostrarDatosPaqueteTuristico: false,
        };
    },
    methods: {
        obtenerPaqueteTuristico() {
            fetch(URL + 'paquetes-turisticos/' + this.codigo)
                .then(response => {
                    if (response.ok) {
                        return response.json()
                    } else {
                        throw new Error('Error al obtener los datos del paquete turístico.');
                    }
                })
                .then(data => {
                    this.codigo = data.codigo;
                    this.descripcion = data.descripcion;
                    this.destino = data.destino;
                    this.duracion = data.duracion;
                    this.alojamiento = data.alojamiento;
                    this.transporte = data.transporte;
                    this.actividades = data.actividades;
                    this.precio = data.precio;
                    this.proveedor = data.proveedor;
                    this.imagen_url = data.imagen_url;
                    this.mostrarDatosPaqueteTuristico = true;
                })
                .catch(error => {
                    console.log(error);
                    alert('Código no encontrado.');
                })
        },
        seleccionarImagen(event) {
            const file = event.target.files[0];
            this.imagenSeleccionada = file;
            this.imagenUrlTemp = URL.createObjectURL(file);
        },
        guardarCambiosPaqueteTuristico() {
            const formData = new FormData();
            formData.append('descripcion', this.descripcion);
            formData.append('destino', this.destino);
            formData.append('duracion', this.duracion);
            formData.append('alojamiento', this.alojamiento);
            formData.append('transporte', this.transporte);
            formData.append('actividades', this.actividades);
            formData.append('precio', this.precio);
            formData.append('proveedor', this.proveedor);
            if (this.imagenSeleccionada) {
                formData.append('imagen', this.imagenSeleccionada, this.imagenSeleccionada.name);
            }
            fetch(URL + 'paquetes-turisticos/' + this.codigo, {
                method: 'PUT',
                body: formData,
            })
            .then(response => {
                if (response.ok) {
                    return response.json();
                } else {
                    throw new Error('Error al guardar los cambios del paquete turístico.');
                }
            })
            .then(data => {
                alert('Paquete turístico actualizado correctamente.');
                this.limpiarFormulario();
            })
            .catch(error => {
                console.error('Error:', error);
                alert('Error al actualizar el paquete turístico.');
            });
        },
        limpiarFormulario() {
            this.codigo = '';
            this.descripcion = '';
            this.destino = '';
            this.duracion = '';
            this.alojamiento = '';
            this.transporte = '';
            this.actividades = '';
            this.precio = '';
            this.proveedor = '';
            this.imagen_url = '';
            this.imagenSeleccionada = null;
            this.imagenUrlTemp = null;
            this.mostrarDatosPaqueteTuristico = false;
        },
    }
});

app.mount('#app');
