# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.alias_body import AliasBody  # noqa: E501
from swagger_server.models.profile_body import ProfileBody  # noqa: E501
from swagger_server.models.track_body import TrackBody  # noqa: E501
from swagger_server.test import BaseTestCase


class TestDefaultController(BaseTestCase):
    """DefaultController integration test stubs"""

    def test_alias_post(self):
        """Test case for alias_post

        Assotiate different identifiers to the same entity.
        """
        body = AliasBody()
        response = self.client.open(
            '/alias',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_profile_post(self):
        """Test case for profile_post

        Save profile attributes for an particular user
        """
        body = ProfileBody()
        response = self.client.open(
            '/profile',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_track_post(self):
        """Test case for track_post

        Log events related with a particular user
        """
        body = TrackBody()
        response = self.client.open(
            '/track',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
