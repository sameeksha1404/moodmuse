# backend.py
import random
from midiutil import MIDIFile

# Simulate configuration object
config = {
    "guitar": {"notes": [[60, 64], [62, 65]], "channel": 1, "velocity": 80},
    "acoustic_guitar": {"notes": [[59, 63], [61, 64]], "channel": 1, "velocity": 75},
    "harp": {"notes": [[57, 62], [60, 65]], "channel": 1, "velocity": 70},
    "brass": {"notes": [[64, 67], [66, 69]], "channel": 1, "velocity": 85},
    "piano": {"notes": [[60, 64, 67], [62, 65, 69]], "channel": 2, "velocity": 90},
    "harmonica": {"channel": 3, "velocity": 60},
    "synth": {"channel": 3, "velocity": 70},
    "pad": {"channel": 4, "velocity": 50},
    "choir": {"channel": 4, "velocity": 55},
    "strings": {"notes": [[55, 60, 64], [57, 62, 65]], "channel": 4, "velocity": 65},
}

# Dummy MIDI-to-WAV converter
def midi_to_wav(midi_path, wav_path):
    # Replace with actual conversion logic
    import shutil
    shutil.copy(midi_path, wav_path)

def generate_song(mood):
    duration = 16
    time = 0
    midi = MIDIFile(8)

    # Harmony instrument
    harmony_instrument = "guitar" if mood == "😊 Happy" else "acoustic_guitar" if mood == "😢 Sad" else "harp" if mood == "🌙 Calm" else "brass"
    
    for i in range(0, duration, 2):
        if random.random() > 0.4:
            note_idx = (i // 2) % len(config[harmony_instrument]["notes"])
            notes = config[harmony_instrument]["notes"][note_idx]
            for note in notes:
                midi.addNote(5, config[harmony_instrument]["channel"], note, time + i + 0.5, 1, config[harmony_instrument]["velocity"] - 10)

    if mood in ["😊 Happy", "⚡ Energetic"]:
        arp_instrument = "harmonica" if mood == "😊 Happy" else "synth"
        for i in range(0, duration, 1):
            chord_idx = (i // 4) % len(config["piano"]["notes"])
            chord = config["piano"]["notes"][chord_idx]
            arp_note = chord[i % len(chord)]
            note_length = 0.25 if mood == "⚡ Energetic" else 0.5
            midi.addNote(6, config[arp_instrument]["channel"], arp_note + 12, time + i, note_length, config[arp_instrument]["velocity"] - 20)

    if mood in ["🌙 Calm", "😢 Sad"]:
        pad_instrument = "pad" if mood == "🌙 Calm" else "choir"
        for i in range(0, duration, 8):
            chord_idx = (i // 8) % len(config["strings"]["notes"])
            chord = config["strings"]["notes"][chord_idx]
            for note in chord:
                midi.addNote(6, config[pad_instrument]["channel"], note - 12, time + i, 8, config[pad_instrument]["velocity"] - 15)

    midi_path = f"/content/{mood}_music.mid"
    with open(midi_path, "wb") as f:
        midi.writeFile(f)

    wav_path = f"/content/{mood}_music.wav"
    midi_to_wav(midi_path, wav_path)

    return wav_path

def generate_tune(mood):
    return generate_song(mood)

def generate_music(mood: str, music_type: str):
    if music_type == "🎤 Riff":
        return generate_song(mood)
    else:
        return generate_tune(mood)