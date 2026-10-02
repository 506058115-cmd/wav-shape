# wav-shape

Show the channel count, sample rate, sample width, frame count, duration, and compression field declared by an uncompressed PCM WAV header. Audio samples are not read or displayed.

## Use

Requires Python 3.8+; no packages to install.

```sh
python wav_shape.py recording.wav
```

Supports PCM WAV files handled by Python's standard `wave` module. `WAVE_FORMAT_EXTENSIBLE` PCM headers require Python 3.12 or newer. Duration comes from the frame count and sample rate in the header; the audio payload is not scanned for truncation or decoded. The exit status is 0 for supported input, 1 for malformed or unsupported WAV, and 2 for unreadable input.

## License

MIT
