import os
from pathlib import Path

import yaml
import pipfile


def test_python_version_is_consistent_accross_all_configuration_and_readme():
    project_dir = Path(__file__).parent.parent

    ci_config_file = project_dir / '.circleci' / 'config.yml'
    ci_config = yaml.safe_load(ci_config_file.read_text())
    ci_docker_image = ci_config['jobs']['build']['docker'][0]['image']
    ci_py_version = ci_docker_image.replace('circleci/python:', '')

    pipfile_data = pipfile.load(os.path.join(project_dir, 'Pipfile')).data
    pipfile_py_version = pipfile_data['_meta']['requires']['python_version']

    readme = (project_dir / 'README.md').read_text()

    assert ci_py_version == pipfile_py_version
    assert f'Python {ci_py_version}' in readme
