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



class Subscription(object):
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
        'account_id': 'Str',
        'bundle_id': 'Str',
        'subscription_id': 'Str',
        'external_key': 'Str',
        'start_date': 'Date',
        'product_name': 'Str',
        'product_category': 'Str',
        'billing_period': 'Str',
        'phase_type': 'Str',
        'price_list': 'Str',
        'plan_name': 'Str',
        'state': 'Str',
        'source_type': 'Str',
        'cancelled_date': 'Date',
        'charged_through_date': 'Date',
        'billing_start_date': 'Date',
        'billing_end_date': 'Date',
        'bill_cycle_day_local': 'Int',
        'events': 'List[EventSubscription]',
        'price_overrides': 'List[PhasePriceOverride]',
        'audit_logs': 'List[AuditLog]'
    }

    attribute_map = {
        'account_id': 'accountId',
        'bundle_id': 'bundleId',
        'subscription_id': 'subscriptionId',
        'external_key': 'externalKey',
        'start_date': 'startDate',
        'product_name': 'productName',
        'product_category': 'productCategory',
        'billing_period': 'billingPeriod',
        'phase_type': 'phaseType',
        'price_list': 'priceList',
        'plan_name': 'planName',
        'state': 'state',
        'source_type': 'sourceType',
        'cancelled_date': 'cancelledDate',
        'charged_through_date': 'chargedThroughDate',
        'billing_start_date': 'billingStartDate',
        'billing_end_date': 'billingEndDate',
        'bill_cycle_day_local': 'billCycleDayLocal',
        'events': 'events',
        'price_overrides': 'priceOverrides',
        'audit_logs': 'auditLogs'
    }

    def __init__(self, account_id=None, bundle_id=None, subscription_id=None, external_key=None, start_date=None, product_name=None, product_category=None, billing_period=None, phase_type=None, price_list=None, plan_name=None, state=None, source_type=None, cancelled_date=None, charged_through_date=None, billing_start_date=None, billing_end_date=None, bill_cycle_day_local=None, events=None, price_overrides=None, audit_logs=None):  # noqa: E501
        """Subscription - a model defined in Swagger"""  # noqa: E501

        self._account_id = None
        self._bundle_id = None
        self._subscription_id = None
        self._external_key = None
        self._start_date = None
        self._product_name = None
        self._product_category = None
        self._billing_period = None
        self._phase_type = None
        self._price_list = None
        self._plan_name = None
        self._state = None
        self._source_type = None
        self._cancelled_date = None
        self._charged_through_date = None
        self._billing_start_date = None
        self._billing_end_date = None
        self._bill_cycle_day_local = None
        self._events = None
        self._price_overrides = None
        self._audit_logs = None
        self.discriminator = None

        if account_id is not None:
            self.account_id = account_id
        if bundle_id is not None:
            self.bundle_id = bundle_id
        if subscription_id is not None:
            self.subscription_id = subscription_id
        if external_key is not None:
            self.external_key = external_key
        if start_date is not None:
            self.start_date = start_date
        self.product_name = product_name
        if product_category is not None:
            self.product_category = product_category
        self.billing_period = billing_period
        if phase_type is not None:
            self.phase_type = phase_type
        self.price_list = price_list
        self.plan_name = plan_name
        if state is not None:
            self.state = state
        if source_type is not None:
            self.source_type = source_type
        if cancelled_date is not None:
            self.cancelled_date = cancelled_date
        if charged_through_date is not None:
            self.charged_through_date = charged_through_date
        if billing_start_date is not None:
            self.billing_start_date = billing_start_date
        if billing_end_date is not None:
            self.billing_end_date = billing_end_date
        if bill_cycle_day_local is not None:
            self.bill_cycle_day_local = bill_cycle_day_local
        if events is not None:
            self.events = events
        if price_overrides is not None:
            self.price_overrides = price_overrides
        if audit_logs is not None:
            self.audit_logs = audit_logs

    @property
    def account_id(self):
        """Gets the account_id of this Subscription.  # noqa: E501


        :return: The account_id of this Subscription.  # noqa: E501
        :rtype: Str
        """
        return self._account_id

    @account_id.setter
    def account_id(self, account_id):
        """Sets the account_id of this Subscription.


        :param account_id: The account_id of this Subscription.  # noqa: E501
        :type: Str
        """


        self._account_id = account_id

    @property
    def bundle_id(self):
        """Gets the bundle_id of this Subscription.  # noqa: E501


        :return: The bundle_id of this Subscription.  # noqa: E501
        :rtype: Str
        """
        return self._bundle_id

    @bundle_id.setter
    def bundle_id(self, bundle_id):
        """Sets the bundle_id of this Subscription.


        :param bundle_id: The bundle_id of this Subscription.  # noqa: E501
        :type: Str
        """


        self._bundle_id = bundle_id

    @property
    def subscription_id(self):
        """Gets the subscription_id of this Subscription.  # noqa: E501


        :return: The subscription_id of this Subscription.  # noqa: E501
        :rtype: Str
        """
        return self._subscription_id

    @subscription_id.setter
    def subscription_id(self, subscription_id):
        """Sets the subscription_id of this Subscription.


        :param subscription_id: The subscription_id of this Subscription.  # noqa: E501
        :type: Str
        """


        self._subscription_id = subscription_id

    @property
    def external_key(self):
        """Gets the external_key of this Subscription.  # noqa: E501


        :return: The external_key of this Subscription.  # noqa: E501
        :rtype: Str
        """
        return self._external_key

    @external_key.setter
    def external_key(self, external_key):
        """Sets the external_key of this Subscription.


        :param external_key: The external_key of this Subscription.  # noqa: E501
        :type: Str
        """


        self._external_key = external_key

    @property
    def start_date(self):
        """Gets the start_date of this Subscription.  # noqa: E501


        :return: The start_date of this Subscription.  # noqa: E501
        :rtype: Date
        """
        return self._start_date

    @start_date.setter
    def start_date(self, start_date):
        """Sets the start_date of this Subscription.


        :param start_date: The start_date of this Subscription.  # noqa: E501
        :type: Date
        """


        self._start_date = start_date

    @property
    def product_name(self):
        """Gets the product_name of this Subscription.  # noqa: E501


        :return: The product_name of this Subscription.  # noqa: E501
        :rtype: Str
        """
        return self._product_name

    @product_name.setter
    def product_name(self, product_name):
        """Sets the product_name of this Subscription.


        :param product_name: The product_name of this Subscription.  # noqa: E501
        :type: Str
        """


        self._product_name = product_name

    @property
    def product_category(self):
        """Gets the product_category of this Subscription.  # noqa: E501


        :return: The product_category of this Subscription.  # noqa: E501
        :rtype: Str
        """
        return self._product_category

    @product_category.setter
    def product_category(self, product_category):
        """Sets the product_category of this Subscription.


        :param product_category: The product_category of this Subscription.  # noqa: E501
        :type: Str
        """


        self._product_category = product_category

    @property
    def billing_period(self):
        """Gets the billing_period of this Subscription.  # noqa: E501


        :return: The billing_period of this Subscription.  # noqa: E501
        :rtype: Str
        """
        return self._billing_period

    @billing_period.setter
    def billing_period(self, billing_period):
        """Sets the billing_period of this Subscription.


        :param billing_period: The billing_period of this Subscription.  # noqa: E501
        :type: Str
        """


        self._billing_period = billing_period

    @property
    def phase_type(self):
        """Gets the phase_type of this Subscription.  # noqa: E501


        :return: The phase_type of this Subscription.  # noqa: E501
        :rtype: Str
        """
        return self._phase_type

    @phase_type.setter
    def phase_type(self, phase_type):
        """Sets the phase_type of this Subscription.


        :param phase_type: The phase_type of this Subscription.  # noqa: E501
        :type: Str
        """


        self._phase_type = phase_type

    @property
    def price_list(self):
        """Gets the price_list of this Subscription.  # noqa: E501


        :return: The price_list of this Subscription.  # noqa: E501
        :rtype: Str
        """
        return self._price_list

    @price_list.setter
    def price_list(self, price_list):
        """Sets the price_list of this Subscription.


        :param price_list: The price_list of this Subscription.  # noqa: E501
        :type: Str
        """


        self._price_list = price_list

    @property
    def plan_name(self):
        """Gets the plan_name of this Subscription.  # noqa: E501


        :return: The plan_name of this Subscription.  # noqa: E501
        :rtype: Str
        """
        return self._plan_name

    @plan_name.setter
    def plan_name(self, plan_name):
        """Sets the plan_name of this Subscription.


        :param plan_name: The plan_name of this Subscription.  # noqa: E501
        :type: Str
        """


        self._plan_name = plan_name

    @property
    def state(self):
        """Gets the state of this Subscription.  # noqa: E501


        :return: The state of this Subscription.  # noqa: E501
        :rtype: Str
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this Subscription.


        :param state: The state of this Subscription.  # noqa: E501
        :type: Str
        """


        self._state = state

    @property
    def source_type(self):
        """Gets the source_type of this Subscription.  # noqa: E501


        :return: The source_type of this Subscription.  # noqa: E501
        :rtype: Str
        """
        return self._source_type

    @source_type.setter
    def source_type(self, source_type):
        """Sets the source_type of this Subscription.


        :param source_type: The source_type of this Subscription.  # noqa: E501
        :type: Str
        """


        self._source_type = source_type

    @property
    def cancelled_date(self):
        """Gets the cancelled_date of this Subscription.  # noqa: E501


        :return: The cancelled_date of this Subscription.  # noqa: E501
        :rtype: Date
        """
        return self._cancelled_date

    @cancelled_date.setter
    def cancelled_date(self, cancelled_date):
        """Sets the cancelled_date of this Subscription.


        :param cancelled_date: The cancelled_date of this Subscription.  # noqa: E501
        :type: Date
        """


        self._cancelled_date = cancelled_date

    @property
    def charged_through_date(self):
        """Gets the charged_through_date of this Subscription.  # noqa: E501


        :return: The charged_through_date of this Subscription.  # noqa: E501
        :rtype: Date
        """
        return self._charged_through_date

    @charged_through_date.setter
    def charged_through_date(self, charged_through_date):
        """Sets the charged_through_date of this Subscription.


        :param charged_through_date: The charged_through_date of this Subscription.  # noqa: E501
        :type: Date
        """


        self._charged_through_date = charged_through_date

    @property
    def billing_start_date(self):
        """Gets the billing_start_date of this Subscription.  # noqa: E501


        :return: The billing_start_date of this Subscription.  # noqa: E501
        :rtype: Date
        """
        return self._billing_start_date

    @billing_start_date.setter
    def billing_start_date(self, billing_start_date):
        """Sets the billing_start_date of this Subscription.


        :param billing_start_date: The billing_start_date of this Subscription.  # noqa: E501
        :type: Date
        """


        self._billing_start_date = billing_start_date

    @property
    def billing_end_date(self):
        """Gets the billing_end_date of this Subscription.  # noqa: E501


        :return: The billing_end_date of this Subscription.  # noqa: E501
        :rtype: Date
        """
        return self._billing_end_date

    @billing_end_date.setter
    def billing_end_date(self, billing_end_date):
        """Sets the billing_end_date of this Subscription.


        :param billing_end_date: The billing_end_date of this Subscription.  # noqa: E501
        :type: Date
        """


        self._billing_end_date = billing_end_date

    @property
    def bill_cycle_day_local(self):
        """Gets the bill_cycle_day_local of this Subscription.  # noqa: E501


        :return: The bill_cycle_day_local of this Subscription.  # noqa: E501
        :rtype: Int
        """
        return self._bill_cycle_day_local

    @bill_cycle_day_local.setter
    def bill_cycle_day_local(self, bill_cycle_day_local):
        """Sets the bill_cycle_day_local of this Subscription.


        :param bill_cycle_day_local: The bill_cycle_day_local of this Subscription.  # noqa: E501
        :type: Int
        """


        self._bill_cycle_day_local = bill_cycle_day_local

    @property
    def events(self):
        """Gets the events of this Subscription.  # noqa: E501


        :return: The events of this Subscription.  # noqa: E501
        :rtype: List[EventSubscription]
        """
        return self._events

    @events.setter
    def events(self, events):
        """Sets the events of this Subscription.


        :param events: The events of this Subscription.  # noqa: E501
        :type: List[EventSubscription]
        """


        self._events = events

    @property
    def price_overrides(self):
        """Gets the price_overrides of this Subscription.  # noqa: E501


        :return: The price_overrides of this Subscription.  # noqa: E501
        :rtype: List[PhasePriceOverride]
        """
        return self._price_overrides

    @price_overrides.setter
    def price_overrides(self, price_overrides):
        """Sets the price_overrides of this Subscription.


        :param price_overrides: The price_overrides of this Subscription.  # noqa: E501
        :type: List[PhasePriceOverride]
        """


        self._price_overrides = price_overrides

    @property
    def audit_logs(self):
        """Gets the audit_logs of this Subscription.  # noqa: E501


        :return: The audit_logs of this Subscription.  # noqa: E501
        :rtype: List[AuditLog]
        """
        return self._audit_logs

    @audit_logs.setter
    def audit_logs(self, audit_logs):
        """Sets the audit_logs of this Subscription.


        :param audit_logs: The audit_logs of this Subscription.  # noqa: E501
        :type: List[AuditLog]
        """


        self._audit_logs = audit_logs

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
        if not isinstance(other, Subscription):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
