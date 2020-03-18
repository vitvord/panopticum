# Generated by Django 2.1.15 on 2020-03-18 11:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('panopticum', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='RuntimeModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Runtime: e.g. C++/Python/Go runtime', max_length=64)),
            ],
            options={
                'verbose_name': 'Runtime',
                'verbose_name_plural': 'Runtimes',
                'ordering': ['name'],
            },
        ),
        migrations.RenameModel(
            old_name='ComponentRuntimeTypeModel',
            new_name='ComponentType',
        ),
        migrations.AlterModelOptions(
            name='componentcategorymodel',
            options={'ordering': ['order', 'name']},
        ),
        migrations.AlterModelOptions(
            name='frameworkmodel',
            options={'ordering': ['name'], 'verbose_name': 'Framework', 'verbose_name_plural': 'Frameworks'},
        ),
        migrations.AlterModelOptions(
            name='loggermodel',
            options={'ordering': ['name'], 'verbose_name': 'Logger', 'verbose_name_plural': 'Loggers'},
        ),
        migrations.AlterModelOptions(
            name='ormmodel',
            options={'ordering': ['name'], 'verbose_name': 'Object-Relational Mapping', 'verbose_name_plural': 'Object-Relational Mappings'},
        ),
        migrations.AlterModelOptions(
            name='programminglanguagemodel',
            options={'ordering': ['name'], 'verbose_name': 'Programming language', 'verbose_name_plural': 'Programming language'},
        ),
        migrations.RenameField(
            model_name='componentmodel',
            old_name='runtime_type',
            new_name='type',
        ),
        migrations.AddField(
            model_name='componentdeploymentmodel',
            name='is_new_deployment',
            field=models.BooleanField(db_index=True, default=False, help_text='This component is new in given product'),
        ),
        migrations.AlterField(
            model_name='componentmodel',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='components', to='panopticum.ComponentCategoryModel'),
        ),
        migrations.AddField(
            model_name='runtimemodel',
            name='language',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='panopticum.ProgrammingLanguageModel'),
        ),
        migrations.AddField(
            model_name='componentdeploymentmodel',
            name='runtime',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='deployments', to='panopticum.RuntimeModel'),
        ),
    ]
