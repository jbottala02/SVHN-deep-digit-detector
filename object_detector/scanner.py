#-*- coding: utf-8 -*-

import cv2

class ImageScanner(object):
    def __init__(self, image):
        self._layer = image
    
    def get_next_patch(self, step_size=(10, 10), window_size=(30, 30)):
        for y in range(0, self._layer.shape[0] - window_size[0], step_size[0]):
            for x in range(0, self._layer.shape[1] - window_size[1], step_size[1]):
                yield (x, y, self._layer[y:y + window_size[1], x:x + window_size[0]])
    
    def get_next_layer(self, scale=0.7, min_size=(30, 30)):
        yield self._layer

        while True:
            h = int(self._layer.shape[0] * scale)
            w = int(self._layer.shape[1] * scale)
            
            self._layer = cv2.resize(self._layer, (w, h))
            
            min_h = min_size[0]
            min_w = min_size[1]
            if h < min_h or w < min_w:
                break
            yield self._layer
    
    
if __name__ == "__main__":
    pass

