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


class ComputeNodeUser(Model):
    """An user account on a compute node.

    :param name: The user name of the account.
    :type name: str
    :param is_admin: Whether the account should be an administrator on the
     compute node. The default value is false.
    :type is_admin: bool
    :param expiry_time: The time at which the account should expire. If
     omitted, the default is 1 day from the current time. For Linux compute
     nodes, the expiryTime has a precision up to a day.
    :type expiry_time: datetime
    :param password: The password of the account. The password is required for
     Windows nodes (those created with 'cloudServiceConfiguration', or created
     with 'virtualMachineConfiguration' using a Windows image reference). For
     Linux compute nodes, the password can optionally be specified along with
     the sshPublicKey property.
    :type password: str
    :param ssh_public_key: The SSH public key that can be used for remote
     login to the compute node. The public key should be compatible with
     OpenSSH encoding and should be base 64 encoded. This property can be
     specified only for Linux nodes. If this is specified for a Windows node,
     then the Batch service rejects the request; if you are calling the REST
     API directly, the HTTP status code is 400 (Bad Request).
    :type ssh_public_key: str
    """ 

    _validation = {
        'name': {'required': True},
    }

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'is_admin': {'key': 'isAdmin', 'type': 'bool'},
        'expiry_time': {'key': 'expiryTime', 'type': 'iso-8601'},
        'password': {'key': 'password', 'type': 'str'},
        'ssh_public_key': {'key': 'sshPublicKey', 'type': 'str'},
    }

    def __init__(self, name, is_admin=None, expiry_time=None, password=None, ssh_public_key=None):
        self.name = name
        self.is_admin = is_admin
        self.expiry_time = expiry_time
        self.password = password
        self.ssh_public_key = ssh_public_key
