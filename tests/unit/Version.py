# EMACS settings: -*-  tab-width: 2; indent-tabs-mode: t -*-
# vim: tabstop=2:shiftwidth=2:noexpandtab
# kate: tab-width 2; replace-tabs off; indent-width 2;
# =============================================================================
#                ____                                       ____ _
#   _ __  _   _ / ___|___  _ __ ___  _ __ ___   ___  _ __  / ___| | __ _ ___ ___  ___  ___
#  | '_ \| | | | |   / _ \| '_ ` _ \| '_ ` _ \ / _ \| '_ \| |   | |/ _` / __/ __|/ _ \/ __|
#  | |_) | |_| | |__| (_) | | | | | | | | | | | (_) | | | | |___| | (_| \__ \__ \  __/\__ \
#  | .__/ \__, |\____\___/|_| |_| |_|_| |_| |_|\___/|_| |_|\____|_|\__,_|___/___/\___||___/
#  |_|    |___/
# =============================================================================
# Authors:            Patrick Lehmann
#
# Python unittest:    Testing the Version module
#
# Description:
# ------------------------------------
#		TODO
#
# License:
# ============================================================================
# Copyright 2020-2020 Patrick Lehmann - Bötzingen, Germany
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
# SPDX-License-Identifier: Apache-2.0
# ============================================================================
#
"""
pyAttributes
############

:copyright: Copyright 2020-2020 Patrick Lehmann - Bötzingen, Germany
:license: Apache License, Version 2.0
"""
from unittest     import TestCase

from pyCommonClasses.Version import Version as UUT


if __name__ == "__main__":
	print("ERROR: you called a testcase declaration file as an executable module.")
	print("Use: 'python -m unitest <testcase module>'")
	exit(1)


class Version(TestCase):
	version : UUT

	# def test_CreateFromNone(self):
	# 	with self.assertRaises(ValueError):
	# 		version = Version(versionString=None)

	def test_CreateFromEmptyString(self):
		with self.assertRaises(ValueError):
			Version("")

	def test_CreateFromSomeString(self):
		with self.assertRaises(ValueError):
			Version("None")

	def test_CreateFromString1(self):
		version = UUT("0.0.0")

		self.assertEqual(version.major, 0, "Major number is not 0.")
		self.assertEqual(version.minor, 0, "Minor number is not 0.")
		self.assertEqual(version.patch, 0, "Patch number is not 0.")
		self.assertEqual(version.build, 0, "Build number is not 0.")

	def test_CreateFromIntegers1(self):
		version = UUT(0, 0, 0)

		self.assertEqual(version.major, 0, "Major number is not 0.")
		self.assertEqual(version.minor, 0, "Minor number is not 0.")
		self.assertEqual(version.patch, 0, "Patch number is not 0.")
		self.assertEqual(version.build, 0, "Build number is not 0.")

	def test_CreateFromIntegers2(self):
		version = UUT(1, 2, 3, 4)

		self.assertEqual(version.major, 1, "Major number is not 1.")
		self.assertEqual(version.minor, 2, "Minor number is not 2.")
		self.assertEqual(version.patch, 3, "Patch number is not 3.")
		self.assertEqual(version.build, 4, "Build number is not 4.")
