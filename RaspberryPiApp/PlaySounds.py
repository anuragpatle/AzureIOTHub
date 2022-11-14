from pygame import mixer, time


class PlaySounds():

    def __init__(self):
        # Instantiate mixer
        mixer.init()

    def play_sound(slef, file_path):
        # Load audio file
        mixer.music.load(file_path)

        print("music started playing....")

        # Set preferred volume
        mixer.music.set_volume(1)

        # Play the music
        mixer.music.play()

        while mixer.music.get_busy():
            time.Clock().tick(10)


if __name__ == "__main__":
    playSounds = PlaySounds()
    playSounds.play_sound("./Files/fan_turned_off.mp3")
    playSounds.play_sound("./Files/fan_turned_on.mp3")

