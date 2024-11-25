import yaml

config = {
    "install_packages": [
        "python3",
        "nginx"
    ]
}

with open("todo.yml", 'r') as file:
    yaml_dict = yaml.safe_load(file)
    ansible_playbook = {
        "hosts": "localhost",
        "become": True,
        "tasks": []
    }

    # Install packages
    if 'install_packages' in yaml_dict['server']:
        ansible_playbook['tasks'].append(
            {"name": "Install packages",
             "ansible.builtin.apt": {"pkg": yaml_dict['server']["install_packages"] + ["redis"]}})

    # Copy over files and run files on a remote server with a Python interpreter
    if 'exploit_files' in yaml_dict['server']:
        for file in yaml_dict['server']['exploit_files']:
            if file == 'exploit.py':
                ansible_playbook['tasks'].append({"name": f"Copy {file} file",
                                                  "ansible.builtin.copy": {"src": f"src/ex00/{file}",
                                                                           "dest": f"src/ex02/{file}"}})
                ansible_playbook['tasks'].append({"name": f"Run a python script {file}",
                                                  "ansible.builtin.script": f"src/ex02/{file}",
                                                  "args": {"executable": "python"}})

            elif file == 'consumer.py':
                ansible_playbook['tasks'].append({"name": f"Copy {file} file",
                                                  "ansible.builtin.copy": {"src": f"src/ex01/{file}",
                                                                           "dest": f"src/ex02/{file}"}})
                if 'bad_guys' in yaml_dict:
                    ansible_playbook['tasks'].append({"name": f"Run a python script {file}",
                                                      "ansible.builtin.script": f"src/ex02/{file} -e {','.join(yaml_dict['bad_guys'])}",
                                                      "args": {"executable": "python3"}})


class CustomDumper(yaml.SafeDumper):
    pass


def dict_representer(dumper, data):
    return dumper.represent_dict(data.items())


CustomDumper.add_representer(dict, dict_representer)

with open("deploy.yml", "w") as file:
    yaml.dump(ansible_playbook, file, Dumper=CustomDumper, default_flow_style=False)
