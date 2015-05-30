# -*- coding: utf-8 -*-
import gzip
import io
import os
from subprocess import Popen, PIPE


class 程式腳本:
	def _執行檔路徑加尾(self, 執行檔路徑):
		if 執行檔路徑 != '' and not 執行檔路徑.endswith('/'):
			return 執行檔路徑 + '/'
		return 執行檔路徑
	def _走指令(self, 指令):
		程序 = Popen([指令], stdout=PIPE, stderr=PIPE, shell=True)
		輸出資訊, 錯誤輸出資訊 = 程序.communicate()
		回傳值 = 程序.poll()
		if 回傳值 != 0:
			raise RuntimeError(
					'指令走到一半發生問題！！指令：{0}\n輸出：{1}\n錯誤資訊：{2}\n'
						.format(指令, 輸出資訊.decode('utf-8'), 錯誤輸出資訊.decode('utf-8'))
				)
	def _細項目錄(self, 資料目錄, 細項名):
		細項目錄 = os.path.join(資料目錄, 細項名)
		os.makedirs(細項目錄, exist_ok=True)
		return 細項目錄
	def _陣列寫入檔案(self, 檔名, 陣列):
		self._字串寫入檔案(檔名, '\n'.join(陣列))
	def _字串寫入檔案(self, 檔名, 字串):
		開檔 = self._開檔函式(檔名)
		檔案 = 開檔(檔名, mode='wt', encoding='utf-8')
		print(字串, file=檔案)
		檔案.close()
	def _讀檔案(self, 檔名):
		開檔 = self._開檔函式(檔名)
		檔案 = 開檔(檔名, mode='rt', encoding='utf-8')
		資料 = []
		for 一逝 in 檔案:
			一逝 = 一逝.rstrip()
			if 一逝 != '':
				資料.append(一逝)
		檔案.close()
		return 資料
	def _檔案合做一个(self, 上尾平行語料檔名, 全部平行語料檔名陣列, 編碼器):
		with open(上尾平行語料檔名, 'w') as 寫檔:
			for 平行語料檔名 in 全部平行語料檔名陣列:
				for 一逝 in self._讀檔案(平行語料檔名):
					print(編碼器.編碼(一逝.strip()), file=寫檔)
	def _開檔函式(self, 檔名):
		if 檔名.endswith('gz'):
			return gzip.open
		else:
			return io.open
