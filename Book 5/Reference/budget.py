#!/usr/bin/env python3
"""
Budget calculator for Book 5 treasure allocation.
Party of 5 PCs, levels 13, 14, and first half of 15.

Budget targets (from 2e treasure-by-level table, adjusted for 5 PCs):
  Level 13: 26,500 gp
  Level 14: 38,750 gp
  Level 15.5: 28,875 gp
  Total: 94,125 gp

Items are categorized as:
  - permanent: fills a required permanent item slot (full value)
  - extra_permanent: above the slot count (full value, eats into budget)
  - consumable: fills a consumable slot (full value)
  - currency: coins, art, or below-level items counted at half price
    (the value listed IS the budget-counted value, already halved where applicable)
  - story: does not count against budget (artifacts, quest items)
  - reference: spellbooks and similar (does not count against budget)
"""


def print_budget(label, target, permanents, extra_permanents, consumables, currency):
    perm_total = sum(v for _, v in permanents)
    extra_total = sum(v for _, v in extra_permanents)
    cons_total = sum(v for _, v in consumables)
    curr_total = sum(v for _, v in currency)
    total = perm_total + extra_total + cons_total + curr_total

    print(f"\n{'=' * 60}")
    print(f"  {label}")
    print(f"{'=' * 60}")

    print(f"\n  Permanent Items (in slots):")
    for name, val in permanents:
        print(f"    {name:50s} {val:>8,} gp")
    print(f"    {'':50s} --------")
    print(f"    {'Subtotal':50s} {perm_total:>8,} gp")

    if extra_permanents:
        print(f"\n  Extra Permanent Items (above slot count):")
        for name, val in extra_permanents:
            print(f"    {name:50s} {val:>8,} gp")
        print(f"    {'':50s} --------")
        print(f"    {'Subtotal':50s} {extra_total:>8,} gp")

    print(f"\n  Consumables:")
    for name, val in consumables:
        print(f"    {name:50s} {val:>8,} gp")
    print(f"    {'':50s} --------")
    print(f"    {'Subtotal':50s} {cons_total:>8,} gp")

    print(f"\n  Currency & Below-Level Items:")
    for name, val in currency:
        print(f"    {name:50s} {val:>8,} gp")
    print(f"    {'':50s} --------")
    print(f"    {'Subtotal':50s} {curr_total:>8,} gp")

    diff = total - target
    pct = diff / target * 100
    print(f"\n  {'TOTAL':50s} {total:>8,} gp")
    print(f"  {'Target':50s} {target:>8,} gp")
    print(f"  {'Difference':50s} {diff:>+8,} gp ({pct:+.1f}%)")


# ============================================================
# LEVEL 13: Parts 1-2 (The Scribbler + Dragon Hoard)
# ============================================================
print_budget(
    "LEVEL 13 (Parts 1-2)",
    target=26_500,
    permanents=[
        ("Fanged Falchion (L14)", 4500),
        ("Wand of Crackling Lightning 3rd-rank (L14)", 4500),
        ("Wand of Shardstorm 3rd-rank (L13)", 3000),
        ("+2 greater striking runestone (L12)", 2000),
        ("+2 resilient breastplate (Scribbler, L11)", 1400),
    ],
    extra_permanents=[],
    consumables=[
        ("Healing Potion Greater x2 (L12)", 800),
        ("Blasting Stone Moderate x2 (L11)", 200),
        ("Potion of Resistance cold x2 (L12)", 700),
        ("Scroll Dispelling Globe rank 6 (L11)", 300),
        ("Scroll Heal rank 6 (L11)", 300),
    ],
    currency=[
        ("Mixed coinage (dragon hoard)", 730),
        ("Tapestries, silverware, jewelry", 1500),
        ("Onyx raven full plate (art)", 240),
        ("Cold iron returning dagger (half)", 125),
        ("Diamond dust", 75),
        ("Ink vials", 5),
        ("Holy water x6", 18),
        ("Everburning torches x6", 90),
        ("Dragon bane ammo x2 (half)", 250),
        ("Healing potions Greater x4 (half)", 800),
        ("Healing potions Moderate x4 (half)", 100),
        ("Scroll Cleanse Affliction (half)", 15),
        ("Chime of Opening (half)", 120),
        ("Duskwood shield (half)", 220),
        ("Wand of Heal rank 3 (half)", 250),
        ("+1 flaming striking longsword (half)", 300),
        ("+1 striking adamantine warhammer (half)", 750),
        ("Dawnsilver chain shirts x2 (half)", 1600),
        ("Cloak of the Bat (half)", 450),
        ("Charm of Resistance cold (half)", 500),
        ("+2 resilient half-plate wolf (half)", 700),
        ("Resistance potions cold x2 (half)", 350),
    ],
)


