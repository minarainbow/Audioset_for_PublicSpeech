# -*- coding: utf-8 -*-
import os
import shutil

def filemove(filename, dst):
						
	# 기 존재할수 있으니 폴더에 같은파일 있는지 검사.
	# 파일명만 추출
	tmp_file = os.path.basename(filename)
	tmp_file = dst + '/' + tmp_file
		
	# 파일이 있나 ?
	if os.path.exists(tmp_file) :
		# 존재하면 파일 삭제
		os.remove(filename)
		print "[FileDelete] " + filename
	else :
		shutil.move(filename, dst)
		print "[FileMove] " +  filename + " ==> " + dst


def search(dirname):
	try:
		folderlist = []
		filelist = []
		
		filenames = os.listdir(dirname)
		for filename in filenames:
			full_filename = os.path.join(dirname, filename)
			if os.path.isdir(full_filename):
				folderlist.append (full_filename)
				# search(full_filename)
				continue
			else :
				filelist.append(full_filename)
				# print(full_filename)
			
	except PermissionError:
		pass

	# 파일목록에서 파일1개 꺼내서
	for filename in filelist:
		bExit = False
		
		# 지정문자열 한개를 꺼내서
		for str in strlist:
			
			str = str.strip()
			
			if len(str) == 0 :
				continue
				
			lst_str = str.split(',')
			
			# 두번째 항목이 존재 이동할 경로가 지정됨
			if len(lst_str) > 1 :
				# 문자열 비교
				if filename.find (lst_str[0]) > -1: 
					foldername = lst_str[1]
					try : 
						# 폴더 없으면 생성.
						if not os.path.isdir(foldername) :
							os.mkdir(foldername) 
					except :
						break
						
					filemove (filename, lst_str[1])
					bExit = True
					break

				continue
				

				
			# 지정문자열이 포함된 파일인가 ?
			if filename.find (str) > -1: 
				#print filename
		
				# 폴더목록에서 해당 문자열을 찾아서 
				for foldername in folderlist:
					#print foldername
					
					# 폴더명 매치됨. 이동 준비
					if foldername.find (str) > -1: 	
						try : 
							filemove (filename, foldername)
							bExit = True
							break
						except :
							print "[FileMove] Error !! " +  filename + " ==> " + foldername
							continue
			
			if bExit :
				break;
						
				
				
# filemove_str.txt 에 저장된 
# 분류할 단어들을 가져온다. (콤마옵션으로 경로 지정가능)
# 예1 첫줄) 무한도전
# 예2 두번째줄) 1박2일,/volume1/uploads/KBS_해피투게더_1박2일

# 설명 : 예1) 은 해당단어가 포함된 파일명을 단어가 포함된 하위폴더로 이동
#        예2) 는 해당단어가 포함된 파일명을 콤마뒤 절대경로로 파일 이동

def get_strings():
	global strlist	
	with open('filemove_str.txt', 'r') as f:
		strlist = f.readlines()
	f.close()

	
get_strings()

search("/volume1/uploads")
