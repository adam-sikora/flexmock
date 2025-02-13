"""Flexmock test runner integrations."""
# pylint: disable=import-outside-toplevel, import-error
import sys
import unittest
from contextlib import suppress
from functools import wraps
from typing import Any, Type

from flexmock.api import flexmock_teardown


def _patch_test_result(klass: Type[Any]) -> None:
    """Patches flexmock into any class that inherits unittest.TestResult.

    This seems to work well for majority of test runners. In the case of nose
    it's not even necessary as it doesn't override unittest.TestResults's
    addSuccess and addFailure methods so simply patching unittest works
    out of the box for nose.

    For those that do inherit from unittest.TestResult and override its
    stopTest and addSuccess methods, patching is pretty straightforward
    (numerous examples below).

    The reason we don't simply patch unittest's parent TestResult class
    is stopTest and addSuccess in the child classes tend to add messages
    into the output that we want to override in case flexmock generates
    its own failures.

    Args:
        klass: the class whose stopTest method needs to be decorated.
    """
    # pylint: disable=invalid-name
    _patch_stop_test(klass)
    _patch_add_success(klass)


def _patch_stop_test(klass: Type[unittest.TextTestResult]) -> None:
    """Add call to teardown in klass.stopTest method.

    Args:
        klass: the class whose stopTest method needs to be decorated.
    """
    saved_add_success = klass.addSuccess
    saved_stop_test = klass.stopTest

    @wraps(saved_stop_test)
    def decorated(self: unittest.TextTestResult, test: unittest.TestCase) -> None:
        if saved_stop_test.__code__ is not decorated.__code__:
            # if parent class was for some reason patched, avoid calling
            # flexmock_teardown() twice and delegate up the class hierarchy
            # this doesn't help if there is a gap and only the parent's
            # parent class was patched, but should cover most screw-ups
            try:
                flexmock_teardown()
                saved_add_success(self, test)
            except Exception:
                if hasattr(self, "_pre_flexmock_success"):
                    self.addFailure(test, sys.exc_info())
            if hasattr(self, "_pre_flexmock_success"):
                del self._pre_flexmock_success  # type: ignore
        return saved_stop_test(self, test)

    if klass.stopTest is not decorated:
        klass.stopTest = decorated  # type: ignore


def _patch_add_success(klass: Type[unittest.TextTestResult]) -> None:
    """Modify the addSuccess method of the klass for flexmock.

    Args:
        klass: the class whose stopTest method needs to be decorated.
    """

    @wraps(klass.addSuccess)
    def decorated(self: unittest.TextTestResult, _test: unittest.TestCase) -> None:
        self._pre_flexmock_success = True  # type: ignore

    if klass.addSuccess is not decorated:
        klass.addSuccess = decorated  # type: ignore


# Hook flexmock into Pytest.
# Pytest is a Python test framework:
# https://github.com/pytest-dev/pytest

with suppress(ImportError):
    from _pytest import runner

    saved_pytest = runner.call_runtest_hook

    @wraps(saved_pytest)
    def call_runtest_hook(
        item: Any,
        when: str,
        **kwargs: Any,
    ) -> runner.CallInfo:
        """Call the teardown at the end of the tests.

        Args:
            item: The runner
            when: The moment this runs
            kwargs: additional arguments

        Returns:
            The teardown function
        """
        ret = saved_pytest(item, when, **kwargs)  # type: ignore
        if when != "call" and ret.excinfo is None:
            return ret
        teardown = runner.CallInfo.from_call(flexmock_teardown, when=when)  # type: ignore
        if hasattr(runner.CallInfo, "duration"):
            # CallInfo.duration only available in Pytest 6+
            teardown.duration = ret.duration
        if ret.excinfo is not None:
            teardown.excinfo = ret.excinfo
        return teardown

    runner.call_runtest_hook = call_runtest_hook


# Hook flexmock into doctest.

with suppress(ImportError):
    from doctest import DocTestRunner, TestResults

    saved_doctest = DocTestRunner.run

    @wraps(saved_doctest)
    def run(
        *args: Any,
        **kwargs: Any,
    ) -> TestResults:
        """Call the teardown at the end of the tests.

        Args:
            args: the arguments passed to the runner
            kwargs: the keyword arguments passed to the runner

        Returns:
            The test results

        """
        try:
            return saved_doctest(*args, **kwargs)
        finally:
            flexmock_teardown()

    DocTestRunner.run = run  # type: ignore


# Hook flexmock into unittest.
# only valid TestResult class for unittest is TextTestResult
_patch_test_result(unittest.TextTestResult)


# Hook into Teamcity unittests.
# This allows flexmock to be used within PyCharm.
with suppress(ImportError):
    from tcunittest import TeamcityTestResult

    _patch_test_result(TeamcityTestResult)


# Hook into teststools.
# testtools is a set of extensions to the Python standard library's unit testing framework:
# https://github.com/testing-cabal/testtools

with suppress(ImportError):
    from testtools import testresult

    _patch_test_result(testresult.TestResult)


# Hook into Zope testrunner.
# Zope is an open-source web application server:
# https://github.com/zopefoundation/Zope

with suppress(ImportError):
    from zope import testrunner  # pylint: disable=no-name-in-module

    _patch_test_result(testrunner.runner.TestResult)


# Hook into subunit.
# Subunit is a test reporting and controlling protocol.
# https://github.com/testing-cabal/subunit

with suppress(ImportError):
    import subunit

    _patch_test_result(subunit.TestProtocolClient)


# Hook into twisted.
# Twisted is an event-based framework for internet applications:
# https://github.com/twisted/twisted

with suppress(ImportError):
    from twisted.trial import reporter

    _patch_test_result(reporter.MinimalReporter)
    _patch_test_result(reporter.TextReporter)
    _patch_test_result(reporter.VerboseTextReporter)
    _patch_test_result(reporter.TreeReporter)
