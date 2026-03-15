#!/usr/bin/env python3
"""
Budget calculator for Book 5 treasure allocation.
Party of 5 PCs, levels 13, 14, and first half of 15.

Tracks both GP totals AND item-level slot requirements.

Budget targets (from 2e treasure-by-level table, adjusted for 5 PCs):
  Level 13: 26,500 gp — permanents: 14th x2, 13th x3 | consumables: 14th x3, 13th x3, 12th x2 | currency: 7,500 gp
  Level 14: 38,750 gp — permanents: 15th x2, 14th x3 | consumables: 15th x3, 14th x3, 13th x2 | currency: 11,250 gp
  Level 15.5: 28,875 gp — permanents: 16th x1, 15th x2 | consumables: 16th x1, 15th x2, 14th x1 | currency: 8,125 gp
"""

# (name, item_level, gp_value)
Item = tuple[str, int, int]


def print_budget(
    label: str,
    target_gp: int,
    target_perm_slots: dict[int, int],  # {item_level: count}
    target_cons_slots: dict[int, int],
    target_currency: int,
    permanents: list[Item],
    extra_permanents: list[Item],
    consumables: list[Item],
    currency: list[tuple[str, int]],
):
    perm_total = sum(v for _, _, v in permanents)
    extra_total = sum(v for _, _, v in extra_permanents)
    cons_total = sum(v for _, _, v in consumables)
    curr_total = sum(v for _, v in currency)
    total = perm_total + extra_total + cons_total + curr_total

    print(f"\n{'=' * 70}")
    print(f"  {label}")
    print(f"{'=' * 70}")

    # --- Permanent items ---
    print(f"\n  Permanent Items:")
    for name, lvl, val in permanents:
        print(f"    L{lvl:<3d} {name:48s} {val:>8,} gp")
    print(f"    {'':52s} --------")
    print(f"    {'Subtotal':52s} {perm_total:>8,} gp")

    # Slot check
    print(f"\n  Permanent Slot Check (target → actual):")
    perm_levels = {}
    for _, lvl, _ in permanents:
        perm_levels[lvl] = perm_levels.get(lvl, 0) + 1
    all_levels = sorted(set(list(target_perm_slots.keys()) + list(perm_levels.keys())), reverse=True)
    for lvl in all_levels:
        target = target_perm_slots.get(lvl, 0)
        actual = perm_levels.get(lvl, 0)
        status = "✓" if actual >= target else f"✗ (need {target - actual} more)"
        if actual > target:
            status = f"⚠ (+{actual - target} extra)"
        print(f"    L{lvl}: {target} needed, {actual} allocated  {status}")

    # --- Extra permanents ---
    if extra_permanents:
        print(f"\n  Extra Permanent Items (above slot count):")
        for name, lvl, val in extra_permanents:
            print(f"    L{lvl:<3d} {name:48s} {val:>8,} gp")
        print(f"    {'':52s} --------")
        print(f"    {'Subtotal':52s} {extra_total:>8,} gp")

    # --- Consumables ---
    print(f"\n  Consumables:")
    for name, lvl, val in consumables:
        print(f"    L{lvl:<3d} {name:48s} {val:>8,} gp")
    print(f"    {'':52s} --------")
    print(f"    {'Subtotal':52s} {cons_total:>8,} gp")

    # Consumable slot check
    print(f"\n  Consumable Slot Check (target → actual):")
    cons_levels = {}
    for _, lvl, _ in consumables:
        cons_levels[lvl] = cons_levels.get(lvl, 0) + 1
    all_cons_levels = sorted(set(list(target_cons_slots.keys()) + list(cons_levels.keys())), reverse=True)
    for lvl in all_cons_levels:
        target = target_cons_slots.get(lvl, 0)
        actual = cons_levels.get(lvl, 0)
        status = "✓" if actual >= target else f"✗ (need {target - actual} more)"
        if actual > target:
            status = f"⚠ (+{actual - target} extra)"
        print(f"    L{lvl}: {target} needed, {actual} allocated  {status}")

    # --- Currency ---
    print(f"\n  Currency & Below-Level Items:")
    for name, val in currency:
        print(f"    {name:52s} {val:>8,} gp")
    print(f"    {'':52s} --------")
    print(f"    {'Subtotal':52s} {curr_total:>8,} gp")
    curr_diff = curr_total - target_currency
    print(f"    {'Target':52s} {target_currency:>8,} gp")
    print(f"    {'Difference':52s} {curr_diff:>+8,} gp")

    # --- Totals ---
    diff = total - target_gp
    pct = diff / target_gp * 100
    print(f"\n  {'TOTAL':52s} {total:>8,} gp")
    print(f"  {'Target':52s} {target_gp:>8,} gp")
    print(f"  {'Difference':52s} {diff:>+8,} gp ({pct:+.1f}%)")

    return total, target_gp


