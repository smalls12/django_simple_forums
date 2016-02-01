from django.contrib.auth import get_user_model
from django.test import TestCase
from django.utils import timezone

from simple_forums import models
from simple_forums.tests.testing_utils import create_message, create_thread


class TestMessageModel(TestCase):
    """ Tests for the message model """

    def test_create_with_all_fields(self):
        """ Test creation of a message with all its fields.

        A message instance should be able to be created with a foreign
        key to a user instance, body text, and a time for its creation.
        """
        user = get_user_model().objects.create_user(
            username='test',
            password='test')
        thread = create_thread()
        body = "Test body text"
        time = timezone.now()

        message = models.Message.objects.create(
            user=user,
            thread=thread,
            body=body,
            time_created=time)

        self.assertEqual(user, message.user)
        self.assertEqual(thread, message.thread)
        self.assertEqual(body, message.body)
        self.assertEqual(time, message.time_created)

    def test_default_time_created(self):
        """ Test the default for the 'time_created' field.

        The field should default to the current time.
        """
        start_time = timezone.now()
        message = create_message()
        end_time = timezone.now()

        self.assertTrue(start_time <= message.time_created <= end_time)

    def test_string_conversion(self):
        """ Test the conversion of a message instance to a string.

        Converting a message instance to a string should return the
        message's body text.
        """
        message = models.Message(body="Test body text")

        self.assertEqual(message.body, str(message))


class TestThreadModel(TestCase):
    """ Tests for the thread model """

    def test_create_with_all_fields(self):
        """ Test creation of a thread with all its fields.

        A thread instance should be able to be created with title text.
        """
        thread = models.Thread.objects.create(
            title='test')

        self.assertEqual('test', thread.title)

    def test_string_conversion(self):
        """ Test converting a thread instance to a string.

        Converting a thread instance to a string should return the
        thread's title.
        """
        thread = models.Thread(title='test')

        self.assertEqual(thread.title, str(thread))
