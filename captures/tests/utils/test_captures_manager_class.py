import os
import uuid
from unittest import TestCase, mock
from captures.utils import CapturesManager
from serissa.settings import BASE_DIR


class TestCapturesManagerClass(TestCase):

    def setUp(self):
        self.base_path = BASE_DIR.child('media').child('captures')
        self.manager = CapturesManager(base_path=self.base_path)
        self.pack_key = str(uuid.uuid4())

    def test_capture_manager_instance(self):
        self.assertIsInstance(self.manager, CapturesManager)

    def test_capture_manager_instance_with_default_args(self):
        manager = CapturesManager()
        self.assertEquals(manager.base_path, './')

    def test_capture_manager_join_with_base_path(self):
        self.assertEqual(
            self.manager._join_with_base_path(self.pack_key),
            os.path.join(self.base_path, self.pack_key)
        )

    @mock.patch('captures.utils.os.mkdir')
    def test_capture_manager_create_capture_pack(self, os_mkdir_mock):
        path = os.path.join(self.base_path, self.pack_key)

        os_mkdir_mock.return_value = None

        location = self.manager.create_pack(self.pack_key)

        self.assertEqual(location, path)

    @mock.patch('captures.utils.os.mkdir')
    def test_capture_manager_create_already_exists(self, os_mkdir_mock):
        os_mkdir_mock.return_value = None
        self.manager.create_pack(self.pack_key)

        os_mkdir_mock.side_effect = FileExistsError

        with self.assertRaises(FileExistsError):
            self.manager.create_pack(self.pack_key)

    @mock.patch('captures.utils.os.path.exists')
    @mock.patch('captures.utils.os.mkdir')
    def test_capture_manager_check_exists_capture_pack(
            self, os_mkdir_mock, os_path_exists_mock):

        os_path_exists_mock.return_value = False
        os_mkdir_mock.return_value = None

        exists_pack = self.manager.exists_pack(self.pack_key)

        self.assertFalse(exists_pack)

        self.manager.create_pack(self.pack_key)

        os_path_exists_mock.return_value = True

        exists_pack = self.manager.exists_pack(self.pack_key)

        self.assertTrue(exists_pack)

    @mock.patch('captures.utils.os.rmdir')
    @mock.patch('captures.utils.os.path.exists')
    @mock.patch('captures.utils.os.mkdir')
    def test_capture_manager_remove_capture_pack(
            self, os_mkdir_mock, os_path_exists_mock, os_rmdir_mock):

        os_mkdir_mock.return_value = None
        os_path_exists_mock.return_value = True
        os_rmdir_mock.return_value = None

        self.manager.create_pack(self.pack_key)

        exists_pack = self.manager.exists_pack(self.pack_key)
        self.assertTrue(exists_pack)

        self.manager.remove_pack(self.pack_key)

        os_path_exists_mock.return_value = False
        exists_pack = self.manager.exists_pack(self.pack_key)

        self.assertFalse(exists_pack)
