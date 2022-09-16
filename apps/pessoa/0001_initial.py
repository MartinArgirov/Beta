import email
from django.db import migrations, models

class Migration(migrations.Migration):
    initial = True

    dependencies = [

    ]

    operations = [
        migrations.CreateModel(
            name='Pessoa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False))
                ('nome', models.CharField(max_length=50)),
                ('idade', models.IntegerField()),
                ('nif', models.CharField(max_length=9)),
                ('email', models.EmailField(max_length=254)),
            ])
    ]