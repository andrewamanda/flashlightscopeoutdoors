from django.urls import re_path as url, include
from ecomstore import settings
from ecomstore.accounts import views as myviews

urlpatterns = [
	url(r'^register/$', myviews.register,
	    {'template_name': 'registration/register.html', 'SSL': settings.ENABLE_SSL }, 'register'),
	url(r'^$', myviews.my_account,
	 	{'template_name': 'registration/my_account.html', 'SSL': settings.ENABLE_SSL}, 'my_account'),

	url(r'^my_account/$', myviews.my_account,
	 	{'template_name': 'registration/my_account.html', 'SSL': settings.ENABLE_SSL }, 'my_account'),
	url(r'^order_info/$', myviews.order_info,
	 	{'template_name': 'checkout/addresses.html', 'SSL': settings.ENABLE_SSL }, 'order_info'),
	url(r'^order_details/(?P<order_id>[-\w]+)/$', myviews.order_details,
	 	{'template_name': 'registration/order_details.html', 'SSL': settings.ENABLE_SSL}, 'order_details'),

	#url(r'^reset_password/$', myviews.reset_password, {'SSL': settings.ENABLE_SSL}, 'reset_password'),

	url(r'^gift_account/$', myviews.gift_account,
	 	{'template_name': 'registration/gift_account.html', 'SSL': settings.ENABLE_SSL}, 'gift_account'),


]

#Dictionary for authentication views
password_reset_dict = {
    'template_name': 'registration/password_reset_form.html',
    'email_template_name': 'registration/password_reset.txt',
    'SSL': settings.ENABLE_SSL,
}

urlpatterns += [
      url(r'^login/$', myviews.login_user,
      	      {'SSL': settings.ENABLE_SSL }, 'login'),

]

#from django.contrib.auth import views as authviews
#urlpatterns += [
      #(r'^login/$', LoginView.as_view(), {'SSL': settings.ENABLE_SSL }),
      #(r'^login/$', 'login',
      #	      {'template_name': 'registration/login.html', 'SSL': settings.ENABLE_SSL }, 'login'),
      #url(r'^password_reset/$', authviews.PasswordResetView, password_reset_dict, 'auth_password_reset'),
      #url(r'^reset/<uidb64>/<token>/', authviews.PasswordResetConfirmView.as_view(template_name="main/password/password_reset_confirm.html"), name='auth_password_reset'),

      #url(r'^password_reset/done/$', authviews.PasswordResetDoneView.as_view(template_name='registration/password_reset_done.html'), name='auth_password_reset_done'),
      #url(r'^password_change/$', authviews.PasswordChangeView, {'template_name':'registration/password_change_form.html', 'SSL': settings.ENABLE_SSL}, 'auth_password_change'),
      #url(r'^password_change/done/$', authviews.PasswordChangeDoneView, {'template_name':'registration/password_change_done.html', 'SSL': settings.ENABLE_SSL}, 'auth_change_done'),
      #url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>.+)/$', authviews.PasswordResetConfirmView, {'SSL': settings.ENABLE_SSL}),
      #url(r'^reset/done/$', authviews.PasswordResetCompleteView),
	  #url(r'^logout/$', authviews.LogoutView, name="logout") ,
	  #url(r'^password_change/$', authviews.PasswordChangeView, name="password_change") ,


#]
