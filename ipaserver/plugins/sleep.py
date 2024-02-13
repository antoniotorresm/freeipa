from ipalib.plugable import Registry
from ipalib import Command
from ipalib import Int
from ipalib.text import _
import time

register = Registry()

@register()
class sleep(Command):
    __doc__ = _('Sleep for the specified amount of time.')

    takes_args = (
        Int('seconds',
            default=1,
            autofill=True,
        ),
    )

    def execute(self, seconds, **options):
        time.sleep(seconds)
        return dict(result='Slept for %s seconds.' % str(seconds))
