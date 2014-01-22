$(window).load(function(){
	$('div.slider').fractionSlider({
		'fullWidth'         : true,
		'controls'          : true, 
		'pager'             : true,
		'responsive'        : true,
		'dimensions'        : "1000,435",
	    'increase'          : false,
		'pauseOnHover'      : true,
		'slideEndAnimation' : true,
		'timeout'           : 4000,
	});

});