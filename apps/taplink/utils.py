import os
import hashlib


def image_upload_to(instance, filename):
    basename = os.path.basename(filename)
    root, ext = os.path.splitext(basename)
    hash_object = hashlib.md5(f"{root}".encode())
    return f'avatars/{instance}/{hash_object.hexdigest()}{ext}'
