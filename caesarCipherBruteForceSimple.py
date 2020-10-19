# Simple Caesar cipher brute force program
import caesarCipher

alphabet = 'abcdefghijklmnopqrstuvwxyz0123456789!@#$%/.'
message = '6@ $2a2/.zb/4 ya a5ya a6!2 y 0#!$960ya21 .a/b4492 dy. z26@4 0y//621 #@ d6a5 4/2ya2/ 52ya a5y@ 2c2/ 6@ a52 56452.a 06/092., z2ad22@ a52 $y/a62. #3 /b!fy@a.2c, a52 3/2@05, !y/fy 321#/#c@y, a52 A.y/2c605, y@1 #a52/., 1/#d@21 y. b.by9 zf a52 zbgg6@4 #3 a52 0#b/a 1/#@2.x Zba a52 0y9!, 9beb/6#b. 9632 #3 $2a2/.zb/4, 0#@02/@21 #@9f yz#ba $5y@a#!. y@1 /23920a6#@. #3 /2y9 9632, d2@a #@ 6@ 6a. #91 dyf y@1 !y12 6a 5y/1, 2e02$a zf y 4/2ya 233#/a, a# /2y96g2 a52 1y@42/ y@1 a52 163360b9a $#.6a6#@ #3 a52 /b..6y@ $2#$92x A52/2 d2/2 a52 .y!2 /202$a6#@. y@1 zy99., a52 .y!2 3/2@05 a52ya2/, a52 .y!2 0#b/a 6@a2/2.a. y@1 .2/c602 6@a2/2.a. y@1 6@a/64b2. y. b.by9x #@9f 6@ a52 c2/f 56452.a 06/092. d2/2 yaa2!$a. !y12 a# 822$ 6@ !6@1 a52 163360b9a62. #3 a52 y0aby9 $#.6a6#@x .a#/62. d2/2 d56.$2/21 #3 5#d 16332/2@a9f a52 ad# 2!$/2..2. z25yc21 6@ a52.2 163360b9a 06/0b!.ay@02.x A52 2!$/2.. !y/fy, 0#@02/@21 3#/ a52 d293y/2 #3 a52 05y/6ayz92 y@1 21b0ya6#@y9 6@.a6aba6#@. b@12/ 52/ $ya/#@y42, 5y1 46c2@ 16/20a6#@. a5ya a52f .5#b91 y99 z2 /2!#c21 a# 8ygy@, y@1 a52 a56@4. z29#@46@4 a# a52.2 6@.a6aba6#@. 5y1 y9/2y1f z22@ $y0821 b$x A52 2!$/2.. 296.yz2a5, 5#d2c2/, d52@ y.821 d5ya 6@.a/b0a6#@. .52 d#b91 z2 $92y.21 a# 46c2- d6a5 52/ 05y/y0a2/6.a60 /b..6y@ $ya/6#a6.! 5y1 /2$9621 a5ya .52 0#b91 46c2 @# 16/20a6#@. yz#ba .aya2 6@.a6aba6#@. 3#/ a5ya dy. a52 y33y6/ #3 a52 .#c2/264@, zba y. 3y/ y. .52 $2/.#@y99f dy. 0#@02/@21 .52 d#b91 z2 a52 9y.a a# %b6a $2a2/.zb/4x'

# Checks every key based on length of the alphabet
for key in range(len(caesarCipher.alphabet)):
    print(key, '--->', caesarCipher.caesar(message, key, 'd'))
