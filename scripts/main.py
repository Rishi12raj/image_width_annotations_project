import cv2
import matplotlib.pyplot as plt

image_path = "original_image/Screenshot (47).jpg"
image = cv2.imread(image_path)
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
height, width, _ = image_rgb.shape
arrow_y = height // 2
arrow_tip = max(10, min(width // 12, height // 8))
thickness = max(1, min(width, height) // 300)

cv2.arrowedLine(
	image,
	(0, arrow_y),
	(width-1, arrow_y),
	(0, 255, 0),
	thickness,
	tipLength=min(0.5, arrow_tip / max(width - 1 - arrow_y, 1)),
)
cv2.arrowedLine(
	image,
	(width - 1, arrow_y),
	(0, arrow_y),
	(0, 255, 0),
	thickness,
	tipLength=min(0.5, arrow_tip / max(width - 1 - arrow_y, 1)),
)

label = f"Width: {width} px"
font = cv2.FONT_HERSHEY_SIMPLEX
font_scale = max(0.4, min(1.2, width / 1000))
estimated_text_width = len(label) * 12 * font_scale
text_x = max(0, int(arrow_y - estimated_text_width // 2))
text_y = max(20, arrow_y - 12)
cv2.putText(
	image,
	label,
	(text_x, text_y),
	font,
	font_scale,
	(0, 255, 0),
	thickness,
	cv2.LINE_AA,
)

cv2.imwrite("output_images/annotated_width.jpg", image)

image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
plt.figure(figsize=(12, 8))
plt.imshow(image_rgb)
plt.axis("off")
plt.show()