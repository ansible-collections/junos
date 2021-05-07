#!/usr/bin/python
# -*- coding: utf-8 -*-

# (c) 2017, Ansible by Red Hat, inc
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import absolute_import, division, print_function

__metaclass__ = type


DOCUMENTATION = """
module: junos_interface
author: Ganesh Nalawade (@ganeshrn)
short_description: (deprecated, removed after 2022-06-01) Manage Interface on Juniper
  JUNOS network devices
description:
- This module provides declarative management of Interfaces on Juniper JUNOS network
  devices.
version_added: 1.0.0
deprecated:
  why: Updated modules released with more functionality
  alternative: Use M(junipernetworks.junos.junos_interfaces) instead.
  removed_at_date: '2022-06-01'
options:
  name:
    description:
    - Specify Name of the Interface.
    type: str
  description:
    description:
    - Description of Interface.
    type: str
  enabled:
    description:
    - Configure interface link status.
    type: bool
    default: True
  speed:
    description:
    - Interface link speed.
    type: str
  mtu:
    description:
    - Maximum size of transmit packet.
    type: int
  duplex:
    description:
    - Interface link status.
    type: str
    choices:
    - full
    - half
    - auto
  tx_rate:
    description:
    - Transmit rate in bits per second (bps).
    - This is state check parameter only.
    - Supports conditionals, see L(Conditionals in Networking Modules,../network/user_guide/network_working_with_command_output.html)
    type: str
  rx_rate:
    description:
    - Receiver rate in bits per second (bps).
    - This is state check parameter only.
    - Supports conditionals, see L(Conditionals in Networking Modules,../network/user_guide/network_working_with_command_output.html)
    type: str
  neighbors:
    description:
    - Check the operational state of given interface C(name) for LLDP neighbor.
    - The following suboptions are available.
    type: list
    elements: dict
    suboptions:
      host:
        description:
        - LLDP neighbor host for given interface C(name).
        type: str
      port:
        description:
        - LLDP neighbor port to which given interface C(name) is connected.
        type: str
  delay:
    description:
    - Time in seconds to wait before checking for the operational state on remote
      device. This wait is applicable for operational state argument which are I(state)
      with values C(up)/C(down), I(tx_rate) and I(rx_rate).
    type: int
    default: 10
  aggregate:
    description: List of Interfaces definitions.
    type: list
    elements: dict
    suboptions:
      name:
        description:
        - Name of the Interface.
        required: true
        type: str
      description:
        description:
        - Description of Interface.
        type: str
      enabled:
        description:
        - Configure interface link status.
        type: bool
      speed:
        description:
        - Interface link speed.
        type: str
      mtu:
        description:
        - Maximum size of transmit packet.
        type: int
      duplex:
        description:
        - Interface link status.
        type: str
        choices:
        - full
        - half
        - auto
      tx_rate:
        description:
        - Transmit rate in bits per second (bps).
        - This is state check parameter only.
        - Supports conditionals, see L(Conditionals in Networking Modules,../network/user_guide/network_working_with_command_output.html)
        type: str
      rx_rate:
        description:
        - Receiver rate in bits per second (bps).
        - This is state check parameter only.
        - Supports conditionals, see L(Conditionals in Networking Modules,../network/user_guide/network_working_with_command_output.html)
        type: str
      neighbors:
        description:
        - Check the operational state of given interface C(name) for LLDP neighbor.
        - The following suboptions are available.
        type: list
        elements: dict
        suboptions:
          host:
            description:
            - LLDP neighbor host for given interface C(name).
            type: str
          port:
            description:
            - LLDP neighbor port to which given interface C(name) is connected.
            type: str
      delay:
        description:
        - Time in seconds to wait before checking for the operational state on remote
          device. This wait is applicable for operational state argument which are I(state)
          with values C(up)/C(down), I(tx_rate) and I(rx_rate).
        type: int
      state:
        description:
        - State of the Interface configuration, C(up) indicates present and operationally
          up and C(down) indicates present and operationally C(down)
        type: str
        choices:
        - present
        - absent
        - up
        - down
      active:
        description:
        - Specifies whether or not the configuration is active or deactivated
        type: bool
  state:
    description:
    - State of the Interface configuration, C(up) indicates present and operationally
      up and C(down) indicates present and operationally C(down)
    type: str
    default: present
    choices:
    - present
    - absent
    - up
    - down
  active:
    description:
    - Specifies whether or not the configuration is active or deactivated
    default: true
    type: bool
requirements:
- ncclient (>=v0.5.2)
notes:
- This module requires the netconf system service be enabled on the remote device
  being managed.
- Tested against vSRX JUNOS version 15.1X49-D15.4, vqfx-10000 JUNOS Version 15.1X53-D60.4.
- Recommended connection is C(netconf). See L(the Junos OS Platform Options,../network/user_guide/platform_junos.html).
- This module also works with C(local) connections for legacy playbooks.
extends_documentation_fragment:
- junipernetworks.junos.junos
"""

