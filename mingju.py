import termcolor, colorama, random, re
from cmd import Cmd

colorama.init()
form4 = """天苍苍,野茫茫,风吹草低见牛羊
春风又绿江南岸,明月何时照我还
志之难也,不在胜人,在自胜
穷则独善其身,达则兼善天下
锲而舍之,朽木不折;锲而不舍,金石可镂
顺境不足喜,逆境不足忧
落霞与孤鹜齐飞,秋水共长天一色
鸟宿池边树,僧敲月下门
洛阳亲友如相问,一片冰心在玉壶
沾衣欲湿杏花雨,吹面不寒杨柳风
问君能有几多愁,恰似一江春水向东流
是非成败转头空,青山依旧在,几度夕阳红
两岸猿声啼不住,轻舟已过万重山
悄悄的我走了,正如我悄悄的来,我挥一挥衣袖,不带走一片云彩
覆巢之下,复有完卵乎
赏务速而后有劝,罚务速而后有惩
欲胜人者,必先自胜;欲论人者,必先自论
先天下之忧而忧,后天下之乐而乐
林花谢了春红,太匆匆,无奈朝来寒雨晚来风
枯藤老树昏鸦,小桥流水人家,古道西风瘦马
哀哀父母,生我劬劳
横眉冷对千夫指,俯首甘为孺子牛
天将降大任于是人也,必先苦其心志,劳其筋骨,饿其体肤,空乏其身,行拂乱其所为
贵而不骄,胜而不恃,贤而能下,刚而能忍
燕雀安知鸿鹄之志哉
不廉,则无所不取;不耻,则无所不为
山不厌高,海不厌深;周公吐哺,天下归心
不识庐山真面目,只缘身在此山中
天行健,君子以自强不息
末大必折,尾大不掉
水至清则无鱼,人至察则无徒
大漠孤烟直,长河落日圆
君子不责人所不及,不强人所不能
流水不腐,户枢不蠹,动也
采菊东篱下,悠然见南山
丹青不知老将至,富贵与我如浮云
世有伯乐,然后有千里马,千里马常有,而伯乐不常有
醉翁之意不在酒,在乎山水之间也
曾经沧海难为水,除却巫山不是云
春蚕到死丝方尽,蜡炬成灰泪始干"""

form5 = """沉舟侧畔千帆过,病树前头万木春
执子之手,与子偕老
不惜歌者苦,但伤知音稀
操千曲而后晓声,观千剑而后识器
问渠那得清如许,为有源头活水来
时穷节乃见,一一垂丹青
落红不是无情物,化作春泥更护花
善欲人见,不是真善;恶恐人知,便是大恶
亦余心之所善兮,虽九死其犹未悔
生,亦我所欲也;义,亦我所欲也;二者不可得兼,舍生而取义者也
高名令志惑,重利使心忧
知我者谓我心忧,不知我者谓我何求
无可奈何花落去,似曾相识燕归来
人言落日是天涯,望极天涯不见家
何当共剪西窗烛,却话巴山夜雨时
晓来谁染霜林醉?总是离人泪
月落乌啼霜满天,江枫渔火对愁眠
多情自古伤离别,更那堪,冷落清秋节
星垂平野阔,月涌大江流
千里莺啼绿映红,水村山郭酒旗风
安能摧眉折腰事权贵,使我不得开心颜
临崖立马收缰晚,船到江心补漏迟
碧云天,黄叶地,秋色连波,波上寒烟翠
旧时王谢堂前燕,飞入寻常百姓家
不要人夸颜色好,只留清气満乾坤
取其道,不取其人;务其实,不务其名
金风玉露一相逢,便胜却人间无数
花自飘零水自流,一种相思,两处闲愁
人情同于怀土兮,岂穷达而异心
疾风知劲草,板荡识诚臣
旧书不厌百回读,熟读深思子自知
读书好,耕田好,学好便好;创业难,守成难,知难不难
回首向来萧瑟处,归去,也无风雨也无晴
众里寻他千百度,蓦然回首,那人却在灯火阑珊处
飘风不终朝,骤雨不终日
自在飞花轻似梦,无边丝雨细如愁
欲治其国者,先齐其家;欲齐其家者,先修其身
风声雨声读书声声声入耳,家事国事天下事事事关心
安而不忘危,存而不忘亡,治而不忘乱
年光似鸟翩翩过,世事如棋局局新"""

