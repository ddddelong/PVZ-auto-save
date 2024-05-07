#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# config.py

class Config:
	def __init__(self):
		# 游戏存档将复制到该文件夹下
		self.index = '04'
		self.target_folder = fr'C:\ProgramData\PopCap Games\{self.index}'
		# 保存副本文件夹下文件夹数量最大值，超过则删除最早存档的文件夹
		self.max_folder_count = 14
		# 游戏原存档文件夹所在路径，即要复制的文件夹
		self.source_folder = r'C:\ProgramData\PopCap Games\PlantsVsZombies'
