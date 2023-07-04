import os
from pydub import AudioSegment
import librosa

# Define the directory with your audio files and noise file
audio_dir = 'male_age20_german_native/Labor/ohne_stopps/'
noise_file = 'hintegrund_konversation.mp3'

# Load the noise audio file
noise = AudioSegment.from_file(noise_file)

# Loop through all files in the directory
for filename in os.listdir(audio_dir):
    # Construct full file path
    filepath = os.path.join(audio_dir, filename)
    
    # Load the audio file
    audio = AudioSegment.from_file(filepath)
    
    # Cut the noise to match the audio length
    noise_cut = noise[5:len(audio)]

    noise_cut = noise_cut
    
    # Mix the audio with the noise
    mixed = audio.overlay(noise_cut)

    # Save the result
    mixed.export(f"male_age20_german_native/noisy/ohne_stopps/{filename}", format='wav')

print("All audio files processed successfully.")
