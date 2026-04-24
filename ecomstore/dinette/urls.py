from django.conf.urls.defaults import *
from django.contrib.syndication.views import feed

from dinette.views import LatestTopicsByCategory,LatestRepliesOfTopic

feeds = {
   'category': LatestTopicsByCategory,
   'topic': LatestRepliesOfTopic
}

# Note:
# all these urls are included under '/forum/' in
# the main project urls.py file

from dinette import views as myviews

urlpatterns = [
    url(r'^$',myviews.index_page,name='dinette_category'),
    url(r'^new/$',myviews.new_topics,name='dinette_new_for_user'),
    url(r'^active/$',myviews.active,name='dinette_active'),
    url(r'^unasnwered/$',myviews.active,name='dinette_unanswered'),
    #Login page, needs to be before category_details, or gets caught by that regex.
    url(r'^login/$',myviews.login,name='dinette_login'),

    url(r'^search/$',myviews.search,name='dinette_search'),

    # user profile page
    url(r'^users/(?P<user_name>[\w-]+)/$', myviews.user_profile, name='dinette_user_profile'),

    url(r'^(?P<categoryslug>[\w-]+)/$',myviews.category_details, name='dinette_index'),
    url(r'^(?P<categoryslug>[\w-]+)/page(?P<pageno>\d+)/$',myviews.category_details, name='dinette_index2'),
    url(r'^post/topic/$',myviews.postTopic, name='dinette_posttopic'),
    url(r'^post/reply/$',myviews.postReply, name='dinette_postreply'),
    url(r'^(?P<categoryslug>[\w-]+)/(?P<topic_slug>[\w-]+)/$',myviews.topic_detail, name='dinette_topic_detail'),
    url(r'^(?P<categoryslug>[\w-]+)/(?P<topic_slug>[\w-]+)/page(?P<pageno>\d+)/$',myviews.topic_detail', name='dinette_reply_detail_paged'),

    #moderation views - Hence dont bother with SEF urls
    url(r'^moderate/topic/(?P<topic_id>\d+)/close/$',myviews.moderate_topic, {'action':'close'}, name='dinette_moderate_close'),
    url(r'^moderate/topic/(?P<topic_id>\d+)/stickyfy/$',myviews.moderate_topic, {'action':'sticky'}, name='dinette_moderate_sticky'),
    url(r'^moderate/topic/(?P<topic_id>\d+)/annoucement/$',myviews.moderate_topic, {'action':'announce'}, name='dinette_moderate_announce'),
    url(r'^moderate/topic/(?P<topic_id>\d+)/hide/$',myviews.moderate_topic, {'action':'hide'}, name='dinette_moderate_hide'),
]

from django.contrib.syndication.views import feed
urlpatterns += [
    url(r'^feeds/(?P<url>.*)/$', feed , {'feed_dict': feeds},name='dinette_feed_url'),
    url(r'^feeds/(?P<url>.*)/$', feed , {'feed_dict': feeds},name='dinette_topic_url'),
]
