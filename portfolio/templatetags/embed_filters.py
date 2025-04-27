# portfolio/templatetags/embed_filters.py
from django import template
import re

register = template.Library()

@register.filter
def video_embed_url(url):
    m = re.search(r'youtu\.be/([^?&]+)', url)
    if m:
        video_id = m.group(1)
        return f'https://www.youtube.com/embed/{video_id}'
    # YouTube normal link
    m = re.search(r'v=([^?&]+)', url)
    if m:
        video_id = m.group(1)
        return f'https://www.youtube.com/embed/{video_id}'
    # Vimeo (exemplo)
    m = re.search(r'vimeo\.com/(\d+)', url)
    if m:
        video_id = m.group(1)
        return f'https://player.vimeo.com/video/{video_id}'
    # Outro caso: retorna original
    return url
