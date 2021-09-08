# Overlaying images

## Setup
```py
import augmented
ar = augmented.ar_overlay(capture:int)#capture = camera number
ar.setup(targetImage: str, overlayImage: str, nfeatures: int, debug: bool=True, confidence: int=25, displayName: str="Augmented by sarang")
```
Here the variable ar is set to the ar_overlay class which takes an arg named `capture` which reffers to the camera number you want to use by defualt its 0
the we are setting the package up using  `ar.setup` which takes 6 args the first 3 being required and the others being optional 
They are explained below
- targetImage = Image to overlay on top of
- overlayImage =Image to overlay
- nfeatures = Features to detect on target image the bigger the more accurate and the more resource intensive 1000 recomended
- Not required but can tweak the ones below computer
- debug = debug mode
- confidence = How many feature matches to confirm
- displayname = title name```

### Example
```py
import augmented
ar = augmented.ar_overlay(0)
ar.setup('Image1.jpeg', 'Image2.jpeg', 1000, True, 25, 'Augmented reality by sarang')
```

## Overlaying
```py
ar.start(display=bool)
```
Here `ar.start` will start the function and it takes an arg named `display` which can be set to `True` to display the visual output 
This function returns the output image and a stacked image of the output and input

### Example
```py
while True:
    ar.start = display()
```
-------------------------------