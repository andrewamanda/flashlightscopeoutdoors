function GetBrowserTimeout(){

        settimeout = jQuery("#settimeout").val() 
	var start = new Date().getTime();
	alert(start);
	$.ajaxSetup({
		type: 'POST',
		error: function(xhr) {
			var end = new Date().getTime();
			var time = end - start;
    			alert('Error: ' + xhr.status + ' ' + xhr.statusText);
			alert("The browser timed out after " + time/1000 + " seconds");
               }
        })
        var p = {
                time_out: jQuery("#setseconds").val(),
        };
        jQuery.post("/functionaltests/getbrowsertimeout/", p,
                function(response){
                        // evaluate the "success" parameter
                        if(response.success == "True"){
                        // disable the submit button to prevent duplicates
                                jQuery("#response").html(response.html).slideDown();
                        }
                        else{
                        }
                }, "json");

};
function SetBrowserTimeout(){

        settimeout = jQuery("#settimeout").val() 
	var start = new Date().getTime();
	alert(start);
	$.ajaxSetup({
		type: 'POST',
		timeout: settimeout * 1000,
		error: function(xhr) {
			var end = new Date().getTime();
			var time = end - start;
    			alert('Error: ' + xhr.status + ' ' + xhr.statusText);
			alert("The browser timed out after " + time/1000 + " seconds");
			$('#timeouterror').show();
				$('#loadingmessage').hide();
               }
        })

	$('#loadingmessage').show();
	
        var p = {
                time_out: jQuery("#settimeout").val(),
        };
        jQuery.post("/functionaltests/getbrowsertimeout/", p,
                function(response){
                        // evaluate the "success" parameter
                        if(response.success == "True"){
                        // disable the submit button to prevent duplicates
				$('#loadingmessage').hide();
                                jQuery("#response").html(response.html).slideDown();
                        }
                        else{
                        }
                }, "json");

};

function prepareDocument(){
	//prepare product review form
        jQuery.localise('ui-multiselect', {/*language: 'en',*/ path: '/static/multiselect-master/js/locale/'});
        jQuery(".multiselect").multiselect();
        //jQuery("#switcher").themeswitcher();
	//jQuery("#GetSellerOffer").click(GetSellerOffer);

};

jQuery(document).ready(prepareDocument);
