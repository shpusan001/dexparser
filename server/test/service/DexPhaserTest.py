from util.Dexparser.DictDexParser import *
import pprint
import unittest
import os
import sys
import time
sys.path.append('./')


class TestInit(unittest.TestCase):
    def __init__(self, methodName: str = ...) -> None:
        super().__init__(methodName)
        self.stime = 0
        self.etime = 0

    def setUp(self) -> None:
        self.stime = time.time()
        return super().setUp()

    def tearDown(self) -> None:
        self.etime = time.time()
        print("Time:", self.etime - self.stime)
        return super().tearDown()


# class DexParserTest_getHeader(TestInit):
#     def test_runs(self):
#         dexPaser = DexPaser()
#         dexPaser.setFile("./src/res/", "classes.dex")
#         res = dexPaser.getHeader()


# class DexParserTest_getStringFull(TestInit):
#     def test_runs(self):
#         dexPaser = DexPaser()
#         dexPaser.setFile("./src/res/", "classes.dex")
#         res = dexPaser.getStringFull()


# class DexParserTest_getTypeFull(TestInit):
#     def test_runs(self):
#         dexPaser = DexPaser()
#         dexPaser.setFile("./src/res/", "classes.dex")
#         res = dexPaser.getTypeFull()


# class DexParserTest_getProtoIds(TestInit):
#     def test_runs(self):
#         dexPaser = DexPaser()
#         dexPaser.setFile("./src/res/", "classes.dex")
#         res = dexPaser.getProtoIds()

# class DexParserTest_getProtoFull(TestInit):
#     def test_runs(self):
#         dexPaser = DexPaser()
#         dexPaser.setFile("./src/res/", "classes.dex")
#         res = dexPaser.getProtoFull()


# class DexParserTest_getFieldFull(TestInit):
#     def test_runs(self):
#         dexPaser = DexPaser()
#         dexPaser.setFile("./src/res/", "classes.dex")
#         res = dexPaser.getFieldFull()


# class DexParserTest_getMethodIds(TestInit):
#     def test_runs(self):
#         dexPaser = DexPaser()
#         dexPaser.setFile("./src/res/", "classes.dex")
#         res = dexPaser.getMethodIds()


# class DexParserTest_getMethodFull(TestInit):
#     def test_runs(self):
#         dexPaser = DexPaser()
#         dexPaser.setFile("./src/res/", "classes.dex")
#         res = dexPaser.getMethodFull()
#         pprint(res)

# class DexParserTest_getClassFull(TestInit):
#     def test_runs(self):
#         dexPaser = DexPaser()
#         dexPaser.setFile("./src/res/", "classes.dex")
#         res = dexPaser.getClassFull("11")

