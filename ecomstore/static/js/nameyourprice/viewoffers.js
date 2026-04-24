function ConfirmCancelOffer() {

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

    alert("Are you sure you want to cancel your offer?");
        var bid = {
                b_id: jQuery("#b_id").val(),
		comment: jQuery("#CancelReason").val(),
        };
        jQuery.post("/nameyourprice/cancelyouroffer/", bid,
                function(response){
                        // evaluate the "success" parameter
                        if(response.success == "True"){
                        // disable the submit button to prevent duplicates
                                //jQuery("#SellerOffer").html(response.html).slideDown();
    				$("#PendingTitle").text("Offer Cancelled");
    				$("#Pending").text("Your offer has been cancelled, you can make a new offer");
    				$("#CancelOffer").hide();
				$("#CancelOfferForm").hide();
				if(response.open_offer_count == 0){
					$("#errorMsg").hide();
				}
				else{
					$("#offer_count").text(response.open_offer_count);
				}
				
                        }
                        else{
                        }
                }, "json");

}



function ShowAcceptOfferForm() {
	jQuery("#OfferAction").hide();
	jQuery("#AcceptForm").slideDown();
}

function ShowCancelOfferForm() {
	jQuery("#CancelOffer").hide();
	jQuery("#AfterAccept").hide();
	jQuery("#ProceedToCheckOut").hide();
	jQuery("#CancelOfferForm").slideDown();
}

function showCancelOfferDiv() {
	jQuery("#CancelOffer").slideDown();
	jQuery("#ProceedToCheckOut").slideDown();
	jQuery("#CancelOfferForm").hide();
}

function showBuyerActionsDiv() {
	jQuery("#OfferAction").slideDown();
	jQuery("#AcceptForm").hide();
	jQuery("#DeclineForm").hide();
	jQuery("#CounterOfferForm").hide();
}


function ShowDeclineOfferForm() {
	jQuery("#OfferAction").hide();
	jQuery("#DeclineForm").slideDown();
}

function ShowCounterOfferForm() {
	jQuery("#OfferAction").hide();
	jQuery("#CounterOfferForm").slideDown();
}

function ConfirmCounterOffer() {

        $.ajaxSetup({
                type: 'POST',
                timeout: 30000,
                error: function(xhr) {
                        alert('Error: ' + xhr.status + ' ' + xhr.statusText);
               }
        })

        var bid = {
                b_id: jQuery("#b_id").val(),
		price: jQuery("#BuyerCounterOfferPrice").val(),
		comment: jQuery("#CounterOfferComment").val(),
        };
        jQuery.post("/nameyourprice/buyercounteryouroffer/", bid,
                function(response){
                        // evaluate the "success" parameter
                        if(response.success == "True"){
                        // disable the submit button to prevent duplicates
				$("#CounterOfferForm").hide();
    				$("#PendingTitle").text("Your Counter Offer has been entered");
    				$("#CounterOfferMade").text("You have entered an counter offer, Pending Andrew's response");
    				$("#CounterOfferMade").slideDown();
    				$("#AfterCounter").slideDown();
                        }
                        else{
                        }
                }, "json");


}

function ConfirmAcceptOffer() {

        $.ajaxSetup({
                type: 'POST',
                timeout: 30000,
                error: function(xhr) {
                        alert('Error: ' + xhr.status + ' ' + xhr.statusText);
               }
        })

        var bid = {
                b_id: jQuery("#b_id").val(),
		comment: jQuery("#AcceptComment").val(),
        };
        jQuery.post("/nameyourprice/acceptoffer/", bid,
                function(response){
                        // evaluate the "success" parameter
                        if(response.success == "True"){
                        // disable the submit button to prevent duplicates
				$("#AcceptForm").hide();
    				$("#PendingTitle").text("Seller's offer accepted");
				$("#Pending").text("You have accepted the offer of $"+response.accepted_price);
    				$("#AfterAccept").slideDown();
                        }
                        else{
                        }
                }, "json");


}
function ConfirmDeclineOffer() {

        $.ajaxSetup({
                type: 'POST',
                timeout: 30000,
                error: function(xhr) {
                        alert('Error: ' + xhr.status + ' ' + xhr.statusText);
               }
        })

        var bid = {
                b_id: jQuery("#b_id").val(),
		comment: jQuery("#DeclineReason").val(),
        };
        jQuery.post("/nameyourprice/declineyouroffer/", bid,
                function(response){
                        // evaluate the "success" parameter
                        if(response.success == "True"){
                        // disable the submit button to prevent duplicates
				$("#DeclineForm").hide();
    				$("#PendingTitle").text("Seller's offer declined");
    				$("#AfterDecline").slideDown();
                        }
                        else{
                        }
                }, "json");


}

function prepareDocument(){
	jQuery("#AcceptOffer").click(ShowAcceptOfferForm);
	jQuery("#ConfirmCancelOffer").click(ConfirmCancelOffer);
	jQuery("#DeclineOffer").click(ShowDeclineOfferForm);
	jQuery("#ConfirmDecline").click(ConfirmDeclineOffer);
	jQuery("#ConfirmCounterOffer").click(ConfirmCounterOffer);
	jQuery("#ConfirmAcceptOffer").click(ConfirmAcceptOffer);

	jQuery("#cancel_cancel").click(showCancelOfferDiv);
	jQuery("#cancel_decline").click(showBuyerActionsDiv);
	jQuery("#cancel_counteroffer").click(showBuyerActionsDiv);
	jQuery("#cancel_acceptoffer").click(showBuyerActionsDiv);
	jQuery("#CancelOffer").click(ShowCancelOfferForm);
	jQuery("#CancelOfferAfterAccept").click(ShowCancelOfferForm);

	jQuery("#CounterOffer").click(ShowCounterOfferForm);

};

//jQuery(document).ready(prepareDocument);
