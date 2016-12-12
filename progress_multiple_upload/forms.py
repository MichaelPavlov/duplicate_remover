from django.forms import Form, FileField, ClearableFileInput
from crispy_forms.helper import FormHelper


class FilesUploadForm(Form):
    files = FileField(widget=ClearableFileInput(attrs={'multiple': True}))

    def __init__(self, *args, **kwargs):
        super(FilesUploadForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-lg-2'
        self.helper.field_class = 'col-lg-8'

        # self.helper.layout



