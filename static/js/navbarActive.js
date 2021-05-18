$(function(){
    var current = location.pathname;
    $('.navbar-nav li a').each(function(){
		if($(this).attr('href').indexOf(current) !== -1){
    		$(this).parent().addClass('active');
        }
        if($(this).attr('href').indexOf(current) == -1){
    		$(this).parent().removeClass('active');
        }
    })
})