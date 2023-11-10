import pyaudio
import wave
import sys
import threading
import time
import uuid
from pygame import mixer

from textual.app import App, ComposeResult
from textual.containers import ScrollableContainer
from textual.reactive import reactive
from textual.widgets import Button, Footer, Header, Static

from dotenv import load_dotenv
load_dotenv()

from src.audio import transcribe_audio, text_to_speech
from src.translator import translate

# Audio recording parameters
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100
CHUNK = 1024
WAVE_OUTPUT_FILENAME = "recorded_audio.wav"

is_recording = False

class TranslationDisplay(Static):
    """A widget to display translated text."""

    translation = reactive("")
    recording_thread : threading.Thread = None
    
    def on_mount(self) -> None:
        """Event handler called when widget is added to the app."""
        self.update("Waiting...")

    def watch_translation(self, translation: str) -> None:
        """Called when the translation attribute changes."""
        self.update(f"{translation}")
        if len(translation) > 0:
            output_filename = self.create_random_filename()
            text_to_speech(translation, f'audios/{output_filename}')
            self.play_translation( f'audios/{output_filename}')

    def start(self) -> None:
        """Method to start recording."""
        self.update("Listening...")
        self.recording_thread = threading.Thread(target=self.record_audio)
        self.recording_thread.start()

    def stop(self):
        """Method to stop recording."""
        
        global is_recording
        is_recording = False
        self.recording_thread.join()
        self.update("Processing...")
        transcript = transcribe_audio(f'audios/{WAVE_OUTPUT_FILENAME}')
        translation = translate(transcript, ["es", "en"])
        self.translation = translation
        self.update(f"{translation}")
        

    def record_audio(self) -> None:
        global is_recording
        audio = pyaudio.PyAudio()

        stream = audio.open(format=FORMAT, channels=CHANNELS,
                            rate=RATE, input=True,
                            frames_per_buffer=CHUNK)

        frames = []
        is_recording = True
        while is_recording:
            data = stream.read(CHUNK, exception_on_overflow=False)
            frames.append(data)

        stream.stop_stream()
        stream.close()
        audio.terminate()

        wf = wave.open(f'audios/{WAVE_OUTPUT_FILENAME}', 'wb')
        wf.setnchannels(CHANNELS)
        wf.setsampwidth(audio.get_sample_size(FORMAT))
        wf.setframerate(RATE)
        wf.writeframes(b''.join(frames))
        wf.close()
    
    def play_translation(self, output_filename="output.mp3") -> None:
        mixer.init()
        mixer.music.load(output_filename)
        mixer.music.play()
    
    def create_random_filename(self) -> str:
        random_filename = str(uuid.uuid4()) + ".mp3"
        return random_filename


class Translator(Static):
    """A translator widget."""

    def on_button_pressed(self, event: Button.Pressed) -> None:
        """Event handler called when a button is pressed."""
        button_id = event.button.id
        translation_display = self.query_one(TranslationDisplay)
        if button_id == "start":
            translation_display.start()
            self.add_class("started")
        elif button_id == "stop":
            self.remove_class("started")
            translation_display.stop()

    def compose(self) -> ComposeResult:
        """Create child widgets of a translator."""
        yield Button("Start", id="start", variant="success")
        yield Button("Stop", id="stop", variant="error")
        yield TranslationDisplay()


class TranslatorApp(App):
    """A Textual app to manage the Translator."""

    CSS_PATH = "whisper_echoes.tcss"

    BINDINGS = [
        ("d", "toggle_dark", "Toggle dark mode"),
    ]

    def __init__(self, language1: str="en", language2: str="es") -> None:
        self.language1 = language1
        self.language2 = language2
        super().__init__()

    def compose(self) -> ComposeResult:
        """Called to add widgets to the app."""
        yield Header()
        yield Footer()
        yield ScrollableContainer(Translator(), id="translations")


    def action_toggle_dark(self) -> None:
        """An action to toggle dark mode."""
        self.dark = not self.dark


if __name__ == "__main__":
    app = TranslatorApp()
    app.run()