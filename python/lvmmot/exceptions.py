# !usr/bin/env python
# -*- coding: utf-8 -*-
#
# Licensed under a 3-clause BSD license.
#
# @Author: Brian Cherinka
# @Date:   2017-12-05 12:01:21
# @Last modified by:   Brian Cherinka
# @Last Modified time: 2017-12-05 12:19:32

from __future__ import print_function, division, absolute_import


class LvmmotError(Exception):
    """A custom core Lvmmot exception"""

    def __init__(self, message=None):

        message = 'There has been an error' \
            if not message else message

        super(LvmmotError, self).__init__(message)


class LvmmotNotImplemented(LvmmotError):
    """A custom exception for not yet implemented features."""

    def __init__(self, message=None):

        message = 'This feature is not implemented yet.' \
            if not message else message

        super(LvmmotNotImplemented, self).__init__(message)


class LvmmotAPIError(LvmmotError):
    """A custom exception for API errors"""

    def __init__(self, message=None):
        if not message:
            message = 'Error with Http Response from Lvmmot API'
        else:
            message = 'Http response error from Lvmmot API. {0}'.format(message)

        super(LvmmotAPIError, self).__init__(message)


class LvmmotApiAuthError(LvmmotAPIError):
    """A custom exception for API authentication errors"""
    pass


class LvmmotMissingDependency(LvmmotError):
    """A custom exception for missing dependencies."""
    pass


class LvmmotWarning(Warning):
    """Base warning for Lvmmot."""


class LvmmotUserWarning(UserWarning, LvmmotWarning):
    """The primary warning class."""
    pass


class LvmmotSkippedTestWarning(LvmmotUserWarning):
    """A warning for when a test is skipped."""
    pass


class LvmmotDeprecationWarning(LvmmotUserWarning):
    """A warning for deprecated features."""
    pass
