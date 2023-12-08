#!/usr/bin/python3
"""Fabric script to generate tgz archive"""
from os.path import exists
from datetime import datetime
from fabric.api import local, task, env, put, run

env.hosts = ['100.26.247.248', '52.91.120.195']


@task
def do_pack():
    """creating an archive"""
    date = datetime.now()
    arc = f"web_static_{date.strftime('%Y%m%d%H%M%S')}.tgz"

    # Create versions directory
    local("mkdir -p versions")

    tgz_arc = local(f"tar -cvzf versions/{arc} web_static")
    if tgz_arc.succeeded:
        return arc
    return None


@task
def do_deploy(archive_path):
    """distributes an archive to your web servers"""
    if not exists(archive_path):
        return False

    try:
        archive_name = archive_path.split('/')[-1]
        archive_no_ext = archive_name.split('.')[0]

        put(archive_path, '/tmp/')
        run(f"rm -rf /data/web_static/releases/{archive_no_ext}")
        run(f"mkdir -p /data/web_static/releases/{archive_no_ext}")
        run(f"tar -xzf /tmp/{archive_name} -C\
            /data/web_static/releases/{archive_no_ext}/")
        run(f"rm /tmp/{archive_name}")
        run(f"mv /data/web_static/releases/{archive_no_ext}/web_static/*\
            /data/web_static/releases/{archive_no_ext}/")
        run(f"rm -rf /data/web_static/releases/{archive_no_ext}/web_static")
        run(f"rm -rf /data/web_static/current")
        run(f"ln -s /data/web_static/releases/{archive_no_ext}/\
            /data/web_static/current")
        print("New version deployed!")
        return True
    except Exception as e:
        print(e)


@task
def deploy():
    """ creates and distributes an archive to your web servers"""
    arc_path = do_pack()
    if arc_path is None:
        return False
    return do_deploy(arc_path)
