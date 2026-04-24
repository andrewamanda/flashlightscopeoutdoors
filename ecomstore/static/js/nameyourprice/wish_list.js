
function MakeOffer() {

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
			$('#loadingmessage_makeoffer').hide();
			$('#MakeOffer').show();

               }
        })

    $('#loadingmessage_makeoffer').show();
    $('#MakeOffer').hide();

    var pList = [];

    jQuery("#wish_list input[type=text]").each(function() {
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
                        msg: jQuery("#buyer_comment").val(),
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
                    // disable the submit button to prevent duplicates
                            $('#loadingmessage_makeoffer').hide();
                            $('#MakeOffer').show();

                            jQuery("#GetSellerOffer").hide();
                            jQuery("#add2cart").hide();
                            jQuery("#MakeOffer").hide();
			    $("#MakeInitialOffer :input").attr("disabled", "disabled");
			    $("#wish_list :input").attr("disabled", "disabled");
                            jQuery("#BuyerOfferMade").html(response.html).slideDown();
                    }
                    else{
			alert(response.text);
                    }
             }, "json");
     }

}

function BuyItNow1() {

        $.ajaxSetup({
                type: 'POST',
                timeout: 30000,
                error: function(xhr) {
                        alert('Internet Connection Error: ' + xhr.status + ' ' + xhr.statusText);
			$('#loadingmessage_buyitnow').hide();
			$('#buyitnow').show();
               }
        })

    $('#loadingmessage_buyitnow').show();
    $('#buyitnow').hide();

    var pList = [];
    
    jQuery("#wish_list input[type=text]").each(function() {
	//borrow the name attribute for the unit price
   	var product = {
			id: this.id, 
			qty: this.value,
	};
	if(this.value > 0) {
		pList.push(product);
	}
    });
    var p = {
		products_chosen: pList,
    }
    jQuery.post("/nameyourprice/buyitnow/", p,
            function(response){
                    // evaluate the "success" parameter
                    if(response.success == "True"){
                    // disable the submit button to prevent duplicates
                            $('#loadingmessage_buyitnow').hide();
			    jQuery("#buyitnow").hide();
			    jQuery("#MakeInitialOffer").hide();
			    jQuery("#Proceed2Checkout").slideDown();
                    }
                    else{
                    }
             }, "json");
}

function updateSubtotal(id) {
    subtotal = 0;
    jQuery("#wish_list input[type=text]").each(function() {
        //borrow the name attribute for the unit price
        subtotal += this.name * this.value;
    });

    subtotal = subtotal.toFixed(2);
    $("#subtotal").text(subtotal);
    $("#BuyerOfferPrice").val(subtotal);
}

function prepareDocument(){
	jQuery("#add2cart").click(BuyItNow);
	jQuery("#MakeOffer").click(MakeOffer);
};

//jQuery(document).ready(prepareDocument);
