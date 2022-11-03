from django.core.exceptions import ValidationError
import os

def audio_file_validator(file):
    if not file:
        raise ValidationError("Couldn't read uploaded file")

    if not os.path.splitext(file.name)[1] in [".mp3",".wav"]:
        raise ValidationError("Doesn't have proper extension")

    return file
