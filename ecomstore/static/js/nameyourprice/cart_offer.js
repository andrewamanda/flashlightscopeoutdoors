function slideOfferToggleForm(){
        jQuery("#MakeOfferFromCart").slideToggle();
}
function prepareDocument(){
        jQuery("#show_offer_form").click(slideOfferToggleForm);
        jQuery("#cancel_offer_form").click(slideOfferToggleForm);
}

jQuery(document).ready(prepareDocument);

function MakeOfferFromCart() {

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
			$('#MakeOfferFromCart').show();

               }
        })

    $('#loadingmessage_makeoffer').show();
    $('#MakeOfferFromCart').show();

    var pList = [];

    jQuery("#forvalidation_cart input[type=text]").each(function() {
        //borrow the name attribute for the unit price
	if(jQuery("#BuyerOfferPrice").val() > 0) {
		offerprice = jQuery("#BuyerOfferPrice").val()
	}
	else {
		offerprice = 0;
	}
        var product = {
                        id: this.id,
                        qty: this.value,
                        msg: "From shopping cart",
                        buyerofferprice: offerprice,
			shipping_country: jQuery("#ShippingCountry").val(),
        };
 	if(this.value > 0) {	
        	pList.push(product);
	}
    });
    var p = {
                products_chosen: pList,
    }
    if (pList.length == 0) {
	alert("Please update the quantity of the products selected");
    	$('#loadingmessage_makeoffer').hide();
    	$('#MakeOffer').show();
    }
    else {
    jQuery.post("/nameyourprice/buyermakeoffer/", p,
            function(response){
                    // evaluate the "success" parameter
                    if(response.success == "True"){
			$('#loadingmessage_makeoffer').hide();
			window.location='/nameyourprice/makeoffer/';

                    }
                    else{
			alert(response.text);
                    }
             }, "json");
     }

}

