# !/usr/bin/env python
# -*- encoding: utf-8 -*-
# switchGameSave.py
import os
import shutil

import config
from saveGame import getLatestFolders

Config = config.Config()

# SOURCE_FOLDER = r'C:\ProgramData\PopCap Games\04'
# 游戏存档的副本文件夹路径
SOURCE_FOLDER = Config.target_folder
# 游戏存档将复制到该文件夹下，即游戏原存档文件夹所在路径
TARGET_FOLDER = Config.source_folder


def switchGameSave(source_folder, target_folder):
	"""
	param source_folder: 源文件夹路径
	param target_folder: 目标文件夹路径
	将source_folder下的所有文件夹复制到target_folder
	"""

	folders = os.listdir(source_folder)
	for folder in folders:
		src = os.path.join(source_folder, folder)
		dst = os.path.join(target_folder, folder)
		shutil.copytree(src=src, dst=dst, dirs_exist_ok=True)
		print(f'成功将\n{src}\n复制到\n{dst}\n')


if __name__ == '__main__':
	# 获取保存副本存档最新的文件夹，即最新的存档
	latest_folder = getLatestFolders(SOURCE_FOLDER)
	SOURCE_FOLDER = os.path.join(SOURCE_FOLDER, "{:02}".format(latest_folder))
	# 询问是否继续
	flag = input(
		'本程序将会将游戏存档从\n{}（你指定的最新的存档文件夹）\n复制到\n{}（游戏原存档文件夹所在路径），\n是否继续(y/n)？\n请按回车或者输入y继续，输入其他字符结束程序。'.format(
			SOURCE_FOLDER, TARGET_FOLDER))
	if flag.lower() == 'y' or flag == '':
		print('程序开始运行...')
		switchGameSave(source_folder=SOURCE_FOLDER, target_folder=TARGET_FOLDER)
	else:
		print('程序结束！！！')
		exit()
