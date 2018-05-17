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

    OpenAPI spec version: 0.19.11-SNAPSHOT
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six



class SimplePlan(object):
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
        'plan_id': 'Str',
        'product_name': 'Str',
        'product_category': 'Str',
        'currency': 'Str',
        'amount': 'Float',
        'billing_period': 'Str',
        'trial_length': 'Int',
        'trial_time_unit': 'Str',
        'available_base_products': 'List[Str]'
    }

    attribute_map = {
        'plan_id': 'planId',
        'product_name': 'productName',
        'product_category': 'productCategory',
        'currency': 'currency',
        'amount': 'amount',
        'billing_period': 'billingPeriod',
        'trial_length': 'trialLength',
        'trial_time_unit': 'trialTimeUnit',
        'available_base_products': 'availableBaseProducts'
    }

    def __init__(self, plan_id=None, product_name=None, product_category=None, currency=None, amount=None, billing_period=None, trial_length=None, trial_time_unit=None, available_base_products=None):  # noqa: E501
        """SimplePlan - a model defined in Swagger"""  # noqa: E501

        self._plan_id = None
        self._product_name = None
        self._product_category = None
        self._currency = None
        self._amount = None
        self._billing_period = None
        self._trial_length = None
        self._trial_time_unit = None
        self._available_base_products = None
        self.discriminator = None

        if plan_id is not None:
            self.plan_id = plan_id
        if product_name is not None:
            self.product_name = product_name
        if product_category is not None:
            self.product_category = product_category
        if currency is not None:
            self.currency = currency
        if amount is not None:
            self.amount = amount
        if billing_period is not None:
            self.billing_period = billing_period
        if trial_length is not None:
            self.trial_length = trial_length
        if trial_time_unit is not None:
            self.trial_time_unit = trial_time_unit
        if available_base_products is not None:
            self.available_base_products = available_base_products

    @property
    def plan_id(self):
        """Gets the plan_id of this SimplePlan.  # noqa: E501


        :return: The plan_id of this SimplePlan.  # noqa: E501
        :rtype: Str
        """
        return self._plan_id

    @plan_id.setter
    def plan_id(self, plan_id):
        """Sets the plan_id of this SimplePlan.


        :param plan_id: The plan_id of this SimplePlan.  # noqa: E501
        :type: Str
        """


        self._plan_id = plan_id

    @property
    def product_name(self):
        """Gets the product_name of this SimplePlan.  # noqa: E501


        :return: The product_name of this SimplePlan.  # noqa: E501
        :rtype: Str
        """
        return self._product_name

    @product_name.setter
    def product_name(self, product_name):
        """Sets the product_name of this SimplePlan.


        :param product_name: The product_name of this SimplePlan.  # noqa: E501
        :type: Str
        """


        self._product_name = product_name

    @property
    def product_category(self):
        """Gets the product_category of this SimplePlan.  # noqa: E501


        :return: The product_category of this SimplePlan.  # noqa: E501
        :rtype: Str
        """
        return self._product_category

    @product_category.setter
    def product_category(self, product_category):
        """Sets the product_category of this SimplePlan.


        :param product_category: The product_category of this SimplePlan.  # noqa: E501
        :type: Str
        """


        self._product_category = product_category

    @property
    def currency(self):
        """Gets the currency of this SimplePlan.  # noqa: E501


        :return: The currency of this SimplePlan.  # noqa: E501
        :rtype: Str
        """
        return self._currency

    @currency.setter
    def currency(self, currency):
        """Sets the currency of this SimplePlan.


        :param currency: The currency of this SimplePlan.  # noqa: E501
        :type: Str
        """


        self._currency = currency

    @property
    def amount(self):
        """Gets the amount of this SimplePlan.  # noqa: E501


        :return: The amount of this SimplePlan.  # noqa: E501
        :rtype: Float
        """
        return self._amount

    @amount.setter
    def amount(self, amount):
        """Sets the amount of this SimplePlan.


        :param amount: The amount of this SimplePlan.  # noqa: E501
        :type: Float
        """


        self._amount = amount

    @property
    def billing_period(self):
        """Gets the billing_period of this SimplePlan.  # noqa: E501


        :return: The billing_period of this SimplePlan.  # noqa: E501
        :rtype: Str
        """
        return self._billing_period

    @billing_period.setter
    def billing_period(self, billing_period):
        """Sets the billing_period of this SimplePlan.


        :param billing_period: The billing_period of this SimplePlan.  # noqa: E501
        :type: Str
        """


        self._billing_period = billing_period

    @property
    def trial_length(self):
        """Gets the trial_length of this SimplePlan.  # noqa: E501


        :return: The trial_length of this SimplePlan.  # noqa: E501
        :rtype: Int
        """
        return self._trial_length

    @trial_length.setter
    def trial_length(self, trial_length):
        """Sets the trial_length of this SimplePlan.


        :param trial_length: The trial_length of this SimplePlan.  # noqa: E501
        :type: Int
        """


        self._trial_length = trial_length

    @property
    def trial_time_unit(self):
        """Gets the trial_time_unit of this SimplePlan.  # noqa: E501


        :return: The trial_time_unit of this SimplePlan.  # noqa: E501
        :rtype: Str
        """
        return self._trial_time_unit

    @trial_time_unit.setter
    def trial_time_unit(self, trial_time_unit):
        """Sets the trial_time_unit of this SimplePlan.


        :param trial_time_unit: The trial_time_unit of this SimplePlan.  # noqa: E501
        :type: Str
        """


        self._trial_time_unit = trial_time_unit

    @property
    def available_base_products(self):
        """Gets the available_base_products of this SimplePlan.  # noqa: E501


        :return: The available_base_products of this SimplePlan.  # noqa: E501
        :rtype: List[Str]
        """
        return self._available_base_products

    @available_base_products.setter
    def available_base_products(self, available_base_products):
        """Sets the available_base_products of this SimplePlan.


        :param available_base_products: The available_base_products of this SimplePlan.  # noqa: E501
        :type: List[Str]
        """


        self._available_base_products = available_base_products

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
        if not isinstance(other, SimplePlan):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
