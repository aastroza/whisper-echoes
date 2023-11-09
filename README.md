# WhisperEchoes
Experience the wonder of conversation without language barriers. This nimble audio translator lends you the power to seamlessly converse in a multitude of languages. It listens, interprets, and echoes back in the language of your choice—effortlessly, accurately, instantly.

WhisperEchoes is a real-time translation application that harnesses the power of [OpenAI's SDK](https://platform.openai.com/docs/overview) for on-the-fly speech-to-text and text-to-speech conversions. Designed to facilitate direct communication between two individuals who do not share a common language, WhisperEchoes provides an immediate spoken language translation, enabling each party to speak and listen in their native tongue.

## Features
- Real-Time Translation: Engage in conversations with speakers of any language using immediate audio translation.
- OpenAI API Integration: Implements the latest OpenAI API for reliable speech recognition and synthesis.
- User-Friendly CLI: Simple command-line interface for effortless operation.
- Continuous Interaction: Designed for ongoing dialogue, allowing for multiple exchanges in a single session.

## Installation

```
conda create --name whisper-echoes -c conda-forge python=3.11
conda activate whisper-echoes
pip install -r requirements.txt
```

## Usage
To start a real-time translation session for a conversation, run the following command with the source and target [ISO 639-1 language codes](https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes):

```
python app.py <source_language_code> <target_language_code>
```

Example for translating a conversation from an english and spanish speakers:

```
python whisper_echoes.py en es
```

Upon initiation, the application will prompt each user to speak after pressing 'Enter'. It will then translate and read out loud the translated speech in the other user's language.

## Supported Languages

Afrikaans, Arabic, Armenian, Azerbaijani, Belarusian, Bosnian, Bulgarian, Catalan, Chinese, Croatian, Czech, Danish, Dutch, English, Estonian, Finnish, French, Galician, German, Greek, Hebrew, Hindi, Hungarian, Icelandic, Indonesian, Italian, Japanese, Kannada, Kazakh, Korean, Latvian, Lithuanian, Macedonian, Malay, Marathi, Maori, Nepali, Norwegian, Persian, Polish, Portuguese, Romanian, Russian, Serbian, Slovak, Slovenian, Spanish, Swahili, Swedish, Tagalog, Tamil, Thai, Turkish, Ukrainian, Urdu, Vietnamese, and Welsh.

## License
This project is distributed under the MIT License. For more details, see the LICENSE.md file.