# image_filters.py

from django import template
import base64

register = template.Library()

@register.filter
def base64_encode(value):
    # Convert the input value to bytes if it's a string
    if isinstance(value, str):
        value = value.encode('utf-8')
    
    # Perform Base64 encoding and return the result as a string
    return base64.b64encode(value).decode('utf-8')
