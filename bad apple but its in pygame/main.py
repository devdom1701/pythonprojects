import os
import pygame
from PIL import Image

# Pygame initialization
pygame.init()

# Constants
IMAGE_WIDTH = 480  # width of the original image
IMAGE_HEIGHT = 360  # height of the original image
SCALE_FACTOR = 2  # Scale factor: 2 image pixels = 1 Pygame pixel
WINDOW_SIZE = 800  # window size (can be larger than the image to add padding
BGCOLOR = (0, 0, 0)  # black background
WHITE = (255, 255, 255)  # RGB value of white
BLACK = (0, 0, 0)  # RGB value of black
FPS = 30  # Set a fixed frame rate (30 FPS)

# Brightness thresholds
BLACK_THRESHOLD = 50  # Below this is black
WHITE_THRESHOLD = 200  # Above this is white

class Visualizer:
    def __init__(self, screen):
        self.screen = screen
        self.imagepixels = []  # Store pixel data
        self.imagewidth = IMAGE_WIDTH
        self.imageheight = IMAGE_HEIGHT
        self.scaled_width = IMAGE_WIDTH // SCALE_FACTOR
        self.scaled_height = IMAGE_HEIGHT // SCALE_FACTOR

    def get_image_pixels(self, imagepath):
        im = Image.open(imagepath).convert("RGB")  # converting the image to RGB
        pixels = list(im.getdata())  # converting the original image to a list of pixels

        for pixel in pixels:
            brightness = sum(pixel) / 3  # the average brightness pixels; this is so that "grey" is classified as black
            if brightness <= BLACK_THRESHOLD:
                self.imagepixels.append(BLACK)
            elif brightness >= WHITE_THRESHOLD:
                self.imagepixels.append(WHITE)
            else:
                # default to white if its still in between thresholds
                self.imagepixels.append(WHITE)

    def preprocess_image(self, imagepath): # this is to avoid the lists getting exponentially larger and larger
        self.imagepixels = []
        self.get_image_pixels(imagepath)

    def render_frame(self):
        x = 150
        y =  200   # Starting coordinates for top-left corner

        for row in range(self.scaled_height):
            for col in range(self.scaled_width):
                original_x = col * SCALE_FACTOR
                original_y = row * SCALE_FACTOR
                index = original_y * self.imagewidth + original_x
                color = self.imagepixels[index]

                pygame.draw.rect(self.screen, color, (x, y, SCALE_FACTOR, SCALE_FACTOR))
                x += SCALE_FACTOR
            x = 150  # Reset x to start of the row
            y += SCALE_FACTOR

def main():
    screen = pygame.display.set_mode((WINDOW_SIZE, WINDOW_SIZE))
    pygame.display.set_caption("Bad Apple!")
    clock = pygame.time.Clock()

    pygame.mixer.init()

    folder_path = "frames"
    image_files = sorted(
        [os.path.join(folder_path, file) for file in os.listdir(folder_path) if file.endswith(".png")]
    )

    visualizer = Visualizer(screen)
    frames = []
    for image_file in image_files:
        visualizer.preprocess_image(image_file)
        print(f'processing file: {image_file}')
        frames.append(visualizer.imagepixels)

    running = True
    current_frame = 0

    while running:
        screen.fill(BGCOLOR)

        if current_frame == 10:
            music_file = "badapple.mp3"
            pygame.mixer.music.load(music_file)

            pygame.mixer.music.play()  # Start the music

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        if frames:
            visualizer.imagepixels = frames[current_frame]
            visualizer.render_frame()

            pygame.display.flip()

            current_frame = (current_frame + 1) % len(frames)

        clock.tick(FPS)  # Use a fixed frame rate

    pygame.mixer.music.stop()
    pygame.quit()

if __name__ == "__main__":
    main()