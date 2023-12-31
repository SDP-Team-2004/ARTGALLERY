# Generated by Django 4.2.4 on 2023-11-24 07:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('adminapp', '0007_product_delete_photo'),
        ('artistapp', '0002_alter_artist_phone'),
    ]

    operations = [
        migrations.CreateModel(
            name='ArtistRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('action', models.CharField(choices=[('change_price', 'Change Price'), ('delete_product', 'Delete Product')], max_length=15)),
                ('new_price', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='adminapp.product')),
            ],
        ),
    ]
