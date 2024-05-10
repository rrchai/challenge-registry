# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from schematic_api.models.base_model_ import Model
from schematic_api import util


class ComponentRequirementSubgraph(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, component1=None, component2=None):  # noqa: E501
        """ComponentRequirementSubgraph - a model defined in OpenAPI

        :param component1: The component1 of this ComponentRequirementSubgraph.  # noqa: E501
        :type component1: str
        :param component2: The component2 of this ComponentRequirementSubgraph.  # noqa: E501
        :type component2: str
        """
        self.openapi_types = {
            'component1': str,
            'component2': str
        }

        self.attribute_map = {
            'component1': 'component1',
            'component2': 'component2'
        }

        self._component1 = component1
        self._component2 = component2

    @classmethod
    def from_dict(cls, dikt) -> 'ComponentRequirementSubgraph':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The ComponentRequirementSubgraph of this ComponentRequirementSubgraph.  # noqa: E501
        :rtype: ComponentRequirementSubgraph
        """
        return util.deserialize_model(dikt, cls)

    @property
    def component1(self):
        """Gets the component1 of this ComponentRequirementSubgraph.

        The display name of the first component in the graph  # noqa: E501

        :return: The component1 of this ComponentRequirementSubgraph.
        :rtype: str
        """
        return self._component1

    @component1.setter
    def component1(self, component1):
        """Sets the component1 of this ComponentRequirementSubgraph.

        The display name of the first component in the graph  # noqa: E501

        :param component1: The component1 of this ComponentRequirementSubgraph.
        :type component1: str
        """
        if component1 is None:
            raise ValueError("Invalid value for `component1`, must not be `None`")  # noqa: E501

        self._component1 = component1

    @property
    def component2(self):
        """Gets the component2 of this ComponentRequirementSubgraph.

        The display name of the second component in the graph  # noqa: E501

        :return: The component2 of this ComponentRequirementSubgraph.
        :rtype: str
        """
        return self._component2

    @component2.setter
    def component2(self, component2):
        """Sets the component2 of this ComponentRequirementSubgraph.

        The display name of the second component in the graph  # noqa: E501

        :param component2: The component2 of this ComponentRequirementSubgraph.
        :type component2: str
        """
        if component2 is None:
            raise ValueError("Invalid value for `component2`, must not be `None`")  # noqa: E501

        self._component2 = component2
