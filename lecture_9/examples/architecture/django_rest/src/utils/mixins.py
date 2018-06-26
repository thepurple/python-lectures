"""
This module contains utils wrapped as mixins.
"""
import os
import subprocess

from django.conf import settings


# pylint: disable=too-few-public-methods
class Cmd:
    """
    Mixin which allows running external commands.
    Is used in conjunction with django BaseCommand class.
    """

    def run_cmd(self, cmd, is_local=True):
        """Runs a command with a real time output."""
        if is_local:
            cmd = os.path.join(settings.ROOT_DIR, cmd)

        process = subprocess.Popen(
            cmd,
            shell=True,
            stderr=subprocess.PIPE,
        )

        while process.poll() is None:
            out = process.stderr.readline().decode('utf-8')

            if out != '':
                self.stdout.write(out)  # pylint: disable=no-member
                self.stdout.flush()     # pylint: disable=no-member
