function ajaxLogin(){
	var xmlhttp;
	xmlhttp = new XMLHttpRequest();
	xmlhttp.onreadystatechange = function(){
		if(this.readyState == 4 && this.status == 200){
			document.getElementById('myCarousel').innerHTML = this.responseText;
		}
	};
	xmlhttp.open('GET', '/login', true);
	xmlhttp.send();
};
function ajaxRegister(){
	var xmlhttp;
	xmlhttp = new XMLHttpRequest();
	xmlhttp.onreadystatechange = function(){
		if(this.readyState == 4 && this.status == 200){
			document.getElementById('myCarousel').innerHTML = this.responseText;
		}
	};
	xmlhttp.open('GET', '/register', true);
	xmlhttp.send();
};
function myAjax(){
	var xhttp;
	xhttp = new XMLHttpRequest();
	xhttp.onreadystatechange = function(){
		if(this.readyState == 4 && this.status == 200){
			document.getElementById('demo').innerHTML = this.response;
		}
	};
	xhttp.open('GET', '/update',true);
	xhttp.send();
};
// function searchStr(ele, str, search, originalStr){
// 	if(search.length > 0){
// 		let regex = new RegExp(search, 'g');
// 		newString = str.replace(regex, "<span class='highlight'>"+ search + "</span>")
// 		ele.innerHTML = newString;
// 	}else{
// 		ele.innerHTML = originalStr;
// 	}
// }
// var content = document.getElementsByClassName('kotakPublik');
// var searchInput = document.getElementsByClassName('form-control mr-sm-2');
// var searchBtn = document.getElementsByClassName('btn');

// let originalContent = content.innerText

// searchBtn.addEventListener("click", searchStr(content, content.innerText, searchInput.value, originalContent));
