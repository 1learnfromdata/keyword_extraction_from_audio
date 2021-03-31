from pydub import AudioSegment


m4a_audio = AudioSegment.from_file(r"hindi/hindi_audio.mp3", format="mp3")
# m4a_audio.export("audio3.wav", format="wav")

# let's just include the first 30 seconds of the first song (slicing
# is done by milliseconds)
beginning_of_song = m4a_audio[60*1000:120*1000]

playlist = beginning_of_song
# for song in playlist_songs:
#
#     # We don't want an abrupt stop at the end, so let's do a 10 second crossfades
#     playlist = playlist.append(song, crossfade=(10 * 1000))

# let's fade out the end of the last song
playlist = playlist.fade_out(60)

# hmm I wonder how long it is... ( len(audio_segment) returns milliseconds )
playlist_length = len(playlist) / (1000*60)

# lets save it!
with open("%s_minute_playlist.wav" % playlist_length, 'wb') as out_f:
    playlist.export(out_f, format='wav')