# ============================================================
# LEVEL 13: Parts 1-2 (The Scribbler + Dragon Hoard)
# ============================================================
t13 = print_budget(
    "LEVEL 13 (Parts 1-2)",
    target_gp=26_500,
    target_perm_slots={14: 2, 13: 3},
    target_cons_slots={14: 3, 13: 3, 12: 2},
    target_currency=7_500,
    permanents=[
        ("Fanged Falchion", 14, 4500),
        ("Wand of Crackling Lightning 3rd-rank", 14, 4500),
        ("Wand of Shardstorm 3rd-rank", 13, 3000),
        ("+2 greater striking runestone", 12, 2000),
        ("+2 resilient breastplate (Scribbler)", 11, 1400),
    ],
    extra_permanents=[],
    consumables=[
        ("Potion of Cold Resistance Greater x2", 14, 1350),
        ("Antidote Major", 14, 675),
        ("Potion of Fire Resistance Greater", 14, 675),
        ("Scroll Dispelling Globe rank 7", 13, 600),
        ("Scroll Heal rank 7", 13, 600),
        ("Elixir of Life Greater", 13, 600),
        ("Healing Potion Greater x2", 12, 800),
        ("Oil of Animation", 12, 330),
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
    ],
)


# ============================================================
# LEVEL 14: Parts 3-8 (Runeforge wings)
# ============================================================
t14 = print_budget(
    "LEVEL 14 (Parts 3-8)",
    target_gp=38_750,
    target_perm_slots={15: 2, 14: 3},
    target_cons_slots={15: 3, 14: 3, 13: 2},
    target_currency=11_250,
    permanents=[
        ("Robe of the Archmagi black", 15, 6500),
        ("Rod of Negation", 14, 4300),
        ("Staff of Hungry Shadows", 14, 4500),
        ("Staff of Mithral Might", 14, 4500),
        ("Sadist's Lash", 14, 4500),
    ],
    extra_permanents=[
        ("+2 GS keen wounding dagger (Xyoddin)", 14, 4500),
        ("+2 resilient glamered dawnsilver chain shirt", 14, 3140),
        ("Golem Stylus", 13, 3000),
    ],
    consumables=[
        ("Scroll Teleport rank 8 (J5)", 15, 1300),
        ("Elixir of Life Major (J5)", 15, 1300),
        ("Potion of Flying Greater (Vraxeris)", 15, 1300),
        ("Antiplague Major (E4)", 14, 675),
        ("Potion of Resistance Greater x2 (Azaven)", 14, 1350),
        ("Antidote Major (Delvahine)", 14, 675),
        ("Scroll Interplanar Teleport rank 7 (F4)", 13, 600),
        ("Scroll Interplanar Teleport rank 7 (F4)", 13, 600),
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
        ("Masquerade Scarf Greater (half)", 100),
        # Part 8: Festering Maze
        ("Spacious Pouch J3 (half)", 150),
        ("Staff of Summoning Greater (half)", 450),
        ("Diamond dust J5", 50),
        ("Ivory plaque", 5),
        ("Silver mirror", 100),
        ("Immovable Rods x2 (half)", 600),
    ],
)


# ============================================================
# LEVEL 15.5: Parts 9-10 (Halls of Wrath + Weapons of Power)
# ============================================================
t15 = print_budget(
    "LEVEL 15.5 (Parts 9-10)",
    target_gp=28_875,
    target_perm_slots={16: 1, 15: 2},
    target_cons_slots={16: 1, 15: 2, 14: 1},
    target_currency=8_125,
    permanents=[
        ("+3 GS flaming adamantine ranseur (Athroxis)", 16, 11900),
        ("+2 GR dawnsilver breastplate (Athroxis)", 15, 6100),
        ("Wand of Crackling Lightning 5th-rank", 15, 4500),
    ],
    extra_permanents=[
        ("Ring of Wizardry Type IV", 14, 4000),
    ],
    consumables=[
        ("Phoenix Cinder (golem eye)", 16, 1800),
        ("Scroll Howling Blizzard rank 8 (Athroxis)", 15, 1300),
        ("Elixir of Life Major (Athroxis)", 15, 1300),
        ("Potion of Resistance Greater (K3)", 14, 675),
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
print(f"\n{'=' * 70}")
print(f"  GRAND TOTAL")
print(f"{'=' * 70}")
grand_total = t13[0] + t14[0] + t15[0]
grand_target = t13[1] + t14[1] + t15[1]
for label, (total, target) in [("Level 13", t13), ("Level 14", t14), ("Level 15.5", t15)]:
    diff = total - target
    pct = diff / target * 100
    print(f"  {label:15s}  total: {total:>8,}  target: {target:>8,}  diff: {diff:>+7,} ({pct:+.1f}%)")
diff = grand_total - grand_target
pct = diff / grand_target * 100
print(f"  {'Grand':15s}  total: {grand_total:>8,}  target: {grand_target:>8,}  diff: {diff:>+7,} ({pct:+.1f}%)")
print()
print("  Note: Level 14 intentionally exceeds budget. Runeforge is a")
print("  megadungeon with 7 wings, each with a boss carrying signature")
print("  permanent items. The party won't use all of them.")
