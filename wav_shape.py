#!/usr/bin/env python3
"""Show PCM WAV header shape without reading audio samples."""

import argparse
from pathlib import Path
import stat
import struct
import sys
import wave


def inspect(path):
    source = Path(path)
    if not stat.S_ISREG(source.stat().st_mode):
        raise wave.Error("input must be a regular file")
    with wave.open(str(source), "rb") as audio:
        channels, width, rate, frames, compression, _ = audio.getparams()
    if rate <= 0:
        raise wave.Error("invalid sample rate")
    return channels, width, rate, frames, compression


def main():
    parser = argparse.ArgumentParser(
        description="Show PCM WAV metadata without reading audio samples."
    )
    parser.add_argument("input", help="uncompressed PCM WAV file")
    args = parser.parse_args()

    try:
        channels, width, rate, frames, compression = inspect(args.input)
    except (wave.Error, EOFError, struct.error) as error:
        print(f"wav-shape: unsupported or malformed WAV: {error}", file=sys.stderr)
        return 1
    except OSError as error:
        print(f"wav-shape: {error.strerror or 'unable to read input'}", file=sys.stderr)
        return 2

    print(f"Channels: {channels}")
    print(f"Sample rate: {rate} Hz")
    print(f"Sample width: {width} byte(s) ({width * 8} bits)")
    print(f"Frames: {frames}")
    print(f"Duration: {frames / rate:.6f} seconds")
    print(f"Compression: {compression}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
