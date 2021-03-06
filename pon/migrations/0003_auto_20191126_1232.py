# Generated by Django 2.2.6 on 2019-11-26 03:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pon', '0002_kategori_kuliner_kuliner'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='kategori_kuliner',
            options={'ordering': ('id_kk',)},
        ),
        migrations.AlterModelOptions(
            name='kota',
            options={'ordering': ('id_kota',)},
        ),
        migrations.AlterModelOptions(
            name='kuliner',
            options={'ordering': ('id_kuliner',)},
        ),
        migrations.CreateModel(
            name='Item_Kuliner',
            fields=[
                ('id_item', models.AutoField(primary_key=True, serialize=False)),
                ('item', models.CharField(max_length=250)),
                ('harga', models.DecimalField(decimal_places=0, max_digits=12)),
                ('available', models.CharField(choices=[('tersedia', 'Tersedia'), ('tidak tersedia', 'Tidak Tersedia')], default='tersedia', max_length=30)),
                ('kuliner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pon.Kuliner')),
            ],
            options={
                'ordering': ('id_item',),
            },
        ),
    ]
