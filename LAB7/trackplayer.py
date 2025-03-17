import pygame
import os

pygame.init()
pygame.mixer.init()

SCREEN_WIDTH, SCREEN_HEIGHT = 400, 300
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Music Player")
font = pygame.font.Font(None, 36)

MUSIC_FOLDER = "music/"

playlist = [os.path.join(MUSIC_FOLDER, f) for f in os.listdir(MUSIC_FOLDER) if f.endswith(".mp3")]

current_track = 0

def play_music():
    if playlist:
        print(f"Playing: {os.path.basename(playlist[current_track])}")
        pygame.mixer.music.load(playlist[current_track])
        pygame.mixer.music.play()
    else:
        print("Playlist is empty")

def stop_music():
    print("Music stopped")
    pygame.mixer.music.stop()

def next_track():
    global current_track
    current_track = (current_track + 1) % len(playlist)
    print(f"Next track: {os.path.basename(playlist[current_track])}")
    play_music()

def previous_track():
    global current_track
    current_track = (current_track - 1) % len(playlist)
    print(f"Previous track: {os.path.basename(playlist[current_track])}")
    play_music()

KEY_BINDINGS = {
    pygame.K_RETURN: play_music, 
    pygame.K_BACKSPACE: stop_music, 
    pygame.K_RIGHT: next_track, 
    pygame.K_LEFT: previous_track,
}

print("Enter - Play track")
print("Backspace - Stop")
print("Right button - Next track")
print("Left button - Previous track")

def draw_text(text, x, y):
    render_text = font.render(text, True, (255, 255, 255))
    screen.blit(render_text, (x, y))

running = True
while running:
    screen.fill((0, 0, 0))
    draw_text("Music Player", 120, 50)
    draw_text("Enter - Play", 120, 100)
    draw_text("Backspace - Stop", 120, 140)
    draw_text("→ - Next", 120, 180)
    draw_text("← - Previous", 120, 220)
    pygame.display.flip()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print("Program is closing...")
            running = False
        elif event.type == pygame.KEYDOWN:
            print(f"Button: {event.key}")
            if event.key in KEY_BINDINGS:
                KEY_BINDINGS[event.key]()   
pygame.quit()
