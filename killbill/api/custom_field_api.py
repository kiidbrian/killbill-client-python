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


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from killbill.api_client import ApiClient


class CustomFieldApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def get_custom_fields(self, api_key=None, api_secret=None, **kwargs):  # noqa: E501
        """List custom fields  # noqa: E501

          # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_custom_fields(api_key, api_secret, async=True)
        >>> result = thread.get()

        :param async bool
        :param Str api_key: (required)
        :param Str api_secret: (required)
        :param Int offset:
        :param Int limit:
        :param Str audit:
        :return: List[CustomField]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.get_custom_fields_with_http_info(api_key, api_secret, **kwargs)  # noqa: E501
        else:
            (data) = self.get_custom_fields_with_http_info(api_key, api_secret, **kwargs)  # noqa: E501
            return data

    def get_custom_fields_with_http_info(self, api_key=None, api_secret=None, **kwargs):  # noqa: E501
        """List custom fields  # noqa: E501

          # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_custom_fields_with_http_info(api_key, api_secret, async=True)
        >>> result = thread.get()

        :param async bool
        :param Str api_key: (required)
        :param Str api_secret: (required)
        :param Int offset:
        :param Int limit:
        :param Str audit:
        :return: List[CustomField]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['api_key', 'api_secret', 'offset', 'limit', 'audit']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_custom_fields" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'api_key' is set
        if ('api_key' not in params or
                params['api_key'] is None):
            raise ValueError("Missing the required parameter `api_key` when calling `get_custom_fields`")  # noqa: E501
        # verify the required parameter 'api_secret' is set
        if ('api_secret' not in params or
                params['api_secret'] is None):
            raise ValueError("Missing the required parameter `api_secret` when calling `get_custom_fields`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'offset' in params:
            query_params.append(('offset', params['offset']))  # noqa: E501
        if 'limit' in params:
            query_params.append(('limit', params['limit']))  # noqa: E501
        if 'audit' in params:
            query_params.append(('audit', params['audit']))  # noqa: E501

        header_params = {}
        if 'api_key' in params:
            header_params['X-Killbill-ApiKey'] = params['api_key']  # noqa: E501
        if 'api_secret' in params:
            header_params['X-Killbill-ApiSecret'] = params['api_secret']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['basicAuth']  # noqa: E501

        return self.api_client.call_api(
            '/1.0/kb/customFields/pagination', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='List[CustomField]',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def search_custom_fields(self, search_key=None, api_key=None, api_secret=None, **kwargs):  # noqa: E501
        """Search custom fields  # noqa: E501

          # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.search_custom_fields(search_key, api_key, api_secret, async=True)
        >>> result = thread.get()

        :param async bool
        :param Str search_key: (required)
        :param Str api_key: (required)
        :param Str api_secret: (required)
        :param Int offset:
        :param Int limit:
        :param Str audit:
        :return: List[CustomField]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.search_custom_fields_with_http_info(search_key, api_key, api_secret, **kwargs)  # noqa: E501
        else:
            (data) = self.search_custom_fields_with_http_info(search_key, api_key, api_secret, **kwargs)  # noqa: E501
            return data

    def search_custom_fields_with_http_info(self, search_key=None, api_key=None, api_secret=None, **kwargs):  # noqa: E501
        """Search custom fields  # noqa: E501

          # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.search_custom_fields_with_http_info(search_key, api_key, api_secret, async=True)
        >>> result = thread.get()

        :param async bool
        :param Str search_key: (required)
        :param Str api_key: (required)
        :param Str api_secret: (required)
        :param Int offset:
        :param Int limit:
        :param Str audit:
        :return: List[CustomField]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['search_key', 'api_key', 'api_secret', 'offset', 'limit', 'audit']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method search_custom_fields" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'search_key' is set
        if ('search_key' not in params or
                params['search_key'] is None):
            raise ValueError("Missing the required parameter `search_key` when calling `search_custom_fields`")  # noqa: E501
        # verify the required parameter 'api_key' is set
        if ('api_key' not in params or
                params['api_key'] is None):
            raise ValueError("Missing the required parameter `api_key` when calling `search_custom_fields`")  # noqa: E501
        # verify the required parameter 'api_secret' is set
        if ('api_secret' not in params or
                params['api_secret'] is None):
            raise ValueError("Missing the required parameter `api_secret` when calling `search_custom_fields`")  # noqa: E501

        if 'search_key' in params and not re.search('.*', params['search_key']):  # noqa: E501
            raise ValueError("Invalid value for parameter `search_key` when calling `search_custom_fields`, must conform to the pattern `/.*/`")  # noqa: E501
        collection_formats = {}

        path_params = {}
        if 'search_key' in params:
            path_params['searchKey'] = params['search_key']  # noqa: E501

        query_params = []
        if 'offset' in params:
            query_params.append(('offset', params['offset']))  # noqa: E501
        if 'limit' in params:
            query_params.append(('limit', params['limit']))  # noqa: E501
        if 'audit' in params:
            query_params.append(('audit', params['audit']))  # noqa: E501

        header_params = {}
        if 'api_key' in params:
            header_params['X-Killbill-ApiKey'] = params['api_key']  # noqa: E501
        if 'api_secret' in params:
            header_params['X-Killbill-ApiSecret'] = params['api_secret']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['basicAuth']  # noqa: E501

        return self.api_client.call_api(
            '/1.0/kb/customFields/search/{searchKey}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='List[CustomField]',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
