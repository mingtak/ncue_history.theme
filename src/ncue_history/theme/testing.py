# -*- coding: utf-8 -*-
from plone.app.contenttypes.testing import PLONE_APP_CONTENTTYPES_FIXTURE
from plone.app.robotframework.testing import REMOTE_LIBRARY_BUNDLE_FIXTURE
from plone.app.testing import applyProfile
from plone.app.testing import FunctionalTesting
from plone.app.testing import IntegrationTesting
from plone.app.testing import PloneSandboxLayer
from plone.testing import z2

import ncue_history.theme


class NcueHistoryThemeLayer(PloneSandboxLayer):

    defaultBases = (PLONE_APP_CONTENTTYPES_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        # Load any other ZCML that is required for your tests.
        # The z3c.autoinclude feature is disabled in the Plone fixture base
        # layer.
        self.loadZCML(package=ncue_history.theme)

    def setUpPloneSite(self, portal):
        applyProfile(portal, 'ncue_history.theme:default')


NCUE_HISTORY_THEME_FIXTURE = NcueHistoryThemeLayer()


NCUE_HISTORY_THEME_INTEGRATION_TESTING = IntegrationTesting(
    bases=(NCUE_HISTORY_THEME_FIXTURE,),
    name='NcueHistoryThemeLayer:IntegrationTesting'
)


NCUE_HISTORY_THEME_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(NCUE_HISTORY_THEME_FIXTURE,),
    name='NcueHistoryThemeLayer:FunctionalTesting'
)


NCUE_HISTORY_THEME_ACCEPTANCE_TESTING = FunctionalTesting(
    bases=(
        NCUE_HISTORY_THEME_FIXTURE,
        REMOTE_LIBRARY_BUNDLE_FIXTURE,
        z2.ZSERVER_FIXTURE
    ),
    name='NcueHistoryThemeLayer:AcceptanceTesting'
)
