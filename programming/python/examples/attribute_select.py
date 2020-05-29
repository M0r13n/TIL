"""
Copy from https://stackoverflow.com/questions/23460857/create-selectfield-options-with-custom-attributes-in-wtforms

This is veeeery useful and I want to backup this code.

NOTE: This is not my own idea. Instead I took it from the link above.
"""

from wtforms.fields  import SelectField
from wtforms.widgets import Select, html_params, HTMLString

class AttribSelect(Select):
    """
    Renders a select field that supports options including additional html params.

    The field must provide an `iter_choices()` method which the widget will
    call on rendering; this method must yield tuples of
    `(value, label, selected, html_attribs)`.
    """

    def __call__(self, field, **kwargs):
        kwargs.setdefault('id', field.id)
        if self.multiple:
            kwargs['multiple'] = True
        html = ['<select %s>' % html_params(name=field.name, **kwargs)]
        for val, label, selected, html_attribs in field.iter_choices():
            html.append(self.render_option(val, label, selected, **html_attribs))
        html.append('</select>')
        return HTMLString(''.join(html))

class AttribSelectField(SelectField):
    widget = AttribSelect()

    def iter_choices(self):
        for value, label, render_args in self.choices:
            yield (value, label, self.coerce(value) == self.data, render_args)

    def pre_validate(self, form):
         if self.choices:
             for v, _, _ in self.choices:
                 if self.data == v:
                     break
             else:
                 raise ValueError(self.gettext('Is Not a valid choice'))
                 
                 
if __name__ == "__main__":
  choices = [('', 'select a name', dict(disabled='disabled'))]
  choices.append(('alex', 'Alex', dict()))
  select_field = AttribSelectField('name', choices=choices, default='')
  # output: <option disabled="disabled" selected ...
