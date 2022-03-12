from django.db import models
from django.contrib.auth.models import AbstractUser, Group, UserManager

class ErvinUserManager(UserManager):
    def get_by_natural_key(self, username):
        case_insensitive_username_field = '{}__iexact'.format(self.model.USERNAME_FIELD)
        return self.get(**{case_insensitive_username_field: username})

class ErvinUser(AbstractUser):
    objects = ErvinUserManager()
    verbose_name = 'user'

class ErvinGroup(Group):

    grp_order = models.IntegerField('Order Number', default=1, help_text='Where this group should appear on a list')

    class Meta:
        verbose_name='group'
        ordering = ['grp_order']


# vim: ai ts=4 sts=4 et sw=4

