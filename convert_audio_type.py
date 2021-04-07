from pydub import AudioSegment

mp3_audio = AudioSegment.from_file(r"dnc-2004-speech.mp3", format="mp3")
mp3_audio.export("dnc-2004-speech_converted.wav", format="wav")