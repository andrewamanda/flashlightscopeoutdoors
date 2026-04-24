from django.urls import re_path as url, include
from ecomstore.heartwoodbeyond import views as myviews
from ecomstore import settings

urlpatterns = [
    url(r'^about/', myviews.about, {'template_name':'heartwoodandbeyond/about.html', 'SSL': settings.ENABLE_SSL}, 'show_about'),

    url(r'^grade/', myviews.grade, {'template_name':'heartwoodandbeyond/our-heartpine-grades.html', 'SSL': settings.ENABLE_SSL}, 'show_grades'),
    url(r'^gallery/', myviews.gallery, {'template_name':'heartwoodandbeyond/galleries/gallery_main.html', 'SSL': settings.ENABLE_SSL}, 'show_gallery'),

    url(r'^free_quote/', myviews.contact, {'template_name':'heartwoodandbeyond/contact.html', 'SSL': settings.ENABLE_SSL}, 'free_quote'),
    url(r'^leave_review/', myviews.leave_review, {'template_name':'heartwoodandbeyond/faq/leave-review.html', 'SSL': settings.ENABLE_SSL}, 'leave_review'),
    url(r'^shipping/', myviews.shipping, {'template_name':'heartwoodandbeyond/faq/shipping.html', 'SSL': settings.ENABLE_SSL}, 'shipping'),
    url(r'^tobacco_pine_rustic/', myviews.tobacco_pine_rustic, {'template_name':'heartwoodandbeyond/tobacco-pine-rustic.html', 'SSL': settings.ENABLE_SSL}, 'tobacco_pine_rustic'),
    url(r'^heartpine_products/', myviews.heartpine_products, {'template_name':'heartwoodandbeyond/heartpine-products.html', 'SSL': settings.ENABLE_SSL}, 'heartpine_products'),
    url(r'^why_reclaiming_process/', myviews.why_reclaiming_process, {'template_name':'heartwoodandbeyond/faq/reclaiming-process.html', 'SSL': settings.ENABLE_SSL}, 'why_reclaiming_process'),

    url(r'^faq_why/', myviews.why, {'template_name':'heartwoodandbeyond/faq/faq.html', 'SSL': settings.ENABLE_SSL}, 'show_why'),
    url(r'^faq_installation_tips/', myviews.installation_tips, {'template_name':'heartwoodandbeyond/faq/installation-tips.html', 'SSL': settings.ENABLE_SSL}, 'installation_tips'),
    url(r'^faq_post_installation/', myviews.post_installation, {'template_name':'heartwoodandbeyond/faq/post_installation.html', 'SSL': settings.ENABLE_SSL}, 'post_installation'),
    url(r'^faq_reclaiming_process/', myviews.reclaiming_process, {'template_name':'heartwoodandbeyond/faq/reclaiming-process.html', 'SSL': settings.ENABLE_SSL}, 'reclaiming_process'),
    url(r'^our_heartpine_grades/', myviews.our_heartpine_grades, {'template_name':'heartwoodandbeyond/our-heartpine-grades.html', 'SSL': settings.ENABLE_SSL}, 'our_heartpine_grades'),
    url(r'^faq_leave_review/', myviews.leave_review, {'template_name':'heartwoodandbeyond/faq/leave-review.html', 'SSL': settings.ENABLE_SSL}, 'leave_review'),
    url(r'^faq_shipping/', myviews.shipping, {'template_name':'heartwoodandbeyond/faq/shipping.html', 'SSL': settings.ENABLE_SSL}, 'shipping'),
    url(r'^faq_contact/', myviews.contact, {'template_name':'heartwoodandbeyond/faq/contact.html', 'SSL': settings.ENABLE_SSL}, 'contact'),
    url(r'^faq_makeapayment', myviews.makeapayment, {'SSL': settings.ENABLE_SSL}, 'hpw_makeapayment'),
    url(r'^iframe_makeapayment', myviews.iframe_makeapayment, {'SSL': settings.ENABLE_SSL}, 'iframe_makeapayment'),
    url(r'^faq_wood_finishes/', myviews.post_installation, {'template_name':'heartwoodandbeyond/faq/wood_finishes.html', 'SSL': settings.ENABLE_SSL}, 'wood_finishes'),
    url(r'^blog/(?P<blog_slug>[-\w]+)/$', myviews.show_blog,
       {'template_name': 'heartwoodandbeyond/faq/faq_template.html', 'SSL': settings.ENABLE_SSL}, 'blog'),


    url(r'^lumber_natural_antique_heartpine/', myviews.natural_antique_heartpine, {'template_name':'heartwoodandbeyond/grades/natural-antique-heartpine.html', 'SSL': settings.ENABLE_SSL}, 'natural_antique_heartpine'),
    url(r'^lumber_character_heartpine/', myviews.character_heartpine, {'template_name':'heartwoodandbeyond/grades/character-heartpine.html', 'SSL': settings.ENABLE_SSL}, 'character_heartpine'),
    url(r'^lumber_antique_southern_yellow_pine/', myviews.antique_southern_yellow_pine, {'template_name':'heartwoodandbeyond/grades/antique-southern-yellow-pine.html', 'SSL': settings.ENABLE_SSL}, 'antique_southern_yellow_pine'),
    url(r'^lumber_american_tobacco_co_reclaimed_tobacco_pine/', myviews.american_tobacco_co_reclaimed_tobacco_pine, {'template_name':'heartwoodandbeyond/grades/american-tobacco-co-reclaimed-tobacco-pine.html', 'SSL': settings.ENABLE_SSL}, 'american_tobacco_co_reclaimed_tobacco_pine'),
    url(r'^lumber_oak/', myviews.oak, {'template_name':'heartwoodandbeyond/grades/oak.html', 'SSL': settings.ENABLE_SSL}, 'oak'),
    url(r'^lumber_select_1_heartpine/', myviews.select_1_heartpine, {'template_name':'heartwoodandbeyond/grades/select-1-heartpine.html', 'SSL': settings.ENABLE_SSL}, 'select_1_heartpine'),
    url(r'^lumber_select_1_heartpine_0/', myviews.select_1_heartpine_0, {'template_name':'heartwoodandbeyond/grades/select-1-heartpine-0.html', 'SSL': settings.ENABLE_SSL}, 'select_1_heartpine_0'),
    url(r'^lumber_antique_quartersawn/', myviews.antique_quartersawn, {'template_name':'heartwoodandbeyond/grades/antique-quarterswan-heartpine.html', 'SSL': settings.ENABLE_SSL}, 'antique_quartersawn'),

    url(r'^finest_heart_pine_floors/', myviews.finest_heart_pine_floors, {'template_name':'heartwoodandbeyond/finest-heart-pine-floors-moncure-nc.html', 'SSL': settings.ENABLE_SSL}, 'finest_heart_pine_floors'),

    url(r'^gallery_quartersawn_heartpine/', myviews.gallery_quartersawn_heartpine, {'template_name':'heartwoodandbeyond/gallery/quartersawn-heartpine.html', 'SSL': settings.ENABLE_SSL}, 'gallery_quartersawn_heartpine'),
    url(r'^gallery_additional_products/', myviews.gallery_additional_products, {'template_name':'heartwoodandbeyond/gallery/additional-products.html', 'SSL': settings.ENABLE_SSL}, 'gallery_additional_products'),
    url(r'^gallery_tobacco_pine_rustic/', myviews.gallery_tobacco_pine_rustic, {'template_name':'heartwoodandbeyond/gallery/tobacco-pine-rustic.html', 'SSL': settings.ENABLE_SSL}, 'gallery_tobacco_pine_rustic'),
    url(r'^gallery_natural_antique_heartpine/', myviews.gallery_natural_antique_heartpine, {'template_name':'heartwoodandbeyond/gallery/natural-antique-heartpine.html', 'SSL': settings.ENABLE_SSL}, 'gallery_natural_antique_heartpine'),
    url(r'^gallery_character_heartpine/', myviews.gallery_character_heartpine, {'template_name':'heartwoodandbeyond/gallery/character-heartpine.html', 'SSL': settings.ENABLE_SSL}, 'gallery_character_heartpine'),
    url(r'^gallery_antique_southern_yellow_pine/', myviews.gallery_character_heartpine, {'template_name':'heartwoodandbeyond/gallery/antique-southern-yellow-pine.html', 'SSL': settings.ENABLE_SSL}, 'gallery_antique_southern_yellow_pine'),


    url(r'^request4moreinfo/', myviews.request4moreinfo, {'template_name':'heartwoodandbeyond/responses/more_info.html', 'SSL': settings.ENABLE_SSL}, 'respond_to_more_info'),
    url(r'^request4sample/', myviews.request4sample, {'template_name':'heartwoodandbeyond/responses/sample_request.html', 'SSL': settings.ENABLE_SSL}, 'respond_to_sample_request'),
    url(r'^testimonial/', myviews.testimonial, {'template_name':'heartwoodandbeyond/responses/testimonial_response.html', 'SSL': settings.ENABLE_SSL}, 'respond_to_testimonial'),

    url(r'^message_center/', myviews.message_center, {'template_name':'heartwoodandbeyond/message_center.html', 'SSL': settings.ENABLE_SSL}, 'message_center'),
    url(r'^heartpine_pricing/', myviews.heartpine_pricing, {'template_name':'heartwoodandbeyond/heartpine_pricing.html', 'SSL': settings.ENABLE_SSL}, 'heartpine_pricing'),
    url(r'^pricing_explain/', myviews.heartpine_pricing, {'template_name':'heartwoodandbeyond/pricing/pricing_explain.html', 'SSL': settings.ENABLE_SSL}, 'pricing_explain'),

    url(r'^pricing_structures/', myviews.heartpine_pricing, {'template_name':'heartwoodandbeyond/pricing/pricing_structure.html', 'SSL': settings.ENABLE_SSL}, 'pricing_structures'),
    url(r'^pricing_floors/', myviews.heartpine_pricing, {'template_name':'heartwoodandbeyond/pricing/pricing_floors.html', 'SSL': settings.ENABLE_SSL}, 'pricing_floors'),
    url(r'^pricing_stairs/', myviews.heartpine_pricing, {'template_name':'heartwoodandbeyond/pricing/pricing_stairs.html', 'SSL': settings.ENABLE_SSL}, 'pricing_stairs'),
    url(r'^pricing_panels/', myviews.heartpine_pricing, {'template_name':'heartwoodandbeyond/pricing/pricing_panels.html', 'SSL': settings.ENABLE_SSL}, 'pricing_panels'),
    url(r'^pricing_registers/', myviews.heartpine_pricing, {'template_name':'heartwoodandbeyond/pricing/pricing_registers.html', 'SSL': settings.ENABLE_SSL}, 'pricing_registers'),
    url(r'^getproductdetails/', myviews.heartpine_productdetails, {'template_name':'heartwoodandbeyond/heartpine_pricing.html', 'SSL': settings.ENABLE_SSL}, 'getproductdetails'),
    url(r'^email_unsubscribe/', myviews.email_unsubscribe, {'template_name':'heartwoodandbeyond/email_unsubscribe.html', 'SSL': settings.ENABLE_SSL}, 'email_unsubscribe'),
    url(r'^milling/', myviews.milling, {'template_name':'heartwoodandbeyond/milling.html', 'SSL': settings.ENABLE_SSL}, 'milling'),
    url(r'^our_products/', myviews.our_products, {'template_name':'heartwoodandbeyond/products/product-collections.html', 'SSL': settings.ENABLE_SSL}, 'our_products'),
    url(r'^product_floors/', myviews.product_floors, {'template_name':'heartwoodandbeyond/products/floors.html', 'SSL': settings.ENABLE_SSL}, 'product_floors'),
    url(r'^product_stairs/', myviews.product_floors, {'template_name':'heartwoodandbeyond/products/stairs.html', 'SSL': settings.ENABLE_SSL}, 'product_stairs'),
    url(r'^product_mantels/', myviews.product_floors, {'template_name':'heartwoodandbeyond/products/mantels.html', 'SSL': settings.ENABLE_SSL}, 'product_mantels'),
    url(r'^product_beams/', myviews.product_floors, {'template_name':'heartwoodandbeyond/products/beams.html', 'SSL': settings.ENABLE_SSL}, 'product_beams'),
    url(r'^product_panels/', myviews.product_floors, {'template_name':'heartwoodandbeyond/products/panels.html', 'SSL': settings.ENABLE_SSL}, 'product_panels'),
    url(r'^product_tabletops/', myviews.product_floors, {'template_name':'heartwoodandbeyond/products/tabletops.html', 'SSL': settings.ENABLE_SSL}, 'product_tabletops'),
    url(r'^product_floorregisters/', myviews.product_floors, {'template_name':'heartwoodandbeyond/products/floorregisters.html', 'SSL': settings.ENABLE_SSL}, 'product_floorregisters'),
    url(r'^wholesalelumber/', myviews.wholesalelumber, {'template_name':'heartwoodandbeyond/wholesalelumber/wholesale_all.html', 'SSL': settings.ENABLE_SSL}, 'wholesalelumber'),
    url(r'^wholesale_all/', myviews.wholesalelumber, {'template_name':'heartwoodandbeyond/wholesalelumber/wholesale_all.html', 'SSL': settings.ENABLE_SSL}, 'wholesale_all'),


]
