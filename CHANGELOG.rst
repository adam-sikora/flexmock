This project follows semantic versioning.

Types of changes:

- **Added**: New features.
- **Changed**: Changes in existing functionality.
- **Deprecated**: Soon-to-be removed features.
- **Removed**: Removed features.
- **Fixed**: Bug fixes.
- **Infrastructure**: Changes in build or deployment infrastructure.
- **Documentation**: Changes in documentation.


Unreleased
----------

Added
#####

- Add Python 3.8, 3.9, 3.10 support.
- Add type annotations.

Changed
#######

- Flexmock needs to be imported explicitly using ``from flexmock import flexmock``.

Removed
#######

- Drop Python 2.7, 3.4, 3.5 support.
- Drop Pytest 4.x support.
- Remove unittest2 and nose integrations. unittest2 and nose are not maintained anymore.

Fixed
#####

- Fix `with_args` not working built-in functions and methods.

Infrastructure
##############

- Run linters and tests using Github Actions.
- Add coverage reporting using Codecov.

Documentation
#############

- Add contribution documentation.

Release 0.10.6
--------------

Fixed
#####

- Fix flexmock broken with Pytest 4 & 5.
- Fix new_instances method not working with Python 2.7.
- Fix multiple expectations for the same classmethod are not matched.

Release 0.10.5
--------------

Added
#####

- Improve error message on unmatched method signature expectation.

Fixed
#####

- Fix using ``should_call`` passes wrong ``runtime_self``.
- Fix pytest ``--durations`` flag when flexmock is installed.

Release 0.10.4
--------------

- drop Python 2.6, 3.3 and Jython support
- add Python 3.6 and 3.7 support
- don't hide exception when flexmock is used as context manager
- fix expectation reset for static methods on pypy 2
- ensure original exception isn't suppressed in pytest hook

Release 0.10.3
--------------

- fix compatibility with py.test 4.1
- minor documentation fixes

Release 0.10.2
--------------

- fix recognizing whether mocked object is a method or not on Python 3

Release 0.10.1
--------------

- fix decode problem in setup.py on Python 3

Release 0.10.0
--------------

- new official upstream repository: https://github.com/bkabrda/flexmock/
- new official homepage: https://flexmock.readthedocs.org
- adopted the official BSD 2-clause license
  `<https://en.wikipedia.org/wiki/BSD_licenses#2-clause_license_.28.22Simplified_BSD_License.22_or_.22FreeBSD_License.22.29>`_
- add support for calling flexmock module directly
- add support for mocking keyword-only args
- add support for Python 3.4 and 3.5
- drop support for Python 2.4, 2.5, 3.1 and 3.2
- add ``__version__`` attribute to flexmock module
- add various metadata to the package archive
- fix properly find out whether function is method or not
  and thanks to that don't strip first args of functions
- fix should_call to work when function returns ``None`` or ``False``
- fix various py.test issues
- fix ``CallOrderError`` with same subsequent mocking calls
- fix PyPy support issues
- various code style issues were fixed, 4-spaces indent is now used

Release 0.9.7
-------------

- small update to add support for TeamCity / PyCharm test runner.

Release 0.9.6
-------------

- fix staticmethod mocking on instances
- fix comparison of kwargs ordering issues
- fix ``ReturnValue.__str__``

Release 0.9.5
-------------

- bugfix: stop enforcing argument signatures on flexmock objects

Release 0.9.4
-------------

- add support for stubbing return values on getter properties
- add custom matcher object support to ``with_args``
- add support for striter function signature checks
- add support for non-callable attributes
- add support chained attributes (thanks Bryce Covert!)
- add iter support to ``Mock`` objects
- add PyPy support
- add Jython support
- fix ``should_call`` to work with class mocks
- fix ``and_return`` to return ``None`` by default
- fix MRO issues on builtin methods on 2.7+/3.2+
- imporove defaults: partial mocks created using the ``func=return_value``
  style now default to ``replace_with`` instead of ``should_receive`` for callables

Release 0.9.3
-------------

- add python 3.3 test target
- add proper handling of ``ordered()`` expectation across different methods
- add property support on fake objects
- fix compatibility with pytest 2.2 (thanks jpvanhal!)
- fix insidious bug with mocking subclasses of ``str`` class
- fix ``tuple`` handling when formatting arguments
- fix reseting subclass methods

Release 0.9.2
-------------

- fix mocking builtins by reseting expectation when raising exceptions
- fix mocking private methods on classes with leading underscores
- limit the damage of ``from flexmock import *`` by limiting to just ``flexmock()``
- ensure ``_pre_flexmock_success`` is cleaned up after each test

Release 0.9.1
-------------

- adding support for more test runners:

  * unittest2
  * django
  * twisted/trial
  * zope.testrunner
  * subunit
  * testtools

Release 0.9.0
-------------

- adding state machine support using ``when()``
- make expectation fail as soon as number of expected calls is exceeded
- ``flexmock_teardown`` no longer returns a function
- allow ``should_call`` on class and static methods
- disallow ``should_call`` on class mocks
- fixing ``unicode`` args handling
- fixing issues with ``@property`` methods misbehaving in the debugger
- fixing pytest integration and instance teardown
- fixing private method handling

