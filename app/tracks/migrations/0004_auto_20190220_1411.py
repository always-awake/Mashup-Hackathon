# Generated by Django 2.1.3 on 2019-02-20 14:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tracks', '0003_auto_20190218_0554'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tracklike',
            name='track',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='tracklikes', to='tracks.Track'),
        ),
    ]
