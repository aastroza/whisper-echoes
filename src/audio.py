from dotenv import load_dotenv
load_dotenv()

from openai import OpenAI

client = OpenAI()

def transcribe_audio(audio_file):

    audio= open(audio_file, "rb")
    transcript = client.audio.transcriptions.create(
                                                    model="whisper-1", 
                                                    file=audio, 
                                                    response_format="text"
                                                    )
    return transcript

def text_to_speech(text, output_file="output.mp3"):
    response = client.audio.speech.create(
                                            model="tts-1",
                                            voice="shimmer",
                                            input=text,
                                        )
    
    response.stream_to_file(output_file)