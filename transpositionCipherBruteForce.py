import math
import transpositionCipher, detectEnglish


def main():
    myMessage = """Wn ttuefoayt r grhduue safsotqeFhee nddmsi tuoudr dngde yirbirni eM  ee o o el  ctnottnrfbfnoiysakhcshhusotr nn enlehceeitruio girdy  o  na seft nv  dawcFensen hitialin,arldandhenecnind peyivesi  re kn htn nishsstr.oeeheacggnsi ehu m ra ihr g pfvepYea dln ah t.ae tol w e otoho cnaeuehibfsfewi Aetmd tetettff se  hb b ahe iiua vFa uhehl ntlclnlernolilatp hle yiredfamodhlge rtofyn  n.n yei m onetciSc gb avkow e.hhnee" easevreP  im p OtenunaenicHnahtwhondr s teoagniei,   easl rud  smt tsh.  iirl on bhpheu stvnedttege lernMpoet  hhverte vgoe lofdiees,hagerrcMy oesrrt"asedyeio trc   u ten  larah lmtfrh !tam,lenesiahoeem"rna  ld annars a ydntn  rve ng,ins? ,haahoi b e nia"a emneonsehtttai  m ed mgoeishrcdhsuo. c   nm ao' eanr ahwhf setdsh mcdTpaiileei u ecohehpttsanltPcb.ovirelth tdfhieu nanlyie lto eedl"crgy edPiewdrr lIl  ,cd ifrei rhe uah a ieeidsaeitudniblhnr n an,m nedsrlicrtgwr  sidd  oemeeh imiuene vfudss aatennl rwoog esttnhdscfmsidohilah    uo,yttkdttfnePatPln  aha    t iphitsabn  rsltllepee c odabaoioyare roisd  rpmm  trlsrroeyysoieotatelle ul?ohud nhle ai.asf"uaglhaelrhtg  l- rdhyod   aih'sysP et tebtadotAe air ,w  ohg ne rsteeo iwdtran,sFvmirafwtaetoio triisrs iht lunts eclfeoit eceg  hcneii nnhhro httrac.nersq i co hhuph gde.ussihfdoegamI  p io no iu gca iilYrms nBngheinonrioyeta onhedt f reu  r (reta yofred iwospdr rh reep aninaie.itif rsrtr ngugat soa pehehe c'u t r yosa i tesxhos Ronstaswep .i hpuusi n heal sroes ebh titneH eursm leooch medflciyte fnh,ao uudea o cfe  nnwtseinf soi.tcdaryerv rtmuc ho da ,sipihilePenpept  nreeldri tl)poaagin e .eFia,e nn ndF n.rrnc daddtcsrpo.reuea s  heheut enadntssse inc a cl dhuaa ipckt bhla ertifn.heese y M e dec mrlunh bob d eoTailptasorohotlghnn e dmtetiwhina'ghrh atltmnanits iiitcl l  tgt  hmosakesetw soisi r ki p hii ,smsh henoouatfo" i ioengfkpth f allsfa   e   P slei fdfhc thhioal,pni.rilwoeieti  sac osae  mrhdIp me"m rliw re  ruerY leltaiertcen  oait ssn shasdapu p o   a,ensenerRsifnntb   erdr u,n eohsaosd ,hbs  tcteonfa h aasaihk  ldfytibppinte Fpu i.hslstad. irathc"e u.in  lnereae  ms s rHi nlldrThuhYmceemacoy ,hasioaep o hr h entnulleant -ielrdag  lalaaa n oe c,hnatsdbntsao hh aarioeldhitkweebvm n  e es ial.eeeagbd w tansd g ,n-renifelg  "ab d o asidl soWnoi "ucphr  aoui rfbEgokesout tltn rxhcidtnn m loeyocthn   dPut   oue o trpeicoytauglanaooareh orr hl  n ossr huymptebhdgmstrgi  sl noe o ioeomnt ewtt p tno'o.ooaai!thoahgdsd w gst lauwe    " iaehDedrayfwfnCbni. e  ey ohiaaevn tlofd,erantp esThifo  n teutsnthec uobta  raot amiknuue Ptei  ut,ovdttrRih ngas  ua   eueoa o .iRssiwtdsrunRon sa!snih.srgdadaT m", ne ieh m mhab  te Ta' nbaealaHth oonsdoas tlliaeff   ibl a' lsk ofPlfriltnsIe ekriieetleod   fni ceteyi,  naia ther l t ttosncfcirriilyoeotkverhm etni fl  .i oesw' gn( lsm tgmneosbseit ayMer .lu e nnhmy odet fla w  ee bn whB dsseat  susP eua sornh1wosiir tnnu,ede3imieeek dor ,  ttenurdia tab aFhhterr tsf nuttr  hs eac ohcth eLwisP nhtree etnihn.itdeh asf hcgog eo nePr olehhm Ir w  i tra  t a rsafceoh trs IboehsoarfaatieR ow,a rpr tlennehue rc tei lrgsgat yeota.th   eiv yo vhi .etwo mehouheenT  honoe iu irm hHwau fnts sse heeatlh th ma dta  s dit,eryyd odsw h sh  e .iw  aanep eChal.nitttso rf hosi.ntrhi twoiwenof.ehyess obnovone r . foauagrar .T,p wa  lbedl f h eTicvFdlr)iooTaarhnter y. efrhtnsaeireb  ir  a'dpt oyneh"n ccts i tn c aI ooo  hrbh phfv tfnniaiaeeoomoeoh vcslmtvyflar wetee lsie  inele hrae eorhht,ve oeslnIlnaaie efmf iio f.gds,trtyfLnnuw  e   h   iegggabP thaebhlcg  hneiwaum oiieisi tgeaknicumfrootf arsegaan,e'n ,otnr nebpd  s p ro ea rlt bt olb  t lw eatuovfeumkowrha,iot o aten aein n  yiHs .oesaldg,Ptocoat wa de o ihuennhI.thy toeee ,ote " u phdvr a rl a gnkae-irmni yFmWrgns ndeadnf,r heroswae n  o eqeeywiitnb'otrinund nnnutysfh nci ia gerl  fetshttlnt  eygae htmehydotrd rnreeea e   he,nai x ana astrn otmypad tmnhhodatiaorf h udaeue"""
    myKey = 15

    # plaintext = transpositionDecrypt.decryptMessage(myMessage, myKey)
    # print(plaintext + "|")

    hackedMessage = bruteForce(myMessage)

    if hackedMessage == None:
        print('Failed to hack encryption.')
    else:
        print(hackedMessage)

def bruteForce(cipherText):
    print('Hacking the Gibson...')

    for key in range(1, len(cipherText)):
        print('Trying key #%s...' % (key))

        decryptedText = transpositionCipher.decrypt(cipherText, key)

        if detectEnglish.isEnglish(decryptedText):
            # Ask user if this is the correct decryption.
            print()
            print('Possible encryption hack:')
            print('Key %s: %s' % (key, decryptedText[:100]))
            print()
            print('Enter D if done, anything else to continue hacking:')
            response = input('> ')

            if response.strip().upper().startswith('D'):
                return decryptedText

    return None


if __name__ == '__main__':
    main()