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
# Python package:     A common version class
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
from dataclasses   import dataclass

from flags         import Flags
from pyMetaClasses import Overloading


@dataclass
class Version(metaclass=Overloading):
	class Parts(Flags):
		Major = 1
		Minor = 2
		Patch = 4
		Build = 8
		Pre   = 16
		Post  = 32
		Prefix = 64
		Postfix = 128
		AHead   = 256

	class Flags(Flags):
		Clean = 1
		Dirty = 2

	parts   : Parts
	flags   : int
	major   : int
	minor   : int
	patch   : int
	build   : int
	pre     : int
	post    : int
	prefix  : str
	postfix : str
	ahead   : int

	def __init__(self, versionString : str):
		if versionString.startswith(("V", "v", "I", "i", "R", "r")):
			versionString = versionString[1:]
		elif versionString.startswith(("rev", "REV")):
			versionString = versionString[3:]

		split = versionString.split(".")
		self.major = int(split[0])
		self.minor = int(split[1])
		self.patch = int(split[2])
		self.flags = self.Flags.Clean

	def __init__(self, major : int, minor : int, patch : int = 0, build : int = 0):
		self.major = major
		self.minor = minor
		self.patch = patch
		self.build = build
		self.flags = self.Flags.Clean

	def __str__(self):
		return "v{0}.{1}.{2}".format(self.major, self.minor, self.patch)

	def __repr__(self):
		return "{0}.{1}.{2}".format(self.major, self.minor, self.patch)
