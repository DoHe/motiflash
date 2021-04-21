from django import template

register = template.Library()


@register.inclusion_tag('form.html')
def nice_form(form, action="post", hidden=None):
    if hidden is None:
        hidden = []
    return {
        'form': form,
        'action': action,
        'hidden': hidden,
    }
