import os
import zipfile
from wsgiref.util import FileWrapper

from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import FormView

from progress_multiple_upload.forms import FilesUploadForm
from progress_multiple_upload.utils import collect_unique_lines, save_file


class UploadFilesView(FormView):
    form_class = FilesUploadForm
    template_name = "upload_files.html"

    def post(self, request, *args, **kwargs):
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        files = request.FILES.getlist('files')

        if form.is_valid():
            i = 0
            os.system('rm -rf %s' % os.path.join(settings.MEDIA_ROOT, '*'))
            if len(files) == 1 and zipfile.is_zipfile(files[0]):
                zfile = zipfile.ZipFile(files[0])
                zfile.extractall(settings.MEDIA_ROOT)
                zfile.close()
            else:
                for f in files:
                    i += 1
                    name = 'file-%s' % i
                    save_file(f, name)

            if collect_unique_lines() == 0:
                path = os.path.join(settings.MEDIA_ROOT, 'result.txt')
                wrapper = FileWrapper(open(path, 'rb'))
                response = HttpResponse(wrapper, content_type='text/plain')
                response['Content-Length'] = os.path.getsize(path)
                response['Content-Disposition'] = 'attachment; filename="result.txt"'
                return response

        message = 'Случилась что-то непредвиденное.'
        return render(request, self.template_name, {'form': form, 'message': message})
