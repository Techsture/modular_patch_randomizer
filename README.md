# Modular Patch Randomizer
Patch randomizer for modular synthesizers.

## Module file format
* The filename should be the name of the module (probably shouldn't use spaces).
* The file itself is space-delimited.  Each line of the file has:
  * An __i__ or __o__ denoting the jack as input or output respectively.
  * A __space (" ")__ follows the i/o designation.
  * A __description__ of the jack (no spaces).
