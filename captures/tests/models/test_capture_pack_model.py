from unittest import mock
from uuid import uuid4
from django.test import TestCase
from model_bakery import baker
from captures.models import CapturePack
from captures.utils import CapturesManager
from users.models import UserProfile


class TestCapturePackModel(TestCase):

    def setUp(self):
        self.profile = baker.make(UserProfile)
        self.capture_pack = CapturePack(profile=self.profile)

    def test_capture_pack_instance(self):
        self.assertIsInstance(
            self.capture_pack,
            CapturePack
        )

    def test_capture_pack_fields(self):
        capture_pack_fields = [f.name for f in self.capture_pack._meta.local_fields]

        expected_fields = [
            'id',
            'profile',
            'path',
            'created_at',
            'updated_at',
            'is_active'
        ]

        self.assertEqual(
            set(capture_pack_fields),
            set(expected_fields)
        )

    def test_capture_pack_set_file_manager(self):
        self.capture_pack.set_captures_file_manager(CapturesManager())
        self.assertIsInstance(
            self.capture_pack._file_manager,
            CapturesManager
        )

    def test_capture_pack_set_non_capture_file_manager_object(self):
        with self.assertRaises(AssertionError):
            self.capture_pack.set_captures_file_manager(object)

        with self.assertRaises(AssertionError):
            self.capture_pack.set_captures_file_manager('Some string')

        with self.assertRaises(AssertionError):
            self.capture_pack.set_captures_file_manager(222)

    def test_capture_pack_get_file_manager(self):
        self.capture_pack.set_captures_file_manager(CapturesManager())

        file_manager = self.capture_pack.get_captures_file_manager()
        self.assertIsInstance(
            file_manager,
            CapturesManager
        )

    def test_get_empty_file_manager(self):
        file_manager = self.capture_pack.get_captures_file_manager()

        self.assertIsNone(
            file_manager
        )

    @mock.patch('captures.utils.os.path.exists')
    @mock.patch('captures.utils.os.mkdir')
    def test_active_capture_pack_with_custom_save_method(
            self, os_mkdir_mock, os_path_exists_mock):

        os_mkdir_mock.return_value = None
        os_path_exists_mock.return_value = True

        pack = CapturePack(
            profile=self.profile
        )

        manager = CapturesManager()

        self.capture_pack.save()

        exists_pack = manager.exists_pack(str(pack.path))

        self.assertTrue(exists_pack)
