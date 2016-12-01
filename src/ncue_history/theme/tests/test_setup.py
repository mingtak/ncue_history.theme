# -*- coding: utf-8 -*-
"""Setup tests for this package."""
from ncue_history.theme.testing import NCUE_HISTORY_THEME_INTEGRATION_TESTING  # noqa
from plone import api

import unittest


class TestSetup(unittest.TestCase):
    """Test that ncue_history.theme is properly installed."""

    layer = NCUE_HISTORY_THEME_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')

    def test_product_installed(self):
        """Test if ncue_history.theme is installed."""
        self.assertTrue(self.installer.isProductInstalled(
            'ncue_history.theme'))

    def test_browserlayer(self):
        """Test that INcueHistoryThemeLayer is registered."""
        from ncue_history.theme.interfaces import (
            INcueHistoryThemeLayer)
        from plone.browserlayer import utils
        self.assertIn(INcueHistoryThemeLayer, utils.registered_layers())


class TestUninstall(unittest.TestCase):

    layer = NCUE_HISTORY_THEME_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')
        self.installer.uninstallProducts(['ncue_history.theme'])

    def test_product_uninstalled(self):
        """Test if ncue_history.theme is cleanly uninstalled."""
        self.assertFalse(self.installer.isProductInstalled(
            'ncue_history.theme'))

    def test_browserlayer_removed(self):
        """Test that INcueHistoryThemeLayer is removed."""
        from ncue_history.theme.interfaces import INcueHistoryThemeLayer
        from plone.browserlayer import utils
        self.assertNotIn(INcueHistoryThemeLayer, utils.registered_layers())
