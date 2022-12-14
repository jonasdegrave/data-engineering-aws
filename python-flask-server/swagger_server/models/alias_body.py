# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class AliasBody(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(
        self,
        new_user_id: str = None,
        original_user_id: str = None,
        timestamp_utc: int = None,
    ):  # noqa: E501
        """AliasBody - a model defined in Swagger

        :param new_user_id: The new_user_id of this AliasBody.  # noqa: E501
        :type new_user_id: str
        :param original_user_id: The original_user_id of this AliasBody.  # noqa: E501
        :type original_user_id: str
        :param timestamp_utc: The timestamp_utc of this AliasBody.  # noqa: E501
        :type timestamp_utc: int
        """
        self.swagger_types = {
            "new_user_id": str,
            "original_user_id": str,
            "timestamp_utc": int,
        }

        self.attribute_map = {
            "new_user_id": "newUserId",
            "original_user_id": "originalUserId",
            "timestamp_utc": "timestampUTC",
        }
        self._new_user_id = new_user_id
        self._original_user_id = original_user_id
        self._timestamp_utc = timestamp_utc

    @classmethod
    def from_dict(cls, dikt) -> "AliasBody":
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The aliasBody of this AliasBody.  # noqa: E501
        :rtype: AliasBody
        """
        return util.deserialize_model(dikt, cls)

    @property
    def new_user_id(self) -> str:
        """Gets the new_user_id of this AliasBody.


        :return: The new_user_id of this AliasBody.
        :rtype: str
        """
        return self._new_user_id

    @new_user_id.setter
    def new_user_id(self, new_user_id: str):
        """Sets the new_user_id of this AliasBody.


        :param new_user_id: The new_user_id of this AliasBody.
        :type new_user_id: str
        """
        if new_user_id is None:
            raise ValueError(
                "Invalid value for `new_user_id`, must not be `None`"
            )  # noqa: E501

        self._new_user_id = new_user_id

    @property
    def original_user_id(self) -> str:
        """Gets the original_user_id of this AliasBody.


        :return: The original_user_id of this AliasBody.
        :rtype: str
        """
        return self._original_user_id

    @original_user_id.setter
    def original_user_id(self, original_user_id: str):
        """Sets the original_user_id of this AliasBody.


        :param original_user_id: The original_user_id of this AliasBody.
        :type original_user_id: str
        """
        if original_user_id is None:
            raise ValueError(
                "Invalid value for `original_user_id`, must not be `None`"
            )  # noqa: E501

        self._original_user_id = original_user_id

    @property
    def timestamp_utc(self) -> int:
        """Gets the timestamp_utc of this AliasBody.


        :return: The timestamp_utc of this AliasBody.
        :rtype: int
        """
        return self._timestamp_utc

    @timestamp_utc.setter
    def timestamp_utc(self, timestamp_utc: int):
        """Sets the timestamp_utc of this AliasBody.


        :param timestamp_utc: The timestamp_utc of this AliasBody.
        :type timestamp_utc: int
        """
        if timestamp_utc is None:
            raise ValueError(
                "Invalid value for `timestamp_utc`, must not be `None`"
            )  # noqa: E501

        self._timestamp_utc = timestamp_utc
