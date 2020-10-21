ALPHABET = "abcdefghijklmnopqrstuvwxyz"

def main():
    key = "SMART"
    message1 = """When he returned to the room Pierre was sitting in the same place as before, with his head in his hands. His face expressed suffering. He really was suffering at that moment. When the captain went out and he was left alone, suddenly he came to himself and realized the position he was in. It was not that Moscow had been taken or that the happy conquerors were masters in it and were patronizing him. Painful as that was it was not that which tormented Pierre at the moment. He was tormented by the consciousness of his own weakness. The few glasses of wine he had drunk and the conversation with this good-natured man had destroyed the mood of concentrated gloom in which he had spent the last few days and which was essential for the execution of his design. The pistol, dagger, and peasant coat were ready. Napoleon was to enter the town next day. Pierre still considered that it would be a useful and worthy action to slay the evildoer, but now he felt that he would not do it. He did not know why, but he felt a foreboding that he would not carry out his intention. He struggled against the confession of his weakness but dimly felt that he could not overcome it and that his former gloomy frame of mind, concerning vengeance, killing, and self-sacrifice, had been dispersed like dust by contact with the first man he met"""
    message2 = '''Otee aw deknjzeu mg fhv kgam Gbwdrv pse szmlunx bf fhv lsye gesoe rl tqffkw, iika zus yxsp ie aae hrgve. Hzl xmcv xpbrvlkqd jnxreibfs. Hv kwmlcr oms jnxreibfs ak mzmt dheqnk. Pzqn kaw oagmsun nxff olm szd yx oms cxxf achfq, slwvqncr zq crfw fo ybeeecy szd ixsxiqxv fhv igeikbgz hv pse ie. Bl iaj ggf tytl Yojvgi hrw tqee mswee hj fhrm lte ythby thfcuvkgds nxjq mrllqrj bf ut rgv ieix hmtihfuzzgy tid. Isunwnd ms kasf wrl af wrl fat kasf wybut tfkeqnkxv Bivkjq ak mzq mffwzt. Yx oms khjyeemwp bp mzq cfgkoifnkzejl gr hzl gin nxswnvlk. Fhv ywi gctkeej hx iiex zq hrw vdued szd kaw ooeowdsrmaan nblt tybk sofw-fmtlkwp mrg zmd uxkfrfrwp tyx eaou hx ooevwztitlqd xegam zg otita zq hrw kbeem lte ctkf fvp vmyj tfp wybut wrl wesvgluac ygd tyx wjetnluoe hx tij wweixg. Lte gbkfoc, wssgvk, szd gxseaem uaak pwde ixspy. Ethalvhf iaj mg qnkxj fhv mgin expf drr. Hueikw etzed ooelapeixv fhrm af wfndp bv t meewnd mnu pgdtyr sotzhf fo jesk tyx whicwgqr, snl zon aw recm ltak aw iolev zok wg ut. Yx vud ehl wnfp oty, snl te wxdf a whjqbfwazg kasf hv pgglu ggf crkjk olm zus zglqnkbgz. Hv llduxzdqd rzsunjm lte thfrejlaan fy zus nxswnvlk nuk waylp ywxt kasf hv vgglu ggf omxjoodx af aew ltak aae ffkeqr xegamp yjmmv hx yiew, uantxjziez nqnxxszcv, daxlzgy, mnu lwxf-jtudiwbuq, hrw tqee waepvkkqd cbcq dlll ny thffatm outy mzq fzkkf mrg zq mvm'''

    ### TESTS ###
    # print(vigenere(key, message1))
    # print(vigenere(key, message2, 'd'))


def keytoIndex(key):
    output = []

    for k in key:
        output.append(ALPHABET.find(k.lower()))

    return output


def vigenere(key, message, mode='d'):
    output = ""

    keytoIndexlists = keytoIndex(key)

    i = 0

    for m in message:
        if m.lower() not in ALPHABET:
            output += m
            continue

        mIndex = ALPHABET.find(m.lower())
        if mode == 'e':
            newIndex = (mIndex + keytoIndexlists[i]) % len(ALPHABET)
        else:
            newIndex = (mIndex - keytoIndexlists[i]) % len(ALPHABET)
        if m.isupper():
            output += ALPHABET[newIndex].upper()
        else:
            output += ALPHABET[newIndex].lower()

        i = (i + 1) % len(key)

    return output


# If program is not called via a function, then start at main function
if __name__ == '__main__':
    main()

