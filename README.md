kibana role
=========
[![License](https://img.shields.io/badge/license-Apache-green.svg?style=flat)](https://raw.githubusercontent.com/lean-delivery/ansible-role-kibana/master/LICENSE)
[![Build Status](https://travis-ci.org/lean-delivery/ansible-role-kibana.svg?branch=master)](https://travis-ci.org/lean-delivery/ansible-role-kibana)
[![Build Status](https://gitlab.com/lean-delivery/ansible-role-kibana/badges/master/build.svg)](https://gitlab.com/lean-delivery/ansible-role-kibana)

## Summary

This Ansible role has the following features:

 - Install kibana
 - Binds kibana with preinstalled elasticsearch host

Requirements
------------

 - Version of the ansible for installation: 2.5
 - **Supported OS**:  
   - EL
     - 6
     - 7
   - Ubuntu
     - 18.04

## Role Variables

- defaults
  - `elastic_branch`  
  Used to select main kibana version to be installed (5.x or 6.x current stable versions). By default this variable is set to `5`. So, `5.x` version is installed by default. You can override this by setting this variable in playbook.
  - `kibana_host`  
  Specifies the address to which the Kibana server will bind. IP addresses and host names are both valid values. The default is 'localhost', which usually means remote machines will not be able to connect. To allow connections from remote users, set this parameter to a non-loopback address.
  - `kibana_port`  
  Specifies the port to use for Kibana. Default value is `5601`.
  - `elasticsearch_host` and `elasticsearch_port`  
  Variables are necessary for Kibana to be able to communicate to running Elasticsearch server. Please set proper values of these variables according to your infrastructure. Default values are `localhost` and `9200`.
  - `kibana_config_path`  
  Path to kibana config directory. Default value is `/etc/kibana`.
  - `kibana_config`
  All Kibana configuration parameters are supported. This is achieved using a configuration map parameter `kibana_config` which is serialized into the kibana.yml file.
  - `kibana_log_path`
  Kibana log storage directory.
  - `kibana_gpg_key`
  GPG key for repositories. Default value is `https://artifacts.elastic.co/GPG-KEY-elasticsearch`.

## Some examples of the installing current role

ansible-galaxy install lean_delivery.kibana

Example Playbook
----------------

### Installing kibana 6.x version:
```yaml
- name: "Install kibana"
  hosts: kibana-host
  vars:
    elastic_branch: "6"
    kibana_host: "localhost"
    elasticsearch_host: "localhost"
    elasticsearch_port: "9200"
  roles:
     - role: "lean-delivery.kibana"
```

### Installing kibana 6.x version with disabled xpack security feature:
```yaml
- name: "Install kibana"
  hosts: kibana-host
  vars:
    elastic_branch: "6"
    kibana_host: "localhost"
    kibana_config:
      xpack.security.enabled: false
  roles:
     - role: "lean-delivery.kibana"
```

### Installing kibana 5.x version:
```yaml
- name: "Install kibana"
  hosts: kibana-host
  vars:
    kibana_host: "kibana.example.org"
    elasticsearch_host: "elasticsearch.example.org"
    elasticsearch_port: "9200"
  roles:
     - role: "lean-delivery.kibana"
```

License
-------

Apache2

Author Information
------------------

authors:
  - Lean Delivery <team@lean-delivery.com>