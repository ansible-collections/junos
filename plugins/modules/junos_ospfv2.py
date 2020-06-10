#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright 2020 Red Hat
# GNU General Public License v3.0+
# (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

#############################################
#                WARNING                    #
#############################################
#
# This file is auto generated by the resource
#   module builder playbook.
#
# Do not edit this file manually.
#
# Changes to this file will be over written
#   by the resource module builder.
#
# Changes should be made in the model used to
#   generate this file or in the resource module
#   builder template.
#
#############################################

"""
The module file for junos_ospfv2
"""

from __future__ import absolute_import, division, print_function

__metaclass__ = type


DOCUMENTATION = """
module: junos_ospfv2
short_description: OSPFv2 resource module
description:
- This module manages global OSPFv2 configuration on devices running Juniper JUNOS.
version_added: 1.0.0
author: Daniel Mellado (@dmellado)
requirements:
- ncclient (>=v0.6.4)
- xmltodict (>=0.12.0)
notes:
- This module requires the netconf system service be enabled on the device being managed.
- This module works with connection C(netconf). See L(the Junos OS Platform Options,../network/user_guide/platform_junos.html).
- Tested against JunOS v18.4R1
options:
  config:
    description: A list of OSPFv2 process configuration.
    type: list
    elements: dict
    suboptions:
      router_id:
        description:
        - The OSPFv2 router id.
        type: str
        required: true
      areas:
        description:
        - A list of OSPFv2 areas' configuration.
        type: list
        elements: dict
        suboptions:
          area_id:
            description:
            - The Area ID as an integer or IP Address.
            type: str
            required: true
          area_range:
            description:
            - Configure an address range for the area.
            type: str
          stub:
            description:
            - Settings for configuring the area as a stub.
            type: dict
            suboptions:
              default_metric:
                description:
                - Metric for the default route in this area.
                type: int
              set:
                description:
                - Configure the area as a stub.
                type: bool
          interfaces:
            description:
            - List of interfaces in this area.
            type: list
            elements: dict
            suboptions:
              authentication:
                type: dict
                suboptions:
                  type:
                    description:
                    - Type of authentication to use.
                    type: dict
              bandwidth_based_metrics:
                type: list
                elements: dict
                suboptions:
                  bandwidth:
                    description:
                    - BW to apply metric to.
                    type: str
                    choices: [1g, 10g]
                  metric:
                    description:
                    type: int
              name:
                description:
                - Name of the interface.
                type: str
                required: true
              priority:
                description:
                - Priority for the interface.
                type: int
              metric:
                description:
                - Metric applied to the interface.
                type: int
              flood_reduction:
                description:
                - Enable flood reduction.
                type: bool
              passive:
                type: bool
              timers:
                type: dict
                suboptions:
                  dead_interval:
                    description:
                    - Dead interval (seconds).
                    type: int
                  hello_interval:
                    description:
                    - Hello interval (seconds).
                    type: int
                  poll_interval:
                    description:
                    - Poll interval (seconds).
                    type: int
                  retransmit_interval:
                    description:
                    - Retransmit interval (seconds).
                    type: int
                  transit_delay:
                    description:
                    - Transit delay (seconds).
                    type: int
      external_preference:
        description:
        - Preference of external routes.
        type: int
      overload:
        type: dict
        suboptions:
          timeout:
            description:
            - Time after which overload mode is reset (seconds).
            type: int
      preference:
        description:
        - Preference of internal routes.
        type: int
      prefix_export_limit:
        description:
        - Maximum number of external prefixes that can be exported.
        type: int
      reference_bandwidth:
        description:
        - Bandwidth for calculating metric defaults.
        type: str
        choices: [1g, 10g]
      rfc1583compatibility:
        description:
        - Set RFC1583 compatibility
        type: bool
      spf_options:
        description:
        - Configure options for SPF.
        type: dict
        suboptions:
          delay:
            description:
            - Time to wait before running an SPF (seconds).
            type: int
          holddown:
            description:
            - Time to hold down before running an SPF (seconds).
            type: int
          rapid_runs:
            description:
            - Number of maximum rapid SPF runs before holddown (seconds).
            type: int
  state:
    description:
    - The state the configuration should be left in.
    type: str
    choices:
    - merged
    - replaced
    - overridden
    - deleted
    - gathered
    default: merged
"""
EXAMPLES = """
# Using merged
#
# Before state
# ------------
#
# admin# show protocols ospf

- name: Merge Junos OSPFv2 config
  junipernetworks.junos.junos_ospfv2:
    config:
    - router_id: 10.200.16.75
      reference_bandwidth: 10g
      areas:
      - area_id: 0.0.0.100
        area_range: 10.200.16.0/24
        stub:
          default_metric: 100
          set: true
        interfaces:
        - name: so-0/0/0.0
          priority: 3
          metric: 5
          flood_reduction: false
          passive: true
          bandwidth_based_metrics:
          - bandwidth: 1g
            metric: 5
          - bandwidth: 10g
            metric: 40
          timers:
            dead_interval: 4
            hello_interval: 2
            poll_interval: 2
            retransmit_interval: 2
      rfc1583compatibility: false
    state: merged

# After state
# -----------
#
# admin# show protocols ospf
# reference-bandwidth 10g;
# no-rfc-1583;
# area 0.0.0.100 {
#     stub default-metric 100;
#     area-range 10.200.16.0/24;
#     interface so-0/0/0.0 {
#         passive;
#         bandwidth-based-metrics {
#             bandwidth 1g metric 5;
#             bandwidth 10g metric 40;
#         }
#         metric 5;
#         priority 3;
#         retransmit-interval 2;
#         hello-interval 2;
#         dead-interval 4;
#         poll-interval 2;
#     }
# }

"""
RETURN = """
before:
  description: The configuration prior to the model invocation.
  returned: always
  sample: >
    The configuration returned will always be in the same format
     of the parameters above.
after:
  description: The resulting configuration model invocation.
  returned: when changed
  sample: >
    The configuration returned will always be in the same format
     of the parameters above.
commands:
  description: The set of commands pushed to the remote device.
  returned: always
  type: list
  sample: ['command 1', 'command 2', 'command 3']
"""


from ansible.module_utils.basic import AnsibleModule
from ansible_collections.junipernetworks.junos.plugins.module_utils.network.junos.argspec.ospf.ospf import (
    OspfArgs,
)
from ansible_collections.junipernetworks.junos.plugins.module_utils.network.junos.config.ospf.ospf import (
    Ospf,
)


def main():
    """
    Main entry point for module execution

    :returns: the result form module invocation
    """
    module = AnsibleModule(
        argument_spec=OspfArgs.argument_spec, supports_check_mode=True
    )

    result = Ospf(module).execute_module()
    module.exit_json(**result)


if __name__ == "__main__":
    main()
