# Generated by Django 4.0.6 on 2022-07-19 13:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('accounts', '0003_rename_transactiontags_transactiontag_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='owner',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='account', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='transactiontag',
            name='owner',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='transaction_tag', to=settings.AUTH_USER_MODEL),
        ),
    ]
