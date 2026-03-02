import pygame
from pygame._sdl2.video import Window
import sys
import os

class SceneController: # !! WIP !!
    def move(self, direction):
        command_map = {
            "up": "UP_COMMAND",
            "down": "DOWN_COMMAND",
            "left": "LEFT_COMMAND",
            "right": "RIGHT_COMMAND"
        }
        print(f"Moving {direction}")
        #self.send_command(command_map[direction])

def create_window(fullscreen, display_index):
    num_displays = pygame.display.get_num_displays()
    display_index = min(display_index, num_displays - 1)

    if fullscreen:
        width, height = pygame.display.get_desktop_sizes()[display_index] # Get monitor resolution
        return pygame.display.set_mode((width, height), pygame.NOFRAME)
    else:
        return pygame.display.set_mode((1280, 720))

def main():
    pygame.init()
    display_index = 1 if pygame.display.get_num_displays() > 1 else 0
    
    fullscreen = False # Default startup is windowed mode
    screen = create_window(fullscreen, display_index)
    window = Window.from_display_module()
    window.position = (100, 100)
    pygame.display.set_caption("Projector Scene")

    clock = pygame.time.Clock()
    running = True
    
    # Square state
    width, height = screen.get_size()
    square_size = 200
    square_x = width // 2 - square_size // 2
    square_y = height // 2 - square_size // 2
    speed = 3 # Control how fast the square moves
    # Attempt to load decal image; fall back to blue square if unavailable
    decal_path = os.path.join(os.path.dirname(__file__), "Decals", "SAFETY_FIRST.png")
    decal_image = None
    if os.path.exists(decal_path):
        try:
            decal_image = pygame.image.load(decal_path).convert_alpha()
            decal_image = pygame.transform.smoothscale(decal_image, (600, 300))
        except Exception as e:
            print(f"Failed to load decal {decal_path}: {e}")

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False

                if event.key == pygame.K_f:
                    fullscreen = not fullscreen
                    screen = create_window(fullscreen, display_index)
                    width, height = screen.get_size() # Update width and height after changing mode
                    if fullscreen:
                        window.position = (0, 0) # !! CHANGE BASED ON DESIRED DISPLAY !!
                    else:
                        window.position = (100, 100) # Set windowed position
        
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            square_x -= speed
        if keys[pygame.K_RIGHT]:
            square_x += speed
        if keys[pygame.K_UP]:
            square_y -= speed
        if keys[pygame.K_DOWN]:
            square_y += speed

        width, height = screen.get_size()
        # Clamp to screen bounds
        square_x = max(0, min(square_x, width - square_size))
        square_y = max(0, min(square_y, height - square_size))

        screen.fill((0, 0, 0))
        if decal_image:
            screen.blit(decal_image, (square_x, square_y))
        else:
            pygame.draw.rect(screen, (0, 0, 255), (square_x, square_y, square_size, square_size))

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
