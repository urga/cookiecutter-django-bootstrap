from fabric.api import task, local

@task
def init_local_db():
    local("")