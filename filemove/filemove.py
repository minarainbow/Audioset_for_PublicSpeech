# -*- coding: utf-8 -*-
import os
import shutil

def filemove(filename, dst):
						
	# �� �����Ҽ� ������ ������ �������� �ִ��� �˻�.
	# ���ϸ� ����
	tmp_file = os.path.basename(filename)
	tmp_file = dst + '/' + tmp_file
		
	# ������ �ֳ� ?
	if os.path.exists(tmp_file) :
		# �����ϸ� ���� ����
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

	# ���ϸ�Ͽ��� ����1�� ������
	for filename in filelist:
		bExit = False
		
		# �������ڿ� �Ѱ��� ������
		for str in strlist:
			
			str = str.strip()
			
			if len(str) == 0 :
				continue
				
			lst_str = str.split(',')
			
			# �ι�° �׸��� ���� �̵��� ��ΰ� ������
			if len(lst_str) > 1 :
				# ���ڿ� ��
				if filename.find (lst_str[0]) > -1: 
					foldername = lst_str[1]
					try : 
						# ���� ������ ����.
						if not os.path.isdir(foldername) :
							os.mkdir(foldername) 
					except :
						break
						
					filemove (filename, lst_str[1])
					bExit = True
					break

				continue
				

				
			# �������ڿ��� ���Ե� �����ΰ� ?
			if filename.find (str) > -1: 
				#print filename
		
				# ������Ͽ��� �ش� ���ڿ��� ã�Ƽ� 
				for foldername in folderlist:
					#print foldername
					
					# ������ ��ġ��. �̵� �غ�
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
						
				
				
# filemove_str.txt �� ����� 
# �з��� �ܾ���� �����´�. (�޸��ɼ����� ��� ��������)
# ��1 ù��) ���ѵ���
# ��2 �ι�°��) 1��2��,/volume1/uploads/KBS_�������Դ�_1��2��

# ���� : ��1) �� �ش�ܾ ���Ե� ���ϸ��� �ܾ ���Ե� ���������� �̵�
#        ��2) �� �ش�ܾ ���Ե� ���ϸ��� �޸��� �����η� ���� �̵�

def get_strings():
	global strlist	
	with open('filemove_str.txt', 'r') as f:
		strlist = f.readlines()
	f.close()

	
get_strings()

search("/volume1/uploads")
