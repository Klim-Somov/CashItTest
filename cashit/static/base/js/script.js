$( document ).ready(function() {
	$('.menu-item').click(function(){
		$('.menu-item').removeClass('menu-active');
		$(this).addClass('menu-active');
	});

	$( ".header .menu-item" ).hover(
	  function() {
	    $( this ).find('.menu-two').fadeIn(200);
	  }, function() {
		$(this).removeClass('menu-hover');  	
	    $( this ).find('.menu-two').fadeOut(200);
	  }
	);


	var scrollTop = $(window).scrollTop();
	$(window).scroll(function() {
	    if($(window).scrollTop() > scrollTop){
	        $('.header, .header-none').addClass('down-header');
	        scrollTop = $(window).scrollTop();
	    }
	    if($(window).scrollTop() == 0){
	        $('.header, .header-none').removeClass('down-header');
	        scrollTop = $(window).scrollTop();
	    }
	});

	$('.have-two').click(function(){
		$(this).find('.menu-two').slideToggle(200);
		$(this).find('.two-icon').slideToggle(0);
	});

	$('.bars').click(function () {
		$('.menu-none-block').fadeIn(300);
	});
	$('.close-none').click(function () {
		$('.menu-none-block').fadeOut(300);
	});


	$(function(){
		$(".info_message").delay(2000).slideUp(300);
	});
});


