# Generated by Django 2.0.10 on 2019-01-09 05:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('Author_Name', models.CharField(max_length=200)),
                ('AuthorRating', models.CharField(max_length=200)),
                ('AuthorInfo', models.CharField(max_length=200)),
            ],
            options={
                'db_table': 'Author_Info',
            },
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('Name', models.CharField(max_length=255)),
                ('cost', models.DecimalField(decimal_places=4, max_digits=10)),
                ('currency', models.CharField(max_length=200)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Details_App.Author')),
            ],
            options={
                'db_table': 'Book_Info',
            },
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('Gen_Name', models.CharField(max_length=255)),
                ('Gen_Details', models.CharField(max_length=255)),
                ('Gen_slug', models.SlugField(max_length=255)),
            ],
            options={
                'db_table': 'Genre_Info',
            },
        ),
        migrations.CreateModel(
            name='SubGenre',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('Sub_Gen_Name', models.CharField(max_length=255)),
                ('Sub_Gen_Description', models.CharField(max_length=255)),
                ('Sub_Gen_Slug', models.SlugField(max_length=255)),
                ('Genre', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Details_App.Genre')),
            ],
            options={
                'db_table': 'SubGenre_Info',
            },
        ),
        migrations.AddField(
            model_name='author',
            name='subGen',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Details_App.SubGenre'),
        ),
    ]
