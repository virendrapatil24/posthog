# Generated by Django 4.2.15 on 2024-09-17 13:14

from django.db import migrations
import posthog.helpers.encrypted_fields


class Migration(migrations.Migration):
    dependencies = [
        ("posthog", "0475_alter_externaldatasource_source_type"),
    ]

    operations = [
        migrations.AlterField(
            model_name="integration",
            name="sensitive_config",
            field=posthog.helpers.encrypted_fields.EncryptedJSONField(default=dict),
        ),
    ]
