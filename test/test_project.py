from walter import project
import os
from path import Path

def test_project1():
    cwd = Path(os.getcwd()).abspath()

    p = project.Project(name='')
    assert p.name

    assert str(cwd) != str(p.dirname)
    p.deactivate()

    whereIam = str(Path(os.getcwd()).abspath())
    assert str(cwd) == whereIam, str(cwd) + ' / '+ whereIam

    assert (cwd/p.name).exists()
    assert (cwd/p.name).isdir()

    p.activate()
    p.remove(force=True)

    assert (cwd/p.name).exists() is False


def test_read_parameters():
    fn = 'sim_scheme_test.csv'
    p = project.Project()
    params = p.csv_parameters('sim_scheme_test.csv')
    assert len(params) == 1
    p.remove(force=True)
