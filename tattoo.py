import os
import glob

from PIL import Image

class Tattoo:

    _default_extensions = [
        '*.jpg', '*.gif', '*.png'
    ]

    def __init__(self, watermark_file, files_folder=None, output_folder=None,
                 file_extensions=None):
        self.watermark_file = Image.open(watermark_file)
        self.files_folder = files_folder or self._current_folder()
        self.output_folder = output_folder or self._current_folder()
        self.file_extensions = file_extensions or self.default_extensions

        pass

    @property
    def default_extensions(self):
        return self._default_extensions

    def start(self):
        files = self.get_files()

        for file in files:
            name, ext = os.path.splitext(file)
            img = Image.open(file)
            img.paste(self.watermark_file, (25, 25))
            img.save(name + '.with-tatto.jpg', 'JPEG')


    def get_files(self):
        files = []
        os.chdir(self.files_folder)

        for extension in self.file_extensions:
            files.extend(glob.glob(extension))

        return files

    def _current_folder(self):
        return os.getcwd()


tattoo = Tattoo('C:/Users/User/Documents/imagens/logos/csharp.jpg', files_folder='C:/Users/User/Desktop/teste')
tattoo.start()
