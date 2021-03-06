# Generated by Django 4.0.3 on 2022-04-07 02:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_pos'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pos',
            old_name='Question_word_counter',
            new_name='Question_word',
        ),
        migrations.RenameField(
            model_name='pos',
            old_name='adjective_counter',
            new_name='adjective',
        ),
        migrations.RenameField(
            model_name='pos',
            old_name='adverb_counter',
            new_name='adverb',
        ),
        migrations.RenameField(
            model_name='pos',
            old_name='article_counter',
            new_name='article',
        ),
        migrations.RenameField(
            model_name='pos',
            old_name='noun_counter',
            new_name='noun',
        ),
        migrations.RenameField(
            model_name='pos',
            old_name='pronoun_counter',
            new_name='pronoun',
        ),
        migrations.RenameField(
            model_name='pos',
            old_name='proposition_counter',
            new_name='proposition',
        ),
        migrations.RenameField(
            model_name='pos',
            old_name='punctation_counter',
            new_name='punctation',
        ),
        migrations.RenameField(
            model_name='pos',
            old_name='sentence_counter',
            new_name='sentence',
        ),
        migrations.RenameField(
            model_name='pos',
            old_name='space_counter',
            new_name='space',
        ),
        migrations.RenameField(
            model_name='pos',
            old_name='verb_counter',
            new_name='verb',
        ),
    ]
