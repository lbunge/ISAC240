from itertools import permutations
import monoalphabeticCipher, detectEnglish

LETTERS = 'abcdefghijklmnopqrstuvwxyz'

def bruteForce(message):
    knownPortion = 'edbwvutsrqponml'
    unknownPortion = 'afghijkxyz'
    perm = permutations(unknownPortion)

    for key in list(perm):
        keyChange = ''.join(key)
        testKey = knownPortion + keyChange
        output = monoalphabeticCipher.decrypt(message, testKey)
        if detectEnglish.isEnglish(output):
            print('Key:', testKey, output)



message = 'Htwn ham lesji mv Vjwnctown elljmectwb htw cjsosnepi enb eh htw mvvscwji cmooenb hmmq htw ham cmnfschi atm ihmmb vsjih sn htw jma Htw cmnfschi ihmllwb atwn htwy jwectwb htw lmih enb atspw iecqi awjw dwsnu djmguth pmmqwb bgodpy ejmgnb ei e amgnbwb dweih pmmqi eh en elljmectsnu tgnhioen Mnw cjmiiwb tsoiwpv cmnhsngeppy htw mhtwj icjehctwb tsi decq enb oebw e omfwownh mv htw psli jwiwodpsnu e iospw Asht tgjjswb tenbi htw impbswji dpsnbvmpbwb htwo bjeasnu htw iecqi mfwj htwsj twebi enb dmgnb htwo hm htw lmih Hawpfw itejlitmmhwji asht ogiqwhi ihwllwb mgh mv htw jenqi asht e vsjo jwugpej hjweb enb tephwb wsuth lecwi vjmo htw lmih Lswjjw hgjnwb eaey hm efmsb iwwsnu ateh aei umsnu hm tellwn Igbbwnpy e cjecqpsnu jmppsnu nmsiw aei twejb atsct iwwowb hm tso pmgbwj hten htw omih hwjjsvsc htgnbwj enb tw pmmqwb jmgnb Htwjw aei imow iomqw enb htw Vjwnctown awjw bmsnu imowhtsnu nwej htw lsh asht lepw vecwi enb hjwodpsnu tenbi Ham omjw ljsimnwji awjw pwb gl Sn htw ieow aey enb asht isospej pmmqi htwiw ham upencwb fesnpy eh htw mnpmmqwji asht mnpy e ispwnh ellwep vmj ljmhwchsmn sn htwsj wywi wfsbwnhpy gnedpw hm gnbwjihenb mj dwpswfw ateh aei umsnu hm tellwn hm htwo Htwy cmgpb nmh dwpswfw sh dwcegiw htwy epmnw qnwa ateh htwsj psvw owenh hm htwo enb im htwy nwshtwj gnbwjihmmb nmj dwpswfwb hteh sh cmgpb dw heqwn vjmo htwo Euesn Lswjjw bsb nmh asit hm pmmq enb euesn hgjnwb eaey dgh euesn htw imgnb ei mv e vjsuthvgp wzlpmismn ihjgcq tsi wej enb eh htw ieow omownh tw iea iomqw dpmmb enb htw lepw icejwb vecwi mv htw Vjwnctown atm awjw euesn bmsnu imowhtsnu dy htw lmih htwsj hjwodpsnu tenbi solwbsnu mnw enmhtwj Lswjjw djwehtsnu twefspy pmmqwb ejmgnb ei sv eiqsnu ateh sh owenh Htw ieow kgwihsmn aei wzljwiiwb sn epp htw pmmqi hteh owh tsi Mn htw vecwi mv epp htw Jgiiseni enb mv htw Vjwnct impbswji enb mvvscwji ashtmgh wzcwlhsmn tw jweb htw ieow bsioey tmjjmj enb cmnvpsch hteh awjw sn tsi man twejh Dgh atm evhwj epp si bmsnu htsi Htwy ejw epp igvvwjsnu ei S eo Atm htwn si sh Atm vpeitwb vmj en snihenh htjmgut tsi osnb'
print(bruteForce(message))