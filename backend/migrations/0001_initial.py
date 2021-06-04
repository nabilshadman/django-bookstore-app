# Generated by Django 3.1.1 on 2021-06-04 10:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book_title', models.CharField(max_length=200, unique=True)),
                ('authors', models.CharField(max_length=200)),
                ('book_type', models.CharField(choices=[('FI', 'Fiction'), ('NF', 'Non-fiction'), ('SC', 'Science')], default='NF', max_length=2)),
                ('price', models.FloatField(db_column='the_price', default=0)),
            ],
        ),
    ]