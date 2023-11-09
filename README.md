# WhisperEchoes
Experience the wonder of conversation without language barriers. This nimble audio translator lends you the power to seamlessly converse in a multitude of languages. It listens, interprets, and echoes back in the language of your choice—effortlessly, accurately, instantly.

WhisperEchoes is a real-time translation application that harnesses the power of [OpenAI's SDK](https://platform.openai.com/docs/overview) and [Instructor](https://github.com/jxnl/instructor) for on-the-fly speech-to-text and text-to-speech conversions. Designed to facilitate direct communication between two individuals who do not share a common language, WhisperEchoes provides an immediate spoken language translation, enabling each party to speak and listen in their native tongue.

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

Afrikaans (af), Arabic (ar), Armenian (hy), Azerbaijani (az), Belarusian (be), Bosnian (bs), Bulgarian (bg), Catalan (ca), Chinese (zh), Croatian (hr), Czech (cs), Danish (da), Dutch (nl), English (en), Estonian (et), Finnish (fi), French (fr), Galician (gl), German (de), Greek (el), Hebrew (he), Hindi (hi), Hungarian (hu), Icelandic (is), Indonesian (id), Italian (it), Japanese (ja), Kannada (kn), Kazakh (kk), Korean (ko), Latvian (lv), Lithuanian (lt), Macedonian (mk), Malay (ms), Marathi (mr), Maori (mi), Nepali (ne), Norwegian (no), Persian (fa), Polish (pl), Portuguese (pt), Romanian (ro), Russian (ru), Serbian (sr), Slovak (sk), Slovenian (sl), Spanish (es), Swahili (sw), Swedish (sv), Tagalog (tl), Tamil (ta), Thai (th), Turkish (tr), Ukrainian (uk), Urdu (ur), Vietnamese (vi), and Welsh (cy).

## License
This project is distributed under the MIT License. For more details, see the LICENSE.md file.