# SunteHo
Detects Distance of the person from the screen and adjustes the volume accordingly

Conceptual | Simple Logic | Accuracy needs to be increased

## How this works?
- Uses OpenCV to detect faces.
- From reading some things online, found that to measure distance from screen, I would need an object with known dimensions in the frame, calculate focal lenght and then use it to find the distance from required objects.
- This did not look feasible. Spent some time and talked to a friend.
- So, this is what the program mainly does : 
  - Makes a box around the faces.
  - Calculates its area.
  - We just want relative distance, so keep on comparing the area in fix intervals of time.
  - Adjusts volume with pynput
  - Not too good results, will keep on in
  
# Requirements
- OpenCV
- pynput


Not getting too good results with this. 
