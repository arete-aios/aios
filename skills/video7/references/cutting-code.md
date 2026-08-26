# The cut, in detail

The method in this file is **Gianluca Mauro's**, developed over a run of talking-head edits and published here with his permission. The snippets are illustrative shapes, not a library. Read them, understand what each calibration is protecting against, then write your own.

---

## Why not just cut where the transcript says

Word timestamps from a speech model are approximate. In one measured take, a word the model placed at 22.56 s actually began at 22.84 s, and another placed at 13.02 s began at 13.43 s. Four hundred milliseconds is not a rounding error, it is the whole first syllable.

So the transcript decides **which** spans to keep. The audio decides **where** the cut lands.

## Verifying a boundary against the sound

Take the audio down to mono at a low sample rate, compute loudness over short windows, and read the envelope directly:

```python
# ffmpeg -i src.mov -map 0:a:0 -ac 1 -ar 8000 -f s16le a8k.raw
a = np.fromfile('a8k.raw', dtype=np.int16).astype(np.float32) / 32768
hop = 80                                   # 10 ms per column at 8 kHz
db = 20*np.log10(np.array([np.sqrt((a[i*hop:(i+1)*hop]**2).mean() + 1e-12)
                           for i in range(len(a)//hop)]) + 1e-12)
```

Print it as characters, one per 10 ms, and the shape of a sentence becomes visible: where breath ends, where the consonant starts, where the previous word decays. Set the region start about 0.10 s before the real onset, and end the previous region just after the previous word's decay.

**Two calibrations, both learned by getting them wrong:**

- **Speech threshold at −35 dB, and it must hold for two frames.** At −45 dB it triggers on room tone and on breathing, and every silence looks like speech.
- **The onset search runs forward only.** Searching backwards from a boundary finds the *previous* region's speech, and then every region reports as clipped, which sends you hunting a bug that is not there.

Make the verifier a separate step that either passes cleanly or names the boundary that failed. A cut you have not measured is a cut you will hear.

## Frame snapping, or the drift that ruins long edits

The single worst bug in this kind of pipeline, because it is inaudible on one join and obvious across twenty:

```python
d = round((end - start) * FPS) / FPS      # duration snapped to a whole frame
# then extract with -ss start -t d, and pad the audio tail
```

Video always rounds up to a whole frame. Audio keeps exactly the length requested. Every join therefore leaks a few milliseconds of audio ahead of picture, and it accumulates. One project reached **440 ms** of drift across twenty-five regions before anyone worked out why the ending looked dubbed. With the snap and an audio pad, the same edit measures within a frame of zero.

Have the build step **print the measured drift**. A number that must read zero is worth more than a comment saying it should.

## Captions that survive a recut

Generate cue timings from the edit itself, resolving every time through the region map:

```python
def O(i, s):  return starts[i] + (s - regions[i][0])   # source time -> output time
```

Then the text is written once per cue and the timings are derived. Recut the video and the captions move with it, with nothing retyped. This is what makes a second language nearly free: the timing is shared, only the words change.

**Four traps that silently delete words if the grouping is rewritten:**

- **Zero duration words exist.** One take produced ten of them out of 198. Pad every word to a minimum width or they overlap nothing and vanish.
- **A word can straddle a trimmed silence.** Assign each word to the region it overlaps most, then rescue any word that overlaps nothing but sits within about 0.25 s of a region. That distinguishes a trimmed pause from a deliberate cut, and without it whole seconds of speech disappear.
- **Do not split on word gaps.** Speech models emit noisy micro-gaps and splitting on them shreds the phrasing. Break on segment boundaries and punctuation instead.
- **In Python, `"" in ".?!"` is `True`.** An unguarded punctuation test therefore fires on every single word and yields one cue per word. Guard the empty string.

And check the line length cap **before** appending a word, not after, or every cue overshoots by exactly one word.

## Rendering text

Many static video builds ship without a text drawing filter. Render type as transparent images and lay them over the frame. This is not a workaround with a cost; drawing at full canvas resolution keeps type crisp instead of scaling it up from a smaller render.

- **Measure text widths, do not estimate them.** Subtitle renderers and image libraries disagree, by around 30 % in one measured case, and a caption style that never wraps will overflow and clip rather than fold.
- **Cards must grow with their content.** A fixed height box filled line by line sits visibly half empty. Animate the height and let the bounds clip what has not appeared yet, which also wipes each new line in.
- **Auto-fit every label.** A layout that fits in one language overflows in the next.
- **One emphatic element per view.** If a logo or corner mark is already using the accent colour, everything else is secondary.

## Mastering

Normalise to about −16 LUFS, then measure the result. Single pass loudness correction can undershoot by more than a decibel; one master landed at −17.4 and would have been quieter than everything around it. If it misses, run the two pass correction rather than shipping it.

Two behaviours that look like bugs and are not: containers report audio around 100 ms longer than video because of codec tail padding, and an overlay set to end with the shortest input drops the final frame unless the overlay stream emits a couple of frames more than the base.

---

## What to keep if you keep nothing else

Three habits, in order of how much time they save:

1. **Verify boundaries against the audio, never against the transcript.**
2. **Snap durations to whole frames, and print the drift.**
3. **Derive caption times from the edit, so a recut costs nothing.**

Everything else in this file is a detail. These three are the difference between an edit that can be revised and one that has to be redone.
