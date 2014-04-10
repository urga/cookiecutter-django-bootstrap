from fabric.api import task, local
import dotenv
import dj_database_url

dotenv.read_dotenv()

@task
def create_db_localhost():
    """
    create the database user and database on localhost
    """

    database = dj_database_url.config()
    local("createuser %(USER)s -h localhost" % database)
    local("createdb %(NAME)s -O %(USER)s -h localhost" % database)

@task
def destroy_db_localhost():
    """
    destroy the database and the database user on localhost
    """

    database = dj_database_url.config()
    local("dropdb %(NAME)s -U %(USER)s -h localhost" % database)
    local("dropuser %(USER)s -h localhost" % database)