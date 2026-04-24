;
!function($) {
    Drupal.behaviors.sprowt = {
        attach: function(context, settings) {
            if (Drupal.settings.sprowt.ctmAccountId) {
                // Insert the Call Tracking Metrics Tracking script if account id is set
                var script = $('<script>');
                var firstScript = $('script').first();
                script.attr('src', '//' + Drupal.settings.sprowt.ctmAccountId + '.tctm.co/t.js');
                script.insertBefore(firstScript);
            }

            //gtm parameter fields
            var utm = {
                utm_source: $('#edit-submitted-utm-source'),
                utm_medium: $('#edit-submitted-utm-medium'),
                utm_campaign: $('#edit-submitted-utm-campaign'),
                utm_content: $('#edit-submitted-utm-content'),
                utm_term: $('#edit-submitted-utm-term')
            }

            $.each(utm, function(key, $field){
                //$field.closest('div').show();
                if($field.length > 0) {
                    var params = new URLSearchParams(window.location.search);
                    if(null !== params.get(key)) {
                        $field.val(params.get(key));
                    }

                    var hash = window.location.hash;
                    var re = new RegExp('[#&]'+ key + '=([^&]+)');
                    if(re.test(hash)) {
                        var matches = re.exec(hash);
                        if(typeof matches[1] != 'undefined') {
                            $field.val(matches[1]);
                        }
                    }
                }
            });
        }
    }
}(jQuery);;
!function($) {
    Drupal.behaviors.referrer = {
        attach: function(context, settings) {
            $('form').each(function(){
                var $referrerField = $(this).find('input[name="submitted[referrer]"]');
                if($referrerField.length > 0) {
                    $referrerField.val(document.referrer);
                }
            });
        }
    }
}(jQuery);;
(function($) {
  $(document).ready(function() {
    if ($('.page-admin-structure-taxonomy-markets-add').length ||
    	$('.page-taxonomy-term-edit #taxonomy-form-term[action$="markets"]').length ||
    	$('.page-admin-structure-taxonomy-services-add').length ||
    	$('.page-taxonomy-term-edit #taxonomy-form-term[action$="services"]').length) {
    	//Set message
    	var message = 'Name cannot contain the string " in "';
    	//Attach to submit buttons
    	$('#taxonomy-form-term #edit-submit').click(function(e) {
    		if ($('#taxonomy-form-term #edit-name').val().indexOf(' in ') !== -1) {
    			e.preventDefault();
    			alert(message);
    		}
    	});
    }
  });
})(jQuery);;