EXAMPLES = """
- name: configure interface
  junipernetworks.junos.junos_interface:
    name: ge-0/0/1
    description: test-interface

- name: remove interface
  junipernetworks.junos.junos_interface:
    name: ge-0/0/1
    state: absent

- name: make interface down
  junipernetworks.junos.junos_interface:
    name: ge-0/0/1
    enabled: false

- name: make interface up
  junipernetworks.junos.junos_interface:
    name: ge-0/0/1
    enabled: true

- name: Deactivate interface config
  junipernetworks.junos.junos_interface:
    name: ge-0/0/1
    state: present
    active: false

- name: Activate interface config
  junipernetworks.junos.junos_interface:
    name: ge-0/0/1
    state: present
    active: true

- name: Configure interface speed, mtu, duplex
  junipernetworks.junos.junos_interface:
    name: ge-0/0/1
    state: present
    speed: 1g
    mtu: 256
    duplex: full

- name: Create interface using aggregate
  junipernetworks.junos.junos_interface:
    aggregate:
    - name: ge-0/0/1
      description: test-interface-1
    - name: ge-0/0/2
      description: test-interface-2
    speed: 1g
    duplex: full
    mtu: 512

- name: Delete interface using aggregate
  junipernetworks.junos.junos_interface:
    aggregate:
    - name: ge-0/0/1
    - name: ge-0/0/2
    state: absent

- name: Check intent arguments
  junipernetworks.junos.junos_interface:
    name: '{{ name }}'
    state: up
    tx_rate: ge(0)
    rx_rate: le(0)

- name: Check neighbor intent
  junipernetworks.junos.junos_interface:
    name: xe-0/1/1
    neighbors:
    - port: Ethernet1/0/1
      host: netdev

- name: Config + intent
  junipernetworks.junos.junos_interface:
    name: '{{ name }}'
    enabled: false
    state: down
"""

RETURN = """
diff.prepared:
  description: Configuration difference before and after applying change.
  returned: when configuration is changed and diff option is enabled.
  type: str
  sample: >
        [edit interfaces]
        +   ge-0/0/1 {
        +       description test-interface;
        +   }
"""
import collections

from copy import deepcopy
from time import sleep

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.ansible.netcommon.plugins.module_utils.network.common.netconf import (
    exec_rpc,
)
from ansible_collections.ansible.netcommon.plugins.module_utils.network.common.utils import (
    remove_default_spec,
)
from ansible_collections.ansible.netcommon.plugins.module_utils.network.common.utils import (
    conditional,
)
from ansible_collections.junipernetworks.junos.plugins.module_utils.network.junos.junos import (
    junos_argument_spec,
    tostring,
)
from ansible_collections.junipernetworks.junos.plugins.module_utils.network.junos.junos import (
    load_config,
    map_params_to_obj,
    map_obj_to_ele,
)
from ansible_collections.junipernetworks.junos.plugins.module_utils.network.junos.junos import (
    commit_configuration,
    discard_changes,
    locked_config,
    to_param_list,
)

try:
    from lxml.etree import Element, SubElement
except ImportError:
    from xml.etree.ElementTree import Element, SubElement

USE_PERSISTENT_CONNECTION = True


def validate_mtu(value, module):
    if value and not 256 <= value <= 9192:
        module.fail_json(msg="mtu must be between 256 and 9192")


def validate_param_values(module, obj, param=None):
    if not param:
        param = module.params
    for key in obj:
        # validate the param value (if validator func exists)
        validator = globals().get("validate_%s" % key)
        if callable(validator):
            validator(param.get(key), module)


