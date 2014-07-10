import os
from os.path import join, basename, dirname
import dotenv
import dj_database_url

from fabric.api import task, local, env, run, cd, get, settings, require

dotenv.read_dotenv()

@task
def production():
    """
    Use PRODUCTION settings.
    """
    env.hosts = os.environ["FABRIC_PRODUCTION_HOSTS"].split(",")  # mandatory setting
    env.branch = os.getenv("FABRIC_PRODUCTION_BRANCH", "master")
    env.basedir = os.getenv("FABRIC_PRODUCTION_BASEDIR", "~/webapps")
    set_appname()
    env.remote = True
    env.settings_name = "production"


@task
def staging():
    """
    Use STAGING settings.
    """
    env.hosts = os.getenv("FABRIC_STAGING_HOSTS", os.environ["FABRIC_PRODUCTION_HOSTS"]).split(",")
    env.branch = os.getenv("FABRIC_STAGING_BRANCH", "develop")
    env.basedir = os.getenv("FABRIC_STAGING_BASEDIR", "~/webapps")
    set_appname()
    env.remote = True
    env.settings_name = "staging"


def set_appname():
    """
    Set env.appname and env.webappdir based on environment or fallback to directory name.
    """
    if env.branch == "master":
        app_suffix = ""
    else:
        app_suffix = "_" + env.branch
    env.appname = os.getenv("APP_NAME", basename(dirname(__file__))) + app_suffix
    env.webappdir = join(env.basedir, env.appname)


def read_remote_dotenv():
    require("remote", provided_by=['staging', 'production'])
    get(join(env.webappdir, ".env"), "/tmp/.env")
    remote_settings = {}
    for k, v in dotenv.parse_dotenv("/tmp/.env"):
        remote_settings[k] = v
    return remote_settings


@task
def show_remote_config():
    require("remote", provided_by=['staging', 'production'])
    print
    print "*******************"
    print "CONFIGURATION FOR: %s" % env.settings_name
    print "*******************"
    print "HOSTS: ", env.hosts
    print "BRANCH: ", env.branch
    print "APP_NAME: ", env.appname
    print "WEBAPPDIR: ", env.webappdir
    print ""
    remote_settings = read_remote_dotenv()
    print "SETTINGS:"
    for k, v in remote_settings.items():
        print k + ":", v


@task
def copy_db():
    """
    recreate the local db with data from remote db
    """
    require("remote", provided_by=[staging, production])
    remote_settings = read_remote_dotenv()
    remote_database_settings = dj_database_url.parse(remote_settings["DATABASE_URL"])
    run("PGPASSWORD=%(PASSWORD)s pg_dump -Fp -b -U %(USER)s %(NAME)s > dump.sql" % remote_database_settings)
    get("dump.sql", "/tmp/")
    drop_db()
    create_db()
    database = dj_database_url.config()
    local("psql -h localhost -d %(NAME)s -U %(USER)s -f /tmp/dump.sql" % database)


@task
def create_db():
    """
    create the Postgresql database user and database on localhost
    """

    database = dj_database_url.config()
    with settings(warn_only=True):
        local("createuser %(USER)s -h localhost" % database)  # Can fail if db_user already exists
    local("createdb %(NAME)s -O %(USER)s -h localhost" % database)


@task
def drop_db():
    """
    destroy the Postgresql database and the database user on localhost
    """

    database = dj_database_url.config()
    with settings(warn_only=True):
        local("dropdb %(NAME)s -U %(USER)s -h localhost" % database)  # Can fail if  database doesn't exist
        local("dropuser %(USER)s -h localhost" % database) # Can fail if  db_user doesn't exist


@task
def reset_db():
    """
    destroy and rebuild the Postgresql database and the database user on localhost
    """
    drop_db()
    create_db()