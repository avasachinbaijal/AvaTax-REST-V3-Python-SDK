"""
AvaTax Software Development Kit for Python.

   Copyright 2022 Avalara, Inc.

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.

    foundation
    Platform foundation consists of services on top of which the Avalara Compliance Cloud platform is built. These services are foundational and provide functionality such as common organization, tenant and user management for the rest of the compliance platform. 

@author     Sachin Baijal <sachin.baijal@avalara.com>
@author     Jonathan Wenger <jonathan.wenger@avalara.com>
@copyright  2022 Avalara, Inc.
@license    https://www.apache.org/licenses/LICENSE-2.0
@version    2.4.34
@link       https://github.com/avadev/AvaTax-REST-V3-Python-SDK
"""

import re  # noqa: F401
import sys  # noqa: F401

from Avalara.SDK.model_utils import (  # noqa: F401
    ApiTypeError,
    ModelComposed,
    ModelNormal,
    ModelSimple,
    cached_property,
    change_keys_js_to_python,
    convert_js_args_to_python_args,
    date,
    datetime,
    file_type,
    none_type,
    validate_get_composed_info,
    OpenApiModel
)
from Avalara.SDK.exceptions import ApiAttributeError


def lazy_import():
    from Avalara.SDK.model.IAMDS.aspect import Aspect
    from Avalara.SDK.model.IAMDS.instance import Instance
    from Avalara.SDK.model.IAMDS.instance_meta import InstanceMeta
    from Avalara.SDK.model.IAMDS.reference import Reference
    from Avalara.SDK.model.IAMDS.tag import Tag
    globals()['Aspect'] = Aspect
    globals()['Instance'] = Instance
    globals()['InstanceMeta'] = InstanceMeta
    globals()['Reference'] = Reference
    globals()['Tag'] = Tag


