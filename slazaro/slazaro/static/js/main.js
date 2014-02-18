$(window).load(function(){
	$('div.slider').fractionSlider({
		'fullWidth'         : true,
		'controls'          : true, 
		'pager'             : true,
		'responsive'        : true,
		'dimensions'        : "1280,435",
	    'increase'          : false,
		'pauseOnHover'      : false,
		'slideEndAnimation' : true,
		'timeout'           : 4000,
	});

});