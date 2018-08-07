from dimensions_client.throttle import Throttle

import pytest
import time

class TestThrottle:

    def setup_method(self):

        '''
            Setup a test throttle with a window_duration of two seconds
            and a max_requests of 10 per window.
        '''

        self.__test_throttle = Throttle(2, 10)

    def tear_down_method(self):

        self.__test_throttle = None

    def test_11_checks_cause_a_sleep_of_nearly_two_seconds_to_be_returned(self):

        self.__test_throttle.start()

        result = 0

        for i in range(11):

            result = self.__test_throttle.check()

        assert result == pytest.approx(2, 0.25)

    def test_not_enough_requests_made_to_hit_the_limit(self):

        self.__test_throttle.start()

        result = 0

        for i in range(3):

            result = self.__test_throttle.check()

        assert result == 0

    def test_throttle_resets_when_two_runs_are_made_with_an_interval_between(self):

        self.__test_throttle.start()

        result = 0

        for i in range(11):

            result = self.__test_throttle.check()

        time.sleep(result)

        for i in range(11):

            result = self.__test_throttle.check()

        assert result == pytest.approx(2, 0.25)

    def test_throttle_resets_across_a_slow_set_of_calls(self):

        self.__test_throttle.start()

        result = 0

        for i in range(16):

            if i == 8:
                time.sleep(2)

            result = self.__test_throttle.check()

        assert result == 0
