# Copyright © Michal Čihař <michal@weblate.org>
#
# SPDX-License-Identifier: GPL-3.0-or-later

"""Example pre commit script."""

from django.utils.translation import gettext_lazy as _

from weblate.addons.events import EVENT_PRE_COMMIT
from weblate.addons.base import BaseAddon
from .forms import HoldOnSettingsForm


class HoldOnAddon(BaseAddon):
    settings_form = HoldOnSettingsForm

    # This addon can be installed multiple times per component
    multiple = True
    icon = "language.svg"

    @classmethod
    def can_install(cls, component, user):
        return True

    # Event used to trigger the script
    events = (EVENT_PRE_COMMIT,)
    # Name of the addon, has to be unique
    name = "weblate.example.pre"
    # Verbose name and long description
    verbose = _("Execute script before commit @@@ add by dennis")
    description = _("This add-on executes a script!!!!.")

    # Script to execute
    script = "/bin/true"
    # File to add in commit (for pre commit event)
    # does not have to be set
    add_file = "po/{{ language_code }}.po"
