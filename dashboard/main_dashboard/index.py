from django.utils.translation import ugettext_lazy as _
from jet.dashboard import modules
from jet.dashboard.models import UserDashboardModule
from jet.dashboard.dashboard import DefaultAppIndexDashboard

from common.models import News


class NewsLinkList(modules.LinkList):
    template = 'admin/news_list.html'


class CustomerIndexDashboard(DefaultAppIndexDashboard):
    columns = 1
    draggable = False
    deletable = False

    def init_with_context(self, context):
        self.available_children.append(NewsLinkList)

        self.children.append(NewsLinkList(
            title=_('Announcement'),
            children=self.get_news(),
            column=0,
            order=0,
            draggable=False,
            deletable=False,
            collapsible=False,
        ))
    
    def render_tools(self):
        return ''

    def load_modules(self):
        """
        Ingore the dashboard loading operations.
        """
        module_models = []

        for i, module in enumerate(self.children):
            column = module.column if module.column is not None else i % self.columns
            order = module.order if module.order is not None else int(i / self.columns)
            module_models.append(UserDashboardModule(
                id=0,  # dummy id
                title=module.title,
                app_label=self.app_label,
                user=self.context['request'].user.pk,
                module=module.fullname(),
                column=column,
                order=order,
                settings=module.dump_settings(),
                children=module.dump_children()
            ))
            i += 1

        loaded_modules = []

        for module_model in module_models:
            module_cls = module_model.load_module()
            if module_cls is not None:
                module = module_cls(model=module_model, context=self.context)
                loaded_modules.append(module)

        self.modules = loaded_modules

    def get_news(self):
        news_list = []

        for news in News.objects.order_by('-created_at')[:5]:
            news_list.append({
                'title': news.title,
                'url': '/common/news/{}'.format(news.id),
                'created_at': news.created_at.strftime('%Y年%m月%d日'),
                'content': news.content,
                'external': False,
            })
        return news_list
