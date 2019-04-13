from django.utils.translation import ugettext_lazy as _
from jet.dashboard import modules
from jet.dashboard.dashboard import DefaultAppIndexDashboard

from common.models import News


class CustomerIndexDashboard(DefaultAppIndexDashboard):
    columns = 1

    def init_with_context(self, context):
        self.available_children.append(modules.LinkList)

        self.children.append(modules.LinkList(
            title=_('Announcement'),
            children=self.get_news(),
            column=0,
            order=0
        ))
    """
    def render_tools(self):
        return ''
    """

    def get_news(self):
        news_list = []

        for news in News.objects.order_by('-created_at')[:5]:
            news_list.append({
                'title': news.title,
                'url': '/common/news/{}'.format(news.id),
                'external': False,
            })
        return news_list
