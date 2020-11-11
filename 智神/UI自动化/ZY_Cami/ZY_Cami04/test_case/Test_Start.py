# -*- coding: utf-8 -*-
__author__ = 'JennyHui'

import unittest
from PO import CameraPage


class Search(unittest.TestCase):

    def setUp(self):
        recipe_list = [u'苦瓜', u'黄瓜']
        self.recipe = recipe_list[-1]

    def test_Search(self):
        u'''测试好豆菜谱搜索框功能'''
        CameraPage.click_camera_loc(self.recipe)

    def tearDown(self):
        pass


if __name__ == '__main__':
    unittest.main()
