import os

import testinfra.utils.ansible_runner

group_name = 'ansible_role_kibana_v5_ubuntu'

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts(group_name)


def test_kibana_package_is_installed(host):
    kibana_pkg = host.package("kibana")
    assert kibana_pkg.is_installed
    assert kibana_pkg.version.startswith("5")


def test_kibana_service_running_and_enabled(host):
    kibana_svc = host.service("kibana")
    assert kibana_svc.is_running
    assert kibana_svc.is_enabled
