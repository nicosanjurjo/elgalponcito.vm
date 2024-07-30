$(document).ready(function() {
  new DataTable('#myTable', {
    order: [[0, 'desc']]
  });

    $('.habilitar').click(function() {
        $('#numberModal').modal('show');
      });

      $('#saveNumberBtn').click(function() {
        var number = $('#numberInput').val();
        $.ajax({
          url: 'establecer_stock/',
          method: 'POST',
          data: JSON.stringify(number),
          success: function(response) {
            alert('Stock para la venta establecido');
            $('#numberModal').modal('hide');
            $('#stock-actual').text('Masas disponibles\n' + response.new_stock);
          },
          error: function(response) {
            alert('Error al guardar el número.');
          }
        });
      });

      var action = '';

      $('.incrementar').click(function() {
        action = 'incrementar';
        $('#action-type').text('incrementar');
        $('#confirmModal').modal('show');
      });

      $('.decrementar').click(function() {
        action = 'decrementar';
        $('#action-type').text('decrementar');
        $('#confirmModal').modal('show');
      });

      $('#confirmActionBtn').click(function() {
        updateStock(action);
        $('#confirmModal').modal('hide');
      });

      function updateStock(action) {
        $.ajax({
          url: 'update_stock/',
          method: 'POST',
          data: {
            'action': action,
            'csrfmiddlewaretoken': '{{ csrf_token }}'
          },
          success: function(response) {
            $('#stock-actual').text('Masas disponibles\n' + response.new_stock);
          },
          error: function(response) {
            alert('Error al actualizar el stock.');
          }
        });
      }
});