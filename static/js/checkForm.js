$(document).ready(function(){
	var email, username, password, name, mail, psw, regex;
	email = $('#emailHelp');
	username = $('#username');
	password = $('#password');
	$(email).hide(); $(username).hide(); $(password).hide();
	$('button').click(function(){
		$(email).toggle(); $(username).toggle(); $(password).toggle()
		name = $('#exampleInputEmail1').val();
		mail = $('inputUserName').val();
		psw = $('exampleInputPassword1').val();
		regex = /^[A-Z][a-z0-9_-]{5,15}$/;
		if(name != "" && mail != "" && psw != ""){
			if(!regex.test(name)){
				$(password).hide();
				$(email).hide();
				$(username).show();
			}
		}else{
			$(email).show(); $(username).show(); $(password).show();
		}
	});
});