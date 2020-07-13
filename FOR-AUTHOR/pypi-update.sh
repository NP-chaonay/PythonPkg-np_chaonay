# Author script for uploading package (Do not run this script 
if [ `basename \`pwd\`` == "FOR-AUTHOR" ]; then
	echo "[ERROR] 'cd ..' before running this"
else
	rm dist/*
	python3 setup.py sdist bdist_wheel
	python3 -m twine upload dist/*
fi
