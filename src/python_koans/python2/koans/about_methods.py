#!/usr/bin/env python
# -*- coding: utf-8 -*-

#
# Partially based on AboutMethods in the Ruby Koans
#

from runner.koan import *


def my_global_function(a, b):
    return a + b


class AboutMethods(Koan):
    def test_calling_a_global_function(self):
        self.assertEqual(__, my_global_function(2, 3))

    # NOTE: Wrong number of arguments is not a SYNTAX error, but a
    # runtime error.
    def test_calling_functions_with_wrong_number_of_arguments(self):
        try:
            my_global_function()
        except Exception as exception:
            # NOTE: The .__name__ attribute will convert the class
            # into a string value.
            self.assertEqual(__, exception.__class__.__name__)
            self.assertMatch(
                r'my_global_function\(\) takes exactly 2 arguments \(0 given\)',
                exception[0])

        try:
            my_global_function(1, 2, 3)
        except Exception as e:

            # Note, watch out for parenthesis. They need slashes in front!
            self.assertMatch(__, e[0])

    # ------------------------------------------------------------------

    def pointless_method(self, a, b):
        sum = a + b

    def test_which_does_not_return_anything(self):
        self.assertEqual(__, self.pointless_method(1, 2))
        # Notice that methods accessed from class scope do not require
        # you to pass the first "self" argument?

    # ------------------------------------------------------------------


