import time

class Throttle:

    '''
    The purpose of the throttle is to limit the number of queries you can make in a given
    period of time (e.g. 120 per 60 seconds).

    The two classes that

    The throttle has four key variables:

        1 - time_last_window_opened (managed internally).
        2 - window_duration (a constant fixed when you set it up).
        3 - the max_requests you can make within a window of time.
        3 - the number of requests_so_far made in the current window (incremented with each request).

    There are two key methods:

        1 - Start - used to get it running in the first place by setting time_last_window_opened
        to the current time.
        2 - Check - used to check if it's safe to make a request i.e. the number of requests is
        below the maximum number for the window. If this number isn't reached before the window closes,
        then both the time_last_window_opened and the requests_so_far are reset.

        Check returns the time in seconds the calling class will have to wait until it's safe to
        make the next request (so this variable can be applied to time.sleep() to stall the requester).
        It does this using:

            (time_last_window_opened + window_duration) - current_time

    When the throttle returns a positive value (i.e. it tells the caller to wait), it also needs to
    reset the start time by adding the window duration to the current start time.

    '''

    def __init__(self, window_duration: int, max_requests: int):

        self.__time_last_window_opened = None
        self.__window_duration = window_duration
        self.__max_requests = max_requests
        self.__requests_so_far = 0

    def start(self):

        self.__time_last_window_opened = time.time()

    def check(self):

        '''
        Checks to see:
            If we're still in the same window.
                If not, open a new one and return 0 seconds to wait...
            If the maximum number of requests has been reached in this window:
                If so -
                 open a new window and return the time remaining in the previous window
                If not -
                 return zero seconds to wait
        :return: The time to wait before you can send another request
        '''

        if time.time() > self.__time_last_window_opened + self.__window_duration:

            #The window is open again

            self.__time_last_window_opened = time.time()
            self.__requests_so_far = 0

            return 0

        self.__requests_so_far += 1

        if self.__requests_so_far > self.__max_requests:

            # Max requests reached within the window so return the time remaining
            # until the window closes

            time_until_window_reopens = (self.__time_last_window_opened + self.__window_duration) - time.time()
            self.__time_last_window_opened = time.time() + time_until_window_reopens
            self.__requests_so_far = 0

            return time_until_window_reopens

        else:

            return 0
