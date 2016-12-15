# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class PoolUpgradeOSParameter(Model):
    """Options for upgrading the operating system of compute nodes in a pool.

    :param target_os_version: The Azure Guest OS version to be installed on
     the virtual machines in the pool.
    :type target_os_version: str
    """ 

    _validation = {
        'target_os_version': {'required': True},
    }

    _attribute_map = {
        'target_os_version': {'key': 'targetOSVersion', 'type': 'str'},
    }

    def __init__(self, target_os_version):
        self.target_os_version = target_os_version
