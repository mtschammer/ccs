import unittest
import ccs
import datetime

####################################################################################################################
# POLONIEX                                                                                                        #
####################################################################################################################

class Valid(unittest.TestCase):
    def setUp(self):
        self.tz = datetime.timezone.utc
        self.json = '{"BTC_BBR":{"id":6,"last":"0.00008635","lowestAsk":"0.00008630","highestBid":"0.00008530","percentChange":"-0.01054199","baseVolume":"2.11645424","quoteVolume":"24981.30391249","isFrozen":"0","high24hr":"0.00008849","low24hr":"0.00008101"},"BTC_BCN":{"id":7,"last":"0.00000005","lowestAsk":"0.00000006","highestBid":"0.00000005","percentChange":"0.00000000","baseVolume":"0.37978404","quoteVolume":"7017786.39329961","isFrozen":"0","high24hr":"0.00000006","low24hr":"0.00000005"},"BTC_BELA":{"id":8,"last":"0.00001303","lowestAsk":"0.00001304","highestBid":"0.00001296","percentChange":"0.01086113","baseVolume":"2.38734134","quoteVolume":"185473.32707926","isFrozen":"0","high24hr":"0.00001343","low24hr":"0.00001270"},"BTC_BITS":{"id":9,"last":"0.00000666","lowestAsk":"0.00000667","highestBid":"0.00000666","percentChange":"0.05379746","baseVolume":"1.02445851","quoteVolume":"159086.24388984","isFrozen":"0","high24hr":"0.00000696","low24hr":"0.00000597"},"BTC_BLK":{"id":10,"last":"0.00003196","lowestAsk":"0.00003206","highestBid":"0.00003195","percentChange":"-0.00249687","baseVolume":"0.88219567","quoteVolume":"27558.82317330","isFrozen":"0","high24hr":"0.00003269","low24hr":"0.00003170"},"BTC_BTCD":{"id":12,"last":"0.00451834","lowestAsk":"0.00457362","highestBid":"0.00451834","percentChange":"-0.03563485","baseVolume":"3.61997463","quoteVolume":"787.94449925","isFrozen":"0","high24hr":"0.00482240","low24hr":"0.00430001"},"BTC_BTM":{"id":13,"last":"0.00010667","lowestAsk":"0.00010666","highestBid":"0.00010501","percentChange":"0.11743138","baseVolume":"18.10040020","quoteVolume":"185836.04203701","isFrozen":"0","high24hr":"0.00010895","low24hr":"0.00008818"},"BTC_BTS":{"id":14,"last":"0.00000431","lowestAsk":"0.00000431","highestBid":"0.00000430","percentChange":"-0.03363228","baseVolume":"33.80647566","quoteVolume":"7751009.21707261","isFrozen":"0","high24hr":"0.00000454","low24hr":"0.00000427"},"BTC_BURST":{"id":15,"last":"0.00000061","lowestAsk":"0.00000061","highestBid":"0.00000060","percentChange":"0.01666666","baseVolume":"4.68025771","quoteVolume":"7757340.67652101","isFrozen":"0","high24hr":"0.00000062","low24hr":"0.00000058"},"BTC_C2":{"id":16,"last":"0.00000104","lowestAsk":"0.00000105","highestBid":"0.00000104","percentChange":"-0.01886792","baseVolume":"1.04815261","quoteVolume":"1003954.16645076","isFrozen":"0","high24hr":"0.00000107","low24hr":"0.00000101"},"BTC_CLAM":{"id":20,"last":"0.00101821","lowestAsk":"0.00101820","highestBid":"0.00101221","percentChange":"0.01819981","baseVolume":"12.82409171","quoteVolume":"12581.30944441","isFrozen":"0","high24hr":"0.00107416","low24hr":"0.00098714"},"BTC_CURE":{"id":22,"last":"0.00003915","lowestAsk":"0.00003912","highestBid":"0.00003873","percentChange":"-0.00330957","baseVolume":"1.26509319","quoteVolume":"31729.42080004","isFrozen":"0","high24hr":"0.00004092","low24hr":"0.00003814"},"BTC_DASH":{"id":24,"last":"0.01650001","lowestAsk":"0.01652300","highestBid":"0.01650001","percentChange":"0.05141880","baseVolume":"711.42090333","quoteVolume":"44002.82091258","isFrozen":"0","high24hr":"0.01652370","low24hr":"0.01560054"},"BTC_DGB":{"id":25,"last":"0.00000030","lowestAsk":"0.00000031","highestBid":"0.00000030","percentChange":"-0.03225806","baseVolume":"14.73799079","quoteVolume":"47874151.51327055","isFrozen":"0","high24hr":"0.00000032","low24hr":"0.00000029"},"BTC_DOGE":{"id":27,"last":"0.00000024","lowestAsk":"0.00000024","highestBid":"0.00000023","percentChange":"0.04347826","baseVolume":"25.66215714","quoteVolume":"107706476.62933750","isFrozen":"0","high24hr":"0.00000025","low24hr":"0.00000023"},"BTC_EMC2":{"id":28,"last":"0.00000118","lowestAsk":"0.00000120","highestBid":"0.00000119","percentChange":"0.07272727","baseVolume":"0.75271627","quoteVolume":"639575.31362296","isFrozen":"0","high24hr":"0.00000120","low24hr":"0.00000113"},"BTC_FLDC":{"id":31,"last":"0.00000135","lowestAsk":"0.00000134","highestBid":"0.00000132","percentChange":"0.02272727","baseVolume":"5.03019341","quoteVolume":"3719487.72766819","isFrozen":"0","high24hr":"0.00000144","low24hr":"0.00000126"},"BTC_FLO":{"id":32,"last":"0.00000384","lowestAsk":"0.00000386","highestBid":"0.00000383","percentChange":"0.04632152","baseVolume":"1.47974167","quoteVolume":"380109.34133527","isFrozen":"0","high24hr":"0.00000405","low24hr":"0.00000376"},"BTC_GAME":{"id":38,"last":"0.00019025","lowestAsk":"0.00019025","highestBid":"0.00018961","percentChange":"-0.03082017","baseVolume":"35.89042784","quoteVolume":"186211.45131562","isFrozen":"0","high24hr":"0.00019740","low24hr":"0.00018880"},"BTC_GRC":{"id":40,"last":"0.00000603","lowestAsk":"0.00000603","highestBid":"0.00000599","percentChange":"-0.05039370","baseVolume":"1.67731366","quoteVolume":"277488.75695017","isFrozen":"0","high24hr":"0.00000649","low24hr":"0.00000599"},"BTC_HUC":{"id":43,"last":"0.00001702","lowestAsk":"0.00001720","highestBid":"0.00001701","percentChange":"0.24324324","baseVolume":"12.14608138","quoteVolume":"683538.58617888","isFrozen":"0","high24hr":"0.00001995","low24hr":"0.00001346"},"BTC_HZ":{"id":46,"last":"0.00000026","lowestAsk":"0.00000027","highestBid":"0.00000026","percentChange":"0.04000000","baseVolume":"1.81494649","quoteVolume":"6619876.77802451","isFrozen":"0","high24hr":"0.00000029","low24hr":"0.00000025"},"BTC_LTC":{"id":50,"last":"0.00429301","lowestAsk":"0.00430697","highestBid":"0.00429301","percentChange":"-0.03156814","baseVolume":"375.12727332","quoteVolume":"85758.17694889","isFrozen":"0","high24hr":"0.00447070","low24hr":"0.00426402"},"BTC_MAID":{"id":51,"last":"0.00013390","lowestAsk":"0.00013421","highestBid":"0.00013390","percentChange":"0.01385628","baseVolume":"384.37829357","quoteVolume":"2881772.44253851","isFrozen":"0","high24hr":"0.00013800","low24hr":"0.00012810"},"BTC_OMNI":{"id":58,"last":"0.00261903","lowestAsk":"0.00262146","highestBid":"0.00261903","percentChange":"0.01293713","baseVolume":"0.70550321","quoteVolume":"270.40895350","isFrozen":"0","high24hr":"0.00262146","low24hr":"0.00251265"},"BTC_MYR":{"id":59,"last":"0.00000024","lowestAsk":"0.00000025","highestBid":"0.00000023","percentChange":"-0.07692307","baseVolume":"4.16572707","quoteVolume":"16287042.80830805","isFrozen":"0","high24hr":"0.00000028","low24hr":"0.00000023"},"BTC_NAUT":{"id":60,"last":"0.00004490","lowestAsk":"0.00004500","highestBid":"0.00004490","percentChange":"0.01952770","baseVolume":"3.79830277","quoteVolume":"85267.91745584","isFrozen":"0","high24hr":"0.00004600","low24hr":"0.00004300"},"BTC_NAV":{"id":61,"last":"0.00004493","lowestAsk":"0.00004494","highestBid":"0.00004443","percentChange":"0.01905193","baseVolume":"20.79124252","quoteVolume":"467750.22508942","isFrozen":"0","high24hr":"0.00004500","low24hr":"0.00004344"},"BTC_NEOS":{"id":63,"last":"0.00007953","lowestAsk":"0.00008066","highestBid":"0.00007905","percentChange":"0.10827759","baseVolume":"4.36444448","quoteVolume":"53905.84464582","isFrozen":"0","high24hr":"0.00009202","low24hr":"0.00007072"},"BTC_NMC":{"id":64,"last":"0.00026173","lowestAsk":"0.00026195","highestBid":"0.00026173","percentChange":"0.00669256","baseVolume":"0.56752066","quoteVolume":"2167.83746283","isFrozen":"0","high24hr":"0.00026603","low24hr":"0.00025763"},"BTC_NOBL":{"id":65,"last":"0.00000008","lowestAsk":"0.00000008","highestBid":"0.00000007","percentChange":"0.00000000","baseVolume":"0.21492833","quoteVolume":"2760140.20716214","isFrozen":"0","high24hr":"0.00000008","low24hr":"0.00000007"},"BTC_NOTE":{"id":66,"last":"0.00000514","lowestAsk":"0.00000514","highestBid":"0.00000508","percentChange":"0.05761316","baseVolume":"1.28775969","quoteVolume":"257396.96274120","isFrozen":"0","high24hr":"0.00000539","low24hr":"0.00000472"},"BTC_NSR":{"id":68,"last":"0.00000019","lowestAsk":"0.00000020","highestBid":"0.00000019","percentChange":"-0.09523809","baseVolume":"2.94007444","quoteVolume":"14793309.38446928","isFrozen":"0","high24hr":"0.00000021","low24hr":"0.00000019"},"BTC_NXT":{"id":69,"last":"0.00000648","lowestAsk":"0.00000650","highestBid":"0.00000647","percentChange":"0.01408450","baseVolume":"26.38565986","quoteVolume":"4063529.76690177","isFrozen":"0","high24hr":"0.00000668","low24hr":"0.00000631"},"BTC_PINK":{"id":73,"last":"0.00000055","lowestAsk":"0.00000055","highestBid":"0.00000054","percentChange":"0.00000000","baseVolume":"1.16418388","quoteVolume":"2143985.17636690","isFrozen":"0","high24hr":"0.00000057","low24hr":"0.00000053"},"BTC_POT":{"id":74,"last":"0.00002004","lowestAsk":"0.00002020","highestBid":"0.00002004","percentChange":"-0.03930968","baseVolume":"106.89676519","quoteVolume":"5227734.63479616","isFrozen":"0","high24hr":"0.00002177","low24hr":"0.00001977"},"BTC_PPC":{"id":75,"last":"0.00032449","lowestAsk":"0.00032427","highestBid":"0.00032250","percentChange":"-0.02832759","baseVolume":"2.01045616","quoteVolume":"6139.09751135","isFrozen":"0","high24hr":"0.00033395","low24hr":"0.00032012"},"BTC_QBK":{"id":78,"last":"0.00016947","lowestAsk":"0.00016717","highestBid":"0.00016431","percentChange":"0.09004952","baseVolume":"0.67721937","quoteVolume":"4090.87434721","isFrozen":"0","high24hr":"0.00017966","low24hr":"0.00015009"},"BTC_QORA":{"id":79,"last":"0.00000008","lowestAsk":"0.00000008","highestBid":"0.00000007","percentChange":"0.00000000","baseVolume":"1.20468749","quoteVolume":"15137505.01045623","isFrozen":"0","high24hr":"0.00000009","low24hr":"0.00000007"},"BTC_QTL":{"id":80,"last":"0.00001444","lowestAsk":"0.00001449","highestBid":"0.00001444","percentChange":"0.01191310","baseVolume":"0.64093246","quoteVolume":"44109.21698551","isFrozen":"0","high24hr":"0.00001524","low24hr":"0.00001420"},"BTC_RBY":{"id":81,"last":"0.00024429","lowestAsk":"0.00024434","highestBid":"0.00024428","percentChange":"0.01432486","baseVolume":"1.89314047","quoteVolume":"7762.88796677","isFrozen":"0","high24hr":"0.00024611","low24hr":"0.00024084"},"BTC_RIC":{"id":83,"last":"0.00001144","lowestAsk":"0.00001144","highestBid":"0.00001124","percentChange":"0.07721280","baseVolume":"5.56867536","quoteVolume":"463345.05611026","isFrozen":"0","high24hr":"0.00001372","low24hr":"0.00001000"},"BTC_SDC":{"id":84,"last":"0.00180500","lowestAsk":"0.00180974","highestBid":"0.00180500","percentChange":"-0.04374407","baseVolume":"13.54575010","quoteVolume":"7532.93533821","isFrozen":"0","high24hr":"0.00188807","low24hr":"0.00175197"},"BTC_SJCX":{"id":86,"last":"0.00016954","lowestAsk":"0.00016954","highestBid":"0.00016849","percentChange":"0.18286471","baseVolume":"49.06733747","quoteVolume":"297639.28606187","isFrozen":"0","high24hr":"0.00018284","low24hr":"0.00013728"},"BTC_STR":{"id":89,"last":"0.00000279","lowestAsk":"0.00000279","highestBid":"0.00000278","percentChange":"-0.02447552","baseVolume":"115.23419696","quoteVolume":"42151354.76938477","isFrozen":"0","high24hr":"0.00000292","low24hr":"0.00000263"},"BTC_SYS":{"id":92,"last":"0.00000949","lowestAsk":"0.00000949","highestBid":"0.00000942","percentChange":"0.00529661","baseVolume":"15.71299356","quoteVolume":"1666032.15506082","isFrozen":"0","high24hr":"0.00000977","low24hr":"0.00000915"},"BTC_UNITY":{"id":95,"last":"0.00251663","lowestAsk":"0.00259995","highestBid":"0.00249995","percentChange":"0.09860526","baseVolume":"0.90393126","quoteVolume":"362.59841109","isFrozen":"0","high24hr":"0.00261936","low24hr":"0.00225420"},"BTC_VIA":{"id":97,"last":"0.00003600","lowestAsk":"0.00003623","highestBid":"0.00003600","percentChange":"-0.00853759","baseVolume":"1.69466689","quoteVolume":"47456.37417358","isFrozen":"0","high24hr":"0.00003714","low24hr":"0.00003471"},"BTC_XVC":{"id":98,"last":"0.00004590","lowestAsk":"0.00004590","highestBid":"0.00004545","percentChange":"-0.01120206","baseVolume":"1.05009308","quoteVolume":"22592.04079888","isFrozen":"0","high24hr":"0.00004730","low24hr":"0.00004481"},"BTC_VRC":{"id":99,"last":"0.00002473","lowestAsk":"0.00002485","highestBid":"0.00002473","percentChange":"0.00121457","baseVolume":"1.18260459","quoteVolume":"48563.32444985","isFrozen":"0","high24hr":"0.00002489","low24hr":"0.00002313"},"BTC_VTC":{"id":100,"last":"0.00003357","lowestAsk":"0.00003456","highestBid":"0.00003357","percentChange":"-0.06775895","baseVolume":"7.19565351","quoteVolume":"191719.88409985","isFrozen":"0","high24hr":"0.00004010","low24hr":"0.00003350"},"BTC_XBC":{"id":104,"last":"0.00196572","lowestAsk":"0.00198837","highestBid":"0.00194671","percentChange":"0.02891419","baseVolume":"5.07747043","quoteVolume":"2319.88980524","isFrozen":"0","high24hr":"0.00239836","low24hr":"0.00188202"},"BTC_XCP":{"id":108,"last":"0.00223457","lowestAsk":"0.00224268","highestBid":"0.00223457","percentChange":"-0.02500141","baseVolume":"20.32868447","quoteVolume":"9098.50892615","isFrozen":"0","high24hr":"0.00230000","low24hr":"0.00216275"},"BTC_XEM":{"id":112,"last":"0.00000401","lowestAsk":"0.00000402","highestBid":"0.00000401","percentChange":"-0.00248756","baseVolume":"38.38975543","quoteVolume":"9562328.95120402","isFrozen":"0","high24hr":"0.00000414","low24hr":"0.00000388"},"BTC_XMG":{"id":113,"last":"0.00002368","lowestAsk":"0.00002396","highestBid":"0.00002368","percentChange":"0.00381517","baseVolume":"0.89012427","quoteVolume":"36331.66920583","isFrozen":"0","high24hr":"0.00002645","low24hr":"0.00002327"},"BTC_XMR":{"id":114,"last":"0.01336000","lowestAsk":"0.01336500","highestBid":"0.01334980","percentChange":"-0.01822457","baseVolume":"1743.98093429","quoteVolume":"129674.24663044","isFrozen":"0","high24hr":"0.01374708","low24hr":"0.01315000"},"BTC_XPM":{"id":116,"last":"0.00005590","lowestAsk":"0.00005668","highestBid":"0.00005587","percentChange":"-0.00480683","baseVolume":"2.32500042","quoteVolume":"40715.63849309","isFrozen":"0","high24hr":"0.00006241","low24hr":"0.00005517"},"BTC_XRP":{"id":117,"last":"0.00000757","lowestAsk":"0.00000757","highestBid":"0.00000754","percentChange":"-0.02699228","baseVolume":"456.13163721","quoteVolume":"59610366.65714734","isFrozen":"0","high24hr":"0.00000790","low24hr":"0.00000743"},"USDT_BTC":{"id":121,"last":"888.00005020","lowestAsk":"888.00005020","highestBid":"888.00005007","percentChange":"0.03617275","baseVolume":"1292844.66938989","quoteVolume":"1470.67214446","isFrozen":"0","high24hr":"899.98000000","low24hr":"850.00000000"},"USDT_DASH":{"id":122,"last":"14.74805612","lowestAsk":"14.74806130","highestBid":"14.72000000","percentChange":"0.09602081","baseVolume":"27604.94873539","quoteVolume":"1942.87851462","isFrozen":"0","high24hr":"14.89999906","low24hr":"13.41468572"},"USDT_LTC":{"id":123,"last":"3.84534456","lowestAsk":"3.84534452","highestBid":"3.82821074","percentChange":"0.00637437","baseVolume":"7540.10204089","quoteVolume":"1958.39854700","isFrozen":"0","high24hr":"3.91000000","low24hr":"3.80000000"},"USDT_NXT":{"id":124,"last":"0.00580706","lowestAsk":"0.00580706","highestBid":"0.00576827","percentChange":"0.02962056","baseVolume":"2102.64303066","quoteVolume":"366136.07037977","isFrozen":"0","high24hr":"0.00586072","low24hr":"0.00550000"},"USDT_STR":{"id":125,"last":"0.00247838","lowestAsk":"0.00247717","highestBid":"0.00245797","percentChange":"-0.02426752","baseVolume":"555.16886508","quoteVolume":"228199.11447927","isFrozen":"0","high24hr":"0.00253000","low24hr":"0.00230000"},"USDT_XMR":{"id":126,"last":"11.89888000","lowestAsk":"11.89888000","highestBid":"11.83330444","percentChange":"0.02566494","baseVolume":"59304.22953897","quoteVolume":"4988.97341933","isFrozen":"0","high24hr":"12.24000000","low24hr":"11.50000000"},"USDT_XRP":{"id":127,"last":"0.00669698","lowestAsk":"0.00673797","highestBid":"0.00669000","percentChange":"-0.00793564","baseVolume":"10291.40845269","quoteVolume":"1526390.75038825","isFrozen":"0","high24hr":"0.00684869","low24hr":"0.00660001"},"XMR_BBR":{"id":128,"last":"0.00652019","lowestAsk":"0.00648766","highestBid":"0.00638101","percentChange":"0.02148022","baseVolume":"5.15513338","quoteVolume":"806.39705582","isFrozen":"0","high24hr":"0.00661663","low24hr":"0.00624230"},"XMR_BCN":{"id":129,"last":"0.00000402","lowestAsk":"0.00000402","highestBid":"0.00000396","percentChange":"0.02030456","baseVolume":"4.88896376","quoteVolume":"1200339.22402296","isFrozen":"0","high24hr":"0.00000450","low24hr":"0.00000385"},"XMR_BLK":{"id":130,"last":"0.00239901","lowestAsk":"0.00239582","highestBid":"0.00238032","percentChange":"0.02942362","baseVolume":"2.90087791","quoteVolume":"1228.21784998","isFrozen":"0","high24hr":"0.00241024","low24hr":"0.00232780"},"XMR_BTCD":{"id":131,"last":"0.33870852","lowestAsk":"0.34050491","highestBid":"0.33763182","percentChange":"0.01845109","baseVolume":"13.11109140","quoteVolume":"38.92625988","isFrozen":"0","high24hr":"0.35651702","low24hr":"0.31937106"},"XMR_DASH":{"id":132,"last":"1.23596910","lowestAsk":"1.23723326","highestBid":"1.23600000","percentChange":"0.07264288","baseVolume":"414.23907854","quoteVolume":"342.26183442","isFrozen":"0","high24hr":"1.23723326","low24hr":"1.15101902"},"XMR_LTC":{"id":137,"last":"0.32190700","lowestAsk":"0.32267335","highestBid":"0.32190700","percentChange":"-0.01964847","baseVolume":"243.04408132","quoteVolume":"745.08887374","isFrozen":"0","high24hr":"0.33388527","low24hr":"0.31696237"},"XMR_MAID":{"id":138,"last":"0.01002517","lowestAsk":"0.01008608","highestBid":"0.01002517","percentChange":"-0.00115973","baseVolume":"28.09623230","quoteVolume":"2852.22084155","isFrozen":"0","high24hr":"0.01022643","low24hr":"0.00954149"},"XMR_NXT":{"id":140,"last":"0.00048994","lowestAsk":"0.00048642","highestBid":"0.00048350","percentChange":"0.06167114","baseVolume":"50.38362305","quoteVolume":"103367.00495534","isFrozen":"0","high24hr":"0.00049673","low24hr":"0.00047000"},"XMR_QORA":{"id":141,"last":"0.00000589","lowestAsk":"0.00000598","highestBid":"0.00000592","percentChange":"-0.07244094","baseVolume":"13.61027478","quoteVolume":"2264218.51127596","isFrozen":"0","high24hr":"0.00000618","low24hr":"0.00000563"},"BTC_IOC":{"id":143,"last":"0.00038511","lowestAsk":"0.00038966","highestBid":"0.00038548","percentChange":"0.01518386","baseVolume":"7.77888376","quoteVolume":"19959.68676988","isFrozen":"0","high24hr":"0.00040843","low24hr":"0.00036819"},"BTC_ETH":{"id":148,"last":"0.01143566","lowestAsk":"0.01143566","highestBid":"0.01143563","percentChange":"-0.00602608","baseVolume":"2346.14463205","quoteVolume":"203025.40563212","isFrozen":"0","high24hr":"0.01178128","low24hr":"0.01131000"},"USDT_ETH":{"id":149,"last":"10.20000000","lowestAsk":"10.20000000","highestBid":"10.16100001","percentChange":"0.03235209","baseVolume":"133390.00811125","quoteVolume":"13157.01303779","isFrozen":"0","high24hr":"10.31591957","low24hr":"9.72753980"},"BTC_SC":{"id":150,"last":"0.00000041","lowestAsk":"0.00000041","highestBid":"0.00000040","percentChange":"0.00000000","baseVolume":"69.26206838","quoteVolume":"168893787.49195519","isFrozen":"0","high24hr":"0.00000043","low24hr":"0.00000040"},"BTC_BCY":{"id":151,"last":"0.00015449","lowestAsk":"0.00015449","highestBid":"0.00015246","percentChange":"-0.02952446","baseVolume":"8.71779070","quoteVolume":"55085.83547105","isFrozen":"0","high24hr":"0.00016816","low24hr":"0.00014735"},"BTC_EXP":{"id":153,"last":"0.00025537","lowestAsk":"0.00025638","highestBid":"0.00025534","percentChange":"0.01664078","baseVolume":"18.62110356","quoteVolume":"72573.31131151","isFrozen":"0","high24hr":"0.00026899","low24hr":"0.00024800"},"BTC_FCT":{"id":155,"last":"0.00339425","lowestAsk":"0.00339536","highestBid":"0.00339425","percentChange":"-0.00139746","baseVolume":"168.73759917","quoteVolume":"49688.89299026","isFrozen":"0","high24hr":"0.00344887","low24hr":"0.00331701"},"BTC_RADS":{"id":158,"last":"0.00044999","lowestAsk":"0.00044999","highestBid":"0.00044084","percentChange":"0.05797851","baseVolume":"2.75261552","quoteVolume":"6378.00934624","isFrozen":"0","high24hr":"0.00045161","low24hr":"0.00041502"},"BTC_AMP":{"id":160,"last":"0.00006431","lowestAsk":"0.00006428","highestBid":"0.00006387","percentChange":"0.06315093","baseVolume":"162.78428019","quoteVolume":"2432995.67835763","isFrozen":"0","high24hr":"0.00007160","low24hr":"0.00006046"},"BTC_VOX":{"id":161,"last":"0.00001072","lowestAsk":"0.00001088","highestBid":"0.00001075","percentChange":"-0.01289134","baseVolume":"12.20575887","quoteVolume":"1115114.06865207","isFrozen":"0","high24hr":"0.00001175","low24hr":"0.00001057"},"BTC_DCR":{"id":162,"last":"0.00109009","lowestAsk":"0.00110000","highestBid":"0.00109009","percentChange":"0.15735550","baseVolume":"34.12975566","quoteVolume":"31946.52004508","isFrozen":"0","high24hr":"0.00120080","low24hr":"0.00094000"},"BTC_LSK":{"id":163,"last":"0.00017547","lowestAsk":"0.00017547","highestBid":"0.00017462","percentChange":"-0.04422898","baseVolume":"70.41784522","quoteVolume":"391799.57460854","isFrozen":"0","high24hr":"0.00018683","low24hr":"0.00017221"},"ETH_LSK":{"id":166,"last":"0.01534602","lowestAsk":"0.01532792","highestBid":"0.01521662","percentChange":"-0.03615452","baseVolume":"58.23858861","quoteVolume":"3704.08694520","isFrozen":"0","high24hr":"0.01599999","low24hr":"0.01532875"},"BTC_LBC":{"id":167,"last":"0.00002946","lowestAsk":"0.00002984","highestBid":"0.00002945","percentChange":"-0.00405679","baseVolume":"120.73414765","quoteVolume":"3977321.38100581","isFrozen":"0","high24hr":"0.00003299","low24hr":"0.00002738"},"BTC_STEEM":{"id":168,"last":"0.00018137","lowestAsk":"0.00018137","highestBid":"0.00018065","percentChange":"-0.00776847","baseVolume":"122.16279936","quoteVolume":"661597.39567921","isFrozen":"0","high24hr":"0.00019182","low24hr":"0.00017705"},"ETH_STEEM":{"id":169,"last":"0.01583986","lowestAsk":"0.01581824","highestBid":"0.01566771","percentChange":"0.01627595","baseVolume":"211.58521144","quoteVolume":"13111.11606151","isFrozen":"0","high24hr":"0.01700000","low24hr":"0.01561147"},"BTC_SBD":{"id":170,"last":"0.00112000","lowestAsk":"0.00112462","highestBid":"0.00111000","percentChange":"-0.01719039","baseVolume":"2.74273588","quoteVolume":"2414.16245856","isFrozen":"0","high24hr":"0.00115368","low24hr":"0.00109247"},"BTC_ETC":{"id":171,"last":"0.00130621","lowestAsk":"0.00131057","highestBid":"0.00130601","percentChange":"-0.03148286","baseVolume":"373.52230663","quoteVolume":"279183.76700259","isFrozen":"0","high24hr":"0.00138924","low24hr":"0.00128000"},"ETH_ETC":{"id":172,"last":"0.11460000","lowestAsk":"0.11470418","highestBid":"0.11397297","percentChange":"-0.02781088","baseVolume":"1328.38212186","quoteVolume":"11372.67517783","isFrozen":"0","high24hr":"0.11886622","low24hr":"0.11364330"},"USDT_ETC":{"id":173,"last":"1.16688449","lowestAsk":"1.17288630","highestBid":"1.16688450","percentChange":"0.00941564","baseVolume":"34988.92450523","quoteVolume":"29804.85174709","isFrozen":"0","high24hr":"1.21520060","low24hr":"1.14230000"},"BTC_REP":{"id":174,"last":"0.00498823","lowestAsk":"0.00499122","highestBid":"0.00498823","percentChange":"0.04686322","baseVolume":"145.44150418","quoteVolume":"29534.96745989","isFrozen":"0","high24hr":"0.00505999","low24hr":"0.00471960"},"USDT_REP":{"id":175,"last":"4.43519067","lowestAsk":"4.45000000","highestBid":"4.43127258","percentChange":"0.05610457","baseVolume":"3871.35950702","quoteVolume":"917.00895507","isFrozen":"0","high24hr":"4.49999999","low24hr":"4.10000000"},"ETH_REP":{"id":176,"last":"0.43665131","lowestAsk":"0.43702397","highestBid":"0.43350944","percentChange":"0.07815138","baseVolume":"1317.87568250","quoteVolume":"3066.80509179","isFrozen":"0","high24hr":"0.43999880","low24hr":"0.40872538"},"BTC_ARDR":{"id":177,"last":"0.00001551","lowestAsk":"0.00001551","highestBid":"0.00001550","percentChange":"0.08461538","baseVolume":"46.33269269","quoteVolume":"2949738.55582328","isFrozen":"0","high24hr":"0.00001676","low24hr":"0.00001430"},"BTC_ZEC":{"id":178,"last":"0.04891901","lowestAsk":"0.04891940","highestBid":"0.04891901","percentChange":"-0.01001579","baseVolume":"292.60991917","quoteVolume":"5947.35590283","isFrozen":"0","high24hr":"0.05077770","low24hr":"0.04815764"},"ETH_ZEC":{"id":179,"last":"4.28945005","lowestAsk":"4.28945006","highestBid":"4.28945005","percentChange":"0.00326430","baseVolume":"402.02020954","quoteVolume":"94.50204948","isFrozen":"0","high24hr":"4.34680600","low24hr":"4.18060517"},"USDT_ZEC":{"id":180,"last":"43.70000000","lowestAsk":"43.79627070","highestBid":"43.55000000","percentChange":"0.02580955","baseVolume":"27619.01064986","quoteVolume":"642.91968834","isFrozen":"0","high24hr":"44.40000000","low24hr":"41.70510000"},"XMR_ZEC":{"id":181,"last":"3.65890970","lowestAsk":"3.67108637","highestBid":"3.64647008","percentChange":"-0.00038760","baseVolume":"105.80525961","quoteVolume":"28.97425754","isFrozen":"0","high24hr":"3.78654568","low24hr":"3.57684988"},"BTC_STRAT":{"id":182,"last":"0.00008075","lowestAsk":"0.00008129","highestBid":"0.00008100","percentChange":"0.23282442","baseVolume":"221.01779754","quoteVolume":"2833986.49554478","isFrozen":"0","high24hr":"0.00008823","low24hr":"0.00006410"},"BTC_NXC":{"id":183,"last":"0.00003525","lowestAsk":"0.00003588","highestBid":"0.00003538","percentChange":"-0.00843881","baseVolume":"200.42386837","quoteVolume":"5973927.25696122","isFrozen":"0","high24hr":"0.00003700","low24hr":"0.00003006"}}'
        # TODO - predelat
        symbol = ccs.poloniex.Symbol(ccs.constants.BTC, ccs.constants.BBR)
        self.ticker = ccs.poloniex.public.response.Ticker(self.json, symbol)

    def testLow(self):
        self.assertEqual(self.ticker.low(), 0.00008101)

    def testHigh(self):
        self.assertEqual(self.ticker.high(), 0.00008849)

    def testAsk(self):
        self.assertEqual(self.ticker.ask(), 0.00008630)

    def testBid(self):
        self.assertEqual(self.ticker.bid(), 0.00008530)

    def testLast(self):
        self.assertEqual(self.ticker.last(), 0.00008635)

    def testVolume24h(self):
        self.assertEqual(self.ticker.volume24h(), 2.11645424)

    # @unittest.skip("timestamp is emulated")
    def testTimestamp(self):
        self.assertAlmostEqual(self.ticker.timestamp(), datetime.datetime.now().timestamp(), delta=50)

    # @unittest.skip("timestamp is emulated")
    def testDt(self):
        dt = self.ticker.dt(tz=self.tz)
        dtnow = datetime.datetime.now()

        # This test should be valid in the middle of day (not midnight)
        self.assertAlmostEqual(dt.year, dtnow.year, delta=1)
        self.assertAlmostEqual(dt.month, dtnow.month, delta=1)
        self.assertAlmostEqual(dt.day, dtnow.day, delta=1)

        # This test should be valid in the middle of hour (not midnight)
        self.assertAlmostEqual(dt.hour, dtnow.hour, delta=1)
        self.assertAlmostEqual(dt.minute, dtnow.minute, delta=1)

    def testSpread(self):
        self.assertEqual(self.ticker.spread(), ((0.00008630 - 0.00008530) / 0.00008630) * 100)