zhushi4 = [\
[0, ["见", ["现", "露出", "显现"]]],\
[1, ["绿", ["吹绿了"]], ["还", ["回到故乡"]]],\
[3, ["善", ["完善"]], ["其身", ["自己"]]],\
[4, ["锲", ["雕刻"]], ["镂", ["凿开"]]],\
[5, ["不足", ["不足以", "没有必要"]]],\
[6, ["鹜", ["野鸭子"]]],\
[7, ["僧", ["僧人"]]],\
[8, ["玉壶", ["品德纯洁无暇"]]],\
[14, ["覆", ["翻覆"]], ["完", ["完整", "没有损坏"]]],\
[15, ["务", ["务必", "一定"]], ["劝", ["勉励"]]],\
[16, ["自胜", ["征服自己"]], ["自论", ["批判自己"]]],\
[18, ["春红", ["春天的花儿"]]],\
[20, ["劬劳", ["劳苦"]]],\
[21, ["横眉", ["怒目而视的样子"]], ["孺子牛", ["全心全意为人民服务的人"]]],\
[22, ["是", ["这"]], ["拂", ["违背"]]],\
[23, ["恃", ["依靠"]], ["下", ["退让", "谦逊"]]],\
[24, ["安", ["怎么"]], ["鸿鹄", ["天鹅"]]],\
[26, ["厌", ["满足"]], ["吐哺", ["嘴里嚼着饭,还来不及下咽,又吐出来"]]],\
[27, ["缘", ["因为"]]],\
[29, ["末", ["树梢"]], ["掉", ["摇动", "摆动"]]],\
[30, ["至", ["过于", "达到了极点"]]],\
[32, ["强", ["勉强"]]],\
[33, ["枢", ["旧式门扇的转轴"]]],\
[35, ["丹青", ["绘画"]]],\
[36, ["伯乐", ["善于选用人才的人"]]],\
[39, ["泪", ["烛泪", "蜡烛燃烧时滴下的蜡油"]]]\
]

zhushi5 = [\
[0, ["病树", ["枯树"]]],\
[1, ["偕", ["一同", "一起"]]],\
[2, ["惜", ["痛惜"]], ["但", ["只"]], ["知音", ["知心朋友"]]],\
[3, ["晓", ["通晓", "懂得"]], ["识", ["识别"]]],\
[5, ["见", ["显现"]], ["丹青", ["史册", "史书"]]],\
[6, ["落红", ["飘落的花朵"]]],\
[7, ["恐", ["担心"]]],\
[8, ["所善", ["所喜爱的东西"]], ["九死", ["死了多次"]]],\
[9, ["得兼", ["同时得到"]]],\
[10, ["惑", ["迷惑"]]],\
[11, ["知", ["理解", "了解"]]],\
[13, ["极", ["尽头"]]],\
[14, ["却", ["再", "还"]]],\
[15, ["总", ["都", "全"]]],\
[16, ["愁眠", ["因忧愁而未能入眠"]]],\
[23, ["王谢", ["豪门世族"]]],\
[24, ["清气", ["高洁的气节"]], ["乾坤", ["天地"]]],\
[25, ["道", ["学说", "主张"]], ["务", ["讲求", "看重"]]],\
[26, ["金风", ["秋风"]], ["玉露", ["冰凉的露水"]], ["金风玉露", ["七夕之夜"]]],\
[27, ["闲", ["徒然"]]],\
[28, ["怀土", ["怀念乡土"]], ["穷", ["穷困失意"]], ["达", ["得意显达"]]],\
[29, ["板荡", ["社会动荡不安", "政局不稳定"]]],\
[30, ["厌", ["嫌弃"]]],\
[32, ["萧瑟", ["风吹树林声"]]],\
[33, ["蓦然", ["突然"]], ["阑珊", ["零落"]]],\
[34, ["飘风", ["狂风"]], ["朝", ["早晨"]], ["骤雨", ["暴雨", "急雨"]]],\
[35, ["自在", ["自由自在"]]],\
[36, ["齐", ["整治"]]],\
[37, ["入耳", ["中听"]]],\
[38, ["治", ["安定", "太平"]]]\
]

p4 = [1,0.30,0.15,1,0.45,1,1,1,0.05,1,1,0.5,0.6,0.6,1,1,1,1,0.05,1,1,1,1,0.3,0.2,1,0.1,0.1,1,0.15,0.05,1,1,0.55,1,1,1,0.55,0.4,1]
p5 = [0.25,1,1,0.2,0.1,1,0.5,0.4,0.5,1,1,1,0.45,0.3,0.2,1,1,1,1,1.00,1,0.25,1,0.15,0.45,0.05,1,1,1,0.35,0.1,0.3,0.25,1,0.5,1,1,0.55,1,1]

version = "beta 0.1.0"