# ============================================================
# LEVEL 14: Parts 3-8 (Runeforge wings)
# ============================================================
print_budget(
    "LEVEL 14 (Parts 3-8)",
    target=38_750,
    permanents=[
        ("Robe of the Archmagi black (L15)", 6500),
        ("Rod of Negation (L14)", 4300),
        ("Staff of Hungry Shadows (L14)", 4500),
        ("Staff of Mithral Might (L14)", 4500),
        ("Sadist's Lash (L14)", 4500),
    ],
    extra_permanents=[
        ("+2 GS keen wounding dagger, Xyoddin (L14)", 4500),
        ("+2 resilient glamered dawnsilver chain shirt (L14)", 3140),
        ("Golem Stylus (L13)", 3000),
    ],
    consumables=[
        ("Scroll Interplanar Teleport rank 7 x2 (L13)", 1200),
        ("Potion of Quickness (L14)", 900),
        ("Healing Potion Greater x3 (L12)", 1200),
        ("Scroll Teleport rank 6 (L11)", 300),
        ("Scroll Stone to Flesh rank 6 (L11)", 300),
    ],
    currency=[
        # Part 3: Abjurant Halls
        ("Ethillion 12x150gp", 1800),
        ("Healing potions Greater x3 E4 (half)", 600),
        # Part 4: Ravenous Crypts
        ("Necrology books F6", 400),
        ("Crypt art F3 (gold+sapphires+amethysts+wine)", 1185),
        ("Necromancy research books F7", 750),
        ("+2 resilient chain shirt Xyoddin (half)", 700),
        ("Lenses x10", 100),
        ("Coins (Xyoddin)", 15),
        ("Charm of Resistance Greater Azaven (half)", 500),
        ("Cloak of the Bat Azaven (half)", 450),
        ("Contingency statuette", 200),
        ("Surgical equipment", 120),
        ("Mixed gems/linens F11", 400),
        ("Octopus Bottle (half)", 225),
        # Part 5: Vault of Greed
        ("Gemstones G1", 50),
        ("Ring of Wizardry II (half)", 360),
        ("Detect Metal (half)", 65),
        ("Transmutation research books G6", 750),
        ("Diamond dust G6", 50),
        # Part 6: Iron Cages of Lust
        ("Alu-demon jewelry x4", 2400),
        ("Silver/gold cages x13", 975),
        ("Spacious Pouches x2 (half)", 300),
        ("Moderate healing potions x4 (half)", 100),
        ("Potion Cleanse Affliction (half)", 30),
        ("Potion Sure Footing (half)", 15),
        ("Boudoir art objects", 150),
        # Part 7: Shimmering Veils
        ("Golden peacock", 80),
        ("Daggers x6", 30),
        ("Noble outfits x6", 60),
        ("Illusion books I3", 150),
        ("Ring of Wizardry III (half)", 1000),
        ("Charlatan's Cape (half)", 400),
        ("Hat of Disguise Greater (half)", 100),
        # Part 8: Festering Maze
        ("Spacious Pouch J3 (half)", 150),
        ("Staff of Summoning Greater (half)", 450),
        ("Diamond dust J5", 50),
        ("Ivory plaque", 5),
        ("Silver mirror", 100),
        ("Immovable Rods x2 (half)", 600),
        ("Scrolls J5 (Teleport + StF, half)", 300),
    ],
)


# ============================================================
# LEVEL 15.5: Parts 9-10 (Halls of Wrath + Weapons of Power)
# ============================================================
print_budget(
    "LEVEL 15.5 (Parts 9-10)",
    target=28_875,
    permanents=[
        ("+3 GS flaming adamantine ranseur Athroxis (L16)", 11900),
        ("+2 GR dawnsilver breastplate Athroxis (L15)", 6100),
        ("Wand of Crackling Lightning 5th-rank (L15)", 4500),
    ],
    extra_permanents=[
        ("Ring of Wizardry Type IV (L14)", 4000),
    ],
    consumables=[
        ("Scroll Howling Blizzard rank 7 (L13)", 720),
        ("Elemental Gem fire (L10)", 200),
    ],
    currency=[
        ("Golem eye gemstone", 250),
        ("Bulk K3 equipment (capped)", 2000),
        ("Bulk K4 equipment (capped)", 1500),
        ("K5 weapons x6 (half)", 300),
        ("Spell component pouch", 5),
    ],
)


# ============================================================
# GRAND TOTAL
# ============================================================
print(f"\n{'=' * 60}")
print(f"  GRAND TOTAL")
print(f"{'=' * 60}")
# Just re-run the numbers
totals = {}
for label, target, parts in [
    ("Level 13", 26_500, [4500+4500+3000+2000+1400, 0, 800+200+700+300+300,
        730+1500+240+125+75+5+18+90+250+800+100+15+120+220+250+300+750+1600+450+500+700+350]),
    ("Level 14", 38_750, [6500+4300+4500+4500+4500, 4500+3140+3000, 1200+900+1200+300+300,
        1800+600+400+1185+750+700+100+15+500+450+200+120+400+225+50+360+65+750+50+2400+975+300+100+30+15+150+80+30+60+150+1000+400+100+150+450+50+5+100+600+300]),
    ("Level 15.5", 28_875, [11900+6100+4500, 4000, 720+200,
        250+2000+1500+300+5]),
]:
    perm, extra, cons, curr = parts
    total = perm + extra + cons + curr
    diff = total - target
    pct = diff / target * 100
    print(f"  {label:15s}  total: {total:>8,}  target: {target:>8,}  diff: {diff:>+7,} ({pct:+.1f}%)")
    totals[label] = (total, target)

grand_total = sum(t for t, _ in totals.values())
grand_target = sum(t for _, t in totals.values())
print(f"  {'Grand':15s}  total: {grand_total:>8,}  target: {grand_target:>8,}  diff: {grand_total - grand_target:>+7,} ({(grand_total - grand_target) / grand_target * 100:+.1f}%)")
