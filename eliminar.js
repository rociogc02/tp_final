//const URL = "http://127.0.0.1:5000/"
const URL = "https://rociogc02.pythonanywhere.com/"

const app = Vue.createApp({
    data() {
        return {
            paquetes: []  
        };
    },
    methods: {
        obtenerPaquetes() {
            fetch(URL + 'paquetes-turisticos')
                .then(response => {
                    if (response.ok) {
                        return response.json();
                    }
                })
                .then(data => {
                    this.paquetes = data;
                })
                .catch(error => {
                    console.log('Error:', error);
                    alert('Error al obtener los paquetes turísticos.');
                });
        },
        eliminarPaquete(codigo) {
            if (confirm('¿Estás seguro de que quieres eliminar este paquete turístico?')) {
                fetch(URL + `paquetes-turisticos/${codigo}`, { method: 'DELETE' })
                    .then(response => {
                        if (response.ok) {
                            this.paquetes = this.paquetes.filter(paquete => paquete.codigo !== codigo);
                            alert('Paquete turístico eliminado correctamente.');
                        }
                    })
                    .catch(error => {
                        alert(error.message);
                    });
            }
        }
    },
    mounted() {
        this.obtenerPaquetes();
    }
});

app.mount('body');
