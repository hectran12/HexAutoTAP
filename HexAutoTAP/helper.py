import pygetwindow, pyautogui
import time
import os
import sys
import base64
import requests
import random
import pyperclip
import json
def random_string(length: int = 10) -> str:
    result = ""
    for i in range(length):
        result += chr(random.randint(65, 90))
    return result

def get_window_by_title(title):
    windows = pygetwindow.getAllWindows()
    result_window = []
    for window in windows:
        if title in window.title:
            result_window.append(window)
    return result_window


def Sort_windows(weight=100, height=100, list_windows: list = []) -> bool:

    if len(list_windows) == 0:
        return False
    for window in list_windows:
        window.activate()
    if len(list_windows) == 1:
        list_windows[0].resizeTo(weight, height)
        list_windows[0].moveTo(0, 0)
        return True
    
    list_windows.sort(key=lambda x: x.left)
    for i in range(len(list_windows)):
        list_windows[i].resizeTo(weight, height)
        list_windows[i].moveTo(i * weight, 0)
    return True


def close_window_by_title(title):
    windows = pygetwindow.getAllWindows()
    for window in windows:
        if title in window.title:
            window.close()


def find_element_and_tap(window: pygetwindow.BaseWindow, image_path: str, confidence: float = 0.9) -> None:
    for x in range(5):
        try:
            window.activate()
            
            left, top, width, height = window.left, window.top, window.width, window.height
            region = (left, top, width, height)
            icon = pyautogui.locateCenterOnScreen(image_path, confidence=confidence, region=region)
            # save screenshot
            screenshot = pyautogui.screenshot(region=region)
            screenshot.save("screenshot.png")
            if icon is None:
                return False
            else:
                pyautogui.moveTo(icon)
                pyautogui.mouseDown()
                pyautogui.mouseUp()

                return True
        except:
            time.sleep(0.5)
    return False

def write(window: pygetwindow.BaseWindow, text: str) -> bool:
    window.activate()
    for character in text:
        pyautogui.typewrite(character)
        time.sleep(0.1)
    return True

def find_element_and_write(window: pygetwindow.BaseWindow, image_path: str, text: str, confidence: float = 0.9) -> bool:
    for x in range(5):
        try:
            window.activate()
            
            left, top, width, height = window.left, window.top, window.width, window.height
            region = (left, top, width, height)
            icon = pyautogui.locateCenterOnScreen(image_path, confidence=confidence, region=region)
            
            if icon is None:
                return False
            else:
                pyautogui.moveTo(icon)
                pyautogui.mouseDown()
                pyautogui.mouseUp()
                time.sleep(1)
                for character in text:
                    pyautogui.typewrite(character)
                    time.sleep(0.1)
                return True
        except:
            time.sleep(0.5)

    return False


def getText(window: pygetwindow.BaseWindow) -> str:
    # Chức năng này cần có tiền để có thể sử dụng
    pass

def waitForElement (window: pygetwindow.BaseWindow, image_path: str, confidence: float = 0.9, counter=10) -> bool:
    for x in range(counter):
        try:
            window.activate()
            
            left, top, width, height = window.left, window.top, window.width, window.height
            region = (left, top, width, height)
            icon = pyautogui.locateCenterOnScreen(image_path, confidence=confidence, region=region)
      
            if icon is not None:
                return True
            time.sleep(2)
        except:
            time.sleep(2)
            return False
    return False

def paste(window: pygetwindow.BaseWindow, setText: str) -> bool:
    # set clipboard
    pyperclip.copy(setText)
    # paste
    pyautogui.hotkey('ctrl', 'v')


def hotkey () -> pyautogui.hotkey:
    return pyautogui.hotkey

def waitForText (window: pygetwindow.BaseWindow, text: str, counter=10)->bool:
    for x in range(counter):
        try:
            window.activate()
            cotnent = getText(window)
            if text in cotnent:
                return True
            time.sleep(2)
        except:
            time.sleep(2)
    return False


def screenshot (window: pygetwindow.BaseWindow, path: str) -> bool:
    window.activate()
    left, top, width, height = window.left, window.top, window.width, window.height
    region = (left, top, width, height)
    screenshot = pyautogui.screenshot(region=region)
    screenshot.save(path)
    return True