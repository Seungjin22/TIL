from django import template
import hashlib

register = template.Library()

@register.filter
def makemd5(email):
    return hashlib.md5(email.strip().lower().encode('utf-8')).hexdigest()