# class DexDecompiler_disassemble(TestInit):
#     def test_runs(self):
#         hexcode = "13001a00120338242e0060015c073401060013001c0037010e0063001200380022001300150034011e0013001c0036011a00131d01001a027903081f220077011d001f00221e38037601f50a1e001a009010080421006e20160004000c0612072804131d000028e81a015f092200be027030840960012205af02702044090500120c6e10450905000c093809ae001a006b006e202b0a09000a001a0a4a04121b380021001a0054136e302c0a090b0a0038000f00130115006e10250a09000a00350161006e202d0a19000c0728db1a01490423b0ba034d09000371303204120028d11a0006006e202a0a09000c082181123033015d00460108034600080b22080b0070401e001870548103001a006e006e20140a01000a0038001f005480050039001b001a00910e7110470a00000c0138011f001a00a3006e202b0a01000a00390017001a009f006e202b0a01000a0039000f0028971a0072006e20140a01000a0038000c00548005003900080008001e006e20e10a80002885390c2e00121c28f72200f9027010380a00006e20400aa0006e20400a90006e10f60900000c002201c40070203a020100281d2200f9027010380a00006e20400aa0006e20400a90006e10f60900000c002201c40070203a02010028081a0074082201c40070203a020100270171101b00060071101b0005007401e40a1e000a0038000a002331ba031a00b7087130320402010e001a1c7d0c2205b50208011c0008001f007030510905012219db010800190070304505500371004c0a00000b0068000800221b38037601f50a1b007401e50a1e000c1a120578011c0b1a000a003800660478011d0b1a000c091f090b002206f9027010380a06001a08f6116e20400a8600549004006e20400a06001a016e006e20400a16006e10f60906000c072206b50208001f007030510906076e10570906000a003900dc0139038000220b38037010f50a0b007401e50a1e000c0a72101c0b0a000a0038002e0072101d0b0a000c001f000b002203f9027010380a03006e20400a8300540004006e20400a03006e20400a13006e10f60903000c0713002e006e20220a07000a0312f03203070012006e302e0a07030c076e20e10a7b0028cf74015a091f000c006e10660900000c0a1208390a0a002383ba031a00ee03713031040203283021a735782e00460d0a086e105c090d000c0308001c006e20150a03000a0039001d006e105c090d000c0c13002e006e20220a0c000a0312f03203070012006e302e0a0c030c0c6e20e30acb000a003900050071101c000d00d808080128d31213220043037010150b00006900090071004c0a00000b0768070600549b030054980500380825001a0029136e20150a80000a0038000b001a0b4a131a14f30c71004c0a00000b12281e2207f9027010380a07001a0049136e20400a07006e20400a87006e10f60907000c0b28e81a007f006e20140a0b000a003800e1ff1a0bb51228dd1a087c132207b50208001f007030510907081a0a291312186a080a006e20140a1b000a0038001e005449010039091100544002006e10210600000c005400480722097c037020970b09005b4901006e209a0bb9000c006e209b0b09000c0928056e201600b4000c091a007a006e20140a0b000a001a0db50b38000b007110a2080a000a007130c208a9000c1128131a0078006e20140a0b000a0038000e001a0af1137110a2080a000a007130c208a9000c1107dc282b1a007e006e20140a0b000a0039000e001a007d006e20140a0b000a00390006000811090007bc28172211a8020800110070203109900007bc13002e006e20220a0b000a0912f03209070012006e302e0a0b090c0c1a0072006e20140a0c000a00120938002b00220a7d030800110070209c0b0a006e109d0b0a000c003800e8016e10940b00006e10940b00000c006e20150ad0000a003800efff13002e006e20220a0c000a0d12f0320d06006e302e0a9c0d0c0c08110a006e20140a1c000a00380052022210ba0208001000702073097000140effffff7f140d0080000023dc9103120b91000e0b7120ea090d000a0f120a35fa150091000f0a080111006e408109c10a0a013b0103002803b01a28f212f033010500390a0300280d12f0320a0b00080010006e408e09c0a9b0ab35eb030028d977011b00100077011b0011006209f80771004c0a00000b009c0000126e306c0b09010b00620809007120e70910000c01080014007230390b08016e206a0967000a0038009601280c6e105b0906007401260620000c006e105b090000281771004c0a00000b0061070600bc706e306c0b09010b00620709007120e70910000c011a0090137230390b07011c0009006e10bc0900000c1822010d0070101f00010022000e0070102200000022080f00704024001860120c121b6e105b0906000c076e10270008000a17631612003816100060015c071300150034010a0013001c0036010600131501003817040013150000130a1a0012093815210060015c0735a1070071304009970c0c01280913001d00350114007110180007000c0138010e003917cc002900c8000d071a01f303080020007140390210b7081118006e202500c8000c0d6e105c0906000c0e2207f9027010380a0700130f2e006e20220afe000a0112f0320106006e302e0ace010c0e6e20400ae7001a0e74006e20400ae7006e10f60907000c072214b5020801140070305309d1077401630914000b12600d5c0734ad060013011c00371d0400081109006e105b0906000c072201f9027010380a0100081007006e20220af7000a0f320f06006e302e0ac70f0c10080010006e20400a01006e20400ae1006e10f60901000c010800110071302b0070010c017401630914000b0e7401640914000b106810ee0231000e12380049006a0bfa023816450013001500340d410013001c00360d3d0039153b00160e0000130764003100120e3900030028171220230eba0374015b0914000c004d000e0c7702e70910000c004d000e0b1a0040117120170ae0000c0e2816220ef9027010380a0e001a00f0026e20400a0e0074015b0914000c006e20400a0e006e10f6090e000c0e0800200071403902e0793917070035ad030028036a0bf90208001b006e20e10a1000381db8fc6e10270008000a003900b2fc39050e0060005c0734a0180008011800080020007120190010000c052201c5000800200070403b0201580800230072205f0b1000290096fc7401210620000c005405480728ec1a01f7132380ba034d0c00097120170a01000c012200bc0270207a09100027000d0008110a00290095000d0312202301ba037110e3090b000c004d0001097110e3090a000c004d0001081a00f90c71403004021327032201f9027010380a01001a0049126e20400a01006e203f0a71001a0020006e20400a01006e203f0a61001a0010006e20400a01006e10f60901000c012200bc0270207a09100027000d0a6e105f0907000c00220369027020b906030060015c071300120034010b006e10bf0603000b056e10bb0603000b03280b6e10be0603000a0081056e10ba0603000a008103bd5328031603ffff1a05f80c12202301ba034d0a01097120e70943000c004d000108713031045201270a0d0177011b00100028172201f9027010380a01001a0055106e20400a01006e20400ab1006e10f60901000c002201c40070203a02010027010d0028040d000811090077011b00110027000d036202f80771004c0a00000b009c0000126e306c0b02010b00620209007120e70910000c01080014007230390b020127030d0523b1ba034d05010c1a00f1037130310402016e10560906000a003900230023c1ba031a00dc03713031040201281a0d056204f80771004c0a00000b0261000600bc026e306c0b24030b00620209007120e70910000c011a0090137230390b020127057401e50a1b000c0272101c0b02000a003800100072101d0b02000c011f01ab027701100320000c006e201303100028ed74014605190071004c0a00000b00680007000e000d0074014605190027000d0271004c0a00000b006800070027020d0028030d00077571101b0006003805050071101b0005002700"
#         bytecode = bytes.fromhex(hexcode)
#         dexDecompiler = DexDecompiler()
#         dexDecompiler.load_bytearray(bytecode)
#         print("========================")
#         pprint(dexDecompiler.disassemble())
#         print("========================")


if __name__ == '__main__':
    unittest.main()
