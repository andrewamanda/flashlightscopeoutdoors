var ctview = "/catalog/relatedproducts/";

function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

function ajaxstp() {
    jQuery.ajaxSetup({
        type: 'POST',
        timeout: 30000,
        beforeSend: function(xhr, settings) {
            if (!this.crossDomain) {
                var csrftoken = getCookie('csrftoken');
                if (csrftoken) {
                    xhr.setRequestHeader('X-CSRFToken', csrftoken);
                }
            }
        },
        error: function(xhr) {
            var message = 'Failed to add the product to the cart.';
            if (xhr.responseJSON && xhr.responseJSON.message) {
                message = xhr.responseJSON.message;
            } else if (xhr.responseText) {
                try {
                    var parsed = JSON.parse(xhr.responseText);
                    if (parsed.message) {
                        message = parsed.message;
                    }
                } catch (e) {}
            }
            alert(message);
        }
    });
}

function addConfiguredRelatedToCart(buttonEl, slug) {
    var $button = jQuery(buttonEl);
    var $card = $button.closest('.js-related-card');
    var quantity = parseInt($card.find('.js-related-qty').val(), 10) || 1;

    $button.prop('disabled', true);

    jQuery.ajax({
        url: ctview,
        method: 'POST',
        dataType: 'json',
        data: {
            quantity: quantity,
            slug: slug
        }
    }).done(function(response) {
        if (response.success) {
            if (jQuery('#miniCartView').length) {
                jQuery('#miniCartView').text(response.cart_count + ' items');
            }
            $card.find('.js-related-confirmation').stop(true, true).fadeIn('slow').delay(1200).fadeOut('slow');
        } else {
            alert(response.message || 'Failed to add the product to the cart.');
        }
    }).always(function() {
        $button.prop('disabled', false);
    });
}

jQuery(document).ready(function() {
    ajaxstp();

    jQuery(document).on('click', '.js-related-add', function(e) {
        e.preventDefault();
        var slug = jQuery(this).data('product-slug');
        addConfiguredRelatedToCart(this, slug);
    });
});
