import typing
from Options import Option, DefaultOnToggle, Choice


class ExpandedPool(DefaultOnToggle):
    """Puts room clear drops and take any caves into the pool of items and locations."""
    display_name = "Expanded Item Pool"


class ShuffleStartingSword(DefaultOnToggle):
    """Shuffles Wood Sword into the item pool"""
    display_name = "Shuffle Starting Sword"


class ShuffleWhiteSword(DefaultOnToggle):
    """Shuffle White Sword into the item pool"""
    display_name = "Shuffle White Sword"


class ShuffleMagicalSword(DefaultOnToggle):
    """Shuffle Magical Sword into the item pool"""
    display_name = "Shuffle Magical Sword"


class TriforceLocations(Choice):
    """Where Triforce fragments can be located. Note that Triforce pieces
    obtained in a dungeon will heal and warp you out, while overworld Triforce pieces obtained will appear to have
    no immediate effect. This is normal."""
    display_name = "Triforce Locations"
    option_vanilla = 0
    option_dungeons = 1
    option_anywhere = 2


class StartingWeaponPosition(Choice):
    """Where can a starting weapon (Swords that are shuffled, Red Candle, or Magical Rod) show up in your game.
    *Note that if ShuffleStartingSword is off, this option is ignored

    Safe means a weapon is guaranteed in Starting Sword Cave.
    Unsafe means that a weapon is guaranteed between Starting Sword Cave, Letter Cave, and Armos Knight.
    Dangerous adds these level locations to the unsafe pool (if they exist):
#       Level 1 Compass, Level 2 Bomb Drop (Keese), Level 3 Key Drop (Zols Entrance), Level 3 Compass
    Very Dangerous is the same as dangerous except it doesn't guarantee a weapon. It will only mean progression
    will be there in single player seeds. In multi worlds, however, this means all bets are off and after checking
    the dangerous spots, you could be stuck until someone sends you a weapon"""
    display_name = "Starting Weapon Position"
    option_safe = 0
    option_unsafe = 1
    option_dangerous = 2
    option_very_dangerous = 3


tloz_options: typing.Dict[str, type(Option)] = {
    "ExpandedPool": ExpandedPool,
    "ShuffleStartingSword": ShuffleStartingSword,
    "ShuffleWhiteSword": ShuffleWhiteSword,
    "ShuffleMagicalSword": ShuffleMagicalSword,
    "TriforceLocations": TriforceLocations,
    "StartingWeaponPosition": StartingWeaponPosition
}
