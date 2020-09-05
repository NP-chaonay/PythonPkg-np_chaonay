# Author script for testing package by temporary substituting installed production-ready package
if [ `basename \`pwd\`` == "PythonPkg-np_chaonay" ]; then
	echo "[ERROR] Change directory to root, or check the root directory name to 'PythonPkg-np_chaonay'"
else
	mv ~/.local/lib/python3.8/site-packages/np_chaonay ~/.local/lib/python3.8/site-packages/np_chaonay_orig~
	ln -s ./np_chaonay ~/.local/lib/python3.8/site-packages/np_chaonay
fi