class shell(Cmd):
    intro = "中学生背名句\n"+version+"\nBy someone who hate memorizing stuff.\nType help or ? to list commands. Use handwrite input method or wubi input method for best result."
    prompt = ">>> "

    def do_train(self, arg):
        """Launch training. Training loop the selected Mingju infinitely until you press CTRL-C. Questions that answered wrongly will occur more frequently.
USAGE: train form4 [start] [end] [--dp]
            form5
            all
start and end is used to specify scope of Mingju to select. They take integer as input.
start is the index of first Mingju, whereas end is the index of last Mingju. All Mingju between these two will be taken.
--dp is an option to disable probabilistic training. By default, the frequency of a question coming up is based on probability generated from the year it has been came up in SPM. Disable with this option if you don't trust the analysis XD.
"""
        start = end = None
        arg = arg.split()
        options = {"form4":form4, "form5":form5, "all":form4+"\n"+form5}
        if len(arg) == 0:
            print(termcolor.colored("No argument!", "red"))
            return
        if arg[0] not in ["form4","form5","all"]:
            print(error_unknown(arg[0]))
            return
        if len(arg) == 3:
            try:
                start = int(arg[1])
                end = int(arg[2])
            except Exception as e:
                pass
        if start == None or end == None:
            textlist = options[arg[0]].split("\n")
            if arg[0] == "form4":
                p_table = p4
            elif arg[0] == "form5":
                p_table = p5
            else:
                p_table = p4+p5
        else:
            textlist = options[arg[0]].split("\n")
            if arg[0] == "form4":
                p_table = p4
            elif arg[0] == "form5":
                p_table = p5
            else:
                p_table = p4+p5
            textlist = textlist[start-1:end]
            p_table = p_table[start-1:end]
        if "--dp" in arg: #if probabilistic training disabled
            p_table = [1 for i in range(len(textlist))] #probability table is all one

        total=len(textlist)
        compare=[i for i in range(total)]
        used=[]
        try:
            num = 1
            wrong = 0
            review = []
            while True:
                question=random.choices(textlist, p_table)[0]
                questions=re.split(',|;|\?',question)
                questiona=questions[random.randint(0,len(questions)-1)]
                questionq=['__' if x==questiona else x for x in questions]
                userans=input(str(num)+". "+str(questionq)+'\nAnswer: ')
                num+=1
                if userans==questiona:
                    print('Correct!\n')
                    if any(question in sublist for sublist in review):
                        index = review.index([i for i in review if question in i][0])
                        if review[index][2] > 0: #Todo:larger than original value instead of larger than zero
                            p_table[textlist.index(question)]-=0.25
                            review[index][2]-=0.5
                else:
                    print('Better luck next time :(')
                    print('Correct answer: '+questiona+'\n')
                    wrong+=1
                    if not any(question in sublist for sublist in review):
                        review.append([question,1,1])
                        p_table[textlist.index(question)]+=0.5
                    else:
                        index = review.index([i for i in review if question in i][0])
                        review[index][1]+=1
                        review[index][2]+=1
                        p_table[textlist.index(question)]+=0.5
        except KeyboardInterrupt:
            print("\n")
            text = "Total number of tries: "+str(num-1)+"\n"+termcolor.colored("Total wrong answer: "+str(wrong), "red")
            print(text)
            rev_mistake = input("Review mistake? [y/n]: ")
            if rev_mistake == "y":
                num = 1
                review.sort(key = lambda x:x[1], reverse = True)
                for i in review:
                    print(str(num)+". "+i[0]+", f="+str(i[1]))
                    num+=1
            return

    def do_quiz(self, arg):
        """Launch quiz. Quiz differs from training in terms of:
1) Quiz does not tell you your answer is correct or not at time of answering.
2) One question only appear once.
3) Score is calculated at the end.
USAGE: quiz form4 [start] [end]
            form5
            all
start and end is used to specify scope of Mingju to select. They take integer as input.
start is the index of first Mingju, whereas end is the index of last Mingju. All Mingju between these two will be taken.
All question will have the same probability of coming up in quiz, unlike in training mode.
"""
        start = end = None
        arg = arg.split()
        options = {"form4":form4, "form5":form5, "all":form4+"\n"+form5}
        #-------------Error handling----------------
        if len(arg) == 0:
            print(termcolor.colored("No argument!", "red"))
            return
        if arg[0] not in ["form4","form5","all"]:
            print(error_unknown(arg[0]))
            return
        if len(arg) == 3:
            try:
                start = int(arg[1])
                end = int(arg[2])
            except Exception as e:
                print(termcolor.colored(repr(e), "red"))
        #-----------------------------------------------
        #--------------------Import mingju into list---------
        if start == None or end == None:
            textlist = options[arg[0]].split("\n")
        else:
            textlist = options[arg[0]].split("\n")
            textlist = textlist[start-1:end]
        #------------------------------------

        total=len(textlist)
        compare=[i for i in range(total)]
        used=[]
        try:
            num = 1
            wrong = 0
            review = []
            while True:
                randomint=random.randint(0,total-1)
                while randomint in used:
                    randomint=random.randint(0,total-1)
                question=textlist[randomint]
                question=re.split(',|;|\?',question)
                questiona=question[random.randint(0,len(question)-1)]
                questionq=['__' if x==questiona else x for x in question]
                userans=input(str(num)+". "+str(questionq)+'\nAnswer: ')
                num+=1
                used.append(randomint)
                if userans==questiona:
                    pass
                else:
                    wrong+=1
                    if randomint not in review:
                        review.append(randomint)
                if all(item in used for item in compare):
                    break
            print("\n")
            score = "Score: "+termcolor.colored(str(((num-1-wrong)/(num-1))*100)+"%","green") if ((num-1-wrong)/(num-1))*100 >= 75 else termcolor.colored(str(((num-1-wrong)/(num-1))*100)+"%","red")
            text = "Total number of tries: "+str(num-1)+"\n"+termcolor.colored("Total wrong answer: "+str(wrong), "red")+"\n"+score
            print(text)
            rev_mistake = input("Review mistake? [y/n]: ")
            if rev_mistake == "y":
                num = 1
                for i in review:
                    print(str(num)+". "+textlist[i])
                    num+=1
            return
        except KeyboardInterrupt:
            print("\n")
            score = "Score: "+termcolor.colored(str(((num-1-wrong)/(num-1))*100)+"%","green") if ((num-1-wrong)/(num-1))*100 >= 75 else termcolor.colored(str(((num-1-wrong)/(num-1))*100)+"%","red")
            text = "Total number of tries: "+str(num-1)+"\n"+termcolor.colored("Total wrong answer: "+str(wrong), "red")+"\n"+score
            print(text)
            rev_mistake = input("Review mistake? [y/n]: ")
            if rev_mistake == "y":
                num = 1
                for i in review:
                    print(str(num)+". "+textlist[i])
                    num+=1
            return

    def do_zhushi(self, arg):
        start = end = None
        arg = arg.split()
        options = {"form4":form4, "form5":form5, "all":form4+"\n"+form5}
        #-------------Error handling----------------
        if len(arg) == 0:
            print(termcolor.colored("No argument!", "red"))
            return
        if arg[0] not in ["form4","form5","all"]:
            print(error_unknown(arg[0]))
            return
        if len(arg) == 3:
            try:
                start = int(arg[1])
                end = int(arg[2])
            except Exception as e:
                print(termcolor.colored(repr(e), "red"))
        #-----------------------------------------------


    def do_list(self, arg):
        """List mingju according to arguments provided.
USAGE: list form4
            form5
            all
"""
        arg = arg.split()
        #-------------Error handling----------------
        if len(arg) == 0:
            print(termcolor.colored("No argument!", "red"))
            return
        if arg[0] not in ["form4","form5","all"]:
            print(error_unknown(arg[0]))
            return
        if len(arg) == 3:
            try:
                start = int(arg[1])
                end = int(arg[2])
            except Exception as e:
                print(termcolor.colored(repr(e), "red"))
        #-----------------------------------------------
        options = {"form4":form4, "form5":form5, "all":form4+"\n"+form5}
        a = 1
        if arg[0] == "form4":
            zhushilist = zhushi4
        elif arg[0] == "form5":
            zhushilist = zhushi5
        else:
            zs5temp = list(zhushi5)
            for i in zs5temp:
                i[0] = i[0] + 40
            zhushilist = zhushi4 + zs5temp
        textlist = options[arg[0]].split("\n")
        for i in textlist:
            print(str(a) + ". " + i)
            for x in zhushilist:
                if x[0] == textlist.index(i):
                    for y in range(1, len(x)):
                        print(termcolor.colored("        " + x[y][0] + ": " + str(x[y][1]), "cyan"))
            a+=1

    def do_debug(self, arg):
        print((form4+"\n"+form5).split("\n"))

    def do_exit(self, arg):
        """Quit the program."""
        print("")
        return True

    def do_about(self, arg):
        """About the author and this program"""
        print("中学生背名句")
        print("Version: "+version)
        print("Created by: TheNooB")
        print("Follow me on Instagram: @py.i.nc")
        print("Subscribe to my YouTube channel: https://www.youtube.com/channel/UC2YiviEyZGj0NfaaY4y7cHQ")
        print("Drop me a message if you find any bug. Feature requests are accepted.")
        print("Next feature update: 注释")

    do_EOF = do_exit

def error_unknown(text):
    return termcolor.colored("Unknown input: " + text, "red")

shell().cmdloop()
