#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/9/3 6:58
# @Author  : ganliang
# @File    : setup.py
# @Desc    : 安装脚本
# from distutils.core import setup

from setuptools import setup, find_packages

"""
编译 python setup.py build
安装 python setup.py install
打包（源代码发布） python setup.py sdist
打包成可执行（exe、rpm） python setup.py bdist
  --formats=rpm      RPM distribution
  --formats=gztar    gzip'ed tar file
  --formats=bztar    bzip2'ed tar file
  --formats=ztar     compressed tar file
  --formats=tar      tar file
  --formats=wininst  Windows executable installer
  --formats=zip      ZIP file 
"""
setup(name="pcrawler",
      version="0.0.1",
      description="python版本的爬虫程序。根据java版本的webmagic改编而成。该爬虫程序主要包含downloader、storage、processor、schemular等四大功能模块。通过该爬虫程序可以快速的编写一个自定义的爬虫程序。",
      author="甘亮",
      author_email="lovercws@gmail.com",
      keywords="python版本的爬虫程序",
      # py_modules=["main"], #将一个模块打成包
      packages=find_packages(),
      include_package_data=True,
      platforms="any",
      install_requires=[],
      scripts=[],
      entry_points={
          'console_scripts': [
              'test = src.main:runner'
          ]
      }
      )