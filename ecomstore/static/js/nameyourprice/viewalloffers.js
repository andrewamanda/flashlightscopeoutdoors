function QueryOffer(id) {

        $.ajaxSetup({
                type: 'POST',
                timeout: 30000,
                beforeSend: function(xhr, settings) {
                        if (!this.crossDomain) {
                                xhr.setRequestHeader("X-CSRFToken", $.cookie('csrftoken'));
                        }
                },
                error: function(xhr) {
                        alert('Error: ' + xhr.status + ' ' + xhr.statusText);
               }
        })

        var bid = {
                b_id: id,
        };
   	if(jQuery("#"+id).text() == "Close Detail") {
		jQuery("#offerhistory_"+id).toggle();
		jQuery("#"+id).text("View Detail");
	}
	else {
          jQuery.post("/nameyourprice/getofferhistory/", bid,
                function(response){
                        // evaluate the "success" parameter
                        if(response.success == "True"){
                        // disable the submit button to prevent duplicates
                                jQuery("#offerhistory_"+id).html(response.html).slideDown();
				jQuery("#"+id).text("Close Detail");
                        }
                        else{
                        }
                }, "json");
	}

}

