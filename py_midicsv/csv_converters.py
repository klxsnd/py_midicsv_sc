### System ###
import struct

### Local ###
from .midi.events import *

def as_midi_bytes(text):
    midi_bytes = b""
    X = iter(text)
    for c in X:
        if c == '\\':
            cc = next(X)
            if cc == '\\':
                midi_bytes += struct.pack("B",ord(cc))
            else:
                Nstr = cc + next(X) + next(X)
                midi_bytes += struct.pack("B",int(Nstr,base=8))
        else:
            midi_bytes += struct.pack("B",ord(c))
    return midi_bytes

def to_NoteOffEvent(track, time, identifier, line):
    channel, pitch, velocity = map(int, line)
    return NoteOffEvent(tick=time, channel=channel, pitch=pitch, velocity=velocity)


def to_NoteOnEvent(track, time, identifier, line):
    channel, pitch, velocity = map(int, line)
    return NoteOnEvent(tick=time, channel=channel, pitch=pitch, velocity=velocity)


def to_AfterTouchEvent(track, time, identifier, line):
    channel, pitch, value = map(int, line)
    return AfterTouchEvent(tick=time, channel=channel, pitch=pitch, value=value)


def to_ControlChangeEvent(track, time, identifier, line):
    channel, control, value = map(int, line)
    return ControlChangeEvent(tick=time, channel=channel, control=control, value=value)


def to_ProgramChangeEvent(track, time, identifier, line):
    channel, value = map(int, line)
    return ProgramChangeEvent(tick=time, channel=channel, value=value)


def to_ChannelAfterTouchEvent(track, time, identifier, line):
    channel, value = map(int, line)
    return ChannelAfterTouchEvent(tick=time, channel=channel, value=value)


def to_PitchWheelEvent(track, time, identifier, line):
    channel, value = map(int, line)
    return PitchWheelEvent(tick=time, channel=channel, pitch=value - 0x2000)


def to_SequenceNumberMetaEvent(track, time, identifier, line):
    value = int(line[0])
    return SequenceNumberMetaEvent(tick=time, value=value)


def to_ProgramNameEvent(track, time, identifier, line):
    text = as_midi_bytes(line[0])
    return ProgramNameEvent(tick=time, data=text)


def to_TextMetaEvent(track, time, identifier, line):
    text = as_midi_bytes(line[0])
    return TextMetaEvent(tick=time, data=text)


def to_CopyrightMetaEvent(track, time, identifier, line):
    text = as_midi_bytes(line[0])
    return CopyrightMetaEvent(tick=time, data=text)


def to_TrackNameEvent(track, time, identifier, line):
    text = as_midi_bytes(line[0])
    return TrackNameEvent(tick=time, data=text)


def to_InstrumentNameEvent(track, time, identifier, line):
    text = as_midi_bytes(line[0])
    return InstrumentNameEvent(tick=time, data=text)


def to_LyricsEvent(track, time, identifier, line):
    text = as_midi_bytes(line[0])
    return LyricsEvent(tick=time, data=text)


def to_MarkerEvent(track, time, identifier, line):
    text = as_midi_bytes(line[0])
    return MarkerEvent(tick=time, data=text)


def to_CuePointEvent(track, time, identifier, line):
    text = as_midi_bytes(line[0])
    return CuePointEvent(tick=time, data=text)


def to_ChannelPrefixEvent(track, time, identifier, line):
    channel = int(line[0])
    return ChannelPrefixEvent(tick=time, data=[channel])


def to_PortEvent(track, time, identifier, line):
    port = int(line[0])
    return PortEvent(tick=time, data=[port])


def to_EndOfTrackEvent(track, time, identifier, line):
    return EndOfTrackEvent(tick=time)


def to_DeviceNameEvent(track, time, identifier, line):
    text = as_midi_bytes(line[0])
    return DeviceNameEvent(tick=time, data=text)


def to_TrackLoopEvent(track, time, identifier, line):
    return TrackLoopEvent(tick=time)


def to_SetTempoEvent(track, time, identifier, line):
    mpqn = int(line[0])
    return SetTempoEvent(tick=time, mpqn=mpqn)


def to_SmpteOffsetEvent(track, time, identifier, line):
    hr, mn, se, fr, ff = map(int, line)
    return SmpteOffsetEvent(tick=time, hr=hr, mn=mn, se=se, fr=fr, ff=ff)


def to_TimeSignatureEvent(track, time, identifier, line):
    num, denom, click, notesq = map(int, line)
    return TimeSignatureEvent(tick=time, numerator=num, denominator=denom, metronome=click, thirtyseconds=notesq)


def to_KeySignatureEvent(track, time, identifier, line):
    key, major = int(line[0]), False if line[1] == "major" else True
    return KeySignatureEvent(tick=time, alternatives=key, minor=major)


def to_SequencerSpecificEvent(track, time, identifier, line):
    length, data = int(line[0]), [int(item) for item in line[1:]]
    return SequencerSpecificEvent(tick=time, data=data)


def to_SysexEvent(track, time, identifier, line):
    length, data = int(line[0]), [int(item) for item in line[1:]]
    return SysexEvent(tick=time, data=data)


def to_Sysex7Event(track, time, identifier, line):
    length, data = int(line[0]), [int(item) for item in line[1:]]
    return SysexF7Event(tick=time, data=data)
