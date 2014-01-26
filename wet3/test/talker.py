#!/usr/bin/env python
PKG='wet3'
import roslib; roslib.load_manifest(PKG)

import sys
import os
import unittest

class TestSample(unittest.TestCase):

	def test_sample(self):
		# nothing to report
		pass
 
if __name__ == '__main__':
	import rosunit
	rosunit.unitrun(PKG, 'test_urdf', TestSample) 
