"""
定义learning_logs的URL模式
"""
from django.conf.urls import url
from learning_logs import views

urlpatterns = [
    # 主页
    url(r'^$', views.index, name='index'),
    url(r'^topics/$', views.topics, name='topics'),
    url(r'^topics/(?P<topic_id>\d+)/$', views.topic, name='topic'),
    url(r'^new_topic/$', views.new_topic, name='new_topic'),

    # 添加新条目的页面
    url(r'^add_entry/(?P<topic_id>\d+)/$', views.add_entry, name='add_entry'),

    # 编辑条目entry的页面
    url(r'^edit_entry/(?P<entry_id>\d+)/$', views.edit_entry, name='edit_entry'),
]