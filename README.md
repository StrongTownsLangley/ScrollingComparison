# ScrollingComparison
Python Script to Generate a Scrolling Video showing a Before and After Comparison for use on Maps, Roads, etc.

# Output Preview
![scrolling_video](https://github.com/StrongTownsLangley/ScrollingComparison/assets/160652425/2d55c810-282d-449c-adb8-e49fb9c2c0f1)

# About
The Township of Langley released a large JPEG file that showed the entire length of road to be improved. The original image is available [here](https://www.tol.ca/en/connect/resources/get-involved/engage-tol/2024/216-Complete-Streets-Project/216-Corridor-Map_r5_Full-Corridor.jpg) and the website about the project is [here](https://www.tol.ca/en/connect/216-street-complete-street-project.aspx).

Rotating the image 90 degrees and resizing it to 1080 pixels wide, it was possible to create a large image that can be panned vertically for a social media video. This was done to create *corridor_vert_1080_after.png*.

Creating the before map image, *corridor_vert_1080_before.png* was done by connecting [QGIS](https://www.qgis.org/) to the Township of Langley's ARCGIS server and exporting a large image of the area at 1:400 scale, and then adjusting the rotating and size to match the after image.

To create the illusion of one road "painting over" another, both images are scrolled simultainously until they reach the bottom.
A seperate fade loop is done to wipe the rest of the after image over the before image, as if the camera has stopped while the painting over continues.
