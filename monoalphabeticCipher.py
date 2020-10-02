KEY1 = 'nmlkjihgfedcbazyxwvutsrqpo'
KEY2 = 'zyxwvutsrqponmlkjihgfedcba'
LETTERS = 'abcdefghijklmnopqrstuvwxyz'

def validateKey (key):
    if len(key) != 26:
        return 'invalidkeylength'
    sortedkey = ''.join(sorted(key))

    if sortedkey != LETTERS:
        return 'invalidkey'
    return True

def monoalphabetic(key, message, mode):
    letters = LETTERS

    if mode == 'decrypt':
        key, letters = letters, key

    if validateKey(key):
        output = ''
        for i in message:
            iindex = letters.find(i)
            output += key[iindex]

    return output

message = "The glow of the first fire that began on the second of September was watched from the various roads by the fugitive Muscovites and by the retreating troops, with many different feelings. The Rostov party spent the night at Mytishchi, fourteen miles from Moscow. They had started so late on the first of September, the road had been so blocked by vehicles and troops, so many things had been forgotten for which servants were sent back, that they had decided to spend that night at a place three miles out of Moscow. The next morning they woke late and were again delayed so often that they only got as far as Great Mytishchi. At ten o'clock that evening the Rostov family and the wounded traveling with them were all distributed in the yards and huts of that large village. The Rostovs' servants and coachmen and the orderlies of the wounded officers, after attending to their masters, had supper, fed the horses, and came out into the porches. In a neighboring hut lay Raevski's adjutant with a fractured wrist. The awful pain he suffered made him moan incessantly and piteously, and his moaning sounded terrible in the darkness of the autumn night. He had spent the first night in the same yard as the Rostovs. The countess said she had been unable to close her eyes on account of his moaning, and at Mytishchi she moved into a worse hut simply to be farther away from the wounded man. In the darkness of the night one of the servants noticed, above the high body of a coach standing before the porch, the small glow of another fire. One glow had long been visible and everybody knew that it was Little Mytishchi burning- set on fire by Mamonov's Cossacks"
message2 = '''Rg dzh kozrm gszg o'znlfi dsrxs gsv Uivmxsnzm dzh hl ulmw lu dzh mlg gszg old zmw hrnkov prmw gszg Krviiv szw lmxv uvog uli srh druv, mli dzh rg gsv ilnzmgrx olev hgrnfozgvw yb srnhvou gszg sv vckvirvmxvw uli Mzgzhsz. (Iznyzoov wvhkrhvw ylgs gsvhv prmwh lu olev vjfzoob: gsv lmv sv xlmhrwvivw gsv "olev lu xolwslkkvih" zmw gsv lgsvi gsv "olev lu hrnkovglmh.") O'znlfi dsrxs gsv Uivmxsnzm dlihsrkvw xlmhrhgvw kirmxrkzoob rm gsv fmmzgfizomvhh lu srh ivozgrlm gl gsv dlnzm zmw rm z xlnyrmzgrlm lu rmxlmtifrgrvh trermt gsv xsrvu xszin gl gsv uvvormt. Gsfh gsv xzkgzrm glfxsrmtob ivxlfmgvw gsv hglib lu srh olev uli z uzhxrmzgrmt nzijfrhv lu gsrigb-urev zmw zg gsv hznv grnv uli z xszinrmt, rmmlxvmg xsrow lu hvevmgvvm, wzftsgvi lu gsv yvdrgxsrmt nzijfrhv. Gsv xlmuorxg lu nztmzmrnrgb yvgdvvm gsv nlgsvi zmw gsv wzftsgvi, vmwrmt rm gsv nlgsvi'h hzxirurxrmt svihvou zmw luuvirmt svi wzftsgvi rm nziirztv gl svi olevi, vevm mld ztrgzgvw gsv xzkgzrm, gslfts rg dzh gsv nvnlib lu z wrhgzmg kzhg. Gsvm sv ivxlfmgvw zm vkrhlwv rm dsrxs gsv sfhyzmw kozbvw gsv kzig lu gsv olevi, zmw sv- gsv olevi- zhhfnvw gsv ilov lu gsv sfhyzmw, zh dvoo zh hvevizo wiloo rmxrwvmgh uiln srh ivxloovxgrlmh lu Tvinzmb, dsviv "hsvogvi" rh xzoovw Fmgvipfmug zmw dsviv gsv sfhyzmwh vzg hzfvipizfg zmw gsv blfmt trioh ziv "gll yolmwv."'''

print(monoalphabetic(KEY1, message, "encrypt"))
#print(monoalphabetic(KEY2, message2, "decrypt"))
