from dataclasses import field
from django import forms
from django.forms import ModelForm
from django import forms
from .models import Project

class ProjectForm(ModelForm):
    class Meta:
        model = Project
        # If we put field='__all__' it'll create a field for all the data in the Project model from models.py (imported from .models)
        fields = ['title', 'featured_image', 'description', 'demo_link', 'source_link', 'tags']

        # This is how we make fields checkboxes:
        widgets = {
            'tags':forms.CheckboxSelectMultiple(),
        }


    # Here we update the classes of the elements in the fields defined in the model
    def __init__(self, *args, **kwargs):
        super(ProjectForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class':'input input--text'})

        # self.fields['title'].widget.attrs.update({'class':'input input--text', 'placeholder':'Add title'})
        # self.fields['description'].widget.attrs.update({'class':'input input--text', 'placeholder':'Description'})