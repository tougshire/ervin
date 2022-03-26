from django.db import models
from django.contrib.auth.models import AbstractUser, Group, UserManager

class ErvinUserManager(UserManager):
    def get_by_natural_key(self, username):
        case_insensitive_username_field = '{}__iexact'.format(self.model.USERNAME_FIELD)
        return self.get(**{case_insensitive_username_field: username})

class Company(models.Model):
    name = models.CharField(
        'name',
        max_length=60,
        help_text="The company name",
    )
    custom_logo = models.FileField(
        'custom logo',
        blank=True,
        null=True,
        help_text='What logo will be used for members in this group?')

    custom_header_image = models.FileField(
        'custom header image',
        blank=True,
        null=True,
        help_text='What header will be used for members in this group?')

    custom_page_title = models.CharField(
        'custom page title',
        blank=True,
        max_length=50,
        help_text="The title to be displayed on the home page"
    )

    custom_page_subtitle = models.CharField(
        'custom page subtitle',
        blank=True,
        max_length=50,
        help_text="The subtitle to be displayed on the home page"
    )

    custom_colorscheme = models.CharField(
        'custom color scheme',
        choices=(("blue","blue"),),
        blank=True,
        max_length=20,
        help_text="The color scheme to be used"
    )

    def __str__(self):
        return self.name

class ErvinUser(AbstractUser):
    objects = ErvinUserManager()
    verbose_name = 'user'

    company = models.ForeignKey(
        Company,
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        help_text="What is this user's company"
    )

    def get_custom_logo(self):
        return self.company.custom_logo if self.company is not None else None

    def get_custom_header_image(self):
        return self.company.custom_header_image if self.company is not None else None

    def get_custom_page_title(self):
        return self.company.custom_page_title if self.company is not None else None

    def get_custom_page_subtitle(self):
        return self.company.custom_page_subtitle if self.company is not None else None

    def get_custom_page_subtitle(self):
        return self.company.custom_page_subtitle if self.company is not None else None

    def get_custom_colorscheme(self):
        return self.company.custom_colorscheme if self.company is not None else None

class ErvinGroup(Group):

    grp_order = models.IntegerField('Order Number', default=1, help_text='Where this group should appear on a list')

    class Meta:
        verbose_name='group'
        ordering = ['grp_order']


# vim: ai ts=4 sts=4 et sw=4

