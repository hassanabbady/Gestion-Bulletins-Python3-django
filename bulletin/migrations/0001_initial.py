# Generated by Django 3.2.8 on 2021-10-29 09:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Classe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nomClasse', models.CharField(max_length=190, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Eleve',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=190, null=True)),
                ('prenom', models.CharField(max_length=190, null=True)),
                ('classe', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='bulletin.classe')),
            ],
        ),
        migrations.CreateModel(
            name='Matiere',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nomMatiere', models.CharField(max_length=190, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Note',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lanote', models.FloatField(null=True)),
                ('semestre', models.CharField(choices=[('semestre1', 'Semestre 1'), ('semestre2', 'Semestre 2')], max_length=100, null=True)),
                ('classe', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='bulletin.classe')),
                ('eleve', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='bulletin.eleve')),
                ('matiere', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='bulletin.matiere')),
            ],
        ),
    ]