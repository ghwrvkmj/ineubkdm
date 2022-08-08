
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [

        ('home', '0005_order'),
    ]






    operations = [
        migrations.CreateModel(
            name='TrackUpdate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_id', models.CharField(default='', max_length=900)),
                ('update', models.CharField(default='', max_length=9000)),
                ('daysleft', models.CharField(default='', max_length=9000)),
      
            ],
        ),
    ]

