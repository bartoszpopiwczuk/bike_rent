from django import forms
from .models import Issue
from bike_portfolio.models import Bicycle

field_formatting = "w-full bg-gray-600 bg-opacity-20 focus:bg-transparent focus:ring-2 focus:ring-yellow-900 rounded border border-gray-600 focus:border-yellow-500 text-base outline-none text-gray-100 py-1 px-3 leading-8 transition-colors duration-200 ease-in-out mb-4"


class AddIssueForm(forms.ModelForm):
    issue_description = forms.CharField(
        widget=forms.Textarea(
            attrs={
                "class": field_formatting,
                "rows": 4,
            }
        ),
        label="Describe the issue",
        max_length=1000,
    )
    issue_image = forms.ImageField(
        widget=forms.FileInput(
            attrs={
                "class": field_formatting,
            }
        ),
        label="Upload an image of the issue",
        required=False,
    )

    class Meta:
        model = Issue
        fields = ["issue_description", "issue_image"]


class AddBikeForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs["class"] = field_formatting

    class Meta:
        model = Bicycle
        fields = "__all__"
