#!/usr/bin/python3
"""Fabric script to generate tgz archive"""

from datetime import datetime
from fabric.api import local, task


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

