# Generated by Django 3.2.25 on 2024-10-18 14:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sub_blog', '0003_auto_20241018_1959'),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.AlterField(
            model_name='posts',
            name='slug',
            field=models.SlugField(editable=False, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='posts',
            name='Author_details',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='sub_blog.author'),
        ),
    ]