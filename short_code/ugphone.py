from HexAutoTAP import helper
import time
all_window = helper.get_window_by_title("UgPhone")
devices = []
for device in all_window:
    if device.width != 1000 and device.height != 600:
        devices.append(device)

helper.Sort_windows(width=devices[0].width, height=devices[0].height, list_windows=devices) # sắp xếp các cửa sổ
helper.find_element_and_tap(
    window=devices[0],
    image_path=r"C:\Users\PC\Desktop\testlib\HexAutoTAP\Screenshot_3.png",
    confidence=0.7
) # click vào nút tìm kiếm


# tìm và gõ vào ô tìm kiếm
if helper.waitForElement(
    window=devices[0],
    image_path=r"C:\Users\PC\Desktop\testlib\HexAutoTAP\Screenshot_4.png",
    confidence=0.7,
    counter=10
):
    content = "Hello world"
    helper.paste(devices[0], content)
else:
    print("Not found")
