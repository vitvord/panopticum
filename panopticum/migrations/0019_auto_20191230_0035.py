# Generated by Django 2.1 on 2019-12-29 21:35

from django.db import migrations, models
import django.db.models.deletion
import panopticum.models


class Migration(migrations.Migration):

    dependencies = [
        ('panopticum', '0018_auto_20191228_1758'),
    ]

    operations = [
        migrations.AddField(
            model_name='componentversionmodel',
            name='qa_anonymisation_tests_notes',
            field=panopticum.models.MarkupField(blank=True, default='', verbose_name=''),
        ),
        migrations.AddField(
            model_name='componentversionmodel',
            name='qa_anonymisation_tests_quality',
            field=panopticum.models.LowMedHighField(choices=[('unknown', '?'), ('n/a', 'N/A'), ('none', 'None'), ('low', 'Low'), ('med', 'Med'), ('high', 'High')], default='unknown', max_length=16, verbose_name=''),
        ),
        migrations.AddField(
            model_name='componentversionmodel',
            name='qa_anonymisation_tests_signoff',
            field=panopticum.models.SigneeField(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='signed_anonymisation_tests', to='panopticum.PersonModel', verbose_name=''),
        ),
        migrations.AddField(
            model_name='componentversionmodel',
            name='qa_upgrade_tests_notes',
            field=panopticum.models.MarkupField(blank=True, default='', verbose_name=''),
        ),
        migrations.AddField(
            model_name='componentversionmodel',
            name='qa_upgrade_tests_quality',
            field=panopticum.models.LowMedHighField(choices=[('unknown', '?'), ('n/a', 'N/A'), ('none', 'None'), ('low', 'Low'), ('med', 'Med'), ('high', 'High')], default='unknown', help_text='Functional, performance, real volume', max_length=16, verbose_name=''),
        ),
        migrations.AddField(
            model_name='componentversionmodel',
            name='qa_upgrade_tests_signoff',
            field=panopticum.models.SigneeField(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='signed_upgrade_tests', to='panopticum.PersonModel', verbose_name=''),
        ),
        migrations.AlterField(
            model_name='componentversionmodel',
            name='compliance_applicable',
            field=models.BooleanField(default=True, verbose_name='Compliance requirements are applicable'),
        ),
        migrations.AlterField(
            model_name='componentversionmodel',
            name='dev_build_jenkins_job',
            field=panopticum.models.URLsField(blank=True, default='', help_text='Multiple links allowed', max_length=2048, verbose_name=''),
        ),
        migrations.AlterField(
            model_name='componentversionmodel',
            name='dev_commit_link',
            field=panopticum.models.URLsField(blank=True, default='', help_text='Multiple links allowed', max_length=2048, verbose_name=''),
        ),
        migrations.AlterField(
            model_name='componentversionmodel',
            name='dev_database',
            field=models.ManyToManyField(blank=True, to='panopticum.DatabaseVendorModel', verbose_name='Supported Databases'),
        ),
        migrations.AlterField(
            model_name='componentversionmodel',
            name='dev_docs',
            field=panopticum.models.URLsField(blank=True, default='', help_text='Multiple links allowed', max_length=2048, verbose_name=''),
        ),
        migrations.AlterField(
            model_name='componentversionmodel',
            name='dev_framework',
            field=models.ManyToManyField(blank=True, to='panopticum.FrameworkModel', verbose_name='Frameworks'),
        ),
        migrations.AlterField(
            model_name='componentversionmodel',
            name='dev_jira_component',
            field=panopticum.models.URLsField(blank=True, default='', help_text='Multiple links allowed', max_length=2048, verbose_name=''),
        ),
        migrations.AlterField(
            model_name='componentversionmodel',
            name='dev_language',
            field=models.ManyToManyField(blank=True, to='panopticum.ProgrammingLanguageModel', verbose_name='Language'),
        ),
        migrations.AlterField(
            model_name='componentversionmodel',
            name='dev_logging',
            field=models.ManyToManyField(blank=True, to='panopticum.LoggerModel', verbose_name='Logging framework'),
        ),
        migrations.AlterField(
            model_name='componentversionmodel',
            name='dev_orm',
            field=models.ManyToManyField(blank=True, to='panopticum.ORMModel', verbose_name='ORM'),
        ),
        migrations.AlterField(
            model_name='componentversionmodel',
            name='dev_public_docs',
            field=panopticum.models.URLsField(blank=True, default='', help_text='Multiple links allowed', max_length=2048, verbose_name=''),
        ),
        migrations.AlterField(
            model_name='componentversionmodel',
            name='dev_public_repo',
            field=panopticum.models.URLsField(blank=True, default='', help_text='Multiple links allowed', max_length=2048, verbose_name=''),
        ),
        migrations.AlterField(
            model_name='componentversionmodel',
            name='dev_raml',
            field=panopticum.models.URLsField(blank=True, default='', help_text='Multiple links allowed', max_length=2048, verbose_name=''),
        ),
        migrations.AlterField(
            model_name='componentversionmodel',
            name='dev_repo',
            field=panopticum.models.URLsField(blank=True, default='', help_text='Multiple links allowed', max_length=2048, verbose_name=''),
        ),
        migrations.AlterField(
            model_name='componentversionmodel',
            name='locations',
            field=models.ManyToManyField(blank=True, help_text='possible component deployment locations', related_name='component_versions', to='panopticum.DeploymentLocationClassModel'),
        ),
        migrations.AlterField(
            model_name='componentversionmodel',
            name='meta_update_date',
            field=models.DateTimeField(db_index=True),
        ),
        migrations.AlterField(
            model_name='componentversionmodel',
            name='mt_applicable',
            field=models.BooleanField(default=True, verbose_name='Maintainability requirements are applicable'),
        ),
        migrations.AlterField(
            model_name='componentversionmodel',
            name='mt_logging_format_status',
            field=panopticum.models.NoPartialYesField(choices=[('unknown', '?'), ('n/a', 'N/A'), ('no', 'No'), ('partial', 'Partial'), ('yes', 'Yes')], default='unknown', help_text='Logs have proper format', max_length=16, verbose_name=''),
        ),
        migrations.AlterField(
            model_name='componentversionmodel',
            name='mt_logging_sanitization_status',
            field=panopticum.models.NoPartialYesField(choices=[('unknown', '?'), ('n/a', 'N/A'), ('no', 'No'), ('partial', 'Partial'), ('yes', 'Yes')], default='unknown', help_text='Logs do not have sensitive information', max_length=16, verbose_name=''),
        ),
        migrations.AlterField(
            model_name='componentversionmodel',
            name='op_applicable',
            field=models.BooleanField(default=True, verbose_name='Operational requirements are applicable'),
        ),
        migrations.AlterField(
            model_name='componentversionmodel',
            name='qa_api_tests_quality',
            field=panopticum.models.LowMedHighField(choices=[('unknown', '?'), ('n/a', 'N/A'), ('none', 'None'), ('low', 'Low'), ('med', 'Med'), ('high', 'High')], default='unknown', help_text='Completeness, coverage, quality', max_length=16, verbose_name=''),
        ),
        migrations.AlterField(
            model_name='componentversionmodel',
            name='qa_applicable',
            field=models.BooleanField(default=True, verbose_name='Tests requirements are applicable'),
        ),
        migrations.AlterField(
            model_name='componentversionmodel',
            name='qa_e2e_tests_quality',
            field=panopticum.models.LowMedHighField(choices=[('unknown', '?'), ('n/a', 'N/A'), ('none', 'None'), ('low', 'Low'), ('med', 'Med'), ('high', 'High')], default='unknown', help_text='Completeness, coverage, quality', max_length=16, verbose_name=''),
        ),
        migrations.AlterField(
            model_name='componentversionmodel',
            name='qa_longhaul_tests_quality',
            field=panopticum.models.LowMedHighField(choices=[('unknown', '?'), ('n/a', 'N/A'), ('none', 'None'), ('low', 'Low'), ('med', 'Med'), ('high', 'High')], default='unknown', help_text='Completeness, coverage, quality', max_length=16, verbose_name=''),
        ),
        migrations.AlterField(
            model_name='componentversionmodel',
            name='qa_manual_tests_quality',
            field=panopticum.models.LowMedHighField(choices=[('unknown', '?'), ('n/a', 'N/A'), ('none', 'None'), ('low', 'Low'), ('med', 'Med'), ('high', 'High')], default='unknown', help_text='Completeness, coverage, quality', max_length=16, verbose_name=''),
        ),
        migrations.AlterField(
            model_name='componentversionmodel',
            name='qa_perf_tests_quality',
            field=panopticum.models.LowMedHighField(choices=[('unknown', '?'), ('n/a', 'N/A'), ('none', 'None'), ('low', 'Low'), ('med', 'Med'), ('high', 'High')], default='unknown', help_text='Completeness, coverage, quality', max_length=16, verbose_name=''),
        ),
        migrations.AlterField(
            model_name='componentversionmodel',
            name='qa_security_tests_quality',
            field=panopticum.models.LowMedHighField(choices=[('unknown', '?'), ('n/a', 'N/A'), ('none', 'None'), ('low', 'Low'), ('med', 'Med'), ('high', 'High')], default='unknown', help_text='Completeness, coverage, quality', max_length=16, verbose_name=''),
        ),
        migrations.AlterField(
            model_name='componentversionmodel',
            name='qa_unit_tests_quality',
            field=panopticum.models.LowMedHighField(choices=[('unknown', '?'), ('n/a', 'N/A'), ('none', 'None'), ('low', 'Low'), ('med', 'Med'), ('high', 'High')], default='unknown', help_text='Completeness, coverage, quality', max_length=16, verbose_name=''),
        ),
        migrations.AlterField(
            model_name='componentversionmodel',
            name='version',
            field=models.CharField(help_text='note: component version instance will be cloned if you change version!', max_length=64, verbose_name='Version or build'),
        ),
        migrations.AlterField(
            model_name='datacentermodel',
            name='grafana',
            field=panopticum.models.URLsField(blank=True, default='', max_length=2048, verbose_name=''),
        ),
        migrations.AlterField(
            model_name='datacentermodel',
            name='info',
            field=panopticum.models.URLsField(blank=True, default='', max_length=2048, verbose_name=''),
        ),
        migrations.AlterField(
            model_name='datacentermodel',
            name='metrics',
            field=panopticum.models.URLsField(blank=True, default='', max_length=2048, verbose_name=''),
        ),
    ]
