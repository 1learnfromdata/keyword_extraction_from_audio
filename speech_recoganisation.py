# A python package for music and audio analysis.
# https://librosa.org/doc/latest/index.html
import librosa
import torch
from transformers import Wav2Vec2ForCTC, Wav2Vec2Tokenizer

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
print(device)
# load model and tokenizer
tokenizer = Wav2Vec2Tokenizer.from_pretrained("facebook/wav2vec2-base-960h")
model = Wav2Vec2ForCTC.from_pretrained("facebook/wav2vec2-base-960h")
model.to(device)
# The base model pretrained and fine-tuned on 960 hours of Librispeech on 16kHz sampled speech audio.
# When using the model make sure that your speech input is also sampled at 16Khz.

# load any audio file of your choice
speech, rate = librosa.load("audio_files/0.5_minute_playlist.wav", sr=16000)

input_values = tokenizer(speech, return_tensors='pt').input_values
# Store logits (non-normalized predictions)
logits = model(input_values).logits

# Store predicted id's
predicted_ids = torch.argmax(logits, dim=-1)
# decode the audio to generate text
# Passing the prediction to the tokenzer decode to get the transcription
transcription = tokenizer.batch_decode(predicted_ids)[0]
# transcriptions = tokenizer.decode(predicted_ids[0])
print(transcription)

import spacy
nlp = spacy.load("en_core_web_lg")
text = """spaCy is an open-source software library for advanced natural language processing, 
written in the programming languages Python and Cython. The library is published under the MIT license
and its main developers are Matthew Honnibal and Ines Montani, the founders of the software company Explosion."""
doc = nlp(transcription.lower())
print(doc.ents)
