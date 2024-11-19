import pygame
import sys
from environment.rocket_landing_env import RocketLandingEnv  # Make sure this matches your environment file name

def main():
    env = RocketLandingEnv()
    clock = pygame.time.Clock()

    obs = env.reset()
    done = False

    while not done:
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                env.close()
                pygame.quit()
                sys.exit()

        # Get pressed keys
        keys = pygame.key.get_pressed()

        # Map keys to actions
        if keys[pygame.K_UP]:
            action = 1  # Apply thrust
        elif keys[pygame.K_LEFT]:
            action = 2  # Rotate left
        elif keys[pygame.K_RIGHT]:
            action = 3  # Rotate right
        else:
            action = 0  # Do nothing

        # Take a step in the environment
        obs, reward, done, info = env.step(action)

        # Render the environment
        env.render()

        # Control the frame rate
        clock.tick(30)  # Limit to 30 FPS

    env.close()

if __name__ == "__main__":
    main()
