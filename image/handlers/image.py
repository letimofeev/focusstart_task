from PIL import Image


class ImageHandler:
    def __init__(self, path):
        self.image = Image.open(path).convert('RGB')

    @property
    def shape(self):
        return self.image.size

    @property
    def pixel_count(self):
        return self.shape[0] * self.shape[1]

    @staticmethod
    def hex_to_rgb(value):
        value = value.lstrip('#')
        lv = len(value)
        return tuple(
            int(value[i:i + lv // 3], 16) for i in range(0, lv, lv // 3)
        )

    def color_counter(self, color):
        count = 0

        if color[0] == '#':
            color = ImageHandler.hex_to_rgb(color)

        for pixel in self.image.getdata():
            if pixel == color:
                count += 1

        return count

