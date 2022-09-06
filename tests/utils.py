# -*- coding: utf-8 -*-
from pathlib import Path

TESTS_LOCATION = Path(__file__).parents[0]
TEST_FILE_DIR = TESTS_LOCATION / "files"
TEST_TEMP_FILE_DIR = TESTS_LOCATION / "files" / "temp"


TEST_271_STRING = 'ISA*00*          *00*          *ZZ*EMEDNYBAT      *ZZ*ETIN           *110101*0100*^*00501*000000001*0*T*:' \
                  '~GS*HB*EMEDNYBAT*ETIN*20110101*010000*1*X*005010X279A1~ST*271*00001*005010X279A1' \
                  '~BHT*0022*11*100270*20110101*010000~HL*1**20*1~NM1*PR*2*NYSDOH*****FI*141797357' \
                  '~PER*IC*eMedNY Provider Services*TE*8003439000*UR*www.emedny.org' \
                  '~HL*2*1*21*1~NM1*1P*2*Busy Provider*****XX*1234567891~HL*3*2*22*0' \
                  '~TRN*2*110010101000002*1141540488*274807891~NM1*IL*1*Patient Last Name*Patient First Name****MI*XX99999X' \
                  '~REF*SY*123456789~N3*123 Any Street~N4*Any Town*NY*11111~DMG*D8*10010101*M' \
                  '~DTP*472*D8*20100608~DTP*346*D8*20100601~DTP*102*D8*19940501~EB*1*IND*30**MA Eligible~MSG*35~MSG*46' \
                  '~MSG*49~MSG*95~MSG*RECERT MONTH=12~EB*B*IND*30****0~EB*1*IND*1~EB*1*IND*35~EB*1*IND*47~EB*1*IND*86~EB*1*IND*88' \
                  '~EB*N*IND*88~LS*2120~NM1*P3*2*Benefit Related Provider*****XX*1987654321~LE*2120~EB*1*IND*98~EB*1*IND*AL~EB*1*IND*MH' \
                  '~EB*1*IND*UC~EB*N*IND*CQ~LS*2120~NM1*P3*2*Benefit Related Provider*****XX*9995995661~LE*2120' \
                  '~EB*R*IND*30~REF*18*012345679C1~LS*2120~NM1*P4*2*MEDICARE ABD~LE*2120~SE*47*00001~GE*1*1~IEA*1*000000001~'
