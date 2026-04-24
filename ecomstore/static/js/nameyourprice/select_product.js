function GetSellerOffer(){

	$.ajaxSetup({
		type: 'POST',
		timeout: 30000,
    		beforeSend: function(xhr, settings) {
        		if (!this.crossDomain) {
            			xhr.setRequestHeader("X-CSRFToken", $.cookie('csrftoken'));
        		}
    		},
		error: function(xhr) {
    			alert('Internet Connection Error: ' + xhr.status + ' ' + xhr.statusText);
			$('#loadingmessage').hide();
			$('#GetQuote').show();
               }
        })

	$('#loadingmessage').show();
	$('#GetQuote').hide();

        var p = {
                products: jQuery("#id_p").val(),
        };
        jQuery.post("/nameyourprice/getselleroffers/", p,
                function(response){
                        // evaluate the "success" parameter
                        if(response.success == "True"){
                        // disable the submit button to prevent duplicates
				$('#loadingmessage').hide();
				$('#GetQuote').show();
				if (response.selected > 0) {
                                	jQuery("#SellerOffer").html(response.html).slideDown();
				}
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
