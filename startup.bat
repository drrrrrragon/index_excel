@echo off
set /p root=�������ļ���·����
if %root% EQU NULL exit
set /p option=�Ƿ�������ļ��У���d/D/n��
if %option% EQU n (
	python-3.7.4-embed-amd64\python.exe python-3.7.4-embed-amd64\project\index.py %root%
) else (
	python-3.7.4-embed-amd64\python.exe python-3.7.4-embed-amd64\project\index.py -%option% %root%
)
pause