# Changelog

## v1.7.1

- Fix compilation on MSYS2.

## v1.7.0

- CMake install target.
- Lib's alias removed, and target renamed `qlementine-icons`.
- Add icons:

  - 16x16:
    - Brand: `github`, `github-fille`, `gitlab`, `gitlab-fill`.

## v1.6.0

- Add icons:

  - 16x16:
    - Action: `decrease`, `eye-crossed`, `filter-crossed`, `increase`, `resize-bigger`, `resize-smaller`, `scroll-lock`, `scroll-unlock`, `sort-user-asc`, `sort-user-desc`, `unlock`.
    - Brand: `mastodon`, `mastodon-fill`, `peertube`, `peertube-fill`, `x`.
    - Hardware: `radio`, `speaker`.
    - Misc: `book-open`, `education`, `function-angle`, `function-curve`, `function-linear`, `library`, `zoom-horizontal`, `zoom-vertical`.
    - Navigation: `arrow-down-left`, `arrow-down-right`, `arrow-up-left`, `arrow-up-right`, `key-return-noframe`, `key-tab`.
    - Shopping: `purcentage`.
  - 24x24:
    - Action: `clear.svg`, `copy.svg`, `cut.svg`, `decrease.svg`, `erase.svg`, `export.svg`, `increase.svg`, `lock.svg`, `minus-circle.svg`, `paste.svg`, `plus-circle.svg`, `redo.svg`, `save.svg`, `select-all.svg`, `sort-alpha-asc.svg`, `sort-alpha-desc.svg`, `sort-asc.svg`, `sort-desc.svg`, `sort-ranking-asc.svg`, `sort-ranking-desc.svg`, `sort-time-asc.svg`, `sort-time-desc.svg`, `trash.svg`, `undo.svg`, `update.svg`.
    - Brand: `android-fill.svg`, `android.svg`, `facebook-fill.svg`, `facebook.svg`, `instagram-fill.svg`, `instagram.svg`, `mac.svg`, `midi.svg`, `rss.svg`, `vst3.svg`, `windows.svg`, `youtube-fill.svg`, `youtube.svg`.
    - File: `folder-filled.svg`, `folder-open.svg`, `folder.svg`, `open-recent.svg`.
    - Hardware: `hdd.svg`, `tape.svg`.
    - Instrument: `amp.svg`, `banjo.svg`, `bass.svg`, `bongos.svg`, `cello.svg`, `clap.svg`, `cowbell.svg`, `cymbal.svg`, `drumkit.svg`, `drumsticks.svg`, `guitar-12-strings.svg`, `guitar-classical.svg`, `guitar-folk.svg`, `guitar-machine-head.svg`, `guitar-strat.svg`, `guitar-tele.svg`, `guitar.svg`, `hi-hat.svg`, `idiophone.svg`, `kick.svg`, `mandolin.svg`, `mastering.svg`, `microphone.svg`, `pedal-outlines.svg`, `pedal.svg`, `pedalboard.svg`, `piano.svg`, `pipe.svg`, `saxophone.svg`, `shakers.svg`, `shamisen.svg`, `snare.svg`, `synthesizer.svg`, `tambourine.svg`, `tamtam.svg`, `tom.svg`, `trumpet.svg`, `ukulele.svg`, `violin.svg`, `woodwind.svg`.
    - Media: `loop.svg`, `pause.svg`, `play.svg`, `record.svg`, `seek-backward.svg`, `seek-forward.svg`, `skip-backward.svg`, `skip-forward.svg`, `stop.svg`.
    - Misc: `color-swatch.svg`,`education.svg`,`empty-slot.svg`,`eye-crossed.svg`,`eye.svg`,`gift.svg`,`hourglass.svg`,`info.svg`,`items-grid-small.svg`,`items-grid.svg`,`items-list.svg`,`items-tree.svg`,`pen.svg`,`question.svg`,`spam.svg`,`tool.svg`,`user.svg`,`warning.svg`,`wave.svg`.
    - Navigation: `arrow-down-left.svg`,`arrow-down-right.svg`,`arrow-down.svg`,`arrow-left.svg`,`arrow-right.svg`,`arrow-up-left.svg`,`arrow-up-right.svg`,`arrow-up.svg`,`chevron-down.svg`,`chevron-left.svg`,`chevron-right.svg`,`chevron-up.svg`,`home.svg`,`menu-dots-circle.svg`,`menu-dots.svg`,`search.svg`,`settings.svg`,`sliders-horizontal.svg`,`sliders-vertical.svg`.
    - Shape: `check-tick-small.svg`, `check-tick.svg`, `heart-filled.svg`, `heart.svg`.
    - Shopping: `purcentage.svg`.

## v1.5.0

- Add icons:
  - 16x16:
    - Hardware: `database`, `server`, `wireless-0`, `wireless-1`, `wireless-2`, `wireless-disabled`, `wireless-none`.
    - Text: `justify-center`, `justify-fill`.
- `fromFreeDesktop` now returns the full path.
- FreeDesktop mappings have been updated.
- Move to Qt6.

## v1.4.0

- Add icons:

  - 12x12:
    - Misc: `zoom`.
    - Navigation: `arrows-left-right`, `arrows-up-down`.
  - 16x16:
    - Food: `burder`.
    - Hardware: `midi`.
    - Instruments: `cowbell`, `drumsticks`.
    - Media: `playlist`.
    - Misc: `cloud-down`, `cloud-up-down`, `cloud-up`, `empty-slot`, `stars`.

- Modified icons:
  - 16x16:
    - Instruments: `saxophone`.
    - Misc: `sun`.

## v1.3.0

- Add icons:
  - Instruments: `banjo`, `cello`, `guitar-12-strings`, `guitar-classical`, `guitar-folk`, `guitar-strat`, `guitar-tele`, `mandolin`, `pipe`, `pitched_idiophone`, `saxophone`, `shamisen`, `synthesizer`, `trumpet`, `ukulele`, `violin`, `woodwind`.
  - Action: `windows-close`, `windows-maximize`, `windows-minimize`, `windows-unmaximize`
  - Hardware: `jack`
  - Misc: `unknown`, `wave`
  - Shape: `check-tick-small`, `radio-tick`
- Update icons `guitar`, `bass`.
- Rename icon `pitched_idiophone` to `idiophone`
- Removed icon `fretboard`.

## v1.2.0

- Add support for more icon sizes, such as 32x32 pixels. **WARNING: paths have changed.**
- Add icons `octogon` and `octogon-filled`.
- Add CMake presets.
- Replace long copyright notice by a shorter one.

## v1.1.0

- Add icons `rename`, `share-external`, `microphone-old`, `accessibility`, `crane-hook`, `crane`, `moon`, `sun`, `address-book`.
- Fix icon paths for `build`, `close-small`, `close`, `move`, `preview`, `refresh`, `send`, `undo`, `youtube`, `youtube-fill`, `bell.svg`, `notes`, `paint-bucket`, `combobox-indicator`, `sliders-horizontal`.
- Rename icon `chevron-left-double` into `chevron-double-left`, and `chevron-right-double` into `chevron-double-right`.
- Rename icon `up` into `chevron-up`, and `down` into `chevron-down`.
- Removed icon `rse`.

## v1.0.1

- New CI jobs for Windows and MacOS.
- Bugfixes on the website.

## v1.0.0

- Initial release. Enjoy!
