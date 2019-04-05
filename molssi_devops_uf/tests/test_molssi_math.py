"""
Tests  for molssi_math moduel
"""

import molssi_devops_uf as md_uf

def test_mean():
	num_list = [1, 2, 3, 4, 5,]
	observed = md_uf.mean(num_list)
	expected = 3

	assert observed ==expected
