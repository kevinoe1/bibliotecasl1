$(function () {

    $("#id_first_name").keydown(function (e) {
    	key = e.keyCode || e.which;
       	tecla = String.fromCharCode(key).toLowerCase();
       	letras = " áéíóúabcdefghijklmnñopqrstuvwxyz";
       	especiales = "8-37-39-46";

       	tecla_especial = false
       	for(var i in especiales){
            if(key == especiales[i]){
                tecla_especial = true;
                break;
            }
        }

        if(letras.indexOf(tecla)==-1 && !tecla_especial){
            return false;
        }
    });

    $("#id_last_name").keydown(function (e) {
    	key = e.keyCode || e.which;
       	tecla = String.fromCharCode(key).toLowerCase();
       	letras = " áéíóúabcdefghijklmnñopqrstuvwxyz";
       	especiales = "8-37-39-46";

       	tecla_especial = false
       	for(var i in especiales){
            if(key == especiales[i]){
                tecla_especial = true;
                break;
            }
        }

        if(letras.indexOf(tecla)==-1 && !tecla_especial){
            return false;
        }
    });

    $("#id_username").keydown(function (e) {
    	var charCode = (e.which) ? e.which : event.keyCode
    	
    	if ((e.keyCode || e.charCode || e.which)==46){
    			return true;
    	}else{
    		
	         if (charCode > 31 && (charCode < 48 || charCode > 57))
	         {
	         	return false;
	         }else{
	         	return true;
	         }     
    	}
    	
      });


    $('#frmRegistro').on('submit', function(e) {
      $.get('/catalogo/registrar', $(this).serialize(), function (data) {
        
        $.noticeAdd({
            text: 'Usuario registrado',
            stay: false,
            stayTime: 10000,
            type: 'info'
          }); 

      }, 'json');
  });

   $('#ds').on('keypress', function (e) {
         if(e.which === 13){

            //Disable textbox to prevent multiple submit
           window.myviewURL = '/catalogo/#libros';
         }
   });

     // Get the modal
  var modal = document.getElementById('myModal');

  // Get the button that opens the modal
  var btn = document.getElementById("myBtn");

  // Get the <span> element that closes the modal
  var span = document.getElementsByClassName("close")[0];

  // When the user clicks on the button, open the modal 
  btn.onclick = function() {
      modal.style.display = "block";
  }

  // When the user clicks on <span> (x), close the modal
  span.onclick = function() {
      modal.style.display = "none";
  }

  // When the user clicks anywhere outside of the modal, close it
  window.onclick = function(event) {
      if (event.target == modal) {
          modal.style.display = "none";
      }
  }
  
});




