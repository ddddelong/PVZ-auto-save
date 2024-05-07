# !/usr/bin/env python
# -*- encoding: utf-8 -*-
# saveGame.py
import os
import shutil
import config

Config = config.Config()
# 保存副本文件夹下文件夹数量最大值，超过则删除最早存档的文件夹
MAX_FOLDER_COUNT = Config.max_folder_count
# 将游戏存档复制到该文件夹下
TARGET_FOLDER = Config.target_folder
# 游戏存档文件夹所在路径（游戏本身存档所在），即要复制的文件夹
SOURCE_FOLDER = Config.source_folder


# 判断是否存在目标文件夹，不存在则创建
def createFolderIfNotExist(folder):
	"""
	param folder: 要检查的文件夹路径
	判断文件夹是否存在，不存在则创建
	"""
	if not os.path.exists(folder):
		os.makedirs(folder)


def checkFolderCount(folder):
	"""
	param folder: 要检查的文件夹路径
	检查文件夹下文件夹的数量，若超过指定数量MAX_FOLDER_COUNT，则删除最早的文件夹
	"""
	folders = os.listdir(folder)
	if len(folders) >= MAX_FOLDER_COUNT:
		folders.sort()
		# 使用内置函数删除文件夹
		shutil.rmtree(os.path.join(folder, folders[0]))
		print(f'由于文件夹数量超过{MAX_FOLDER_COUNT}，所以删除了最早的文件夹{os.path.join(folder, folders[0])}！')


def getLatestFolders(folder):
	"""
	param folder: 要检查的文件夹路径
	获取文件夹下最新的文件夹名称
	"""
	folders = os.listdir(folder)
	# 判断是否为文件夹
	if len(folders) == 0:
		return 0
	folders.sort(reverse=True)
	# print(folders[0])
	return int(folders[0])


def copyFolder(target_folder, destination):
	"""
	param target_folder: 要复制的文件夹路径
	param destination: 目标文件夹路径
	将target_folder复制到destination
	"""
	# 使用内置函数复制文件夹
	shutil.copytree(target_folder, destination)
	print(f'成功将 {target_folder} 复制到 {destination}  ！！！！')


def copyGameSave():
	"""
	复制游戏存档，即将SOURCE_FOLDER复制到TARGET_FOLDER
	存档文件夹名称为最新文件夹名称+1
	而且TARGET_FOLDER下文件夹数量不能超过MAX_FOLDER_COUNT，超过则删除最早的文件夹
	"""

	# 判断是否存在目标文件夹，不存在则创建
	createFolderIfNotExist(TARGET_FOLDER)

	# 检查文件夹下文件夹的数量，若超过指定数量MAX_FOLDER_COUNT，则删除最早的文件夹
	checkFolderCount(TARGET_FOLDER)

	# 根据最新文件夹名称创建新文件夹，即把最新的文件夹名称+1并格式化为两位数
	newFolderName = os.path.join(TARGET_FOLDER, f'{getLatestFolders(TARGET_FOLDER) + 1:0>2}')

	# 复制游戏存档
	copyFolder(target_folder=SOURCE_FOLDER, destination=newFolderName)


# 询问是否要修改存档保存文件夹路径
def changeGameSavePath():
	"""
	修改游戏存档保存路径
	return: 新的存档保存路径
	"""
	global TARGET_FOLDER
	INDEX = input('请输入新的存档保存路径序号：')
	TARGET_FOLDER = fr'C:\ProgramData\PopCap Games\{INDEX}'
	print(f'新的存档保存路径为：{TARGET_FOLDER}')


if __name__ == '__main__':
	flag = input(f'是否要复制游戏存档到{TARGET_FOLDER}？(y/n)\n请按回车或者输入y继续，输入n可以修改存档保存路径，输入其他字符结束程序。')
	if flag.lower() == 'y' or flag.lower() == '':
		print('开始复制游戏存档...')
		copyGameSave()
		print('程序结束...')
	elif flag.lower() == 'n':
		changeGameSavePath()
		copyGameSave()
		print('程序结束...')
	else:
		print('程序结束...')
