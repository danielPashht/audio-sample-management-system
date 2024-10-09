DB_DATA = {
    'host': 'localhost',
    'dbname': 'audio_sample_library',
    'user': 'postgres',
    'password': '946815',
}

DB_URL = 'postgresql://{user}:{password}@{host}:5432/{dbname}'.format(**DB_DATA)

DEFAULT_CATEGORIES = [
    "Drums", "Kick", "Snare", "Hi-Hat", "Cymbals", "Toms", "Percussion",
    "Bass", "Synth Bass", "Electric Bass", "Acoustic Bass",
    "Synths", "Lead Synth", "Pad Synth", "Arpeggiator", "Pluck Synth",
    "FX", "Risers", "Fallers", "Impacts", "Whooshes", "Glitch", "Transitions",
    "Vocals", "One-Shots", "Acapellas", "Vocal Chops",
    "Guitar", "Electric Guitar", "Acoustic Guitar",
    "Keys", "Piano", "Electric Piano", "Organ",
    "Orchestral", "Strings", "Brass", "Woodwinds",
    "Ambience", "Atmosphere", "Textures", "Drones",
    "Loops", "Drum Loops", "Bass Loops", "Melody Loops",
    "Foley", "Nature Sounds", "Urban Sounds", "Household Objects",
    "World Instruments", "Ethnic Percussion", "Traditional Instruments",
    "808s", "808 Kicks", "808 Bass",
    "Leads", "Synth Leads", "Guitar Leads",
    "Pads", "Synth Pads", "Ambient Pads",
    "Chords", "Synth Chords", "Guitar Chords"
]
