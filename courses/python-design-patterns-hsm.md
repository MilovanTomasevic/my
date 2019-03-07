---
layout: page
title: Python-Design-Patterns hsm
description: >
  Python Design Patterns Tutorial for beginners - Learn Python Design Patterns in simple and easy steps starting from basic to advanced concepts with examples ...
hide_description: true

---

## Table of Contents
{:.no_toc}
0. this unordered seed list will be replaced by toc as unordered list
{:toc}

---

## hsm Model

![](/courses/python-fesign-patterns/other/hsm/classes_hsm.png)
Classes
{:.figure}

![](/courses/python-fesign-patterns/other/hsm/classes_test_hsm.png)
Test
{:.figure}

## Python-Design-Patterns hsm

```py
"""
Implementation of the HSM (hierarchical state machine) or
NFSM (nested finite state machine) C++ example from
http://www.eventhelix.com/RealtimeMantra/HierarchicalStateMachine.htm#.VwqLVEL950w
in Python

- single source 'message type' for state transition changes
- message type considered, messages (comment) not considered to avoid complexity
"""

class UnsupportedMessageType(BaseException):
    pass

class UnsupportedState(BaseException):
    pass

class UnsupportedTransition(BaseException):
    pass

class HierachicalStateMachine(object):
    def __init__(self):
        self._active_state = Active(self)  # Unit.Inservice.Active()
        self._standby_state = Standby(self)  # Unit.Inservice.Standby()
        self._suspect_state = Suspect(self)  # Unit.OutOfService.Suspect()
        self._failed_state = Failed(self)  # Unit.OutOfService.Failed()
        self._current_state = self._standby_state
        self.states = {
            'active': self._active_state,
            'standby': self._standby_state,
            'suspect': self._suspect_state,
            'failed': self._failed_state,
        }
        self.message_types = {
            'fault trigger': self._current_state.on_fault_trigger,
            'switchover': self._current_state.on_switchover,
            'diagnostics passed': self._current_state.on_diagnostics_passed,
            'diagnostics failed': self._current_state.on_diagnostics_failed,
            'operator inservice': self._current_state.on_operator_inservice,
        }

    def _next_state(self, state):
        try:
            self._current_state = self.states[state]
        except KeyError:
            raise UnsupportedState

    def _send_diagnostics_request(self):
        return 'send diagnostic request'

    def _raise_alarm(self):
        return 'raise alarm'

    def _clear_alarm(self):
        return 'clear alarm'

    def _perform_switchover(self):
        return 'perform switchover'

    def _send_switchover_response(self):
        return 'send switchover response'

    def _send_operator_inservice_response(self):
        return 'send operator inservice response'

    def _send_diagnostics_failure_report(self):
        return 'send diagnostics failure report'

    def _send_diagnostics_pass_report(self):
        return 'send diagnostics pass report'

    def _abort_diagnostics(self):
        return 'abort diagnostics'

    def _check_mate_status(self):
        return 'check mate status'

    def on_message(self, message_type):  # message ignored
        if message_type in self.message_types.keys():
            self.message_types[message_type]()
        else:
            raise UnsupportedMessageType

class Unit(object):
    def __init__(self, HierachicalStateMachine):
        self.hsm = HierachicalStateMachine

    def on_switchover(self):
        raise UnsupportedTransition

    def on_fault_trigger(self):
        raise UnsupportedTransition

    def on_diagnostics_failed(self):
        raise UnsupportedTransition

    def on_diagnostics_passed(self):
        raise UnsupportedTransition

    def on_operator_inservice(self):
        raise UnsupportedTransition

class Inservice(Unit):
    def __init__(self, HierachicalStateMachine):
        self._hsm = HierachicalStateMachine

    def on_fault_trigger(self):
        self._hsm._next_state('suspect')
        self._hsm._send_diagnostics_request()
        self._hsm._raise_alarm()

    def on_switchover(self):
        self._hsm._perform_switchover()
        self._hsm._check_mate_status()
        self._hsm._send_switchover_response()

class Active(Inservice):
    def __init__(self, HierachicalStateMachine):
        self._hsm = HierachicalStateMachine

    def on_fault_trigger(self):
        super(Active, self).perform_switchover()
        super(Active, self).on_fault_trigger()

    def on_switchover(self):
        self._hsm.on_switchover()  # message ignored
        self._hsm.next_state('standby')

class Standby(Inservice):
    def __init__(self, HierachicalStateMachine):
        self._hsm = HierachicalStateMachine

    def on_switchover(self):
        super(Standby, self).on_switchover()  # message ignored
        self._hsm._next_state('active')

class OutOfService(Unit):
    def __init__(self, HierachicalStateMachine):
        self._hsm = HierachicalStateMachine

    def on_operator_inservice(self):
        self._hsm.on_switchover()  # message ignored
        self._hsm.send_operator_inservice_response()
        self._hsm.next_state('suspect')

class Suspect(OutOfService):
    def __init__(self, HierachicalStateMachine):
        self._hsm = HierachicalStateMachine

    def on_diagnostics_failed(self):
        super(Suspect, self).send_diagnostics_failure_report()
        super(Suspect, self).next_state('failed')

    def on_diagnostics_passed(self):
        super(Suspect, self).send_diagnostics_pass_report()
        super(Suspect, self).clear_alarm()  # loss of redundancy alarm
        super(Suspect, self).next_state('standby')

    def on_operator_inservice(self):
        super(Suspect, self).abort_diagnostics()
        super(Suspect, self).on_operator_inservice()  # message ignored

class Failed(OutOfService):
    """No need to override any method."""

    def __init__(self, HierachicalStateMachine):
        self._hsm = HierachicalStateMachine
```
hsm.py
{:.figure}

