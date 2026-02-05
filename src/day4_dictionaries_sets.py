# -*- coding: utf-8 -*-
"""
Created on Thu Feb  5 10:56:36 2026

@author: divya
"""

# ---------- 1) Digital Rolodex ----------
contacts = {"Alice":"1234567890","Bob":"9876543210","Charlie":"5555555555"}
contacts["David"]="1112223333"; contacts["Alice"]="9998887777"
print("=== Rolodex ===\nBob:",contacts.get("Bob"),"\nEve:",contacts.get("Eve","Contact not found"))
for n,p in contacts.items(): print(f"{n} -> {p}")

# ---------- 2) Unique Visitors ----------
logs=["ID01","ID02","ID01","ID05","ID02","ID08","ID01"]; unique=set(logs)
print("\n=== Unique Visitors ===\nID05 in unique?", "Yes" if "ID05" in unique else "No")
print(f"Total logs: {len(logs)} | Unique: {len(unique)}\nIDs:", unique)

# ---------- 3) Friend Interests ----------
a={"Python","Cooking","Hiking","Movies"}; b={"Hiking","Gaming","Photography","Python"}
print("\n=== Friend Interests ===\nShared:",a&b,"| All:",a|b,"| Unique to A:",a-b)
