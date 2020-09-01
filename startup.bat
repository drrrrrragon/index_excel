@echo off
set /p root=请输入文件夹路径：
if %root% EQU NULL exit
set /p option=是否遍历子文件夹？（d/D/n）
if %option% EQU n (
	python-3.7.4-embed-amd64\python.exe python-3.7.4-embed-amd64\project\index.py %root%
) else (
	python-3.7.4-embed-amd64\python.exe python-3.7.4-embed-amd64\project\index.py -%option% %root%
)
pause