## hsm Test

```py
#!/usr/bin/env python
# -*- coding: utf-8 -*-
import unittest
from other.hsm.hsm import (
    HierachicalStateMachine,
    UnsupportedMessageType,
    UnsupportedState,
    UnsupportedTransition,
    Active,
    Standby,
    Suspect,
)

try:
    from unittest.mock import patch
except ImportError:
    from mock import patch

class HsmMethodTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.hsm = HierachicalStateMachine()

    def test_initial_state_shall_be_standby(cls):
        cls.assertEqual(isinstance(cls.hsm._current_state, Standby), True)

    def test_unsupported_state_shall_raise_exception(cls):
        with cls.assertRaises(UnsupportedState):
            cls.hsm._next_state('missing')

    def test_unsupported_message_type_shall_raise_exception(cls):
        with cls.assertRaises(UnsupportedMessageType):
            cls.hsm.on_message('trigger')

    def test_calling_next_state_shall_change_current_state(cls):
        cls.hsm._current_state = Standby  # initial state
        cls.hsm._next_state('active')
        cls.assertEqual(isinstance(cls.hsm._current_state, Active), True)
        cls.hsm._current_state = Standby(cls.hsm)  # initial state

    def test_method_perform_switchover_shall_return_specifically(cls):
        """ Exemplary HierachicalStateMachine method test.
        (here: _perform_switchover()). Add additional test cases... """
        return_value = cls.hsm._perform_switchover()
        expected_return_value = 'perform switchover'
        cls.assertEqual(return_value, expected_return_value)

class StandbyStateTest(unittest.TestCase):
    """ Exemplary 2nd level state test class (here: Standby state). Add missing
    state test classes... """

    @classmethod
    def setUpClass(cls):
        cls.hsm = HierachicalStateMachine()

    def setUp(cls):
        cls.hsm._current_state = Standby(cls.hsm)

    def test_given_standby_on_message_switchover_shall_set_active(cls):
        cls.hsm.on_message('switchover')
        cls.assertEqual(isinstance(cls.hsm._current_state, Active), True)

    def test_given_standby_on_message_switchover_shall_call_hsm_methods(cls):
        with patch.object(cls.hsm, '_perform_switchover') as mock_perform_switchover, patch.object(
            cls.hsm, '_check_mate_status'
        ) as mock_check_mate_status, patch.object(
            cls.hsm, '_send_switchover_response'
        ) as mock_send_switchover_response, patch.object(
            cls.hsm, '_next_state'
        ) as mock_next_state:
            cls.hsm.on_message('switchover')
            cls.assertEqual(mock_perform_switchover.call_count, 1)
            cls.assertEqual(mock_check_mate_status.call_count, 1)
            cls.assertEqual(mock_send_switchover_response.call_count, 1)
            cls.assertEqual(mock_next_state.call_count, 1)

    def test_given_standby_on_message_fault_trigger_shall_set_suspect(cls):
        cls.hsm.on_message('fault trigger')
        cls.assertEqual(isinstance(cls.hsm._current_state, Suspect), True)

    def test_given_standby_on_message_diagnostics_failed_shall_raise_exception_and_keep_in_state(cls):
        with cls.assertRaises(UnsupportedTransition):
            cls.hsm.on_message('diagnostics failed')
        cls.assertEqual(isinstance(cls.hsm._current_state, Standby), True)

    def test_given_standby_on_message_diagnostics_passed_shall_raise_exception_and_keep_in_state(cls):
        with cls.assertRaises(UnsupportedTransition):
            cls.hsm.on_message('diagnostics passed')
        cls.assertEqual(isinstance(cls.hsm._current_state, Standby), True)

    def test_given_standby_on_message_operator_inservice_shall_raise_exception_and_keep_in_state(cls):
        with cls.assertRaises(UnsupportedTransition):
            cls.hsm.on_message('operator inservice')
        cls.assertEqual(isinstance(cls.hsm._current_state, Standby), True)
```
test_hsm.py
{:.figure}
