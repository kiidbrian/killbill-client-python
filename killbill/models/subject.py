# coding: utf-8

#
# Copyright 2014-2017 Groupon, Inc.
# Copyright 2014-2017 The Billing Project, LLC
#
# The Billing Project, LLC licenses this file to you under the Apache License, version 2.0
# (the "License"); you may not use this file except in compliance with the
# License.  You may obtain a copy of the License at:
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.  See the
# License for the specific language governing permissions and limitations
# under the License.
#

"""
    Kill Bill

    Kill Bill is an open-source billing and payments platform  # noqa: E501

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six



class Subject(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'principal': 'Str',
        'is_authenticated': 'Bool',
        'is_remembered': 'Bool',
        'session': 'Session'
    }

    attribute_map = {
        'principal': 'principal',
        'is_authenticated': 'isAuthenticated',
        'is_remembered': 'isRemembered',
        'session': 'session'
    }

    def __init__(self, principal=None, is_authenticated=False, is_remembered=False, session=None):  # noqa: E501
        """Subject - a model defined in Swagger"""  # noqa: E501

        self._principal = None
        self._is_authenticated = None
        self._is_remembered = None
        self._session = None
        self.discriminator = None

        if principal is not None:
            self.principal = principal
        if is_authenticated is not None:
            self.is_authenticated = is_authenticated
        if is_remembered is not None:
            self.is_remembered = is_remembered
        if session is not None:
            self.session = session

    @property
    def principal(self):
        """Gets the principal of this Subject.  # noqa: E501


        :return: The principal of this Subject.  # noqa: E501
        :rtype: Str
        """
        return self._principal

    @principal.setter
    def principal(self, principal):
        """Sets the principal of this Subject.


        :param principal: The principal of this Subject.  # noqa: E501
        :type: Str
        """

        self._principal = principal

    @property
    def is_authenticated(self):
        """Gets the is_authenticated of this Subject.  # noqa: E501


        :return: The is_authenticated of this Subject.  # noqa: E501
        :rtype: Bool
        """
        return self._is_authenticated

    @is_authenticated.setter
    def is_authenticated(self, is_authenticated):
        """Sets the is_authenticated of this Subject.


        :param is_authenticated: The is_authenticated of this Subject.  # noqa: E501
        :type: Bool
        """

        self._is_authenticated = is_authenticated

    @property
    def is_remembered(self):
        """Gets the is_remembered of this Subject.  # noqa: E501


        :return: The is_remembered of this Subject.  # noqa: E501
        :rtype: Bool
        """
        return self._is_remembered

    @is_remembered.setter
    def is_remembered(self, is_remembered):
        """Sets the is_remembered of this Subject.


        :param is_remembered: The is_remembered of this Subject.  # noqa: E501
        :type: Bool
        """

        self._is_remembered = is_remembered

    @property
    def session(self):
        """Gets the session of this Subject.  # noqa: E501


        :return: The session of this Subject.  # noqa: E501
        :rtype: Session
        """
        return self._session

    @session.setter
    def session(self, session):
        """Sets the session of this Subject.


        :param session: The session of this Subject.  # noqa: E501
        :type: Session
        """

        self._session = session

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, Subject):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
