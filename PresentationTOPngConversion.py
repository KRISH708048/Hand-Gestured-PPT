import aspose.slides as slides
import aspose.pydrawing as drawing
import os


# Input and output path
ppt_name = "Presentation1"
input_path = f"Input_presentation/{ppt_name}.pptx"
output_folder = f"Presentations/{ppt_name}"
os.makedirs(output_folder, exist_ok=True)

# Load the presentation
pres = slides.Presentation(input_path)


for index, slide in enumerate(pres.slides):
    # Save as PNG
    slide.get_thumbnail().save(f"{output_folder}/slide_{index + 1}.png", drawing.imaging.ImageFormat.png)

print(f"Slides from {ppt_name}.pptx have been successfully converted to PNG images.")
