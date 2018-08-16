# Developer Notes

## Project Status

The Hispa project is only in the beginning stages.

Work done:

- Initial UFOs and designspace based on Source Serif Pro and Toto glyphs designed in 2016-2018.
- Toto glyphs are only one weight, and that weight may change
- Working build process (see below)

Not yet done:

- ExtraLight and Black master weights (anything but Medium) of Toto glyphs
- Medium weight may change
- Fine-tuning of punctuation and other characters in relation to Toto glyphs
- Individual glyph designs may change
- More characters may be added

We're not encouraging the public to participate in developing Hispa at this point, however please contact the development team through filing issues if you are intersted in getting involved.

## Editing

If you want to contribute to the project directly by editing the font source (mainly the designspaces and UFOs), then there are some important things you need to know.

### Source formats

The Hispa font sources are primarily three UFOs in the /source/masters folder.  HispaMaster-Medium.ufo is the source for the medium weight, and is in the [UFO3 format](http://unifiedfontobject.org/versions/ufo3/). If you edit the UFO3 sources you must commit your changes in that format. Pull requests in other formats, including UFO2, will not be accepted.

The three master UFOs are tied together using files in the [designspace format](https://github.com/LettError/designSpaceDocument) (HispaRoman.designspace is the main one). That file lists the three masters (sources) and defines six instances based on those masters.This follows the pattern of the [Source Serif Pro fonts](https://github.com/adobe-fonts/source-serif-pro) that serve as the source for the Latin glyphs. Please don't edit the designspace files without talking with us first by filing an issue in the github project. The HispaVariableRoman.designspace file is there in hopes that we may someday be able to build Hispa variation fonts, but is not actively kept up-to-date.

### Editing tools

You can use any editor that supports the UFO3 format to edit the project - including a simple text editor! Most font editing tools, however, do not support the format. If they do they typically produce app-specific 'flavors' of UFO3. Here are some notes on possible editing tools:

- **Robofont 3** directly opens, edits, and saves in the UFO3 format, although it may add some app-specific additional data to fonts it edits, which is mostly harmless and sometimes useful. It will not open the designspace directly, but an extension is available.
- **Glyphs** will open a UFO3 font, edit it, and then offer to save it in that format, although it may lose some metadata in the process and tends to add a lot of app-specific stuff to the lib.plist. It will also open up the designspace, which is a good way to edit all three masters together.
- **FontLab VI** seems to be making progress in their UFO support, but it's not ready yet. It still loses important data, so please don't use it.
- **FontForge** may be able to be used, but does not yet support the UFO3 format. So the fonts must first be _normalized/converted_ to the UFO2 format, opened, edited, saved as UFO2, then normalized back to UFO3 (see pysilfont tool below). That process may, however, lose some important data, so be aware that FF is not currently recommended, although we're working with the developer to improve the situation.
- **Text editors** can be used to edit the fonts, as the source is all text-based.

### Normalization

No matter which editor you use, you will need to _normalize_ the font before committing any changes. Because there is no canonical normalized format specified in the UFO3 standard, every editor - except some pure text editors - tends to change basic things: indentation, ordering, number formats, etc. That causes lots of problems for version control systems, as a single change to one glyph can result in changes to thousands of files!

**Normalization solves these problems**. It takes the edited UFO and brings it back into a standard format so that only the intended changes are indicated. This project uses the normalization capabilities of the [pysilfont python library](https://github.com/silnrsi/pysilfont) project. You will need to download and install pysilfont. Then after editing one of the UFO masters (such as HispaMaster-Medium.ufo)  you can normalize it by running the following from the command line on macOS or Linux systems while in the /source/masters folder:

```psfnormalize HispaMaster-Medium.ufo```

Pysilfont currently runs only with python 2.7.x - not 3 - although it sounds like efforts are underway to support python3. If you are on Windows it may be a bit trickier to get pysilfont and other tools to work easily, so you'll need to figure that out yourself.

**In any case, you must normalize the font using pysilfont before committing or initiating pull requests.**

### Preflight

If you've installed pysilfont (and you need to), then you can take advantage of a special tool that will take care of normalization, as well as syncing metadata changes throughout the family. From the root of the project run

```./preflight```

and it will do the hard work for you.

### Glyphs-specific import and export

If you want to edit the project on the Mac using the Glyphs application, there is a specific procedure you need to use:

- Open the _designspace_ file.
- Do your changes.
- Save as a Glyphs file with the name _HispaRoman.glyphs_ in the /source/masters folder.
- From the project root run the following Glyphs-specific version of _preflight_: ```./preflightg```

You will need to use Glyphs 2.5 or later, and in addition to the pysilfont package you will also need to have installed version 2.4 (not 3!) of the [glyphsLib library](https://github.com/googlei18n/glyphsLib) and all its dependencies. Not for the faint-hearted!

## Building

For intermediate testing purposes you may be able to use your font editor to generate a test font, although be aware that the master Medium weight of the Latin glyphs is slightly lighter in weight than the Regular instance produced by the build process. *Please do not distribute any fonts produced in this way to anyone.*

The actual fonts for use are produced using the [Smith](https://github.com/silnrsi/smith) build system. The _wscript_ file defines the details of that build.

The easiest way to get Smith running is to use the files in the [vm-install](https://github.com/silnrsi/smith/tree/master/vm-install) folder to spin up a virtual machine using Vagrant. Contact us for more information.

## Design Notes

At the moment, the Toto script glyphs in all three masters are identical. Please keep them identical unless you produce actual ExtraLight/Black weights. That means:

- Please only edit the _HispaMaster-Medium.ufo_ master.
- Then when you're ready to commit changes, copy what you did to the other two masters (ExtraLight/Black)
- Please always keep all three masters interpolation compatible or the build will break!


## Other

For copyright and licensing information - including any Reserved Font Names - see [OFL.txt](OFL.txt).

For practical information about using, modifying and redistributing this font see [OFL-FAQ.txt](OFL-FAQ.txt).

For more details about this project, including changelog and acknowledgements see [FONTLOG.txt](FONTLOG.txt) and [README.txt](README.txt).
