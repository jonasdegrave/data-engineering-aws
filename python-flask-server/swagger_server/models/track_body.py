# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.event import Event  # noqa: F401,E501
from swagger_server import util


class TrackBody(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, user_id: str = None, events: List[Event] = None):  # noqa: E501
        """TrackBody - a model defined in Swagger

        :param user_id: The user_id of this TrackBody.  # noqa: E501
        :type user_id: str
        :param events: The events of this TrackBody.  # noqa: E501
        :type events: List[Event]
        """
        self.swagger_types = {"user_id": str, "events": List[Event]}

        self.attribute_map = {"user_id": "userId", "events": "events"}
        self._user_id = user_id
        self._events = events

    @classmethod
    def from_dict(cls, dikt) -> "TrackBody":
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The trackBody of this TrackBody.  # noqa: E501
        :rtype: TrackBody
        """
        return util.deserialize_model(dikt, cls)

    @property
    def user_id(self) -> str:
        """Gets the user_id of this TrackBody.


        :return: The user_id of this TrackBody.
        :rtype: str
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id: str):
        """Sets the user_id of this TrackBody.


        :param user_id: The user_id of this TrackBody.
        :type user_id: str
        """
        if user_id is None:
            raise ValueError(
                "Invalid value for `user_id`, must not be `None`"
            )  # noqa: E501

        self._user_id = user_id

    @property
    def events(self) -> List[Event]:
        """Gets the events of this TrackBody.


        :return: The events of this TrackBody.
        :rtype: List[Event]
        """
        return self._events

    @events.setter
    def events(self, events: List[Event]):
        """Sets the events of this TrackBody.


        :param events: The events of this TrackBody.
        :type events: List[Event]
        """
        if events is None:
            raise ValueError(
                "Invalid value for `events`, must not be `None`"
            )  # noqa: E501

        self._events = events
