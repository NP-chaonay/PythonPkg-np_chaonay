# Author script for uploading package (Do not run this script 
if [ `basename \`pwd\`` != "np_chaonay_dev" ]; then
	echo "[ERROR] Change directory to root, or check the root directory name to 'np_chaonay_dev'"
else
	rm dist/*
	python3 setup.py sdist bdist_wheel
	python3 -m twine upload dist/*
fi
