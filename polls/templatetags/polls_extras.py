from django import template
from ..models import DecorationZone

register = template.Library()

@register.filter
def get_zone(zones, zone_id):
    return zones.get(str(zone_id))
