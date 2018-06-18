"""
This module defines a command to check source code with pep8 and pylint.
"""
from django.core.management.base import BaseCommand

from utils.mixins import Cmd


# pylint: disable=too-few-public-methods
class Command(Cmd, BaseCommand):
    """
    Runs pep8 and lint tests
    """
    help = """Runs pep8 and lint tests"""

    def add_arguments(self, parser):
        parser.add_argument(
            'target',
            type=str,
            nargs='?',
            default=None,
            help="Check specific module/file.",
        )

    def handle(self, *args, **options):  # pragma: no cover
        commands = (
            ('Run pep8', './utils/check-pep8.sh'),
            ('Run pylint', './utils/check-lint.sh'),
        )

        target = options['target']

        for command in commands:
            title, cmd = command
            if target:
                cmd += f' {target}'

            # pylint: disable=no-member
            self.stdout.write(self.style.SUCCESS(title))
            self.run_cmd(cmd)
