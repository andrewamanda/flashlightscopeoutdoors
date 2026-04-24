    // JQUERY ".Class" SELECTOR.
    //$(document).ready(function() {
    //    $("#BuyerOfferPrice").keypress(function(event) { return isNumber(event) });
    //    $("#BuyerCounterOfferPrice").keypress(function(event) { return isNumber(event) });
    //});
    
    // THE SCRIPT THAT CHECKS IF THE KEY PRESSED IS A NUMERIC OR DECIMAL VALUE.
    function isNumber(evt) {
        var charCode = (evt.which) ? evt.which : event.keyCode;
        if (charCode!=8 && (charCode != 46 || $(evt.target).val().indexOf('.') != -1) && 
                (charCode < 48 || charCode > 57)) 
            return false;
	else {
    	//if dot sign entered more than once then don't allow to enter dot sign again. 46 is the code for dot sign
		var target = evt.target || evt.srcElement;
    		var parts = target.value.split('.');
    		if (parts.length > 1 && charCode == 46)
        		return false;
    		return true;
	}

    }    

function numbersonly(e){
	var unicode=e.charCode? e.charCode : e.keyCode;
	if (unicode!=8){ //if the key isn't the backspace key (which we should allow)
		if (unicode<48||unicode>57) //if not a number
			return false; //disable key press
	}
}

function isPositiveInteger(n) {
	return n >>> 0 === parseFloat(n);
}


function limitlength(obj, length){
	var maxlength=length;
	if (obj.value.length>maxlength)
		obj.value=obj.value.substring(0, maxlength);
}
