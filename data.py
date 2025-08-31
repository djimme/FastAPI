from modelC import Creature

_creatures: list[Creature] = [
    Creature(
        name='yeti', country='CN', area='Himalyas', description='Hirsute H', aka='ASnomwman'
    ),
    Creature(
        name='sasquatch', country='us', area='*', description="yeti's coursin Eddie", aka='bigfoot'
    )
]

def get_creatures() -> list[Creature]:
    return _creatures