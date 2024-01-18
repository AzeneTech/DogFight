from shared.isprite import ISprite
from PIL import Image


class Sprite(ISprite):
    __image: str

    def __init__(self, image: str):
        self.__image = image

    def getImage(self) -> str:
        return self.__image

    def rotateSprite(self, angle: float):
        # https://note.nkmk.me/en/python-pillow-rotate/
        planeImg = Image.open(f'{self.__image.strip(".png")}Base.png')
        planeImg = planeImg.rotate(-angle, resample=Image.BICUBIC, expand=True)
        # if angle > 0.8:
        #     planeImg.show()
        planeImg.save(f'{self.__image}')
