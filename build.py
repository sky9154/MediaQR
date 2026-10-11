from MyQR import myqr
import os
import requests
import eel
import cv2

eel.init("gui")


@eel.expose
def buildQRcode(url, img, name):
  kirito = myqr
  if "https" in img or "http" in img:
    imgURL = img
    img_data = requests.get(imgURL).content

    if ".gif" in img or ".GIF" in img:
      img = "./picData.gif"
    else:
      img = "./picData.png"
    with open(img, "wb") as f:
      f.write(img_data)

    f.close()

  version, level, qr_name = kirito.run(words=url,
                                       version=20,
                                       picture=img,
                                       colorized=True,
                                       save_name=name)

  print("產生成功！！！")

  if name.lower().endswith(".gif"):
    os.startfile(qr_name)
  else:
    preview_image = cv2.imread(qr_name)

    if preview_image is None:
      raise ValueError(f"無法讀取產生的圖片：{qr_name}")

    cv2.imshow("Ciallo～(∠・ω< )⌒☆", preview_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


eel.start("index.html", mode="edge", size=(600, 400), port=8763)