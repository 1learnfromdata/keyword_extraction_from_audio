from pydub import AudioSegment


m4a_audio = AudioSegment.from_file(r"audio3.wav", format="wav")
# m4a_audio.export("audio3.wav", format="wav")
print(len(m4a_audio)/(1000*60))
# let's just include the first 30 seconds of the first song (slicing
# is done by milliseconds)

# 12 Minutes audio breaks into 2 minutes 7 audio files
counter_audio = 120
split_audio = [m4a_audio[:120*1000]]
for i in range(7):
    split_audio.append(m4a_audio[counter_audio*1000:(counter_audio+120)*1000])
    counter_audio += 120


# beginning_of_song = m4a_audio[60*1000:120*1000]
#
# playlist = beginning_of_song
# for song in playlist_songs:
#
#     # We don't want an abrupt stop at the end, so let's do a 10 second crossfades
#     playlist = playlist.append(song, crossfade=(10 * 1000))

# # let's fade out the end of the last song
# playlist = playlist.fade_out(60)
#
# # hmm I wonder how long it is... ( len(audio_segment) returns milliseconds )
# playlist_length = len(playlist) / (1000*60)

count = 0
# # lets save it!
for count, audio_object in enumerate(split_audio):
    count += 1
    with open(f"{count}_audi_file.wav", 'wb') as out_f:
        audio_object.export(out_f, format='wav')

