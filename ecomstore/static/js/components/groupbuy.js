function ajaxstp(){
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
	   }
	})
};


function updtEventsTable(tbltag,djview){
	ajaxstp();
        var table = $("#"+ tbltag).DataTable();
	if (table) table.destroy();
    	$("#"+ tbltag).DataTable( {
       		ajax: djview + '?load_participants=1',
		idSrc: "id",
    		language: {
        		emptyTable: "No participant has joined the group buy",
    		},

		'order': [1, 'asc'],
        	columns: [
            		{ data: "id" },
            		{ data: "user" },
            		{ data: "name" },
            		{ data: "quantity" },
            		{ data: "reason" },
            		{ data: "state" },
            		{ data: "country" },
            		{ data: "last_updated" },
			],
                columnDefs: [
                           {
                             targets:2,
                             render: function ( data, type, row, meta ) {
                                  if(type === 'display'){
                                    data = '';
                                  }

                                 return data;
                            }
                        },]

    	} );
};

function updtButtons(ctview) {
        var query_status = {
                action: "get_status" };
       	jQuery.post(ctview, query_status,
               	function(response){
                       	jQuery("#id_event_form_errors").empty();
                       	if(response.success == "True"){
				if (response.already_participated === true) {
					$('#button_event_record_add').hide();
					$('#button_event_record_withdraw').show();
					$('#button_event_record_delete').show();
					$('#button_event_record_submit').hide();
				}
				else {
					$('#button_event_record_add').show();
					$('#button_event_record_withdraw').hide();
					$('#button_event_record_delete').hide();
					$('#button_event_record_submit').show();

				}
                       	}
                       	else{
				alert("You have already participated under the user ID: " + response.username);
                       	}

               	}, "json");


}

var ctid;
$( document ).ready(function() {
	var ctview = "/marketing/groupbuy/";
	
	updtEventsTable("id_groupbuy",ctview);
	updtButtons(ctview);

        $('#button_event_record_delete').click( function () {
                var table = $('#id_groupbuy').DataTable();
                var id2delete = {
                        action: "delete",
                        };
                jQuery.post(ctview, id2delete,
                        function(response){
                                jQuery("#id_event_form_errors").empty();
                                if(response.success == "True"){
					updtEventsTable("id_groupbuy",ctview);
                                        //table.row('.selected').remove().draw( false );
					$('#id_event_form').slideToggle();
					$('#button_event_record_add').show();
					$('#button_event_record_add').text('Enter your participation').button("refresh");
					$('#button_event_record_delete').hide();
					$('#button_event_record_submit').show();

                                }
                                else{
                                        jQuery("#id_event_form_errors").append(response.html);
                                }
                        }, "json");
        } );

        $('#button_event_record_add').on( 'click', function () {
		$('#id_event_form').slideToggle();
		$('#button_event_record_add').hide();
		$('#button_event_record_submit').show();
		$('#button_event_record_delete').hide();
		$('#button_event_record_cancel').show();
		
        });
        $('#button_event_record_withdraw').on( 'click', function () {
		$('#id_event_form').slideToggle();
		$('#button_event_record_withdraw').hide();
		$('#button_event_record_delete').show();
		$('#button_event_record_submit').hide();
		$('#button_event_record_cancel').show();
		
        });
        $('#button_event_record_cancel').on( 'click', function () {
		$('#id_event_form').slideToggle();
		$('#button_event_record_add').show();
		$('#button_event_record_submit').hide();
		$('#button_event_record_delete').hide();
		$('#button_event_record_cancel').hide();
		
        });
        $('#button_event_record_submit').on( 'click', function () {
        	var new_record = {
                	name: jQuery("#id_name").val(),
                	quantity: jQuery("#id_quantity").val(),
                	reason: jQuery("#id_reason").val(),
                	state: jQuery("#id_state").val(),
                	country: jQuery("#id_country").val() };
        	jQuery.post(ctview, new_record,
                	function(response){
                        	jQuery("#id_event_form_errors").empty();
                        	if(response.success == "True"){
					$('#id_event_form').slideToggle();
					$('#button_event_record_add').hide();
					$('#button_event_record_withdraw').show();
                                        new_record.id = response.id;
					new_record.user = response.username;
					new_record.last_updated = response.date;
                                        var table = $('#id_groupbuy').DataTable();
                                        table.row.add(new_record).draw();
					$('#button_event_record_add').text('Withdraw your participation').button("refresh");
                        	}
                        	else{
					alert("You have already participated under the user ID: " + response.username);
                        	}

                	}, "json");

		
        	});

});
