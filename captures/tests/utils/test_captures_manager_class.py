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

    @mock.patch('captures.utils.CapturesManager._mkdir')
    def test_capture_manager_mkdir_method(self, mkdir_mock):
        path = os.path.join(self.base_path, self.pack_key)
        mkdir_mock.return_value = path

        self.manager._mkdir(path)

    @mock.patch('captures.utils.CapturesManager.create_pack')
    def test_capture_manager_create_capture_pack(self, create_pack_mock):
        path = os.path.join(self.base_path, self.pack_key)

        create_pack_mock.return_value = path

        location = self.manager.create_pack(self.pack_key)

        self.assertEqual(location, path)

    @mock.patch('captures.utils.CapturesManager.create_pack')
    def test_capture_manager_create_already_exists(self, create_pack_mock):
        create_pack_mock.return_value = 'somepath'
        self.manager.create_pack(self.pack_key)

        create_pack_mock.side_effect = FileExistsError

        with self.assertRaises(FileExistsError):
            self.manager.create_pack(self.pack_key)

    @mock.patch('captures.utils.CapturesManager.exists_pack')
    @mock.patch('captures.utils.CapturesManager.create_pack')
    def test_capture_manager_check_exists_capture_pack(
            self, create_pack_mock, exists_pack_mock):

        exists_pack_mock.return_value = False
        create_pack_mock.return_value = 'somepath'

        exists_pack = self.manager.exists_pack(self.pack_key)

        self.assertFalse(exists_pack)

        self.manager.create_pack(self.pack_key)

        exists_pack_mock.return_value = True

        exists_pack = self.manager.exists_pack(self.pack_key)

        self.assertTrue(exists_pack)

    @mock.patch('captures.utils.CapturesManager.remove_pack')
    @mock.patch('captures.utils.CapturesManager.exists_pack')
    @mock.patch('captures.utils.CapturesManager.create_pack')
    def test_capture_manager_remove_capture_pack(
            self, create_pack_mock, exists_pack_mock, remove_pack_mock):

        create_pack_mock.return_value = 'somepath'
        exists_pack_mock.return_value = True
        remove_pack_mock.return_value = None

        self.manager.create_pack(self.pack_key)

        exists_pack = self.manager.exists_pack(self.pack_key)
        self.assertTrue(exists_pack)

        self.manager.remove_pack(self.pack_key)

        exists_pack_mock.return_value = False
        exists_pack = self.manager.exists_pack(self.pack_key)

        self.assertFalse(exists_pack)
