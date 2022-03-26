# Generated by Django 4.0.2 on 2022-03-26 07:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ervin', '0005_company_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='custom_page_title',
            field=models.CharField(blank=True, help_text='The title to be displayed on the home page', max_length=50, verbose_name='custom page title'),
        ),
    ]