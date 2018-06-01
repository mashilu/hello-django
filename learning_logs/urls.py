"""
定义learning_logs的URL模式
"""
from django.conf.urls import url
from learning_logs import views

urlpatterns = [
    # 主页
    url(r'^$', views.index, name='index'),

    # 显示所有主题
    url(r'^show_topics/$', views.show_topics, name='show_topics'),

    # 显示单个主题及其所有的条目
    url(r'^show_topic/(?P<topic_id>\d+)/$', views.show_topic, name='show_topic'),

    # 添加新主题
    url(r'^add_new_topic/$', views.add_new_topic, name='add_new_topic'),

    # 在特定的主题中添加新条目
    url(r'^add_new_entry/(?P<topic_id>\d+)/$', views.add_new_entry, name='add_new_entry'),

    # 编辑条目entry的页面
    url(r'^edit_entry/(?P<entry_id>\d+)/$', views.edit_entry, name='edit_entry'),
]