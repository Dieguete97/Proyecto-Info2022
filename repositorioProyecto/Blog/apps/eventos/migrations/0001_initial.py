# Generated by Django 3.2 on 2022-09-02 01:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=60)),
                ('descripcion', models.CharField(blank=True, max_length=250, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Evento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=60)),
                ('fecha', models.CharField(max_length=60, null=True)),
                ('creado', models.DateField(auto_now_add=True)),
                ('modalidad', models.CharField(max_length=20, null=True)),
                ('lugar', models.CharField(max_length=60)),
                ('cuerpo', models.TextField()),
                ('categoria', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='eventos.categoria')),
            ],
        ),
    ]
