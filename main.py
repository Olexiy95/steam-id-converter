def steam_64bit_to_32bit(steam_id_64bit):
    steam_id_32bit = (steam_id_64bit - 76561197960265728) & 0xFFFFFFFF
    return steam_id_32bit


steam_id_64bit = 000000000000000 # Replace with your 64 bit ID
steam_id_32bit = steam_64bit_to_32bit(steam_id_64bit)
print(steam_id_32bit)