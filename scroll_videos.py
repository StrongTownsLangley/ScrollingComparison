import cv2
import numpy as np

def create_alpha_gradient(height, width):
    """Create an alpha gradient with the specified height and width."""
    alpha_gradient = np.zeros((height, width), dtype=np.uint8)
    for y in range(height):
        alpha = int(255 * (y / height))
        alpha_gradient[y, :] = alpha
    return alpha_gradient

# Load the images
after_image_path = 'corridor_vert_1080_after.png'
before_image_path = 'corridor_vert_1080_before.png'
overlay_image_path = 'overlay.png'
after_image = cv2.imread(after_image_path)
before_image = cv2.imread(before_image_path)
overlay_image = cv2.imread(overlay_image_path, cv2.IMREAD_UNCHANGED)

# Ensure both images are loaded correctly
if after_image is None or before_image is None or overlay_image is None:
    print("Error loading images.")
    exit()

# Convert the images to 4-channel (with alpha if not already)
if after_image.shape[2] == 3:
    after_image = cv2.cvtColor(after_image, cv2.COLOR_BGR2BGRA)
if before_image.shape[2] == 3:
    before_image = cv2.cvtColor(before_image, cv2.COLOR_BGR2BGRA)

# Parameters
fps = 60
scroll_duration_seconds = 58
fade_duration_seconds = 2
hold_duration_seconds = 3
scroll_frames = fps * scroll_duration_seconds
fade_frames = fps * fade_duration_seconds
hold_frames = fps * hold_duration_seconds
total_frames = scroll_frames + fade_frames + hold_frames
frame_width = 1080
frame_height = 1920
gradient_height = 20
output_video = 'scrolling_video.mp4'

# Get image dimensions
after_img_height, after_img_width, _ = after_image.shape
before_img_height, before_img_width, _ = before_image.shape

# Calculate the step size for scrolling
step_size = (after_img_height - frame_height) / scroll_frames

# Define the codec and create VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
video_writer = cv2.VideoWriter(output_video, fourcc, fps, (frame_width, frame_height))

# Create the alpha gradients
alpha_gradient = create_alpha_gradient(gradient_height, frame_width)

# Pre-compute the alpha channel for the overlay image
if overlay_image.shape[2] == 4:
    overlay_alpha_channel = overlay_image[:, :, 3] / 255.0

# Scrolling phase
for i in range(scroll_frames):
    # Calculate the starting y-coordinate for the current frame
    start_y = int(i * step_size)
    
    # Extract the scrolling section from the 'after' image
    after_section = after_image[start_y:start_y + frame_height, 0:frame_width]
    
    # Create an overlay with the 'after' image
    overlay = np.zeros((frame_height, frame_width, 4), dtype=np.uint8)
    overlay[:, :, :3] = after_section[:, :, :3]
    overlay[:, :, 3] = 255  # Set alpha channel to 255

    # Apply the alpha gradient to the overlay
    overlay[frame_height // 2:frame_height // 2 + gradient_height, :, 3] = 255 - alpha_gradient
    overlay[frame_height // 2 + gradient_height:, :, 3] = 0  # Make bottom half transparent

    # Draw the complete 'before' image on the frame
    frame = before_image[start_y:start_y + frame_height, 0:frame_width].copy()
    
    # Combine the 'before' image and the 'after' image with the gradient
    alpha = overlay[:, :, 3] / 255.0
    for c in range(3):
        frame[:, :, c] = overlay[:, :, c] * alpha + frame[:, :, c] * (1.0 - alpha)
    
    # Add the PNG overlay
    for c in range(3):
        frame[:, :, c] = overlay_image[:, :, c] * overlay_alpha_channel + frame[:, :, c] * (1.0 - overlay_alpha_channel)

    # Write the frame to the video
    video_writer.write(cv2.cvtColor(frame, cv2.COLOR_BGRA2BGR))

    # Print progress
    if i % (total_frames // 100) == 0:
        print(f"Scrolling progress: {i / scroll_frames * 100:.2f}%")

# Fade-out phase
final_y = after_img_height - frame_height
for i in range(fade_frames):
    # Draw the final positions of 'before' and 'after' images
    after_section = after_image[final_y:final_y + frame_height, 0:frame_width]
    frame = before_image[final_y:final_y + frame_height, 0:frame_width].copy()

    # Calculate the current gradient position
    gradient_start = (frame_height // 2) + int(i * ((frame_height // 2 + gradient_height) / fade_frames))

    # Create an overlay with the 'after' image and moving gradient
    overlay = np.zeros((frame_height, frame_width, 4), dtype=np.uint8)
    overlay[:, :, :3] = after_section[:, :, :3]
    overlay[:, :, 3] = 255  # Set alpha channel to 255

    # Apply the alpha gradient to the overlay
    if gradient_start + gradient_height < frame_height:
        overlay[gradient_start:gradient_start + gradient_height, :, 3] = 255 - alpha_gradient
        overlay[gradient_start + gradient_height:, :, 3] = 0  # Make bottom part transparent

    # Combine the 'before' image and the 'after' image with the moving gradient
    alpha = overlay[:, :, 3] / 255.0
    for c in range(3):
        frame[:, :, c] = overlay[:, :, c] * alpha + frame[:, :, c] * (1.0 - alpha)

    # Add the PNG overlay
    for c in range(3):
        frame[:, :, c] = overlay_image[:, :, c] * overlay_alpha_channel + frame[:, :, c] * (1.0 - overlay_alpha_channel)

    # Write the frame to the video
    video_writer.write(cv2.cvtColor(frame, cv2.COLOR_BGRA2BGR))

    # Print progress
    if i % (fade_frames // 100) == 0:
        print(f"Fading progress: {i / fade_frames * 100:.2f}%")

# Hold the last frame for the specified duration
last_frame = frame.copy()
for i in range(hold_frames):
    video_writer.write(cv2.cvtColor(last_frame, cv2.COLOR_BGRA2BGR))

# Release the video writer object
video_writer.release()

print(f"Video saved as {output_video}")
