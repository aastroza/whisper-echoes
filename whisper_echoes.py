import pyaudio
import wave
import sys
import threading
import time
import uuid
from pygame import mixer

from dotenv import load_dotenv
load_dotenv()

from src.audio import transcribe_audio, text_to_speech
from src.translator import translate

# Check if language parameters are given
if len(sys.argv) != 3:
    print("Usage: python app.py <language1> <language2>")
    sys.exit(1)

# Store the languages from command line arguments
language1 = sys.argv[1]
language2 = sys.argv[2]

# Audio recording parameters
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100
CHUNK = 1024
WAVE_OUTPUT_FILENAME = "recorded_audio.wav"

# Flag to control the recording
is_recording = False

def record_audio():
    global is_recording
    audio = pyaudio.PyAudio()

    # Start recording
    stream = audio.open(format=FORMAT, channels=CHANNELS,
                        rate=RATE, input=True,
                        frames_per_buffer=CHUNK)
    print("Recording... Press 'Enter' to stop.\n")

    frames = []
    is_recording = True
    while is_recording:
        data = stream.read(CHUNK, exception_on_overflow=False)
        frames.append(data)

    # Stop and close the stream
    stream.stop_stream()
    stream.close()
    audio.terminate()

    # Save the recorded data as a WAV file
    wf = wave.open(f'audios/{WAVE_OUTPUT_FILENAME}', 'wb')
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(audio.get_sample_size(FORMAT))
    wf.setframerate(RATE)
    wf.writeframes(b''.join(frames))
    wf.close()
    print("Recording stopped.\n")

def play_translation(output_filename="output.mp3"):
    mixer.init()
    mixer.music.load(output_filename)
    mixer.music.play()

    while mixer.music.get_busy():  # wait for music to finish playing
        time.sleep(0.1)

def create_random_filename(extension='.mp3'):
    random_filename = str(uuid.uuid4()) + extension
    return random_filename

def main_loop():
    while True:
        print("\n\n=====================================================\n")
        input("Press 'Enter' to start recording\n")
        recording_thread = threading.Thread(target=record_audio)
        recording_thread.start()

        input("Press 'Enter' again to stop the recording\n")
        global is_recording
        is_recording = False
        recording_thread.join()

        # Process the recording here
        transcript = transcribe_audio(f'audios/{WAVE_OUTPUT_FILENAME}')
        translation = translate(transcript, [language1, language2])

        output_filename = create_random_filename()
        text_to_speech(translation, f'audios/{output_filename}')
        play_translation( f'audios/{output_filename}')

        continue_recording = input("Press 'Enter' to translate another phrase or type 'exit' to quit: ")
        if continue_recording.lower() == 'exit':
            break

if __name__ == "__main__":
    main_loop()