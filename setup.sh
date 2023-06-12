#!/bin/bash

echo "Library published by HexTran"

if ! command -v python &> /dev/null ; then
    echo "Python is not installed"
    exit 1
fi

# pip upgrade
python -m pip install --upgrade pip
# install pygetwindow
echo "Installing pygetwindow"
pip install pygetwindow
# install pyautogui
echo "Installing pyautogui"
pip install pyautogui
# install opencv-python
echo "Installing opencv-python"
pip install opencv-python

# end
echo "Setup completed"
echo "Thanks for using hexTran's products"
read -p "Press any key to continue..." var