Release 0.8.1
-------------

- fixing pytest and doctest integration to always call ``flexmock_teardown``
- fixing ``flexmock_teardown`` to return a function as before so it can be used as a decorator

Release 0.8.0
-------------

- big changes in runner integration support (no more stack examination or sketchy teardown replacement)
- doctest integration
- fixing ordering verification when the method has a default stub
- fixing calling ``with_args()`` without arguments to match exactly no arguments (thanks jerico-dev!)
- 20% performance improvement
- make sure to return object itself when partial mocking instances unless the object already has some of the methods
- ensure consecutive calls return same mock object

Release 0.7.4.2
---------------

- adding regex support for arg matching and spy return values
- enabling ``replace_with`` for class mocks
- disabling expectation checking if an exception has already been raised
- massive refactoring of the way flexmock does monkey patching

Release 0.7.4.1
---------------

- Fixing replace_with to work properly like ``and_execute``
- (``and_execute`` will be deprecated in next release!)

Release 0.7.4
-------------

- Fixed exception type check when no message specified
- Make properties work optionally with parentheses
- Make sure ``should_receive`` does not replace flexmock methods
- Removed ``new_instances=`` param in favor of ``new_instances()`` method
- Refactoring to move all state to ``FlexmockContainer`` class

Release 0.7.3
-------------

- Added ``new_instances`` method (``new_instances`` param will be deprecated in next release!)
- Added ``replace_with`` to enable returning results of custom functions
- Added ``with`` support for ``FlexMock`` objects
- Moved tests to their own directory
- Lots of documentation cleanup and updates

Release 0.7.2
-------------

- Added support for chained methods
- Moved ``flexmock_teardown`` to module level to expose it for other test runners
- Added py.test support (thanks to derdon)
- Lots of test refactoring and improvements for multiple test runner support
- Fix loop in teardown
- Fix ``should_call`` for same method with different args

Release 0.7.1
-------------

- Fix bug with "never" not working when the expectation is not met
- Fix bug in duplicate calls to original method in ``pass_thru`` mode (thanks sagara-!)
- Fix bug in handling unicode characters in ``ReturnValue``

Release 0.7.0
-------------

- Better error handling for trying to mock builtins
- Added simple test harness for running on multiple versions / test runners
- Fixed ``unicode`` arg formatting (thanks to sagara-!)
- Made it impossible to mock non-existent methods
- Ensure flexmock teardown takes varargs (for better runner integration)

Release 0.6.9
-------------

- Initial nose integration (still no support for generated tests)
- Fixing private class methods
- Some test refactoring to support different test runners

Release 0.6.8
-------------

- Add ``should_call()`` alias for ``should_receive().and_execute``
- Ensure ``new_instances`` can't be used with expectation modifiers
- Make ``and_execute`` match return value by class in addition to value
- Support for mocking out static methods
- Bit of test fixage (thanks to derdon)

Release 0.6.7
-------------

- Fixing clobbering of original method by multiple flexmock calls
- Making ``and_raise`` work properly with exception classes and args
- Proper exception matching with ``and_execute``
- Fix mocking same class twice

Release 0.6.6
-------------

- Removing extra args from ``should_receive``
- Making ``and_execute`` check return/raise value of original method
- Refactoring FlexMock constructor into factory method
- Fixing ``new_instances`` to accept multiple args instead of just none
- Raising an exception when ``and_execute`` is set on class mock

Release 0.6.5
-------------

- Adding support for multiple ``flexmock()`` calls on same object
- Adding error detection on ``and_execute`` for missing or unbound methods
- Make sure empty args don't include ``None``

Release 0.6.4
-------------

- Fixing up teardown cleanup code after an exception is raised in tests
- Fixing ``and_yield`` to return proper generator
- Adding ``and_yield`` returning a predefined generator
- Replacing ``and_passthru`` with ``and_execute``
- Make it easier to mock private methods

Release 0.6.3
-------------

- Adding keyword argument expectation matching

Release 0.6.2
-------------

- Changing ``and_return(multiple=True)`` to ``one_by_one``
- Making it possible to supply multiple args to ``and_return`` instead of a tuple
- Changing default mock behavior to create attributes instead of methods
- FIX teardown for python3

Release 0.6.1
-------------

- Make it even easier to integrate with new test runners
- Adding support for mixing returns and raises in return values

Release 0.6
-----------

- Adding support for multiple arg type matches
- Pulling out the entry point code from constructor into its own method.

Release 0.5
-----------

- FIX: ensuring that mocks are cleaned up properly between tests
- BROKEN: part1 on ensuring mocking multiple objects works correctly
- Make sure ``pass_thru`` doesn't try to call a non-existent method
- Fixing up copyright notice
- Adding some missing pydocs

Release 0.4
-----------

- Fixing tests and ensuring mock methods really get created properly
- Making sure shortcuts create methods rather than attributes
- Fixing doc strings
- Removing the new-style/old-style convert code, it's stupid

Release 0.3
-----------

- Making ``Expectation.mock`` into a property so that it shows up in pydoc
- Adding proxying/spying and ``at_least``/``at_most`` expectation modifiers
