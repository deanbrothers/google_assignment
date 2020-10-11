$(document).ready(function(){

    $("#myModal").modal('show');
});

$('#order').click(function(){
    $("#orderModal").modal('show');
})

$('#fortuneSave').submit(async function(event){
	event.preventDefault();
	let fortune_option=$('#fortuneOption').val();
	let fortune_id=$('#fortuneID').val();
	let csrf = $('#csrfToken').val()
    let data = {
        'fortune_id':fortune_id,
		'fortune_option':fortune_option,
    };
    await getData('/savefortune/', 'post', data, csrf);

});

var getData = async(request_url, method, data, csrf_token) =>{
	header = {'X-CSRFToken':csrf_token}
	console.log(header);
	$("#myModal").modal('hide');
	await $.ajax({
		url: request_url,
		type: method,
		dataType: "json",
		data:data,
		headers:header,
		//contentType: "application/json",
		success: function(response) {
			console.log(response);
			$('#successModal').modal('show');
		},
		error:function(error) {
			
			$('#failureModal').modal('show');
		}
	  });	
}


$('#orderForm').submit(async function(event){
	event.preventDefault();
	$("#orderModal").modal('hide');
	let data = $('#orderForm').serialize();
	let csrf = $('#csrfToken').val()
    await getData('/saveorder/', 'post', data, csrf);

});

$('#dispalyCookie').click(function(event) {
	event.preventDefault();
	$('.back').show();
	$('.footer-content').show();
	$('.front').hide();
	$('.cookei-header').hide();
	
});
