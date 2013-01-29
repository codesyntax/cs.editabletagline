from Products.CMFCore.utils import getToolByName
from Persistence import PersistentMapping

import logging

PROFILE_ID = 'profile-cs.editabletagline:default'


def upgrade_to_1001(context, logger=None):
    """Upgrade to cs.editablefooter 2.0"""
    if logger is None:
        # Called as upgrade step: define our own logger.
        logger = logging.getLogger('cs.editabletagline')

    setup = getToolByName(context, 'portal_setup')
    # Remove previous controlpanel registration
    controlpanel = getToolByName(context, 'portal_controlpanel')
    controlpanel.unregisterConfiglet('EditableTagline')
    # import permission settings
    setup.runImportStepFromProfile(PROFILE_ID, 'rolemap')
    # import new controlpanel
    setup.runImportStepFromProfile(PROFILE_ID, 'controlpanel')
    logger.info("All set")
