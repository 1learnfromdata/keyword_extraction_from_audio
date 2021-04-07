from pydub import AudioSegment


mp3_audio = AudioSegment.from_file(r"dnc-2004-speech_converted.wav", format="wav")
print(len(mp3_audio)/(1000*60))

# 12 Minutes audio breaks into 2 minutes 7 audio files
counter_audio = 120
split_audio = [mp3_audio[:120*1000]]
for i in range(7):
    split_audio.append(mp3_audio[counter_audio*1000:(counter_audio+120)*1000])
    counter_audio += 120

count = 0
# # lets save it!
for count, audio_object in enumerate(split_audio):
    count += 1
    with open(f"{count}_audi_file.wav", 'wb') as out_f:
        audio_object.export(out_f, format='wav')

