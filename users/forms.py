from crispy_forms.helper import FormHelper
from crispy_forms.layout import Column, Layout, Row, Submit
from django import forms
from django.utils.translation import gettext_lazy as _
from django_ckeditor_5.widgets import CKEditor5Widget

from .models import LunUser


class LunUserForm(forms.ModelForm):
    class Meta:
        model = LunUser
        fields = [
            "first_name",
            "last_name",
            "bio",
            "birth_date",
        ]
        widgets = {
            "first_name": forms.TextInput(attrs={"placeholder": _("e.g. Mykola")}),
            "last_name": forms.TextInput(attrs={"placeholder": _("e.g. Shkredov")}),
            "bio": CKEditor5Widget(config_name="default"),
            "birth_date": forms.DateInput(attrs={"type": "date"}),
        }
        labels = {
            "first_name": _("First name"),
            "last_name": _("Last name"),
            "bio": _("Bio"),
            "birth_date": _("Birth date"),
        }

    def __init__(self, *args: tuple, **kwargs: dict) -> None:
        super(LunUserForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_method = "post"
        self.helper.layout = Layout(
            Row(
                Column("first_name", css_class="col s6"),
                Column("last_name", css_class="col s6"),
            ),
            Row(
                Column("bio", css_class="col s12"),
            ),
            Row(
                Column("birth_date", css_class="col s12"),
            ),
            Submit(
                "submit",
                "Update",
                css_class="btn waves-effect waves-light submit-button",
            ),
        )
        self.field_order = [
            "first_name",
            "last_name",
            "bio",
            "birth_date",
        ]
