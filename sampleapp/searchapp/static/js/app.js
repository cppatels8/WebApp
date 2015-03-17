$(document).ready(function(){

	// Can be used to get form data 
	function getFromData(className){
		var data = $(className).serializeArray(),
			formData = {};
		$.map(data, function(x) {
			formData[x.name] = x.value;
		});
		return formData;
	}
	
	$('.mp-data-table').DataTable();

	$(".delete-data").click( function(e){
		/*
		 * Write code to delete mp data. 
		 * */
	});
	
	$(".edit-mp-data").click( function(e){
		/*
		 * Write code to edit mp data. 
		 * */
	});
	
	$('.submit-mp-data').click(function(e) {
		e.preventDefault();
		console.log(getFromData('.create-mp-data-form'));
	    /*
	     * Make a ajax call to rest api to save data
	     * 
	     * */
	});
	
	$(".filter-results").submit(function(e) {
		e.preventDefault();
		console.log(getFromData('.filter-results'));
	    /*
	     * Make a ajax call to rest Fiter data
	     * 
	     * */
	});
	
});