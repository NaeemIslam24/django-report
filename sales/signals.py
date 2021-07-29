from . models import Sale
from django.db.models.signals import m2m_changed
from django.dispatch import receiver


@receiver(m2m_changed, sender=Sale.position.through)
def calculate_all_price(sender, action, instance, **kwargs):

    totol_price = 0
    if action == 'post_add' or action == 'post_remove':
        # for item in instance.position():
        print('hi')
