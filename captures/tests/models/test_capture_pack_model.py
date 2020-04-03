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
        self.capture_pack = CapturePack(
            profile=self.profile
        )

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

    @mock.patch('captures.utils.os.mkdir')
    def test_capture_custom_save_with_empty(self, os_mkdir_mock):
        os_mkdir_mock.return_value = None
        profile = baker.make(UserProfile)
        CapturePack(profile=profile).save()

    @mock.patch('captures.utils.os.mkdir')
    def test_capture_custom_save_non_capture_file_manager_object(
            self, os_mkdir_mock):

        os_mkdir_mock.return_value = None

        profiles = baker.make(UserProfile, _quantity=3)

        pack = CapturePack(profile=profiles[0])
        pack.save(file_manager=object)

        self.assertIsInstance(
            pack._file_manager,
            CapturesManager
        )

        pack = CapturePack(profile=profiles[1])
        pack.save(file_manager=222)

        self.assertIsInstance(
            pack._file_manager,
            CapturesManager
        )

        pack = CapturePack(profile=profiles[2])
        pack.save(file_manager='Some string')

        self.assertIsInstance(
            pack._file_manager,
            CapturesManager
        )

    @mock.patch('captures.utils.os.path.exists')
    @mock.patch('captures.utils.os.mkdir')
    def test_active_capture_pack_with_custom_save_method(
            self, os_mkdir_mock, os_path_exists_mock):

        os_mkdir_mock.return_value = None
        os_path_exists_mock.return_value = True

        pack = CapturePack(
            profile=baker.make(UserProfile)
        )

        manager = CapturesManager()

        pack.save()

        exists_pack = manager.exists_pack(str(pack.path))

        self.assertTrue(exists_pack)
