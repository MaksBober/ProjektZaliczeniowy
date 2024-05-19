import wave
import numpy as np

import wave
import numpy as np
import os

def hide_data(audio_file, data_to_hide, output_file):
    with wave.open(audio_file, 'rb') as audio:
        frames = audio.readframes(audio.getnframes())
        samples = np.frombuffer(frames, dtype=np.int16)
        data = np.frombuffer(data_to_hide.encode('utf-8'), dtype=np.uint8)

        if len(data) * 8 > len(samples):
            raise ValueError("Not enough samples in the audio to hide the data.")

        if not os.path.exists(output_file):
            raise FileNotFoundError("Plik wyjściowy nie istnieje.")
        if not os.access(output_file, os.W_OK):
            raise PermissionError("Brak uprawnień do zapisu pliku wyjściowego.")

        modified_samples = samples.copy()

        for i in range(len(data)):
            modified_samples[i] = (modified_samples[i] & 0xFFFE) | ((data[i] & 0x80) >> 7)

    with wave.open(output_file, 'wb') as audio_out:
        audio_out.setparams(audio.getparams())
        audio_out.writeframes(modified_samples.tobytes())


def reveal_data(audio_file):
    with wave.open(audio_file, 'rb') as audio:
        frames = audio.readframes(-1)
        samples = np.frombuffer(frames, dtype=np.int16)

        data = []
        for i in range(len(samples)):
            data_byte = 0
            for j in range(8):
                data_byte |= (samples[i] & 1) << (7 - j)
                i += 1
            data.append(data_byte)
            if data_byte == 0:
                break

    return bytes(data).decode('utf-8')
