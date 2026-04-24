/**
 * This is the WebTrends Finding Method implementation for Cabela's
 */
function FindingMethod() {
	var fm=this;
	this.bindFunc = "click";
	this.wtTags = {};
	this.WTz_pg = "";
	
	/**
	 * Method to initialize the object.
	 */
	var init = function() {
		// Set the bind function based on the browser
		this.bindFunc = ($.browser.msie?"click":"mousedown");
		
		// Store all the WT MetaTags in an object so we can reference them
		// if/when needed
		$('meta').each(function(){
			if($(this).attr('name').match("^WT\.")) {
				fm.wtTags[$(this).attr('name').replace("WT.", '')] = $(this).attr('content');
			}
		});
		// If the tag is empty, perhaps it came through on the url parmas
		if (fm.wtTags.z_l == undefined) {
			url = $.url(window.location.href);
			fm.wtTags.z_l = url.param('WTz_l');
		}

		// Handle the main navigation
		$('.navigation>li>a').each(function(index) {
			$(this).bind(fm.bindFunc, fm.bind(function() {
				url = $.url($(this).attr('href'));
				if (url.toString().indexOf("javascript") < 0) {
					url.param('WTz_l', 'SBC');
					$(this).attr('href', url.toString());
				}
			}, this, fm));
		});
		
		// Handle the home page content
		$('#homepageTemplate1 .layoutCenterColumn a, #homepageTemplate2 .layoutCenterColumn a, #homepageTemplate1 .layoutCenterColumn area, #homepageTemplate2 .layoutCenterColumn area').each(function(index) {
			$(this).bind(fm.bindFunc, fm.bind(function() {
				if (fm.wtTags.cg_s == 'Google') {
					wtzl = 'GHome';
				} else if (fm.wtTags.cg_s == 'Regular') {
					wtzl = 'Home';
				} else {
					wtzl = fm.wtTags.cg_s+'Home';
				}
				url = $.url($(this).attr('href'));
				if (url.toString().indexOf("javascript") < 0) {
					url.param('WTz_l', wtzl);
					$(this).attr('href', url.toString());
				}
			}, this, fm));
		});

		// Handle the category/subcategory page content
		$('#categoryTemplate1 .layoutCenterColumn a, #categoryTemplate2 .layoutCenterColumn a, #subcategoryTemplate1 .layoutCenterColumn a, #subcategoryTemplate2 .layoutCenterColumn a, #subcategoryTemplate1 .layoutCenterColumn area, #subcategoryTemplate2 .layoutCenterColumn area').each(function(index) {
			$(this).bind(fm.bindFunc, fm.bind(function() {
				url = $.url($(this).attr('href'));
				if (url.toString().indexOf("javascript") < 0) {
					url.param('WTz_l', fm.wtTags.z_l+";"+fm.wtTags.z_pg);
					$(this).attr('href', url.toString());
				}
			}, this, fm));
		});
		
		// Handle the search results page
		$('#searchResults .includeEndecaProducts a.itemName').each(function(index) {
			$(this).bind(fm.bindFunc, fm.bind(function() {
				url = $.url($(this).attr('href'));
				if (url.toString().indexOf("javascript") < 0) {
					url.param('WTz_l', fm.wtTags.z_l);
					$(this).attr('href', url.toString());
				}
			}, this, fm));
		});
		
		// Handle the no search results
		if (fm.wtTags.z_pg == 'NoSearchResults') {
			$('#searchResults .layoutCenterColumn a').each(function(index) {
				$(this).bind(fm.bindFunc, fm.bind(function() {
					url = $.url($(this).attr('href'));
					if (url.toString().indexOf("javascript") < 0) {
						url.param('WTz_l', "Search No items Found");
						$(this).attr('href', url.toString());
					}
				}, this, fm));
			});
		}
		
		// MegaMenu tracking
		$('.megaMenuList a').each(function(index) {
			// Try to first fetch from the webTrendsCategoryId hidden value
			catId = $(this).parents(".js-navLink").children(".webTrendsCategoryId").val();
			if (catId == undefined) {
				catUrl = $.url($(this).parents(".js-navLink").children('a:first-child'));
				if (catUrl.param('categoryId') != null) {
					catId = "cat"+catUrl.param('categoryId');
				}
			}
			if (catId == undefined || catId == null) catId = "";
			url = $.url($(this).attr('href'));
			if (url.toString().indexOf("javascript") < 0) {
				url.param('WTz_l', 'SBC;MM'+catId);
				$(this).attr('href', url.toString());
			}
		});

		// Footer!
		$('#siteFooter a').each(function(index) {
			$(this).bind(fm.bindFunc, fm.bind(function() {
				url = $.url($(this).attr('href'));
				if (url.toString().indexOf("javascript") < 0) {
					url.param('WTz_l', "Footer");
					$(this).attr('href', url.toString());
				}
			}, this, fm));
		});
		
		// Tag the links in the header
		$('#siteHeader .content a, .logo, .customerService').each(function(index) {
			$(this).bind(fm.bindFunc, fm.bind(function() {
				url = $.url($(this).attr('href'));
				if (url.toString().indexOf("javascript") < 0) {
					url.param('WTz_l', "Header");
					$(this).attr('href', url.toString());
				}
			}, this, fm));
		});
		
		// Handle the YMAL
		$('.youMayAlsoLike a').each(function(index) {
			$(this).bind(fm.bindFunc, fm.bind(function() {
				url = $.url($(this).attr('href'));
				if (url.toString().indexOf("javascript") < 0) {
					wtzl = "YMAL"
					if (fm.wtTags.z_typ != undefined && fm.wtTags.z_typ != "") {
						wtzl += ";"+fm.wtTags.z_typ;
					}
					if (fm.wtTags.pn_sku != undefined && fm.wtTags.pn_sku != "") {
						wtzl += ";"+fm.wtTags.pn_sku;
					}
					url.param('WTz_l', wtzl);
					$(this).attr('href', url.toString());
				}
			}, this, fm));
		});
		
		// Handle all the index links on subcategory pages and the product links on index pages
		if (fm.wtTags.cg_s == 'SubCategory' || fm.wtTags.cg_s == 'Index') {
			$('.itemEntry a').each(function(index) {
				$(this).bind(fm.bindFunc, fm.bind(function() {
					url = $.url($(this).attr('href'));
					if (url.toString().indexOf("javascript") < 0) {
						url.param('WTz_l', fm.wtTags.z_l+";"+fm.wtTags.z_pg);
						$(this).attr('href', url.toString());
					}
				}, this, fm));
			});
		}
		
		// Inject an input param into the header search form
		$("#js-headerSearchForm").append("<input type=\"hidden\" name=\"WTz_l\" id=\"searchWTz_l\" value=\"Header\" />");
		$("#js-headerSearchForm").bind('submit', function() {
				$('#searchWTz_l').val($('#searchWTz_l').val() + ';Search-'+$("#searchBy option:selected").text());
			});
		
		// Handle the catalog left nav
		$('.catalogNavigation a').each(function(index) {
			$(this).bind(fm.bindFunc, fm.bind(function() {
				url = $.url($(this).attr('href'));
				if (url.toString().indexOf("javascript") < 0) {
					// If the current finding method set to unknown, use the SBC;LN method
					if (fm.wtTags.z_l == 'Unknown') {
						url.param('WTz_l', 'SBC; LN'+fm.wtTags.z_pg);
					}
					// If we are simply going deeper, this is easy
					if (fm.clickDepth($(this)) > fm.activeDepth()) {
						url.param('WTz_l', fm.wtTags.z_l+";"+fm.wtTags.z_pg);
					}
					// It's also easy if we are staying at the same level
					if (fm.clickDepth($(this)) == fm.activeDepth()) {
						url.param('WTz_l', fm.wtTags.z_l);
					}
					// This is where the fun starts!
					if (fm.clickDepth($(this)) < fm.activeDepth()) {
						fmTokens = fm.wtTags.z_l.split(";");
						// If we are already using SBC, we need to try to determine
						// where to add the current link
						if (fmTokens.length >= 1 && fmTokens[0] == 'SBC') {
							i = 1;
							fmString = 'SBC;';
							while (i < fmTokens.length && i <= fm.clickDepth($(this))) {
								fmString += fmTokens[i] + ";";
								i++;
							}
							fmString = fmString.replace(/;$/, '');
							//fmString += fm.getCategoryIdFromUrl(url);
							url.param('WTz_l', fmString);
						// Otherwise, we need to jump to SBC; LN;
						} else {
							url.param('WTz_l', 'SBC; LN'+fm.wtTags.z_pg);
						}
					}
					$(this).attr('href', url.toString());
				}
			}, this, fm));
		});
		
		// Recently viewed "seeAll" links
		$('.seeAll a').each(function(index) {
			$(this).bind(fm.bindFunc, fm.bind(function() {
				url = $.url($(this).attr('href'));
				if (url.toString().indexOf("javascript") < 0) {
					url.param('WTz_l', "RV");
					$(this).attr('href', url.toString());
				}
			}, this, fm));
		});
	}

	this.activeDepth = function() {
		var activeNav=$(".catalogNavigation .active");
		return activeNav.eq(activeNav.length-1).parents("ul").length;
	}
	
	/**
	 * A bind function which takes a function and arguments used to essentially
	 * overload the default jQuery bind function.
	 * @param fn The bind function to call
	 * @param scope The arguments to pass to fn.apply
	 * @return A function
	 */
	this.bind = function(fn, scope) {
		return function() { fn.apply(scope, arguments) };
	}

	this.breadcrumb = function(breadCrumbIds) {
		bcTokens = breadCrumbIds.split("|");
		fmTokens = fm.wtTags.z_l.split(";");
		if (bcTokens.length == 0) {
			return;
		}
		if (fmTokens.length >= 1 && fmTokens[0] == 'SBC') {
			fmStr = 'SBC';
			// This isn't standard SBC so append the second token
			if (fmTokens.length >= 2 && fmTokens[1].indexOf('cat') != 0) {
				fmStr += ';'+fmTokens[1];
			}
		} else {
			fmStr = 'SBC;BR'+fm.wtTags.z_pg;
		}
		ii = 0;
		$('.breadcrumb a').each(function(index) {
			url = $.url($(this).attr('href'));
			url.param('WTz_l', fmStr);
			$(this).attr('href', url.toString());
			// If we are in SBC, just append the tokens until they match
			if (fmTokens.length >= 1 && fmTokens[0] == 'SBC') {
				if ('cat'+bcTokens[ii] == fmTokens[ii+1]) {
					fmStr += ";" + fmTokens[ii+1];
				}
			}
			ii++;
		});
	}

	this.clickDepth = function(element) {
		return $(element).parents("ul").length;
	}
	
	/**
	 * Method to get the categoryId from a jQuery url object
	 * @param url A jQuery url object
	 * @return String The categoryId
	 */
	this.getCategoryIdFromUrl = function(url) {
		if (url.param('categoryId') != null) {
			return url.param('categoryId');
		} else {
			// Pull it from the category id in the URL (eg Ns-CATEGORY_SEQ_99141480)
			return url.attr("path").replace(/.*Ns-CATEGORY_SEQ_([0-9]*).*/, '$1');
		}
		
	}


	init();
	return this;
}

$(document).ready(function() {
	fm=new FindingMethod();
});
