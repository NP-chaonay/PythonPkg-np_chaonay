# Author script for uploading package (Do not run this script 
if [ `basename \`pwd\`` != "PythonPkg-np_chaonay" ]; then
	echo "[ERROR] Change directory to root, or check the root directory name to 'PythonPkg-np_chaonay'"
else
	rm dist/*
	python3 setup.py sdist bdist_wheel
	python3 -m twine upload dist/*
fi
