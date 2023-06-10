# Discussion
Offering several options to the player.

## Game concept:
- Make decision

## Programming concepts:
- dictionaries
- user input

# Having an item - The golden feather
During the first quest you can decide to take the feather. If you take the feather it will add some luck
to the fights.

## Game concept:
- Having an "item"

## Programming concept:
- Having a property in your class

# Fight - Against the wolves
When fighting against the wolves we introduce a nested loop. There are 3 wolves, each with some health
    and attack damage. In each turn the hero attacks first, and then the wolves.

There can be 2 outcomes each time when a wolf attacks:
 - misses (0 damage)
 - bites (some damage)

Damage is calculated by the next formula:
```
dmg = BASE_DAMAGE * (2/3) + random() * BASE_DAMAGE
``` 

There is a slight chance that the hero performs a "Critical hit" (double damage) when the hero has the
    feather.

The loop run until either the hero or all of the wolves died. (Must ensure that the hero wins every time!)


