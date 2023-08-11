#!/usr/bin/env python
import shutil
import ansible.constants as C
from ansible.executor.task_queue_manager import TaskQueueManager
from ansible.module_utils.common.collections import ImmutableDict
from ansible.inventory.manager import InventoryManager
from ansible.parsing.dataloader import DataLoader
from ansible.vars.manager import VariableManager
from ansible import context
from ansible.executor.playbook_executor import PlaybookExecutor
import os
from ansible.utils.display import Display
import getpass


loader = DataLoader()

context.CLIARGS = ImmutableDict(
    listtasks=False,
    listhosts=False,
    syntax=False,
    connection="smart",
    forks=10,
    become=False,
    verbosity=4,
    check=False,
    start_at_task=None,
    become_method="sudo",
    become_user=None,
    become_ask_pass=True,
)

host_list = ["localhost"]
sources = ",".join(host_list)
inventory = InventoryManager(loader=loader, sources=sources, cache=False)
variable_manager = VariableManager(loader=loader, inventory=inventory)
sudo_password = getpass.getpass("Enter your root password :")
passwords = dict(become_pass=sudo_password)

tqm = TaskQueueManager(
    inventory=inventory,
    variable_manager=variable_manager,
    loader=loader,
    passwords=passwords,
)
display = Display()
display.verbosity = 1
playbook_executor = PlaybookExecutor(
    playbooks=[os.path.join(os.path.dirname(os.path.abspath(__file__)), "one_installer.yml")],
    inventory=inventory,
    variable_manager=variable_manager,
    loader=loader,
    passwords=passwords,
)


try:
    results = playbook_executor.run()

finally:
    tqm.cleanup()
    if loader:
        loader.cleanup_all_tmp_files()


shutil.rmtree(C.DEFAULT_LOCAL_TMP, True)
