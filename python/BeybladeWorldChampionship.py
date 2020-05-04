'''Beyblade World Championship (100 Marks)
Tyson is all prepared for the Beyblade World Championship. The tournament is team-based and each team can have N members. A player can fight against a single player only. Team G-Revolution is all excited and pumped up as they have practised a lot. Kenny, the mind of team G-Revolution, has created a database where he has the data about the power of other teams’ members and his own team members. The tournament is going to start in some time and Kenny moves to the cafeteria to have a snack before the competition.







The team G-Revolution is to fight in some time and they are tensed up as someone has kidnapped Kenny from the cafeteria. They have made a police complaint and the police are searching for Kenny. Luckily, they have found his device with all the data. The problem is, the data is present randomly and not in the order they have to fight the opponent. Team G-Revolution wants to win at any cost and for that, they need the order in which they have to fight optimally to win the maximum number of battles.



A player can win only when his/her beyblade power is strictly greater than the opponents beyblade power.



Example:

Consider the team size is 3, N = 3


The 3 players of both the teams are shown with their beyblade powers.

Team G-Revolution is presented in the order: Tyson, Max, Ray

Team All Starz is presented in the order: Michael, Eddy, Steve

With the given arrangement, Team G-Revolution would be able to win only 1 fight. Team G-Revolution should be shuffled in an optimal manner as below:

The maximum number of fights Team G-Revolution can win is 2 when they are arranged optimally or fight in an optimal order.

Team G-Revolution needs help with the device. Tyson has heard about your skills and called you up to help them shuffle their positions in an order such that they would be able to win the maximum number of fights. Can you help Tyson and Team G-Revolution?
Input Format
The first line of input consists of the number of test cases, T

The first line of each test case consists of the number of members each team can have, N.

The second line of each test case consists of N space-separated integers representing the power of beyblades of Team G-Revolution members.

The third line of each test case consists of N space-separated integers representing the power of beyblades of opponent team members.

Constraints
1<= T <=100000
1<= N <=100000

0<= Power of Beyblade <= LLONG_MAX 

Output Format
For each test case, print the maximum number of fights Team G-Revolution can win if they go to fight in an optimal manner.

Sample TestCase 1
Input
1
10
3 6 7 5 3 5 6 2 9 1 
2 7 0 9 3 6 0 6 2 6 

Output
7
Sample TestCase 2
Input
10
481
28013 18171 19169 15795 6429 7405 31298 26402 5208 27108 26537 29003 4349 27599 7828 10696 5649 32310 31420 29307 24252 3371 7996 27682 10900 13437 26868 12075 25375 24366 24624 1737 14994 31527 28037 25159 10207 5419 22012 28829 25583 28938 17011 6721 19500 29207 22079 19775 20035 26587 6422 20364 16680 4875 14381 2967 20314 30392 25245 2850 22120 18886 17675 5200 24500 7327 26760 7423 5751 1832 30902 2135 24325 29429 13612 25251 29523 21945 4636 3936 10422 28672 19507 7572 17133 25632 29633 13922 30818 14700 13082 23002 2989 8108 21564 24086 7770 1738 18866 25730 8428 24270 16056 14715 1057 5132 29343 21020 3960 7068 25459 23636 241 9227 3036 5436 23060 15952 14402 22952 32308 4866 14132 9469 1525 30664 26891 29250 27660 30992 29386 13177 30534 11268 6217 21295 1484 23737 403 29778 7589 27818 28556 25667 26236 30054 9175 29484 28836 901 32758 9876 27993 32224 8115 31280 15433 3330 29375 8956 29267 5849 6554 2187 15758 8881 2482 26779 19085 14692 15567 22765 3809 5578 28590 6996 7392 14711 13292 30731 25765 14758 22823 4683 1624 22640 29023 27421 6576 15938 29858 1646 3765 26509 18408 26209 3019 6847 11068 20713 27884 31347 21276 5014 18485 2020 12579 14767 7076 10664 12261 26754 2080 2715 26139 22008 15801 25881 1280 3436 32050 3696 1530 30397 21180 22164 23421 21410 28165 4117 10540 10046 15217 21583 18242 15349 8871 22497 5425 15229 3664 25440 24457 3384 8475 17484 23834 28353 15365 19010 1885 31429 14807 9332 21008 4628 1008 13143 1569 23287 25668 8859 17357 19141 14501 24416 28681 28081 27458 16039 4385 24806 21613 26630 24223 13014 27041 22689 2158 7630 24003 4693 31039 20686 5800 19254 6188 15001 7128 12604 19867 2824 25233 5689 20326 24227 6927 6158 30777 18546 25355 6431 11835 11793 386 7428 7408 10755 4023 23938 18014 26696 13179 11193 12142 12594 20140 29086 11158 5748 18428 26540 2997 30332 20723 21207 13374 18947 19768 24258 24217 28642 16140 26673 2502 27431 23831 19393 24132 18280 13671 3287 2353 5975 438 26838 21170 16791 4331 10901 29589 4046 27108 21008 28213 13308 2931 25693 28318 14347 28070 30690 30194 2983 10316 20678 21772 9295 25268 8613 14946 25516 28856 17544 22320 14370 16634 20 24531 11174 110 11521 27506 21711 5913 20430 30436 24111 25112 31411 3790 6115 20195 3032 25868 18281 15315 7108 21843 10674 16866 12312 7444 23416 19379 1661 19107 7122 7634 3035 10136 7430 13372 21452 8822 22430 6434 9296 31626 5054 6378 27074 14614 7348 30583 9994 9903 21201 2730 13845 25572 3959 24104 27778 17952 3956 17502 30878 4562 22414 30915 2707 20170 18271 14173 7644 15334 20068 28039 30460 9711 30544 26609 10608 9662 15782 8680 14818 2467 24966 6616 12447 28167 11719 20239 12363 18767 25671 19651 25812 28420 17535 26199 24228 20017 24667 2266 11803 28429 13128 17873 
21308 29658 12174 31542 21926 8461 13792 15552 6342 12463 11057 25189 16460 29955 8394 24606 14555 3689 17050 19178 14597 14466 32717 12053 20086 29333 8608 7098 19311 1842 17523 1927 10359 14101 26399 29376 11853 2892 1163 27270 31776 4765 27514 20826 15874 3618 18599 4317 10139 20790 5908 6361 1818 22677 27295 20357 1137 23742 18646 22277 24770 25500 1036 19505 18964 5478 19629 25239 5963 22724 27854 451 87 31283 25096 18366 9899 25258 18823 5332 497 8574 21086 1178 1276 19843 10781 30768 3838 372 6054 5572 31995 30612 14396 24919 28541 2198 4829 21188 6282 4538 30162 3326 9683 1594 21124 6809 6958 12260 2961 21388 12614 25352 26911 20533 3217 10644 10097 3485 24707 10622 21432 9982 21250 19042 27435 18562 13337 24173 28761 16206 24048 21113 27326 19135 20732 10617 1173 4851 24691 18200 15086 26764 771 19869 21504 12720 7107 4882 4032 10324 20330 29093 18099 19899 14783 30542 27392 14137 5968 14514 8137 6205 14183 19272 23227 11663 19002 10938 17380 28117 24418 3470 18373 9052 10382 27909 4009 21269 21625 17475 21557 5342 5657 19121 15935 16643 11290 11680 18916 5893 31882 3375 24532 16794 6358 16494 6385 23540 15861 9411 24601 23622 9443 31885 26175 1925 14161 8456 7361 21100 31899 2929 10741 21442 21242 31082 3077 11231 18683 12447 24062 1389 11055 9642 29475 4972 6692 2612 15495 12408 15509 1629 11483 847 25054 8542 3716 19598 10418 7533 32753 16827 32272 19170 2603 6536 2163 5783 1453 11606 21322 22420 16759 21497 20135 8172 8286 22971 30523 5346 8358 14755 14978 4688 466 31735 27451 7498 31931 24063 23067 27134 16864 9996 26306 30942 12797 20153 7406 3842 1247 22641 12783 3527 21110 2097 30299 28093 12844 21647 4098 24768 25717 14844 4132 24420 15015 21318 14818 9623 12557 23393 3315 25217 28470 31846 26776 8111 8851 4060 23250 9073 26434 13367 28626 21120 13092 23454 5553 21732 30517 14321 26721 533 27421 10251 31204 22625 14082 2628 27323 909 28577 6202 26274 14015 6301 12242 22906 23964 8470 11641 28807 26797 3710 15280 15323 14599 18856 15303 1042 28459 16930 11240 10304 8491 23493 11864 6184 15374 23178 5626 16047 5238 16544 7189 28816 27264 21179 9046 13136 25836 13998 11289 28789 18302 24636 24036 26867 26787 16427 18996 31975 10840 27035 19581 7047 31304 8598 11116 28505 7476 3304 24431 6820 18840 28721 8823 6181 21900 13880 11517 5122 31720 12418 17475 20740 31915 17956 32220 28160 7326 1237 23662 8086 18484 18503 10679 12830 23989 27576 12750 26592 25243 14788 17323 1923 10301 3709 6890 11977 9130 24509 5836 15737 31960 8123 25215 27804 6398 11741 29343 26091 9278 18893 31740 28553 24199 15567 18334 32750 12218 11602 2054 20003 18187 20676 5047 12853 18859 28587 10485 27108 21668 28658 7885 5531 22020 22912 10069 421 317 2320 1845 3997 25292 1340 26214 21542 
297
10714 7738 15581 26782 7564 10397 21132 22860 17811 5274 27553 23338 11236 9249 25310 15424 2942 30471 9809 2483 30458 26446 12935 28209 19812 31399 19965 20367 29001 3381 6359 28593 30225 6548 17620 5291 14223 16922 2434 31781 4055 32604 10414 7684 8016 6132 5919 583 23306 17794 7556 11822 21841 10993 1450 27810 29826 32764 10226 30161 3101 5616 27907 14873 3100 6579 6076 21543 14979 14085 27500 26208 11065 262 582 26495 27158 17400 26639 8832 2877 9287 19738 28094 5548 11974 25974 23896 31761 15932 18534 29912 6111 23071 25617 7191 23202 29343 22907 23387 10640 7655 21684 8899 5984 15007 13648 8421 28767 7093 6934 27829 19648 8541 11005 1705 7475 25430 8276 29978 26042 20591 32320 32750 6840 26443 30059 20340 21579 27745 20987 29327 19420 16710 1473 4119 22517 16687 8883 18300 23122 18098 22941 1196 21562 16076 20755 19255 5392 27944 26794 15537 14117 17822 15464 24153 24272 32507 31864 25079 28609 17152 27938 30219 11410 8109 8955 24867 29855 7615 20313 27789 5144 8311 12554 25134 23124 29341 32070 8626 27240 9413 21729 4326 31225 8401 6597 27489 29262 5815 14496 13674 10153 9860 15066 22038 6872 27553 13514 7345 30983 19797 25641 13663 19928 14476 4807 20739 7094 9943 4476 1120 20070 5811 24418 8831 15326 22798 20801 5712 10075 22535 19787 32659 31406 15094 28426 5881 10710 2988 10134 7559 29908 16636 11787 23356 31675 21114 21562 28915 22791 14722 5023 395 13871 892 26260 30276 3710 22879 16835 25196 5150 8308 16865 19004 27510 6237 24986 20733 12470 6741 19399 4718 31663 23993 7655 11114 21993 26056 11981 13766 22255 31911 11670 15225 23278 24487 11486 25855 1918 203 28212 26367 4800 389 458 29483 169 19137 3697 12391 19101 26148 21957 32302 9536 
31894 18597 1842 22665 7678 16359 26435 24088 13900 11593 26738 14793 21437 22698 7030 16521 8794 32122 20303 16744 16579 23663 11305 17648 21034 5497 30082 22197 29090 24057 14223 3374 27290 26414 25564 17347 23204 2287 8500 15143 8316 1184 21184 5096 15429 29791 6770 22341 1301 14974 23205 575 22452 1334 31485 18163 8865 15001 29845 30758 29526 24777 26969 21282 26829 22120 19120 7105 12099 28495 21343 16071 26940 18819 22698 28276 10695 28260 14011 27994 25603 5160 23624 31597 29666 5000 14705 6489 9261 26041 5607 5656 21961 16030 4691 6851 11320 5948 22774 10408 25442 15470 16780 15774 12950 13786 27767 4757 24780 6435 6425 10353 28205 7521 15234 5913 30421 718 5451 21194 13015 8897 21953 23474 14209 15329 1351 3002 24034 20114 16373 30371 29322 7604 901 4180 4753 10125 5232 3442 23003 11011 15956 12850 18073 3343 29593 875 30227 12910 4180 3568 7846 8602 17515 14364 27400 248 26875 20910 6868 17747 17654 21975 3138 9353 1297 5010 4917 8324 27357 12340 16764 15980 30515 14404 1105 15899 5078 12940 15142 26066 84 26992 11170 13866 1581 24191 30438 6733 14391 7240 29716 26725 16705 23151 5138 18005 1527 10240 12939 18088 7686 4098 30775 20934 26752 27728 12893 12142 16257 23204 17302 17504 3859 2037 4563 22618 21327 17923 5537 30790 16837 7984 28332 18610 8734 23697 8578 23680 6656 12869 25242 25567 28722 1541 4757 18298 2817 1021 20419 1007 11746 30170 16617 22914 14936 4133 32066 9235 30744 10703 13763 28493 10348 4621 931 6945 26837 30822 27 9330 10484 6921 2411 26130 14250 12133 22813 26094 11135 14580 20365 645 10816 16983 6313 5279 21484 11432 3574 22843 21714 2316 31188 14281 25331 12423 8194 14489 10925 3605 12132 16276 28315 20214 260 
362
24247 27977 18520 22411 27329 18652 6339 5658 5093 16963 25693 18718 408 3111 22519 23483 24003 9953 14426 28194 15395 14919 9424 7684 4335 16838 25318 13132 31420 16050 5999 1293 25503 25817 4300 10937 15761 30046 1643 19861 24087 15301 29070 11881 15650 24906 25422 13180 6963 2679 31711 4799 21188 29429 26389 27721 22756 31651 551 26883 12577 24293 3764 12709 22698 32575 5891 20961 27829 1058 26511 23517 4127 14597 16835 24551 21586 25272 11266 3173 10604 32501 746 2570 6558 8761 12250 26704 21457 26577 10417 11810 18832 10296 7385 25304 25634 27040 29573 9065 5366 16079 32566 6108 17733 2092 2692 23808 26866 19226 8731 13917 14517 4996 16388 7274 22392 5049 15398 31489 26369 30331 9740 13327 20434 5970 27624 14992 16461 5415 29400 22971 10012 29453 1129 31865 11472 15202 13658 2332 28872 22807 10658 9550 3413 6988 22963 30279 10011 5920 15617 12612 3003 23495 32190 4148 9135 11485 6632 32436 15221 14073 5510 4925 26607 29318 8751 10396 2570 10446 24523 11171 13726 20312 6814 28959 32661 11636 10882 10250 30544 20 22387 15361 20294 4061 26449 15352 30958 28030 14562 6444 14304 18497 4119 21081 28727 4831 30608 24365 13369 27289 23393 28669 21818 29828 16663 21944 31677 9509 16630 9753 2781 9789 9349 28704 21227 20198 20045 5314 22361 25055 20189 6112 11222 1573 19217 32118 11451 11715 6036 1813 5798 24298 11684 26003 16740 4932 23829 13057 533 8582 24473 18653 30858 25925 12606 18057 19442 6410 21048 23548 6838 5800 21985 11448 8609 29133 25342 24315 24132 8408 2372 11066 12441 10218 4123 32715 16358 31296 8865 3298 9956 1472 31986 19646 11041 7377 32423 23588 931 12912 18076 14093 29390 7297 15351 11676 14216 20578 10341 9554 6554 19910 18343 31365 5465 11201 28750 5646 27271 31775 14786 2883 4724 30970 17289 21029 24936 12428 454 29146 22341 9025 13056 12125 25449 2064 25381 5236 8146 11020 8143 25314 18309 6710 16837 18398 27696 5270 28613 25541 12046 28554 16001 31244 267 26205 4583 23928 11817 2075 9125 27793 14370 14244 21229 12884 17487 29184 8565 32552 8392 20210 451 3603 9421 28624 23207 2606 28772 20625 
25609 2134 20292 12072 16612 18725 17138 32017 31379 22304 30762 3881 16716 21810 11136 32706 5610 4442 16711 30455 16623 12192 5298 19773 15049 333 16953 15419 26964 23643 28990 4572 22177 1835 24817 6562 17654 3190 15473 12349 17429 2950 31284 13660 11201 22694 19112 20419 8063 471 23066 14237 32666 3012 27096 31508 27497 31480 1170 28960 14548 32079 20998 20124 1301 18346 19933 4511 17084 31719 26063 14089 26870 11025 17166 28252 10254 18387 17122 16334 18228 7475 25232 22684 3966 7549 8833 29088 26668 7548 9376 1062 2096 20464 2564 16636 24814 5437 21455 32200 9792 29537 19286 3230 6077 18984 13698 12754 28475 6051 21878 11275 6290 24790 625 665 5795 4785 21750 3593 14745 28482 12075 28406 2671 23336 9344 26402 4019 8011 1168 18629 20361 29386 3404 28708 13042 24885 2134 31590 11854 24829 22443 13475 21280 11816 13701 25151 12050 15689 11136 29046 7225 23216 1275 12087 26265 18910 16577 822 27372 31036 17897 24893 4767 7692 24570 25794 20766 19615 18003 19135 1617 24776 13002 15806 27238 19090 19348 10291 26322 4910 25701 271 146 11823 23255 18066 14263 27386 4624 7009 33 6775 20895 14808 14219 15629 2984 12705 15560 19662 20033 9094 3147 30702 25627 28547 1517 24442 26725 2336 16363 11846 20973 26110 2862 7208 14729 15023 3280 12643 24501 31178 4315 24166 13693 18751 31316 15287 27806 25065 29816 1578 21224 3426 18757 11094 31974 13851 316 31305 961 15788 12390 19579 23138 3432 5269 15105 32215 5429 26860 13315 1272 11419 4769 1136 21322 2586 2818 10736 29475 17601 10934 283 23311 5116 14918 9192 8819 16814 27612 3176 26992 639 8778 20404 30730 10360 10573 1316 22666 25549 17171 11713 28960 1529 12028 12285 24781 31504 3486 15266 9088 27985 17931 10761 16768 18171 20566 11916 3593 1635 2387 27453 14650 6210 29599 15833 14639 11347 2528 22775 20074 14366 1614 32133 10103 7182 17267 26741 26575 7882 6702 18612 5630 12994 24830 20828 13569 14856 28797 15402 3314 15458 20779 20530 26343 17309 30317 16593 16407 21028 10966 30948 14398 10193 4516 9783 16195 18690 24974 6465 17944 31728 15549 19726 30435 12348 18968 11132 
427
1227 29636 25002 116 24532 28395 22702 14910 19767 28861 9862 17162 5905 13493 2897 17104 19597 14366 20160 25549 11005 20181 4551 11632 7465 30032 26776 1655 17638 991 20689 8790 17131 10034 22516 24024 12513 16924 1561 20232 441 7318 24799 3154 15426 1031 6824 28390 17403 16579 16902 21597 9254 1233 1392 9119 4381 14321 24378 6404 5097 17629 15812 7609 5137 19408 31729 11878 13232 24133 15834 5389 12746 10241 1476 31286 18144 10579 5456 4425 12226 26267 28402 25659 23205 12553 2980 620 27253 27815 6364 5840 1133 30618 21179 10574 7140 5797 20103 3941 12394 2798 18779 20501 12819 13573 20253 32509 19 26914 19889 21185 13707 22702 26732 31406 14499 13573 8140 30625 16345 28539 8550 31780 16793 15005 21535 6107 525 12473 29855 12831 13110 17312 22019 6120 23356 22954 6866 8432 29954 15355 31283 12309 32510 14853 25949 4863 27720 9806 8526 1284 11248 4211 10432 22856 14997 24686 27225 4137 29235 14100 14114 23514 3133 14305 30010 22605 2540 8184 27340 31319 30422 20070 13630 31247 14786 8615 16555 15479 26555 20075 21396 94 19811 5018 722 21124 8842 28565 8655 3328 7167 15039 758 26079 20390 19260 7272 20750 7883 1528 25841 14714 6838 235 32058 21877 6016 6812 31040 6748 24869 10980 24068 4982 18137 12533 10117 8224 28832 8858 27371 23847 13081 16577 26885 15734 21914 5430 9461 5617 32386 32177 21290 8352 14795 26643 13455 15120 19935 9197 12802 25590 21165 27970 19464 15382 16123 5262 12991 3683 24574 26630 6676 9064 28456 16930 7733 25574 14913 24921 19530 3775 4537 27947 9056 1554 28989 19557 8613 30632 5768 12449 12763 25743 31356 31500 3335 19460 24689 24172 25705 32151 28621 25185 26545 22153 3028 11242 31600 28281 24002 12076 13261 30527 17687 11887 26489 21529 8755 10858 28389 11269 12066 10176 25522 31597 23225 28106 29801 26889 23010 8855 8300 25090 25396 26673 28716 16723 18631 24354 32157 1653 25670 12855 24807 24379 2373 3972 21855 2299 29141 12968 10933 19694 22870 25683 22126 7129 14733 4869 14741 3309 24055 26904 28334 17388 16732 1024 13292 654 27046 12498 17828 26915 13812 20995 15616 10873 21227 21106 18168 14080 18764 18857 18302 9004 23244 13664 15609 19739 8480 27715 30709 1400 9047 11766 31513 16287 21868 29781 5977 3330 13852 27136 6253 26571 32501 10775 5505 4291 6832 11586 14894 1138 21952 2037 7081 19336 32043 24050 28218 10875 24473 12047 12016 29810 25770 24889 5524 1378 11917 11193 25307 10102 31183 18358 24287 26549 12144 2555 7120 7647 23868 18939 20711 
11159 2136 14866 24988 14023 3612 5390 25881 25409 1824 17646 16878 20386 24730 26346 12806 22908 8167 20659 17114 27828 1127 31483 9700 25128 31630 30008 25943 12693 6968 18085 20749 31417 5693 24714 14273 10676 24390 1470 16510 15028 28127 19306 30807 24785 22989 5903 26713 5174 16545 15819 18366 19330 10637 10456 7779 25710 23415 9045 27517 32687 22860 13641 9351 21534 30871 12261 8319 15638 18002 20233 17233 2077 11771 5130 32148 17863 5867 15795 29812 8664 27620 393 26095 1705 16617 27219 7493 4045 2898 32730 2985 4083 8223 7150 22845 11790 27789 4265 573 23988 7399 1016 21626 14020 9631 9302 24843 28748 25245 6875 13887 682 16599 24182 30166 13553 9762 19575 7024 6542 2887 10832 1861 15915 31834 29852 8471 4819 29511 8032 10085 19543 16558 11153 32482 17905 30449 13783 5669 9768 2955 25233 12706 19187 8867 19225 13273 16673 14560 20553 13773 19192 8064 30270 952 14877 32420 11611 20989 8372 20974 11409 15966 7623 4942 16606 29039 18668 2073 13844 29770 290 25692 15580 3717 8957 14447 29178 16481 27139 23757 27347 11588 341 20514 27436 2666 1938 15270 10292 26071 2552 4522 15557 22928 15052 31344 13031 32522 26364 832 18070 14051 28420 17336 17861 6352 18190 28004 12706 8151 16989 31119 1308 26302 11755 26968 17570 2243 32337 19464 15150 31373 5352 32674 2179 28515 24622 24508 25779 7836 23403 22158 15587 32086 12692 1097 3410 16491 1903 28842 7320 15009 12536 31438 31788 27425 22020 31560 29225 20523 18980 19569 12370 20999 7116 11519 31827 23103 7860 12505 11594 27403 30079 13354 8837 19213 24219 1204 6029 6462 18536 13672 31076 23849 28828 20531 8460 26455 4838 23066 5960 5642 27345 23945 17831 21038 3308 28392 14525 22668 23336 24432 22452 9025 6273 4669 13572 1902 24544 10148 23678 23346 576 29382 17039 14293 4112 28005 14531 11334 4569 7671 2952 29640 13345 9209 11573 1256 27279 24198 4682 3250 20048 24872 8953 10788 15288 10990 26086 32227 29485 21439 18476 25133 16705 9197 9888 24335 29214 18957 31833 11992 5159 8967 23152 26317 19932 18537 3332 6174 19198 22785 4481 32025 1268 12202 16930 1694 27246 31846 23221 24019 10824 29613 15007 11800 9649 2053 2079 19262 19852 25043 6359 2035 28438 2417 17288 20609 13258 30592 32541 23993 22658 32640 29419 5161 24542 18590 23607 25494 17385 18636 27896 15014 27386 30231 2015 25308 25561 8757 32149 22729 11555 13406 12100 29825 3056 13662 14936 30285 13746 25063 4487 19359 20833 14123 9998 8267 5077 11690 3134 4083 31603 5705 10808 
11
28427 19877 30709 18527 17409 14758 20873 18458 28587 17751 21672 
21865 26619 20213 26217 407 30558 15430 17994 31674 2019 10539 
108
21477 10656 25721 24897 32415 22610 12037 21500 11412 17475 28926 18152 19083 8817 22912 643 15768 18412 7269 4619 12179 5248 16991 9026 32712 28820 16196 4975 11248 25170 17064 19877 17761 32264 30385 24135 18049 13774 8487 24524 23680 19562 23243 9408 31047 28528 20714 17163 16811 15534 17713 25718 11239 14022 16323 107 25161 27933 10121 25340 15915 23284 13513 9512 28453 16853 29179 31321 8833 817 16088 30512 16111 15687 2483 13701 2170 12103 13068 31146 16571 10424 20323 15600 5965 2071 15178 16749 32385 3265 13758 4860 14418 19 29879 6532 12187 31183 26622 8318 29063 17345 7743 30641 23369 8355 95 4416 
20494 31295 22287 16615 2864 15059 20130 130 25261 21945 27931 24015 3543 17223 11915 30068 17485 29685 15258 8004 18729 32445 28259 12222 13947 3784 6533 29398 7415 21574 17782 17401 19434 31902 22555 26443 21875 30151 23190 2099 8943 245 20832 281 11701 22649 23191 20590 12292 27874 1689 24301 25145 32105 7889 31521 6213 3980 20177 11816 21343 2552 25505 19894 7158 30380 5463 28509 14314 12380 3816 8459 4347 32531 10302 2772 24450 26653 1675 24049 27999 13604 5852 13577 1330 30361 5873 18864 25038 1366 8268 9006 12778 18305 27016 8833 1050 15539 12780 4005 12030 5465 2880 3090 2489 22875 30175 3719 
213
25084 782 19462 4678 11010 29068 12831 8316 16150 30827 22130 508 17261 13341 32624 20480 26280 27090 10849 27710 14073 5378 12971 6935 9096 29509 32337 3602 11541 619 21434 29320 2526 9417 15540 22689 16579 24529 6840 1663 32680 26854 20592 3000 12571 29806 9334 10506 5430 31528 16735 24650 25031 27071 30456 16542 11695 28320 8399 17132 11144 23049 22005 19090 30603 17507 17923 7768 31920 28370 26459 28066 13590 4618 23216 13803 18854 3940 10185 7278 21748 14385 14209 4134 19813 8014 12051 18425 23191 10489 4244 28977 6653 19682 17601 8747 5834 16005 29179 25939 30993 28600 17552 28752 12330 8576 3132 23419 7255 30505 21232 28054 31655 16278 20689 20411 7707 26837 24964 15762 9480 20982 24233 1479 20924 28446 933 28347 10084 29655 16037 21370 25646 30634 4832 3310 5546 18672 28700 31570 19574 25061 9075 17384 13082 13310 17751 5871 3121 15741 18644 4560 23498 7490 4117 4504 16397 6372 10794 2474 15650 18688 7688 12982 78 24529 26321 9701 24159 15873 1366 14422 4427 18879 19163 10958 30996 15378 16666 427 25582 22637 21386 6426 8612 17027 7648 18826 26168 26204 982 12385 16330 9897 30252 28909 9146 17749 2285 413 22289 14940 16116 22897 13853 27872 11950 4527 8028 634 25634 20440 1436 
14542 9262 3034 27999 32098 29971 1671 22916 14256 4148 1094 27428 31097 8474 8200 14523 2397 30140 19070 8328 31657 1021 18826 6710 19824 26743 19443 19387 13789 17015 25948 25985 8647 4424 1655 2499 3462 30389 17782 17211 12549 713 2754 20218 12825 27865 30192 15767 20753 24005 3825 12171 17295 12154 6024 12508 12694 17851 4353 30713 2275 25634 18977 3045 6785 9569 2393 5528 13976 30670 10046 24739 14982 17183 11582 20242 17712 7025 19595 17558 1434 9616 16732 19684 22454 4210 30293 344 9082 18436 31811 29150 12853 17706 10765 5394 28195 7936 30952 934 16447 16743 28873 772 88 27837 14624 9013 11111 25323 8643 29698 21536 26021 14376 5465 455 27117 15576 9970 28997 9433 3360 23345 27771 21911 21770 12623 11222 28846 7564 6837 30244 4230 2814 4008 29350 20267 24529 22315 24934 27982 6015 1569 11722 27277 11710 31155 3946 29428 26105 20721 11551 17859 9984 10684 30300 31089 16127 9443 9922 16626 9133 30092 10222 5686 709 32726 17814 28146 14010 19132 26580 22690 29607 18749 18369 13519 16516 16057 21062 22157 4256 17055 11567 18505 4427 10053 4737 2241 32723 18455 30222 27220 7091 756 10566 30588 2310 24789 29008 153 14146 12720 17242 14064 8226 8092 6957 30963 29412 32053 8196 
251
32693 21314 2974 32243 30570 29077 1938 20367 21360 1843 29923 31580 31238 1461 20948 19810 29353 21486 12797 29352 16080 5070 31903 3647 10970 32646 25909 8065 11077 8685 21067 7579 6688 28195 9875 27721 26819 31348 8246 3553 6589 25215 17000 13971 5902 5271 32063 9455 14487 3689 1989 25511 3790 19679 8268 22679 17846 29509 9985 17666 13327 28075 18116 6943 27337 4746 8247 19668 22719 1962 11029 30657 22178 28226 16838 4736 12083 6754 2864 32555 30646 22926 14031 10015 19619 3243 16136 1024 18078 6432 9658 14846 15273 30005 24343 10070 8345 21438 24242 3355 7878 13054 31448 13622 12807 21190 6692 14764 25310 21981 24398 20767 28911 4772 18244 17560 439 22266 28028 29315 10106 9054 27272 763 21629 8531 235 12616 3702 22793 3115 20134 30273 27193 26151 25160 30676 19537 13995 2717 13941 22993 24898 978 2347 10997 1355 30616 7026 916 17487 31271 1586 22600 17042 22659 29938 11983 5608 7166 11081 23985 5834 26366 32406 28451 18345 3840 6129 11052 18050 6109 4706 3334 31923 29772 18768 10183 269 12201 27452 15937 24618 25845 9391 4646 16129 10013 30576 11888 2999 15999 4603 12543 12473 24490 15151 22404 32263 16229 9799 21407 15571 10228 17163 10820 8522 29590 24135 8803 3762 4178 9853 1736 25013 28915 26839 16192 13564 3922 6751 1277 21504 25555 370 13883 20509 30258 4978 3364 27625 27520 23228 15857 20675 13672 30938 16467 17071 18103 6393 18449 18017 28956 26269 12530 28055 20523 23699 25053 15788 
26024 40 27455 25706 19203 23704 25773 12065 7199 21193 19915 30709 32599 4409 30316 32124 28355 18485 12794 22665 9911 28237 23065 1090 23949 10500 25735 11385 10405 11724 4166 13881 12969 12081 28158 13982 10006 10836 18333 19434 30456 10395 11072 3286 23285 18855 7510 550 13964 10630 13826 24192 16543 30506 11714 26750 5423 20250 7503 19202 5224 11880 29892 16330 13021 4579 28161 18500 7956 5517 32338 26787 24645 10320 2892 6450 21087 10220 26360 25064 9036 31028 22324 21565 13686 28794 11349 22333 2954 7752 11025 31195 8572 21585 19869 16263 22219 30374 8210 6915 19974 27949 15381 2930 25999 18768 10167 4018 11679 29682 7066 25579 32650 30631 29782 15720 6724 15140 21274 30886 26660 16372 12695 28075 20969 14701 27929 24217 17147 4067 3319 13443 17139 9243 18478 32383 18524 26370 3657 26365 10427 6559 6020 4951 18894 18759 16432 8617 30738 23568 13145 14562 1671 16776 10407 24347 7095 7078 14722 2600 20469 29696 4473 7789 227 20799 32229 20467 32311 16592 8393 6588 29630 10461 19197 16211 13473 30332 16780 3238 19431 31782 29274 18456 30267 5226 23562 2771 26863 23778 11550 29531 2626 7527 24160 26217 32478 12161 19585 20982 12453 31265 5377 9878 12973 21907 14926 31495 9865 27566 21296 3594 1739 26702 18788 6769 31430 3588 27528 12666 6041 779 22071 3931 12905 27262 30836 7710 10221 7625 14156 6831 15664 6750 29879 4148 32146 30633 32192 7580 14864 31045 9189 14715 3526 4464 1473 26645 2994 26556 19176 
72
31163 14344 22291 5968 15602 7599 14461 23349 23319 7935 21900 1095 13663 3309 7604 23869 24692 2822 16793 16954 15806 21417 13939 9889 14817 3188 2231 11563 21639 16124 16884 1591 21855 18881 26106 2145 21094 23905 19266 14165 27493 23051 21130 11494 24250 8503 16832 6234 23388 12180 17953 18440 13338 4930 24994 28966 22563 4674 18319 10716 13515 5419 27762 18844 25740 10782 19766 9142 20299 13307 12684 20519 
8157 6613 28046 30386 13002 2724 26274 20531 25169 10554 24482 21039 21420 13433 20538 14511 10645 32706 19345 25167 16392 20400 14891 12946 21835 28423 27406 28280 17452 4071 16419 18259 13194 19782 31200 2006 24342 24733 26148 5999 23899 24544 30306 18391 1788 6068 258 8423 25405 21981 12804 7853 15813 14325 28391 5567 18851 21092 12745 12751 30094 17292 8143 17024 21873 1860 24263 19064 17703 7816 28172 1206 
370
24430 1706 21542 27795 348 18115 20851 11813 14713 11314 27421 10635 31585 8813 19403 22428 12829 10160 31458 23547 1362 19800 27478 10396 32440 6029 27841 31363 9166 35 12978 5071 22477 8386 26183 22264 6618 18501 30206 10069 29567 32609 6088 13025 11100 16519 12639 2366 4122 26379 6874 9210 28577 6533 28543 17426 3723 13176 24792 18612 13272 29233 16393 25417 7395 26866 12640 19635 28052 80 15918 24531 28888 1242 14549 15695 15694 2299 10019 23698 4676 7714 9950 11796 225 10527 160 13019 13731 21969 23781 11586 30221 28158 20323 20217 9881 6018 11418 2125 27892 15788 23979 23721 17002 10725 9837 24669 2719 3986 4542 17311 641 3900 30743 3791 7034 29934 21604 29696 5866 13791 23314 22963 30164 29009 1897 741 4312 30905 4892 30797 27745 8992 3102 5855 7455 28617 31928 26516 20664 15380 23001 9325 20154 4258 11181 3766 1493 18874 9328 31368 31047 7916 6533 13201 8855 19956 4802 7959 7046 27873 25615 16187 9283 10102 1327 31611 23006 27600 7133 21115 12543 19017 27675 22789 2264 3229 8903 10830 27224 18507 11887 11643 18337 28734 6758 21603 20413 10669 8215 14231 10892 26688 25242 13216 12545 5492 2181 27527 30094 18240 10245 21659 12509 18937 14637 12142 26305 371 653 4641 22380 25961 13319 26593 4322 7454 9182 2482 13486 32325 25104 21611 17875 29470 5606 24578 4869 3043 22985 15370 4377 16226 2391 21882 14779 7915 13750 27056 16991 364 13352 10934 16250 27099 31456 30915 2033 11476 16405 21765 27857 6532 3924 29085 6466 10693 18714 748 11958 32138 16546 13837 29030 9598 27644 28834 6399 232 23135 15828 6552 13010 25792 3221 30952 29290 19619 9000 950 15016 15666 27620 30608 7473 25228 32565 29888 15484 2911 3811 19580 12595 2233 5783 32605 24284 16411 30107 19 31672 9168 21985 3670 20459 1404 1095 15903 28638 30456 7705 32537 30178 11613 14295 14418 32534 6751 24889 19511 28554 12253 10865 6335 16804 437 3760 18406 25795 14813 26603 1117 28451 4784 20447 26240 9985 19333 4691 11656 9983 19334 5277 6402 8649 26304 22119 30336 2297 31094 28595 14222 6968 19899 12317 9191 7590 32576 17248 31721 17533 20842 32540 8007 3825 11175 15831 3070 6746 
12291 27457 18826 12436 8182 9660 5209 5542 896 6427 23936 22691 18040 30378 29357 11214 16418 11887 25180 2049 22783 19888 28750 8016 17129 9910 11831 25321 30559 9680 3256 8254 28701 30618 30860 31079 19951 25726 22534 15553 25032 1404 31931 24540 19470 13863 23932 8596 9785 26608 11399 6013 27292 15015 7677 10885 3714 32319 29335 18132 637 466 6805 17143 3323 21476 1272 16958 13082 22508 28401 5730 9150 21777 18329 25707 22752 25137 31714 4305 25385 21287 16078 14050 5055 2894 8671 12131 30815 22849 4558 27258 23980 16357 2944 8396 19398 20650 7477 8162 12575 31501 2051 13777 12170 30050 5507 26 16277 8912 30154 8655 7705 6813 14746 9463 14351 13483 15578 2868 2213 16195 5444 20899 7570 16914 22878 27652 13734 29297 21419 31515 11685 15594 30242 16981 12117 2039 8671 8367 22230 5132 5913 4308 16946 7384 8532 29829 16181 8137 21463 12094 2943 27598 27233 21527 23255 24160 8728 27368 6082 29123 7874 4272 4692 137 12343 30520 4423 25177 3094 2035 31050 17902 20408 11817 32411 27746 24162 3156 5336 10669 28607 8395 4371 20073 25229 7581 12836 24280 10134 30656 835 15143 22754 29035 19670 7412 20779 9152 1927 3599 22417 19374 1434 15485 13199 24086 18045 20419 15662 10028 10401 9057 15736 31009 28041 2716 13104 11775 17441 384 20416 212 19792 28454 16499 530 20176 23859 6116 11062 2110 18593 27575 21928 24173 28610 31366 6370 20736 16769 28190 21461 28216 20972 3564 25992 14602 30703 30130 22787 13685 30818 9342 2155 3858 25159 30685 31598 3565 76 26444 1250 19859 920 5103 25512 27244 19395 134 27351 6475 28710 1436 29974 23876 28246 22017 10058 20414 8683 10107 18034 11976 27014 21433 9422 9649 7442 1416 27207 978 14665 17994 15371 21935 25722 32675 1912 5183 12426 17781 29755 24199 15930 31759 16825 29038 9639 11937 5038 20940 18455 10739 29203 23748 28402 12119 70 12884 23567 21469 12133 11818 12081 24517 28666 25273 17618 16954 9950 19085 29215 27965 26967 9179 16963 11743 17540 10845 6376 21683 5115 9052 24059 17027 11184 28687 5808 11586 22809 6691 4039 12610 32655 3739 32013 679 21496 31450 12837 21276 31651 32766 22664 16324 4723 12400 18123 
Output
468
294
345
413
9
101
203
238
59
351
Time Limit(X):
0.80 sec(s) for each input.
Memory Limit:
512 MB
Source Limit:
100 KB'''
testcases = int(input())
for i in range(testcases):
    k=0
    count=int(input())
    g1 = input().split()
    g1 = [int(g) for g in g1]
    g1 = sorted(g1,reverse=True)
    g2 = input().split()
    g2 = [int(g) for g in g2]
    g2 = sorted(g2,reverse=True)
    c=0
    for i in range(len(g1)):
        for j in range(c,count):
            if g1[i] > g2[j] : 
                c = j + 1
                k += 1
                break
    print(k)        
''' 1
1
10
3 6 7 5 3 5 6 2 9 1 
2 7 0 9 3 6 0 6 2 6 

g1='3 6 7 5 3 5 6 2 9 1'.split()
g2='2 7 0 9 3 6 0 6 2 6 '.split()


'''