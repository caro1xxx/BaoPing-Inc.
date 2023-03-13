from django.conf.urls import url, re_path
from main.views.support import Support
from main.views.voteuser import VoteUser, Comment, RecentVoteRecord, Feedback
from main.views.Request404 import Request404
from main.views.vote_target import VoteTarget
from main.views.vote_activity import AloneVoteActivity, TodayStar
from main.views.keys import Keys
from main.views.gift import Gift
from vote_front import settings
from main.views.Settings import Settings
from django.views.static import serve

urlpatterns = [
    re_path(r'^media/(?P<path>.*)$',serve,{
        'document_root':settings.MEDIA_ROOT
    }),
    url(r'^support/$', Support.Support.as_view()),
    url(r'^voteuser/$', VoteUser.VoteUser.as_view()),
    url(r'^recentvoterecord/$', RecentVoteRecord.RecentVoteRecord.as_view()),
    url(r'^votetarget/$', VoteTarget.VoteTarget.as_view()),
    url(r'^alonevoteactivity/$', AloneVoteActivity.AloneVoteActivity.as_view()),
    url(r'^keys/$', Keys.Keys.as_view()),
    url(r'^settings/$', Settings.as_view()),
    url(r'^comment/$', Comment.Comment.as_view()),
    url(r'^feedback/$', Feedback.Feedback.as_view()),
    url(r'^gift/$', Gift.Gift.as_view()),
    url(r'^todaystar/$', TodayStar.TodayStar.as_view()),
    url(r'$', Request404.as_view())
]