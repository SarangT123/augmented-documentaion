# Aruco code scanning 
## Setup
```py
import augmented
arucoar = augmented.arucoar(cap:int=0)
imgAug = {0: 'assets/unnamed.jpg'}
arucoar.setup(imgAug: dict, markerSize: int = 6, totalMarkers: int = 250, debug: bool = True, cam: int = 0, displayName: str = 'Augmented by Sarang')
```
setting the var `arucoar` to use `augmented.arucoar` taked one arg named `cap` which is the camera id
setting `imgAug` variable to a dict which contains the `Aruco` code and the location of the image to augment on top of 
The format of the dict is as follows 
{<id of the aruco code>(Must be an int) : <"Location of the image">(Must be a str)}

Then calls arucoar.setup (augmented.arucoar.setup) which takes 6 args 

The first one `imgAug` being compulsory and others being defualted to a value if not given

Their use are as following

- imgAug = a dict containing the aruco id as value and the image(location) to display when the value is True
- Markersize, totalMarkers = aruco code properties
- debug = to use debug mode
- cam = camera number
- displayName = tite of the display window


### Example
```py
import augmented
arucoar = augmented.arucoar(0)
imgAug = {0: 'assets/unnamed.jpg'}
arucoar.setup(imgAug,4,250,False,0,'Augmented by Sarang')
```
--------

## Scanning 
#### (Not nessecery/Might not be what you are looking for)
This function returns the aruco marker id and bounding boxes of the aruco marker in a list ([bboxes , id])
* Code given after the `setup` part
```py
arucoar.findArucoMakers(img, draw=True, markersize=6, totoalmarkers=250
```
*You dont need to pass in any args if u have done `arucoar.setup`/`augmented.arucoar.setup`

Args are as follows 
- img = frame to find aruco on
- Markersize, totalMarkers = aruco code properties
- draw = Wheather or not to draw the bounting box (* Not required used for augmenting)

### Example
```py
arucoar.findArucoMakers(img)
```
--------------

## Augmenting on top
The augmenting process can be done in two ways this documentaion will only explain the first way (`augment.arucoar.start`) in depth 

# Way 1 of augmenting `augment.arucoar.start`
Given code is after the `setup`/`augment.arucoar.setup` part
```py
arucoar.start(display:bool = True)
```
FInnally you can put this to start running the code 
this will return the augmented image and if you will se the `display` arg to True which it is by defualt 
It will also output the image in a window with the displayname you gave on the `setup`/`augment.arucoar.setup` part
## *recomended to use in a loop

## The other way 
#### (*not recomended only for specific use cases)
Given code is after the `setup`/`augment.arucoar.setup` part
```py
arucoar.augmentAruco(bbox, ids, img, imgAug, draw=True):
```
- bbox  = Bounding box of the aruco marker 
- id = id of the aruco marker
- img = The frame which contains the aruco marker
- imgAug = The image to augment on top of the marker 
- draw = Currently unused 
## *recomended to use in a loop