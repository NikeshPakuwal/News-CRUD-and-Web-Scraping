# Generated by Django 3.1.3 on 2020-12-05 15:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('newsApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=99)),
            ],
        ),
        migrations.AlterField(
            model_name='newsdetails',
            name='newsChannel',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='newsdetails',
            name='newsDescription',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='newsdetails',
            name='newsTitle',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='newsdetails',
            name='newsCategory',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='newsApp.category'),
        ),
    ]
