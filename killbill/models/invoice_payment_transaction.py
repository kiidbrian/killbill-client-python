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



class InvoicePaymentTransaction(object):
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
        'transaction_id': 'Str',
        'transaction_external_key': 'Str',
        'payment_id': 'Str',
        'payment_external_key': 'Str',
        'transaction_type': 'Str',
        'amount': 'Float',
        'currency': 'Str',
        'effective_date': 'Datetime',
        'processed_amount': 'Float',
        'processed_currency': 'Str',
        'status': 'Str',
        'gateway_error_code': 'Str',
        'gateway_error_msg': 'Str',
        'first_payment_reference_id': 'Str',
        'second_payment_reference_id': 'Str',
        'properties': 'List[PluginProperty]',
        'is_adjusted': 'Bool',
        'adjustments': 'List[InvoiceItem]',
        'audit_logs': 'List[AuditLog]'
    }

    attribute_map = {
        'transaction_id': 'transactionId',
        'transaction_external_key': 'transactionExternalKey',
        'payment_id': 'paymentId',
        'payment_external_key': 'paymentExternalKey',
        'transaction_type': 'transactionType',
        'amount': 'amount',
        'currency': 'currency',
        'effective_date': 'effectiveDate',
        'processed_amount': 'processedAmount',
        'processed_currency': 'processedCurrency',
        'status': 'status',
        'gateway_error_code': 'gatewayErrorCode',
        'gateway_error_msg': 'gatewayErrorMsg',
        'first_payment_reference_id': 'firstPaymentReferenceId',
        'second_payment_reference_id': 'secondPaymentReferenceId',
        'properties': 'properties',
        'is_adjusted': 'isAdjusted',
        'adjustments': 'adjustments',
        'audit_logs': 'auditLogs'
    }

    def __init__(self, transaction_id=None, transaction_external_key=None, payment_id=None, payment_external_key=None, transaction_type=None, amount=None, currency=None, effective_date=None, processed_amount=None, processed_currency=None, status=None, gateway_error_code=None, gateway_error_msg=None, first_payment_reference_id=None, second_payment_reference_id=None, properties=None, is_adjusted=False, adjustments=None, audit_logs=None):  # noqa: E501
        """InvoicePaymentTransaction - a model defined in Swagger"""  # noqa: E501

        self._transaction_id = None
        self._transaction_external_key = None
        self._payment_id = None
        self._payment_external_key = None
        self._transaction_type = None
        self._amount = None
        self._currency = None
        self._effective_date = None
        self._processed_amount = None
        self._processed_currency = None
        self._status = None
        self._gateway_error_code = None
        self._gateway_error_msg = None
        self._first_payment_reference_id = None
        self._second_payment_reference_id = None
        self._properties = None
        self._is_adjusted = None
        self._adjustments = None
        self._audit_logs = None
        self.discriminator = None

        if transaction_id is not None:
            self.transaction_id = transaction_id
        if transaction_external_key is not None:
            self.transaction_external_key = transaction_external_key
        if payment_id is not None:
            self.payment_id = payment_id
        if payment_external_key is not None:
            self.payment_external_key = payment_external_key
        if transaction_type is not None:
            self.transaction_type = transaction_type
        if amount is not None:
            self.amount = amount
        if currency is not None:
            self.currency = currency
        if effective_date is not None:
            self.effective_date = effective_date
        if processed_amount is not None:
            self.processed_amount = processed_amount
        if processed_currency is not None:
            self.processed_currency = processed_currency
        if status is not None:
            self.status = status
        if gateway_error_code is not None:
            self.gateway_error_code = gateway_error_code
        if gateway_error_msg is not None:
            self.gateway_error_msg = gateway_error_msg
        if first_payment_reference_id is not None:
            self.first_payment_reference_id = first_payment_reference_id
        if second_payment_reference_id is not None:
            self.second_payment_reference_id = second_payment_reference_id
        if properties is not None:
            self.properties = properties
        if is_adjusted is not None:
            self.is_adjusted = is_adjusted
        if adjustments is not None:
            self.adjustments = adjustments
        if audit_logs is not None:
            self.audit_logs = audit_logs

    @property
    def transaction_id(self):
        """Gets the transaction_id of this InvoicePaymentTransaction.  # noqa: E501


        :return: The transaction_id of this InvoicePaymentTransaction.  # noqa: E501
        :rtype: Str
        """
        return self._transaction_id

    @transaction_id.setter
    def transaction_id(self, transaction_id):
        """Sets the transaction_id of this InvoicePaymentTransaction.


        :param transaction_id: The transaction_id of this InvoicePaymentTransaction.  # noqa: E501
        :type: Str
        """

        self._transaction_id = transaction_id

    @property
    def transaction_external_key(self):
        """Gets the transaction_external_key of this InvoicePaymentTransaction.  # noqa: E501


        :return: The transaction_external_key of this InvoicePaymentTransaction.  # noqa: E501
        :rtype: Str
        """
        return self._transaction_external_key

    @transaction_external_key.setter
    def transaction_external_key(self, transaction_external_key):
        """Sets the transaction_external_key of this InvoicePaymentTransaction.


        :param transaction_external_key: The transaction_external_key of this InvoicePaymentTransaction.  # noqa: E501
        :type: Str
        """

        self._transaction_external_key = transaction_external_key

    @property
    def payment_id(self):
        """Gets the payment_id of this InvoicePaymentTransaction.  # noqa: E501

        Associated payment id, required when notifying state transitions  # noqa: E501

        :return: The payment_id of this InvoicePaymentTransaction.  # noqa: E501
        :rtype: Str
        """
        return self._payment_id

    @payment_id.setter
    def payment_id(self, payment_id):
        """Sets the payment_id of this InvoicePaymentTransaction.

        Associated payment id, required when notifying state transitions  # noqa: E501

        :param payment_id: The payment_id of this InvoicePaymentTransaction.  # noqa: E501
        :type: Str
        """

        self._payment_id = payment_id

    @property
    def payment_external_key(self):
        """Gets the payment_external_key of this InvoicePaymentTransaction.  # noqa: E501


        :return: The payment_external_key of this InvoicePaymentTransaction.  # noqa: E501
        :rtype: Str
        """
        return self._payment_external_key

    @payment_external_key.setter
    def payment_external_key(self, payment_external_key):
        """Sets the payment_external_key of this InvoicePaymentTransaction.


        :param payment_external_key: The payment_external_key of this InvoicePaymentTransaction.  # noqa: E501
        :type: Str
        """

        self._payment_external_key = payment_external_key

    @property
    def transaction_type(self):
        """Gets the transaction_type of this InvoicePaymentTransaction.  # noqa: E501


        :return: The transaction_type of this InvoicePaymentTransaction.  # noqa: E501
        :rtype: Str
        """
        return self._transaction_type

    @transaction_type.setter
    def transaction_type(self, transaction_type):
        """Sets the transaction_type of this InvoicePaymentTransaction.


        :param transaction_type: The transaction_type of this InvoicePaymentTransaction.  # noqa: E501
        :type: Str
        """
        allowed_values = ["AUTHORIZE", "CAPTURE", "CHARGEBACK", "CREDIT", "PURCHASE", "REFUND", "VOID"]  # noqa: E501
        if transaction_type not in allowed_values:
            raise ValueError(
                "Invalid value for `transaction_type` ({0}), must be one of {1}"  # noqa: E501
                .format(transaction_type, allowed_values)
            )

        self._transaction_type = transaction_type

    @property
    def amount(self):
        """Gets the amount of this InvoicePaymentTransaction.  # noqa: E501

        Transaction amount, required except for void operations  # noqa: E501

        :return: The amount of this InvoicePaymentTransaction.  # noqa: E501
        :rtype: Float
        """
        return self._amount

    @amount.setter
    def amount(self, amount):
        """Sets the amount of this InvoicePaymentTransaction.

        Transaction amount, required except for void operations  # noqa: E501

        :param amount: The amount of this InvoicePaymentTransaction.  # noqa: E501
        :type: Float
        """

        self._amount = amount

    @property
    def currency(self):
        """Gets the currency of this InvoicePaymentTransaction.  # noqa: E501

        Amount currency (account currency unless specified)  # noqa: E501

        :return: The currency of this InvoicePaymentTransaction.  # noqa: E501
        :rtype: Str
        """
        return self._currency

    @currency.setter
    def currency(self, currency):
        """Sets the currency of this InvoicePaymentTransaction.

        Amount currency (account currency unless specified)  # noqa: E501

        :param currency: The currency of this InvoicePaymentTransaction.  # noqa: E501
        :type: Str
        """
        allowed_values = ["AED", "AFN", "ALL", "AMD", "ANG", "AOA", "ARS", "AUD", "AWG", "AZN", "BAM", "BBD", "BDT", "BGN", "BHD", "BIF", "BMD", "BND", "BOB", "BRL", "BSD", "BTN", "BWP", "BYR", "BZD", "CAD", "CDF", "CHF", "CLP", "CNY", "COP", "CRC", "CUC", "CUP", "CVE", "CZK", "DJF", "DKK", "DOP", "DZD", "EGP", "ERN", "ETB", "EUR", "FJD", "FKP", "GBP", "GEL", "GGP", "GHS", "GIP", "GMD", "GNF", "GTQ", "GYD", "HKD", "HNL", "HRK", "HTG", "HUF", "IDR", "ILS", "IMP", "INR", "IQD", "IRR", "ISK", "JEP", "JMD", "JOD", "JPY", "KES", "KGS", "KHR", "KMF", "KPW", "KRW", "KWD", "KYD", "KZT", "LAK", "LBP", "LKR", "LRD", "LSL", "LTL", "LVL", "LYD", "MAD", "MDL", "MGA", "MKD", "MMK", "MNT", "MOP", "MRO", "MUR", "MVR", "MWK", "MXN", "MYR", "MZN", "NAD", "NGN", "NIO", "NOK", "NPR", "NZD", "OMR", "PAB", "PEN", "PGK", "PHP", "PKR", "PLN", "PYG", "QAR", "RON", "RSD", "RUB", "RWF", "SAR", "SBD", "SCR", "SDG", "SEK", "SGD", "SHP", "SLL", "SOS", "SPL", "SRD", "STD", "SVC", "SYP", "SZL", "THB", "TJS", "TMT", "TND", "TOP", "TRY", "TTD", "TVD", "TWD", "TZS", "UAH", "UGX", "USD", "UYU", "UZS", "VEF", "VND", "VUV", "WST", "XAF", "XCD", "XDR", "XOF", "XPF", "YER", "ZAR", "ZMW", "ZWD", "BTC"]  # noqa: E501
        if currency not in allowed_values:
            raise ValueError(
                "Invalid value for `currency` ({0}), must be one of {1}"  # noqa: E501
                .format(currency, allowed_values)
            )

        self._currency = currency

    @property
    def effective_date(self):
        """Gets the effective_date of this InvoicePaymentTransaction.  # noqa: E501


        :return: The effective_date of this InvoicePaymentTransaction.  # noqa: E501
        :rtype: Datetime
        """
        return self._effective_date

    @effective_date.setter
    def effective_date(self, effective_date):
        """Sets the effective_date of this InvoicePaymentTransaction.


        :param effective_date: The effective_date of this InvoicePaymentTransaction.  # noqa: E501
        :type: Datetime
        """

        self._effective_date = effective_date

    @property
    def processed_amount(self):
        """Gets the processed_amount of this InvoicePaymentTransaction.  # noqa: E501


        :return: The processed_amount of this InvoicePaymentTransaction.  # noqa: E501
        :rtype: Float
        """
        return self._processed_amount

    @processed_amount.setter
    def processed_amount(self, processed_amount):
        """Sets the processed_amount of this InvoicePaymentTransaction.


        :param processed_amount: The processed_amount of this InvoicePaymentTransaction.  # noqa: E501
        :type: Float
        """

        self._processed_amount = processed_amount

    @property
    def processed_currency(self):
        """Gets the processed_currency of this InvoicePaymentTransaction.  # noqa: E501


        :return: The processed_currency of this InvoicePaymentTransaction.  # noqa: E501
        :rtype: Str
        """
        return self._processed_currency

    @processed_currency.setter
    def processed_currency(self, processed_currency):
        """Sets the processed_currency of this InvoicePaymentTransaction.


        :param processed_currency: The processed_currency of this InvoicePaymentTransaction.  # noqa: E501
        :type: Str
        """
        allowed_values = ["AED", "AFN", "ALL", "AMD", "ANG", "AOA", "ARS", "AUD", "AWG", "AZN", "BAM", "BBD", "BDT", "BGN", "BHD", "BIF", "BMD", "BND", "BOB", "BRL", "BSD", "BTN", "BWP", "BYR", "BZD", "CAD", "CDF", "CHF", "CLP", "CNY", "COP", "CRC", "CUC", "CUP", "CVE", "CZK", "DJF", "DKK", "DOP", "DZD", "EGP", "ERN", "ETB", "EUR", "FJD", "FKP", "GBP", "GEL", "GGP", "GHS", "GIP", "GMD", "GNF", "GTQ", "GYD", "HKD", "HNL", "HRK", "HTG", "HUF", "IDR", "ILS", "IMP", "INR", "IQD", "IRR", "ISK", "JEP", "JMD", "JOD", "JPY", "KES", "KGS", "KHR", "KMF", "KPW", "KRW", "KWD", "KYD", "KZT", "LAK", "LBP", "LKR", "LRD", "LSL", "LTL", "LVL", "LYD", "MAD", "MDL", "MGA", "MKD", "MMK", "MNT", "MOP", "MRO", "MUR", "MVR", "MWK", "MXN", "MYR", "MZN", "NAD", "NGN", "NIO", "NOK", "NPR", "NZD", "OMR", "PAB", "PEN", "PGK", "PHP", "PKR", "PLN", "PYG", "QAR", "RON", "RSD", "RUB", "RWF", "SAR", "SBD", "SCR", "SDG", "SEK", "SGD", "SHP", "SLL", "SOS", "SPL", "SRD", "STD", "SVC", "SYP", "SZL", "THB", "TJS", "TMT", "TND", "TOP", "TRY", "TTD", "TVD", "TWD", "TZS", "UAH", "UGX", "USD", "UYU", "UZS", "VEF", "VND", "VUV", "WST", "XAF", "XCD", "XDR", "XOF", "XPF", "YER", "ZAR", "ZMW", "ZWD", "BTC"]  # noqa: E501
        if processed_currency not in allowed_values:
            raise ValueError(
                "Invalid value for `processed_currency` ({0}), must be one of {1}"  # noqa: E501
                .format(processed_currency, allowed_values)
            )

        self._processed_currency = processed_currency

    @property
    def status(self):
        """Gets the status of this InvoicePaymentTransaction.  # noqa: E501

        Transaction status, required for state change notifications  # noqa: E501

        :return: The status of this InvoicePaymentTransaction.  # noqa: E501
        :rtype: Str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this InvoicePaymentTransaction.

        Transaction status, required for state change notifications  # noqa: E501

        :param status: The status of this InvoicePaymentTransaction.  # noqa: E501
        :type: Str
        """
        allowed_values = ["SUCCESS", "UNKNOWN", "PENDING", "PAYMENT_FAILURE", "PLUGIN_FAILURE", "PAYMENT_SYSTEM_OFF"]  # noqa: E501
        if status not in allowed_values:
            raise ValueError(
                "Invalid value for `status` ({0}), must be one of {1}"  # noqa: E501
                .format(status, allowed_values)
            )

        self._status = status

    @property
    def gateway_error_code(self):
        """Gets the gateway_error_code of this InvoicePaymentTransaction.  # noqa: E501


        :return: The gateway_error_code of this InvoicePaymentTransaction.  # noqa: E501
        :rtype: Str
        """
        return self._gateway_error_code

    @gateway_error_code.setter
    def gateway_error_code(self, gateway_error_code):
        """Sets the gateway_error_code of this InvoicePaymentTransaction.


        :param gateway_error_code: The gateway_error_code of this InvoicePaymentTransaction.  # noqa: E501
        :type: Str
        """

        self._gateway_error_code = gateway_error_code

    @property
    def gateway_error_msg(self):
        """Gets the gateway_error_msg of this InvoicePaymentTransaction.  # noqa: E501


        :return: The gateway_error_msg of this InvoicePaymentTransaction.  # noqa: E501
        :rtype: Str
        """
        return self._gateway_error_msg

    @gateway_error_msg.setter
    def gateway_error_msg(self, gateway_error_msg):
        """Sets the gateway_error_msg of this InvoicePaymentTransaction.


        :param gateway_error_msg: The gateway_error_msg of this InvoicePaymentTransaction.  # noqa: E501
        :type: Str
        """

        self._gateway_error_msg = gateway_error_msg

    @property
    def first_payment_reference_id(self):
        """Gets the first_payment_reference_id of this InvoicePaymentTransaction.  # noqa: E501


        :return: The first_payment_reference_id of this InvoicePaymentTransaction.  # noqa: E501
        :rtype: Str
        """
        return self._first_payment_reference_id

    @first_payment_reference_id.setter
    def first_payment_reference_id(self, first_payment_reference_id):
        """Sets the first_payment_reference_id of this InvoicePaymentTransaction.


        :param first_payment_reference_id: The first_payment_reference_id of this InvoicePaymentTransaction.  # noqa: E501
        :type: Str
        """

        self._first_payment_reference_id = first_payment_reference_id

    @property
    def second_payment_reference_id(self):
        """Gets the second_payment_reference_id of this InvoicePaymentTransaction.  # noqa: E501


        :return: The second_payment_reference_id of this InvoicePaymentTransaction.  # noqa: E501
        :rtype: Str
        """
        return self._second_payment_reference_id

    @second_payment_reference_id.setter
    def second_payment_reference_id(self, second_payment_reference_id):
        """Sets the second_payment_reference_id of this InvoicePaymentTransaction.


        :param second_payment_reference_id: The second_payment_reference_id of this InvoicePaymentTransaction.  # noqa: E501
        :type: Str
        """

        self._second_payment_reference_id = second_payment_reference_id

    @property
    def properties(self):
        """Gets the properties of this InvoicePaymentTransaction.  # noqa: E501


        :return: The properties of this InvoicePaymentTransaction.  # noqa: E501
        :rtype: List[PluginProperty]
        """
        return self._properties

    @properties.setter
    def properties(self, properties):
        """Sets the properties of this InvoicePaymentTransaction.


        :param properties: The properties of this InvoicePaymentTransaction.  # noqa: E501
        :type: List[PluginProperty]
        """

        self._properties = properties

    @property
    def is_adjusted(self):
        """Gets the is_adjusted of this InvoicePaymentTransaction.  # noqa: E501


        :return: The is_adjusted of this InvoicePaymentTransaction.  # noqa: E501
        :rtype: Bool
        """
        return self._is_adjusted

    @is_adjusted.setter
    def is_adjusted(self, is_adjusted):
        """Sets the is_adjusted of this InvoicePaymentTransaction.


        :param is_adjusted: The is_adjusted of this InvoicePaymentTransaction.  # noqa: E501
        :type: Bool
        """

        self._is_adjusted = is_adjusted

    @property
    def adjustments(self):
        """Gets the adjustments of this InvoicePaymentTransaction.  # noqa: E501


        :return: The adjustments of this InvoicePaymentTransaction.  # noqa: E501
        :rtype: List[InvoiceItem]
        """
        return self._adjustments

    @adjustments.setter
    def adjustments(self, adjustments):
        """Sets the adjustments of this InvoicePaymentTransaction.


        :param adjustments: The adjustments of this InvoicePaymentTransaction.  # noqa: E501
        :type: List[InvoiceItem]
        """

        self._adjustments = adjustments

    @property
    def audit_logs(self):
        """Gets the audit_logs of this InvoicePaymentTransaction.  # noqa: E501


        :return: The audit_logs of this InvoicePaymentTransaction.  # noqa: E501
        :rtype: List[AuditLog]
        """
        return self._audit_logs

    @audit_logs.setter
    def audit_logs(self, audit_logs):
        """Sets the audit_logs of this InvoicePaymentTransaction.


        :param audit_logs: The audit_logs of this InvoicePaymentTransaction.  # noqa: E501
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
        if not isinstance(other, InvoicePaymentTransaction):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
