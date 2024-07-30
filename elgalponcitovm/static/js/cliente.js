$(document).ready(function() {

    window.vaciarCarrito = function(){
        localStorage.clear()
        alert("Se eliminaron todos los productos del pedido, puedes volver a seleccionar");
    }

    window.agregarProducto = function(id, nombre, precio, masasxunidad) {
        // Obtener los productos existentes del Local Storage
        let productos = JSON.parse(localStorage.getItem('productos')) || [];
        // Crear un nuevo objeto de producto
        let nuevoProducto = {
            id: id,
            nombre: nombre,
            precio: precio,
        };
        // Agregar el nuevo producto a la lista
        productos.push(nuevoProducto);

        // Guardar la lista actualizada en el Local Storage
        localStorage.setItem('productos', JSON.stringify(productos));
        let masasActuales = parseInt(localStorage.getItem('masas')) || 0;

        // Sumar el nuevo valor al existente, asegurando que ambos son enteros
        masasActuales += parseInt(masasxunidad);
    
        // Guardar el valor actualizado en el Local Storage
        localStorage.setItem('masas', masasActuales);
        // Opcional: Mostrar un mensaje de confirmación
        alert("Se agrego una unidad de " + nombre + " al pedido");
    }


});
