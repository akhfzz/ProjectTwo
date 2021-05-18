$(document).ready(function(){
	$('#target').hide()
	$("#click").click(function(){
		$("#target").animate({
			height: 'toggle'
		});
	});
});