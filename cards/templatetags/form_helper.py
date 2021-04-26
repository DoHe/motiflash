from django import template

import json

register = template.Library()


@register.inclusion_tag('form.html')
def nice_form(
    form,
    method="post",
    hidden='{}',
    extra_classes='{}',
    custom_inputs='{}',
):
    hidden = json.loads(hidden)
    extra_classes = json.loads(extra_classes)
    custom_inputs = json.loads(custom_inputs)
    return {
        'form': form,
        'method': method,
        'hidden': hidden,
        'extra_classes': extra_classes,
        'custom_inputs': custom_inputs,
    }
