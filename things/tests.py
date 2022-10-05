from django.core.exceptions import ValidationError
from django.test import TestCase

from things.models import Thing


# Create your tests here.
class ThingTestCase(TestCase):
    def setUp(self):
        self.thing = Thing.objects.create(
            name="Pen",
            description="A fully functional tool that uses ink",
            quantity=100
        )

    def test_valid_thing(self):
        self._assert_item_is_valid()

    def test_name_cannot_be_blank(self):
        self.thing.name = ''
        self._assert_item_is_invalid()

    def test_name_can_be_of_30_characters(self):
        self.thing.name = 'p' * 30
        self._assert_item_is_valid()

    def test_name_cannot_be_31_characters(self):
        self.thing.name = 'p' * 31
        self._assert_item_is_invalid()

    def test_name_must_be_unique(self):
        second_thing = self._create_second_item()
        self.thing.name = second_thing.name
        self._assert_item_is_invalid()

    def test_description_can_be_blank(self):
        self.thing.description = ''
        self._assert_item_is_valid()

    def test_description_can_be_of_120_characters(self):
        self.thing.description = 'd' * 120
        self._assert_item_is_valid()

    def test_description_cannot_be_121_characters(self):
        self.thing.description = 'd' * 121
        self._assert_item_is_invalid()

    def test_description_can_repeat(self):
        second_thing = self._create_second_item()
        self.thing.description = second_thing.description
        self._assert_item_is_valid()

    def test_quantity_can_be_0(self):
        self.thing.quantity = 0
        self._assert_item_is_valid()

    def test_quantity_cannot_be_less_than_0(self):
        self.thing.quantity = -1
        self._assert_item_is_invalid()

    def test_quantity_can_be_100(self):
        self.thing.quantity = 100
        self._assert_item_is_valid()

    def test_quantity_cannot_be_greater_than_100(self):
        self.thing.quantity = 101
        self._assert_item_is_invalid()

    def test_quantity_can_repeat(self):
        second_thing = self._create_second_item()
        self.thing.quantity = second_thing.quantity
        self._assert_item_is_valid()


    def _create_second_item(self):
        return Thing.objects.create(
            name="Pencil",
            description="Made from graphite, does what a pen does",
            quantity=10
        )

    def _assert_item_is_valid(self):
        try:
            self.thing.full_clean()
        except (ValidationError):
            self.fail('Test thing should have been valid')

    def _assert_item_is_invalid(self):
        with self.assertRaises(ValidationError):
            self.thing.full_clean()
