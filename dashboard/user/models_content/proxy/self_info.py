from user.models_content.user import User
from django.utils.translation import gettext_lazy as _
from django.utils.safestring import mark_safe


class UserSelfInfoProxy(User):

    def user_name(self):
        return self.username
    user_name.short_description = _('User Name')

    def change_password(self):
        return mark_safe('<a href="/password_change/" target="_blank">{}</a>'.format(_('Click to change password'))) 
    change_password.short_description = _('Password')

    def client_name(self):
        return "{} {}".format(self.first_name, self.last_name)
    client_name.short_description = _('Client Name')
    
    class Meta:
        proxy = True
        verbose_name = _('user detail')
        verbose_name_plural = _('user detail')