class User(ModelComposed):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    Attributes:
      allowed_values (dict): The key is the tuple path to the attribute
          and the for var_name this is (var_name,). The value is a dict
          with a capitalized key describing the allowed value and an allowed
          value. These dicts store the allowed enum values.
      attribute_map (dict): The key is attribute name
          and the value is json key in definition.
      discriminator_value_class_map (dict): A dict to go from the discriminator
          variable value to the discriminator class name.
      validations (dict): The key is the tuple path to the attribute
          and the for var_name this is (var_name,). The value is a dict
          that stores validations for max_length, min_length, max_items,
          min_items, exclusive_maximum, inclusive_maximum, exclusive_minimum,
          inclusive_minimum, and regex.
      additional_properties_type (tuple): A tuple of classes accepted
          as additional properties values.
    """

    allowed_values = {
    }

    validations = {
        ('emails',): {
            'min_items': 1,
        },
    }

    additional_properties_type = None

    _nullable = False

    @cached_property
    def openapi_types():
        """
        This must be a method because a model may have properties that are
        of type self, this must run after the class is loaded

        Returns
            openapi_types (dict): The key is attribute name
                and the value is attribute type.
        """
        lazy_import()
        return {
            'user_name': (str,),  # noqa: E501
            'organization': (Reference,),  # noqa: E501
            'emails': ([{str: (bool, date, datetime, dict, float, int, list, str, none_type)}],),  # noqa: E501
            'id': (str,),  # noqa: E501
            'external_id': (str,),  # noqa: E501
            'name': ({str: (bool, date, datetime, dict, float, int, list, str, none_type)},),  # noqa: E501
            'display_name': (str,),  # noqa: E501
            'nick_name': (str,),  # noqa: E501
            'profile_url': (str,),  # noqa: E501
            'title': (str,),  # noqa: E501
            'user_type': (str,),  # noqa: E501
            'preferred_language': (str,),  # noqa: E501
            'locale': (str,),  # noqa: E501
            'timezone': (str,),  # noqa: E501
            'active': (bool,),  # noqa: E501
            'password': (str,),  # noqa: E501
            'phone_numbers': ([{str: (bool, date, datetime, dict, float, int, list, str, none_type)}],),  # noqa: E501
            'addresses': ([{str: (bool, date, datetime, dict, float, int, list, str, none_type)}],),  # noqa: E501
            'default_tenant': (Reference,),  # noqa: E501
            'custom_claims': ([{str: (bool, date, datetime, dict, float, int, list, str, none_type)}],),  # noqa: E501
            'meta': (InstanceMeta,),  # noqa: E501
            'aspects': ([Aspect],),  # noqa: E501
            'tags': ([Tag],),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None


    attribute_map = {
        'user_name': 'userName',  # noqa: E501
        'organization': 'organization',  # noqa: E501
        'emails': 'emails',  # noqa: E501
        'id': 'id',  # noqa: E501
        'external_id': 'externalId',  # noqa: E501
        'name': 'name',  # noqa: E501
        'display_name': 'displayName',  # noqa: E501
        'nick_name': 'nickName',  # noqa: E501
        'profile_url': 'profileUrl',  # noqa: E501
        'title': 'title',  # noqa: E501
        'user_type': 'userType',  # noqa: E501
        'preferred_language': 'preferredLanguage',  # noqa: E501
        'locale': 'locale',  # noqa: E501
        'timezone': 'timezone',  # noqa: E501
        'active': 'active',  # noqa: E501
        'password': 'password',  # noqa: E501
        'phone_numbers': 'phoneNumbers',  # noqa: E501
        'addresses': 'addresses',  # noqa: E501
        'default_tenant': 'defaultTenant',  # noqa: E501
        'custom_claims': 'customClaims',  # noqa: E501
        'meta': 'meta',  # noqa: E501
        'aspects': 'aspects',  # noqa: E501
        'tags': 'tags',  # noqa: E501
    }

    read_only_vars = {
        'id',  # noqa: E501
    }

    @classmethod
    @convert_js_args_to_python_args
    def _from_openapi_data(cls, *args, **kwargs):  # noqa: E501
        """User - a model defined in OpenAPI

        Keyword Args:
            user_name (str): Human readable unique identifier of the user, typically used to authenticate with an identity provider
            organization (Reference):
            emails ([{str: (bool, date, datetime, dict, float, int, list, str, none_type)}]): A List of email addresses associated with the user
            id (str): Unique identifier for the Object
            _check_type (bool): if True, values for parameters in openapi_types
                                will be type checked and a TypeError will be
                                raised if the wrong type is input.
                                Defaults to True
            _path_to_item (tuple/list): This is a list of keys or values to
                                drill down to the model in received_data
                                when deserializing a response
            _spec_property_naming (bool): True if the variable names in the input data
                                are serialized names, as specified in the OpenAPI document.
                                False if the variable names in the input data
                                are pythonic names, e.g. snake case (default)
            _configuration (Configuration): the instance to use when
                                deserializing a file_type parameter.
                                If passed, type conversion is attempted
                                If omitted no type conversion is done.
            _visited_composed_classes (tuple): This stores a tuple of
                                classes that we have traveled through so that
                                if we see that class again we will not use its
                                discriminator again.
                                When traveling through a discriminator, the
                                composed schema that is
                                is traveled through is added to this set.
                                For example if Animal has a discriminator
                                petType and we pass in "Dog", and the class Dog
                                allOf includes Animal, we move through Animal
                                once using the discriminator, and pick Dog.
                                Then in Dog, we will make an instance of the
                                Animal class but this time we won't travel
                                through its discriminator because we passed in
                                _visited_composed_classes = (Animal,)
            external_id (str): Identifier for the user in external systems (clients). The external systems manage this. [optional]  # noqa: E501
            name ({str: (bool, date, datetime, dict, float, int, list, str, none_type)}): The components of the user's real name.  Providers MAY return just the full name as a single string in the formatted sub-attribute, or they MAY return just the individual component attributes using the other sub-attributes, or they MAY return both.  If both variants are returned, they SHOULD be describing the same name, with the formatted name indicating how the component attributes should be combined.. [optional]  # noqa: E501
            display_name (str): The name of the User, suitable for display to end-users.  The name SHOULD be the full name of the User being described, if known. [optional]  # noqa: E501
            nick_name (str): The casual way to address the user in real life, e.g., 'Bob' or 'Bobby' instead of 'Robert'.  This attribute SHOULD NOT be used to represent a User's username (e.g., 'bjensen' or 'mpepperidge'). [optional]  # noqa: E501
            profile_url (str): A fully qualified URL pointing to a page representing the User's online profile. [optional]  # noqa: E501
            title (str): The user's title, such as \"Vice President.\". [optional]  # noqa: E501
            user_type (str): Used to identify the relationship between the organization and the user.  Typical values used might be 'Contractor', 'Employee', 'Intern', 'Temp', 'External', and 'Unknown', but any value may be used. [optional]  # noqa: E501
            preferred_language (str): Indicates the User's preferred written or spoken language.  Generally used for selecting a localized user interface; e.g., 'en_US' specifies the language English and country US. [optional]  # noqa: E501
            locale (str): Used to indicate the User's default location for purposes of localizing items such as currency, date time format, or numerical representations. [optional]  # noqa: E501
            timezone (str): The User's time zone in the 'Olson' time zone database format, e.g., 'America/Los_Angeles'. [optional]  # noqa: E501
            active (bool): A Boolean value indicating the User's administrative status. [optional]  # noqa: E501
            password (str): The User's cleartext password.  This attribute is intended to be used as a means to specify an initial password when creating a new User or to reset an existing User's password. [optional]  # noqa: E501
            phone_numbers ([{str: (bool, date, datetime, dict, float, int, list, str, none_type)}]): A List of phone numbers associated with the user. [optional]  # noqa: E501
            addresses ([{str: (bool, date, datetime, dict, float, int, list, str, none_type)}]): A physical mailing address for this User, as described in (address Element). Canonical Type Values of work, home, and other. The value attribute is a complex type with the following sub-attributes. [optional]  # noqa: E501
            default_tenant (Reference): [optional]  # noqa: E501
            custom_claims ([{str: (bool, date, datetime, dict, float, int, list, str, none_type)}]): Custom claims that are returned along with a requested scope during authentication. [optional]  # noqa: E501
            meta (InstanceMeta): [optional]  # noqa: E501
            aspects ([Aspect]): Identifier of the Resource (if any) in other systems. [optional]  # noqa: E501
            tags ([Tag]): User defined tags in the form of key:value pair. [optional]  # noqa: E501
        """

        _check_type = kwargs.pop('_check_type', True)
        _spec_property_naming = kwargs.pop('_spec_property_naming', False)
        _path_to_item = kwargs.pop('_path_to_item', ())
        _configuration = kwargs.pop('_configuration', None)
        _visited_composed_classes = kwargs.pop('_visited_composed_classes', ())

        self = super(OpenApiModel, cls).__new__(cls)

        if args:
            raise ApiTypeError(
                "Invalid positional arguments=%s passed to %s. Remove those invalid positional arguments." % (
                    args,
                    self.__class__.__name__,
                ),
                path_to_item=_path_to_item,
                valid_classes=(self.__class__,),
            )

        self._data_store = {}
        self._check_type = _check_type
        self._spec_property_naming = _spec_property_naming
        self._path_to_item = _path_to_item
        self._configuration = _configuration
        self._visited_composed_classes = _visited_composed_classes + (self.__class__,)

        constant_args = {
            '_check_type': _check_type,
            '_path_to_item': _path_to_item,
            '_spec_property_naming': _spec_property_naming,
            '_configuration': _configuration,
            '_visited_composed_classes': self._visited_composed_classes,
        }
        composed_info = validate_get_composed_info(
            constant_args, kwargs, self)
        self._composed_instances = composed_info[0]
        self._var_name_to_model_instances = composed_info[1]
        self._additional_properties_model_instances = composed_info[2]
        discarded_args = composed_info[3]

        for var_name, var_value in kwargs.items():
            if var_name in discarded_args and \
                        self._configuration is not None and \
                        self._configuration.discard_unknown_keys and \
                        self._additional_properties_model_instances:
                # discard variable.
                continue
            setattr(self, var_name, var_value)

        return self

    required_properties = set([
        '_data_store',
        '_check_type',
        '_spec_property_naming',
        '_path_to_item',
        '_configuration',
        '_visited_composed_classes',
        '_composed_instances',
        '_var_name_to_model_instances',
        '_additional_properties_model_instances',
    ])

    @convert_js_args_to_python_args
    def __init__(self, *args, **kwargs):  # noqa: E501
        """User - a model defined in OpenAPI

        Keyword Args:
            user_name (str): Human readable unique identifier of the user, typically used to authenticate with an identity provider
            organization (Reference):
            emails ([{str: (bool, date, datetime, dict, float, int, list, str, none_type)}]): A List of email addresses associated with the user
            _check_type (bool): if True, values for parameters in openapi_types
                                will be type checked and a TypeError will be
                                raised if the wrong type is input.
                                Defaults to True
            _path_to_item (tuple/list): This is a list of keys or values to
                                drill down to the model in received_data
                                when deserializing a response
            _spec_property_naming (bool): True if the variable names in the input data
                                are serialized names, as specified in the OpenAPI document.
                                False if the variable names in the input data
                                are pythonic names, e.g. snake case (default)
            _configuration (Configuration): the instance to use when
                                deserializing a file_type parameter.
                                If passed, type conversion is attempted
                                If omitted no type conversion is done.
            _visited_composed_classes (tuple): This stores a tuple of
                                classes that we have traveled through so that
                                if we see that class again we will not use its
                                discriminator again.
                                When traveling through a discriminator, the
                                composed schema that is
                                is traveled through is added to this set.
                                For example if Animal has a discriminator
                                petType and we pass in "Dog", and the class Dog
                                allOf includes Animal, we move through Animal
                                once using the discriminator, and pick Dog.
                                Then in Dog, we will make an instance of the
                                Animal class but this time we won't travel
                                through its discriminator because we passed in
                                _visited_composed_classes = (Animal,)
            external_id (str): Identifier for the user in external systems (clients). The external systems manage this. [optional]  # noqa: E501
            name ({str: (bool, date, datetime, dict, float, int, list, str, none_type)}): The components of the user's real name.  Providers MAY return just the full name as a single string in the formatted sub-attribute, or they MAY return just the individual component attributes using the other sub-attributes, or they MAY return both.  If both variants are returned, they SHOULD be describing the same name, with the formatted name indicating how the component attributes should be combined.. [optional]  # noqa: E501
            display_name (str): The name of the User, suitable for display to end-users.  The name SHOULD be the full name of the User being described, if known. [optional]  # noqa: E501
            nick_name (str): The casual way to address the user in real life, e.g., 'Bob' or 'Bobby' instead of 'Robert'.  This attribute SHOULD NOT be used to represent a User's username (e.g., 'bjensen' or 'mpepperidge'). [optional]  # noqa: E501
            profile_url (str): A fully qualified URL pointing to a page representing the User's online profile. [optional]  # noqa: E501
            title (str): The user's title, such as \"Vice President.\". [optional]  # noqa: E501
            user_type (str): Used to identify the relationship between the organization and the user.  Typical values used might be 'Contractor', 'Employee', 'Intern', 'Temp', 'External', and 'Unknown', but any value may be used. [optional]  # noqa: E501
            preferred_language (str): Indicates the User's preferred written or spoken language.  Generally used for selecting a localized user interface; e.g., 'en_US' specifies the language English and country US. [optional]  # noqa: E501
            locale (str): Used to indicate the User's default location for purposes of localizing items such as currency, date time format, or numerical representations. [optional]  # noqa: E501
            timezone (str): The User's time zone in the 'Olson' time zone database format, e.g., 'America/Los_Angeles'. [optional]  # noqa: E501
            active (bool): A Boolean value indicating the User's administrative status. [optional]  # noqa: E501
            password (str): The User's cleartext password.  This attribute is intended to be used as a means to specify an initial password when creating a new User or to reset an existing User's password. [optional]  # noqa: E501
            phone_numbers ([{str: (bool, date, datetime, dict, float, int, list, str, none_type)}]): A List of phone numbers associated with the user. [optional]  # noqa: E501
            addresses ([{str: (bool, date, datetime, dict, float, int, list, str, none_type)}]): A physical mailing address for this User, as described in (address Element). Canonical Type Values of work, home, and other. The value attribute is a complex type with the following sub-attributes. [optional]  # noqa: E501
            default_tenant (Reference): [optional]  # noqa: E501
            custom_claims ([{str: (bool, date, datetime, dict, float, int, list, str, none_type)}]): Custom claims that are returned along with a requested scope during authentication. [optional]  # noqa: E501
            meta (InstanceMeta): [optional]  # noqa: E501
            aspects ([Aspect]): Identifier of the Resource (if any) in other systems. [optional]  # noqa: E501
            tags ([Tag]): User defined tags in the form of key:value pair. [optional]  # noqa: E501
        """

        _check_type = kwargs.pop('_check_type', True)
        _spec_property_naming = kwargs.pop('_spec_property_naming', False)
        _path_to_item = kwargs.pop('_path_to_item', ())
        _configuration = kwargs.pop('_configuration', None)
        _visited_composed_classes = kwargs.pop('_visited_composed_classes', ())

        if args:
            raise ApiTypeError(
                "Invalid positional arguments=%s passed to %s. Remove those invalid positional arguments." % (
                    args,
                    self.__class__.__name__,
                ),
                path_to_item=_path_to_item,
                valid_classes=(self.__class__,),
            )

        self._data_store = {}
        self._check_type = _check_type
        self._spec_property_naming = _spec_property_naming
        self._path_to_item = _path_to_item
        self._configuration = _configuration
        self._visited_composed_classes = _visited_composed_classes + (self.__class__,)

        constant_args = {
            '_check_type': _check_type,
            '_path_to_item': _path_to_item,
            '_spec_property_naming': _spec_property_naming,
            '_configuration': _configuration,
            '_visited_composed_classes': self._visited_composed_classes,
        }
        composed_info = validate_get_composed_info(
            constant_args, kwargs, self)
        self._composed_instances = composed_info[0]
        self._var_name_to_model_instances = composed_info[1]
        self._additional_properties_model_instances = composed_info[2]
        discarded_args = composed_info[3]

        for var_name, var_value in kwargs.items():
            if var_name in discarded_args and \
                        self._configuration is not None and \
                        self._configuration.discard_unknown_keys and \
                        self._additional_properties_model_instances:
                # discard variable.
                continue
            setattr(self, var_name, var_value)
            if var_name in self.read_only_vars:
                raise ApiAttributeError(f"`{var_name}` is a read-only attribute. Use `from_openapi_data` to instantiate "
                                     f"class with read only attributes.")

    @cached_property
    def _composed_schemas():
        # we need this here to make our import statements work
        # we must store _composed_schemas in here so the code is only run
        # when we invoke this method. If we kept this at the class
        # level we would get an error because the class level
        # code would be run when this module is imported, and these composed
        # classes don't exist yet because their module has not finished
        # loading
        lazy_import()
        return {
          'anyOf': [
          ],
          'allOf': [
              Instance,
          ],
          'oneOf': [
          ],
        }
