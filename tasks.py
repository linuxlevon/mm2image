from invoke import task

@task
def generate_requirements(c):
    """Generate requirements.txt from requirements.in"""
    c.run(f"pip-compile requirements.in")
    print('done')

@task
def sync_requirements(c):
    """Install/synchronize requirements.txt"""
    c.run("pip-sync requirements.txt")
    print('done')


def generate_dev_requirements(c):
    """Generate requirements.txt from dev-requirements.in"""
    c.run(f"pip-compile dev-requirements.in")
    print('done')

@task
def sync_dev_requirements(c):
    """Install/synchronize dev-requirements.txt"""
    c.run("pip-sync dev-requirements.txt")
    print('done')
