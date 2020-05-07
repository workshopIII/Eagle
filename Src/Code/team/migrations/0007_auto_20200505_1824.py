# Generated by Django 2.2.2 on 2020-05-05 10:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('team', '0006_remove_team_leader'),
    ]

    operations = [
        migrations.AddField(
            model_name='team',
            name='leader',
            field=models.IntegerField(default=0),
        ),
        migrations.CreateModel(
            name='Vote',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vote_id', models.IntegerField(default=0)),
                ('member', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('team', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='team.Team')),
            ],
        ),
    ]