def main():
    """ main entry point for module execution
    """
    neighbors_spec = dict(host=dict(), port=dict())

    element_spec = dict(
        name=dict(),
        description=dict(),
        enabled=dict(default=True, type="bool"),
        speed=dict(type="str"),
        mtu=dict(type="int"),
        duplex=dict(choices=["full", "half", "auto"]),
        tx_rate=dict(),
        rx_rate=dict(),
        neighbors=dict(type="list", elements="dict", options=neighbors_spec),
        delay=dict(default=10, type="int"),
        state=dict(
            default="present", choices=["present", "absent", "up", "down"]
        ),
        active=dict(default=True, type="bool"),
    )

    aggregate_spec = deepcopy(element_spec)
    aggregate_spec["name"] = dict(required=True)

    # remove default in aggregate spec, to handle common arguments
    remove_default_spec(aggregate_spec)

    argument_spec = dict(
        aggregate=dict(type="list", elements="dict", options=aggregate_spec)
    )

    argument_spec.update(element_spec)
    argument_spec.update(junos_argument_spec)

    required_one_of = [["name", "aggregate"]]
    mutually_exclusive = [["name", "aggregate"]]

    module = AnsibleModule(
        argument_spec=argument_spec,
        required_one_of=required_one_of,
        mutually_exclusive=mutually_exclusive,
        supports_check_mode=True,
    )

    warnings = list()
    result = {"changed": False}

    if warnings:
        result["warnings"] = warnings

    top = "interfaces/interface"

    param_to_xpath_map = collections.OrderedDict()
    param_to_xpath_map.update(
        [
            ("name", {"xpath": "name", "is_key": True}),
            ("description", "description"),
            ("speed", "speed"),
            ("mtu", "mtu"),
            ("duplex", "link-mode"),
            ("disable", {"xpath": "disable", "tag_only": True}),
        ]
    )

    choice_to_value_map = {
        "link-mode": {
            "full": "full-duplex",
            "half": "half-duplex",
            "auto": "automatic",
        }
    }

    params = to_param_list(module)

    requests = list()
    for param in params:
        # if key doesn't exist in the item, get it from module.params
        for key in param:
            if param.get(key) is None:
                param[key] = module.params[key]

        item = param.copy()
        state = item.get("state")
        item["disable"] = True if not item.get("enabled") else False

        if state in ("present", "up", "down"):
            item["state"] = "present"

        validate_param_values(module, param_to_xpath_map, param=item)
        want = map_params_to_obj(module, param_to_xpath_map, param=item)
        requests.append(
            map_obj_to_ele(
                module, want, top, value_map=choice_to_value_map, param=item
            )
        )

    diff = None
    with locked_config(module):
        for req in requests:
            diff = load_config(module, tostring(req), warnings, action="merge")

        # issue commit after last configuration change is done
        commit = not module.check_mode
        if diff:
            if commit:
                commit_configuration(module)
            else:
                discard_changes(module)
            result["changed"] = True

            if module._diff:
                result["diff"] = {"prepared": diff}

    failed_conditions = []
    neighbors = None
    for item in params:
        state = item.get("state")
        tx_rate = item.get("tx_rate")
        rx_rate = item.get("rx_rate")
        want_neighbors = item.get("neighbors")

        if (
            state not in ("up", "down")
            and tx_rate is None
            and rx_rate is None
            and want_neighbors is None
        ):
            continue

        element = Element("get-interface-information")
        intf_name = SubElement(element, "interface-name")
        intf_name.text = item.get("name")

        if result["changed"]:
            sleep(item.get("delay"))

        reply = exec_rpc(module, tostring(element), ignore_warning=False)
        if state in ("up", "down"):
            admin_status = reply.xpath(
                "interface-information/physical-interface/admin-status"
            )
            if not admin_status or not conditional(
                state, admin_status[0].text.strip()
            ):
                failed_conditions.append("state " + "eq(%s)" % state)

        if tx_rate:
            output_bps = reply.xpath(
                "interface-information/physical-interface/traffic-statistics/output-bps"
            )
            if not output_bps or not conditional(
                tx_rate, output_bps[0].text.strip(), cast=int
            ):
                failed_conditions.append("tx_rate " + tx_rate)

        if rx_rate:
            input_bps = reply.xpath(
                "interface-information/physical-interface/traffic-statistics/input-bps"
            )
            if not input_bps or not conditional(
                rx_rate, input_bps[0].text.strip(), cast=int
            ):
                failed_conditions.append("rx_rate " + rx_rate)

        if want_neighbors:
            if neighbors is None:
                element = Element("get-lldp-interface-neighbors")
                intf_name = SubElement(element, "interface-device")
                intf_name.text = item.get("name")

                reply = exec_rpc(
                    module, tostring(element), ignore_warning=False
                )
                have_host = [
                    item.text
                    for item in reply.xpath(
                        "lldp-neighbors-information/lldp-neighbor-information/lldp-remote-system-name"
                    )
                ]
                have_port = [
                    item.text
                    for item in reply.xpath(
                        "lldp-neighbors-information/lldp-neighbor-information/lldp-remote-port-id"
                    )
                ]

            for neighbor in want_neighbors:
                host = neighbor.get("host")
                port = neighbor.get("port")
                if host and host not in have_host:
                    failed_conditions.append("host " + host)
                if port and port not in have_port:
                    failed_conditions.append("port " + port)
    if failed_conditions:
        msg = "One or more conditional statements have not been satisfied"
        module.fail_json(msg=msg, failed_conditions=failed_conditions)

    module.exit_json(**result)


if __name__ == "__main__":
    main()
