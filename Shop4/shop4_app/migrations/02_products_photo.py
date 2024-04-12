from django.db import migrations, models

class Migration(migrations.Migration):

    dependencies = [
        ('shop4_app', '01_initional'),
    ]

    operations = [
        migrations.AddField(
            model_name = 'product',
            name = 'photo',
            field = models.ImageField(blank=True, null=True, upload_to='product_photos/'),
        ),
    ]