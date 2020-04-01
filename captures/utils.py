import os
import os.path


class CapturesManager:
    def __init__(self, base_path='./'):
        self.base_path = base_path

    def create_pack(self, key):
        path = self._join_with_base_path(key)
        self._mkdir(path)
        return path

    def exists_pack(self, key):
        path = self._join_with_base_path(key)
        return os.path.exists(path)

    def remove_pack(self, key):
        path = self._join_with_base_path(key)
        os.rmdir(path)

    def _join_with_base_path(self, key):
        return os.path.join(self.base_path, key)

    def _mkdir(self, path):
        os.mkdir(path)
