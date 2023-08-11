# `Ansika`: One-line installer for Smoother Employee Onboarding
<div align="center">
<img src="assets/ANSIKA.png" width="100%" />

[![Binary Build And Release](https://github.com/HexmosTech/Ansika/actions/workflows/build-and-release.yml/badge.svg)](https://github.com/HexmosTech/Ansika/actions/workflows/build-and-release.yml)
</div>

## Overview
Ansika (Ansible + Nuitka), simplifies installation into just one line. It swiftly downloads, authorizes, and activates the binary file on your employees' or interns' computers. With Ansika, you can effortlessly set up and install software packages, libraries, and even system or package configurations across your team's devices, eliminating hassle.

Ansika streamlines the process into a solitary executable file, eliminating the need for external dependencies. By configuring your software packages, libraries, and settings within the ansible playbook file (one_installer.yml), a single command takes care of the rest. This command seamlessly downloads, provides permissions, and executes the binary file on local machines.

## Benefits
- Install any combination of software packages, libraries and extensions
- Run commands and configure setting files
- Produce zero-dependency binaries
- Provide one-liner to perform every on-boarding task
- 100% Free and Open Source Software
- Built upon solid tech: Ansible and Nuitka (Python)

## Usage
### Requirements
- python: Version 2.7 or 3.5 and higher
- Ansible: Version 2.7 or higher (depends on python version installed)
- Nuitka: Version 1.7.5 or higher

### Installing Requirements
- Install Ansible : `pip3 install ansible==8.2.0`
- Install Nuitka : `pip3 install nuitka==1.7.5`
### Editing yaml

 Modify the ansible playbook file in this repository ([one_installer.yml](https://github.com/HexmosTech/Ansika/blob/main/one_installer.yml)) to include additional instructions for installing software packages, tools, extensions, and configurations. For further insights into ansible and ansible playbook, you can refer to the [Ansible documentation](https://docs.ansible.com/ansible/latest/getting_started/index.html).

### Local Testing
#### Executing Ansible Python API
#### Build Binary using Nuitka 
#### Executing binary

### Release and Oneline command
#### Github Workflow
#### Binary Release
#### Oneline Command

### Blog Post about Ansika

### Acknowledgements
