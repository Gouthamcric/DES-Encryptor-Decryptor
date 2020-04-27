$(document).ready(function () {
     
        $('#submit').click(function () {

        var message=document.getElementById("message").value;
        var key=document.getElementById("key").value;
        var func=document.getElementById("function").value;
//alert(message+" "+key+" "+func);


        $.ajax({
            type: 'POST',
            url: '/process',
            data: {message:message,key:key,func:func},
          
            success: function (data) {
      
                $('#result').text('Result: ' + data);
                
            }
        });
    event.preventDefault();
    });
    
});

