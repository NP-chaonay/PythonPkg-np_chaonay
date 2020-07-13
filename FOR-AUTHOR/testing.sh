# Author script for testing package by temporary substituting installed production-ready package
if [ `basename \`pwd\`` == "FOR-AUTHOR" ]; then
	echo "[ERROR] 'cd ..' before running this"
else
	mv ~/.local/lib/python3.8/site-packages/np_chaonay ~/.local/lib/python3.8/site-packages/np_chaonay_orig~
	ln -s ~/Projects/Applications/Python/Packages/np_chaonay_beta/np_chaonay ~/.local/lib/python3.8/site-packages/np_chaonay
	echo "Press enter to restore the original package..."
	read -s
	rm ~/.local/lib/python3.8/site-packages/np_chaonay
	mv ~/.local/lib/python3.8/site-packages/np_chaonay_orig~ ~/.local/lib/python3.8/site-packages/np_chaonay
fi
