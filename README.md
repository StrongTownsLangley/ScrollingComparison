# ScrollingComparison
Python Script to Generate a Scrolling Video showing a Before and After Comparison for use on Maps, Roads, etc. 

The idea was inpired by [this excellent video](https://www.reddit.com/r/Sacramento/comments/1d31ziz/a_reminder_of_what_freeways_and_urban_renewal/) by **Troy Sankey** from **Strong Sactown** who produced a guide on how they made it [here](https://www.strongsactown.org/2024/06/02/how-to-make-freeway-before-after-animations/).

This in turn was inspired by [Segregation By Design](https://www.segregationbydesign.com/).

The script this video produces is a lot less flashy, but useful for a simple before and after comparison.

# Output Preview
![scrolling_video](https://github.com/StrongTownsLangley/ScrollingComparison/assets/160652425/2d55c810-282d-449c-adb8-e49fb9c2c0f1)

Instagram post: https://www.instagram.com/p/C77oHi0yvYP/

# About
The Township of Langley released a large JPEG file that showed the entire length of road to be improved. The original image is available [here](https://www.tol.ca/en/connect/resources/get-involved/engage-tol/2024/216-Complete-Streets-Project/216-Corridor-Map_r5_Full-Corridor.jpg) and the website about the project is [here](https://www.tol.ca/en/connect/216-street-complete-street-project.aspx).

Rotating the image 90 degrees and resizing it to 1080 pixels wide, it was possible to create a large image that can be panned vertically for a social media video. This was done to create *corridor_vert_1080_after.png*.

Creating the before map image, *corridor_vert_1080_before.png* was done by connecting [QGIS](https://www.qgis.org/) to the Township of Langley's ARCGIS server and exporting a large image of the area at 1:400 scale, and then adjusting the rotating and size to match the after image.

To create the illusion of one road "painting over" another, both images are scrolled simultainously until they reach the bottom.
A seperate fade loop is done to wipe the rest of the after image over the before image, as if the camera has stopped while the painting over continues.

# Using the Script

* Install the [latest version of python](https://www.python.org/).
* After install, open a command line and type the following:
`pip install opencv-python`
(if this doesn't work you may need to change to the Scripts folder in the Python install folder first)
* After install, double click the *scroll_videos.py* script

# Creating the Script

The script was created using ChatGPT's 4o model as of 2024-06-06. *[chatgpt_log.html](https://htmlpreview.github.io/?https://github.com/StrongTownsLangley/ScrollingComparison/blob/main/chatgpt_log.html)* is the record of the conversation.
