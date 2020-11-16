#The following code will give you headaches, you have been warned.
import termcolor, colorama, random, re, os, difflib
from cmd import Cmd

colorama.init()
if os.name == "nt": #Setting code page to 936 (chinese) for windows device
    os.system("chcp 936 > nul")

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
丹青不知老将至,富贵于我如浮云
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
[0, [["见", ["现", "露出", "显现"]]]],\
[1, [["绿", ["吹绿了"]], ["还", ["回到故乡"]]]],\
[3, [["善", ["完善"]], ["其身", ["自己"]]]],\
[4, [["锲", ["雕刻"]], ["镂", ["凿开"]]]],\
[5, [["不足", ["不足以", "没有必要"]]]],\
[6, [["鹜", ["野鸭子"]]]],\
[7, [["僧", ["僧人"]]]],\
[8, [["玉壶", ["品德纯洁无暇"]]]],\
[14, [["覆", ["翻覆"]], ["完", ["完整", "没有损坏"]]]],\
[15, [["务", ["务必", "一定"]], ["劝", ["勉励"]]]],\
[16, [["自胜", ["征服自己"]], ["自论", ["批判自己"]]]],\
[18, [["春红", ["春天的花儿"]]]],\
[20, [["劬劳", ["劳苦"]]]],\
[21, [["横眉", ["怒目而视的样子"]], ["孺子牛", ["全心全意为人民服务的人"]]]],\
[22, [["是", ["这"]], ["拂", ["违背"]]]],\
[23, [["恃", ["依靠"]], ["下", ["退让", "谦逊"]]]],\
[24, [["安", ["怎么"]], ["鸿鹄", ["天鹅"]]]],\
[26, [["厌", ["满足"]], ["吐哺", ["嘴里嚼着饭,还来不及下咽,又吐出来"]]]],\
[27, [["缘", ["因为"]]]],\
[29, [["末", ["树梢"]], ["掉", ["摇动", "摆动"]]]],\
[30, [["至", ["过于", "达到了极点"]]]],\
[32, [["强", ["勉强"]]]],\
[33, [["枢", ["旧式门扇的转轴"]]]],\
[35, [["丹青", ["绘画"]]]],\
[36, [["伯乐", ["善于选用人才的人"]]]],\
[39, [["泪", ["烛泪", "蜡烛燃烧时滴下的蜡油"]]]]\
]

zhushi5 = [\
[0, [["病树", ["枯树"]]]],\
[1, [["偕", ["一同", "一起"]]]],\
[2, [["惜", ["痛惜"]], ["但", ["只"]], ["知音", ["知心朋友"]]]],\
[3, [["晓", ["通晓", "懂得"]], ["识", ["识别"]]]],\
[5, [["见", ["显现"]], ["丹青", ["史册", "史书"]]]],\
[6, [["落红", ["飘落的花朵"]]]],\
[7, [["恐", ["担心"]]]],\
[8, [["所善", ["所喜爱的东西"]], ["九死", ["死了多次"]]]],\
[9, [["得兼", ["同时得到"]]]],\
[10, [["惑", ["迷惑"]]]],\
[11, [["知", ["理解", "了解"]]]],\
[13, [["极", ["尽头"]]]],\
[14, [["却", ["再", "还"]]]],\
[15, [["总", ["都", "全"]]]],\
[16, [["愁眠", ["因忧愁而未能入眠"]]]],\
[23, [["王谢", ["豪门世族"]]]],\
[24, [["清气", ["高洁的气节"]], ["乾坤", ["天地"]]]],\
[25, [["道", ["学说", "主张"]], ["务", ["讲求", "看重"]]]],\
[26, [["金风", ["秋风"]], ["玉露", ["冰凉的露水"]], ["金风玉露", ["七夕之夜"]]]],\
[27, [["闲", ["徒然"]]]],\
[28, [["怀土", ["怀念乡土"]], ["穷", ["穷困失意"]], ["达", ["得意显达"]]]],\
[29, [["板荡", ["社会动荡不安", "政局不稳定"]]]],\
[30, [["厌", ["嫌弃"]]]],\
[32, [["萧瑟", ["风吹树林声"]]]],\
[33, [["蓦然", ["突然"]], ["阑珊", ["零落"]]]],\
[34, [["飘风", ["狂风"]], ["朝", ["早晨"]], ["骤雨", ["暴雨", "急雨"]]]],\
[35, [["自在", ["自由自在"]]]],\
[36, [["齐", ["整治"]]]],\
[37, [["入耳", ["中听"]]]],\
[38, [["治", ["安定", "太平"]]]]\
]

m4 = """描写塞外一幅动人的草原放牧图
表面上写出一派生机勃勃的江南春景，实际上是描写重新出现的某种美好的社会景象
说明克服了自我的缺点，在立下志愿时才不会为了要胜过别人,而遭遇困难
说明不管在朝在野，都要保全个人的良好品德，有能力时，更要使德泽惠及众人
比喻坚持不懈、有恒心的人才能取得成功，相反的，没有恒心的人什么事也干不了
说明了应当以坦然的态度面对顺境与逆境
描写黄昏时分瑰丽迷人的景色
描写居处荒僻、幽静的景象，反映了隐居生活的闲适
比喻光明磊落，不受世俗污染的高尚品德
描写细雨蒙蒙的江南迷人春色
形容忧愁无穷无尽，难以自解
劝人对得失成败不必斤斤计较
形容当时诗人的心境是十分轻松愉快的
比喻一种潇洒自如的性格，给人一种轻淡而宁静的离愁
比喻一个国家如果被摧毁了，所有的人民也必会遭殃、受累
说明了奖赏和惩罚都必须及时，才能发挥劝善或警诫的效果
劝人凡事要有白知之明
赞颂事事以人民的利益为主，爱国爱民的好领袖
描写春残花谢，冷风寒雨的萧索景象，寄托作者深感人生短促、好景不常的悲哀
描绘深秋萧索而凄凉的景象
形容父母抚养子女，操劳辛苦，也用以表达对父母养育之恩的感激
说明为个人理想而奋斗的当儿，不理会一般人的无理指责，一心一意为后辈的利益而鞠躬尽瘁
说明一个人要成就一逢大事业，必定要经历许多磨难和挫折，即使受苦受累也不胡来，行为上能守节不乱
说明不傲慢、不自大、能自制是我们待人处事应有的态度
比喻胸怀大志的人，一般人往往不能理解他的志向
说明一个不顾廉耻的人，会因贪得无厌，而什么坏事都做得出来
表达了求贤若渴的愿望
包含着“当局者迷，旁观者清”的道理，告诉人们要客观看待问题
勉励人们要努力向上
比喻属下力量过于强大，就不听使唤，在上的就难以控制
说明为人处世不能过于斤斤计较，在一些非原则性的小事上，不能过于认真
形容辽阔的沙漠、荒原等地烟尘徐上，夕阳西下的景色
说明品德高尚的人宽宏大量，不会过于苛求，更不会强人所难
比喻人经常运动，才不会生病，也比经常运动的东西不易受侵蚀
描写诗人恬淡的个性和与世无争的心情
赞扬一个人品德高尚，不慕名利
比喻能识别人才的人，比人才更难得、更可贵
说明做某件事，本意不在这件事上，而在别的方面，比喻别有用心
比喻对亡妻的感情深挚不渝
比喻坚贞的爱情至死不渝"""

m5 = """说明新事物必将取代旧事物
说明情侣之间，约定白头到老，永不分离
感慨知音难寻
说明累积经验，可以提高一个人的辨识能力
比喻读书时要注意知识更新并要从生活中吸取新的养料，不断充实自己
赞颂临危不屈的忠贞之士所显现的坚贞不渝的节操和高尚气质
说明为培养新生代而贡献自己的力量，即使牺牲自己也在所不惜
说明做善事要发自内心；做了恶事要有羞愧反省之心
赞扬一个人坚持信念，不轻易改变自己的理想
表达了愿为正义事业而献身的决心
劝人勿太重视名和利，以致善良的本性被蒙蔽，而迷失了自己
感叹知己难求的忧思和苦闷
描写旧地重游，对前尘往事怀着无限的眷恋，对飞逝的时光引发起无限的惆怅和感触
反映出诗人对故土家园的思念之情
表达对远别的亲友和妻子的思念和渴望重逢之情
说明即将离别的感伤之情
描写霜天夜景，游人满怀愁绪
以萧瑟凄凉的秋天景色，衬托出有情人离别时的凄苦悲凉
描写江边平野雄浑宽阔的景观
描绘江南春景的广阔和丰富多彩
赞颂不肯苟且屈从的独立精神和高尚品德
比喻凡事等出了问题才去补救，已来不及了劝人要及时行事，以免后悔莫及
描写秋天苍茫和凄清的景色
感慨沧海桑田，世事变化极大
勉励人们不要迎合世俗，应保持清高节操的心志
劝导人们应当以才干实学来录用人才
强调真情的相聚即使短暂，要比虚假的朝夕相对来得珍贵和有意义
描写相隔两地的爱侣互相思念之情
说明怀念故乡之情是人人都有的，不应因个人的境遇好坏而有所变化
比喻在严峻的考验下，才能显示出一个人人的坚强意志和坚定的立场
说明对已经读过的好书要反复地阅读，深入思考，才能从中悟出新的道理来
劝勉人们要认真学习和要有不惧困难的精神
描写一个人虽经历风雨，只要泰然处之，便什么也不觉得了
形容一个人一直在努力寻觅某个人，却突然找到，心情非常喜悦
比喻事情不会持续至永远，终有停止的时候
表示人在遇到挫折时，因为无力改变处境而在心中产生了如缠绵细雨的愁绪
强调做事要按部就班，先从自己本身做起，修身养性，才有条件做好更大更重要的事
描写读书人不只是埋头学习，也深切关心周遭的事物
告诫人们要居安思危，对可能发生的任何威胁，要及时防备
前半句形容时光的飞逝，后半句则比喻世事多变，谁也无从预料它的结局"""

p4 = [1, 0.3, 0.15, 1, 0.45, 1, 1, 1, 0.05, 1, 1, 0.5, 0.6, 0.6, 1, 1, 1, 1, 0.05, 1, 1, 1, 1, 0.3, 0.2, 1, 0.1, 0.1, 1, 0.15, 0.05, 1, 1, 0.55, 1, 1, 1, 0.55, 0.4, 1]
p5 = [0.25, 1, 1, 0.2, 0.1, 1, 0.5, 0.4, 0.5, 1, 1, 1, 0.45, 0.3, 0.2, 1, 1, 1, 1, 1.0, 1, 0.25, 1, 0.15, 0.45, 0.05, 1, 1, 1, 0.35, 0.1, 0.3, 0.25, 1, 0.5, 1, 1, 0.55, 1, 1]
p4m = [0.7, 0.3, 0.15, 1, 0.45, 1, 0.7, 1, 0.05, 0.7, 1, 0.5, 0.6, 0.6, 1, 1, 1, 1, 0.05, 0.7, 1, 1, 1, 0.3, 0.2, 1, 0.1, 0.1, 1, 0.15, 0.05, 0.7, 1, 0.55, 1, 1, 1, 0.55, 0.4, 1]
p5m = [0.25, 1, 1, 0.2, 0.1, 1, 0.5, 0.4, 0.5, 1, 1, 1, 0.45, 0.3, 0.2, 1, 1, 1, 0.7, 0.7, 1, 0.25, 0.7, 0.15, 0.45, 0.05, 1, 1, 1, 0.35, 0.1, 0.3, 0.25, 1, 0.5, 1, 1, 0.55, 1, 1]

version = "development 0.2.0"

class shell(Cmd):
    intro = "中学生背名句\n"+version+"\nBy someone who hate memorizing stuff.\nType help or ? to list commands. Use handwrite input method or wubi input method for best result."
    prompt = ">>> "

    def do_train(self, arg):
        """Launch training. Training will begin with infinite loop on the selected mingju until you press Ctrl-C to exit. Questions that are answered wrongly will show up more frequent.
USAGE: train {form4|form5|all} [<start>] [<end>] [--p]
<start> and <end> is used to specify scope of Mingju to select. (TYPE=integer)
<start> is the index of first mingju, whereas <end> is the index of last mingju. All mingju between these two will be taken.
--p is an option to enable probabilistic mode. The probability of a question that never came out in SPM showing up is higher than that came out, and older questions will have a higher probability of showing up than newer questions."""
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
                p_table = list(p4)
            elif arg[0] == "form5":
                p_table = list(p5)
            else:
                p_table = p4+p5
        else:
            textlist = options[arg[0]].split("\n")
            if arg[0] == "form4":
                p_table = list(p4)
            elif arg[0] == "form5":
                p_table = list(p5)
            else:
                p_table = p4+p5
            textlist = textlist[start-1:end]
            p_table = p_table[start-1:end]
        if "--p" not in arg: #if probabilistic training disabled
            p_table = [1 for i in range(len(textlist))] #probability table is all one
        total=len(textlist)
        compare=[i for i in range(total)]
        used=[]
        try:
            num = 1
            wrong = 0
            review = []
            triad = []
            trained = []
            while True:
                question=random.choices(textlist, p_table)[0]
                while question in triad:
                    question=random.choices(textlist, p_table)[0]
                triad.append(question)
                if len(triad) > 3:
                    del triad[0]
                questions=re.split(',|;|\?',question) #question splitted
                questiona=questions[random.randint(0,len(questions)-1)] #question answer
                questionq=['__' if x==questiona else x for x in questions] #question question
                userans=input(str(num)+". "+str(questionq)+'\nAnswer: ')
                num+=1
                if question not in trained:
                    trained.append(question)
                if userans==questiona:
                    print('Correct!\n')
                    if any(question in sublist for sublist in review):
                        index = review.index([i for i in review if question in i][0])
                        if review[index][2] > 0:
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
            print("Percentage of mingju trained: {}%".format(str(round(len(trained)/len(textlist)*100, 2))))
            rev_mistake = input("Review mistake? [y/n]: ")
            if rev_mistake == "y":
                num = 1
                review.sort(key = lambda x:x[1], reverse = True)
                for i in review:
                    print(str(num)+". "+i[0]+", f="+str(i[1]))
                    num+=1
            rev_trained = input("Review mingju that are not trained? [y/n]: ")
            if rev_trained == "y":
                num = 1
                untrained = [x for x in textlist if x not in trained]
                for i in untrained:
                    print(str(num)+". "+i)
                    num+=1
            return

    def do_quiz(self, arg):
        """Launch quiz. Ctrl-C to quit. quiz differs from train in terms of:
1) quiz will not provide any answer at the time of answering.
2) One question will only appear once.
3) Score will be shown once quiz is finished.
USAGE: quiz {form4|form5|all} [<start>] [<end>]
<start> and <end> is used to specify scope of Mingju to select. (TYPE=integer)
<start> is the index of first mingju, whereas <end> is the index of last mingju. All mingju between these two will be taken."""
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
        """Training mode for zhushi. Loop infinitely until you press Ctrl+C to quit. Questions that are answered wrongly will show up more frequent.
USAGE: zhushi {form4|form5|all} [--p]
--p enable probabilistic training."""
        arg = arg.split()
        options = {"form4":[zhushi4,form4], "form5":[zhushi5,form5], "all":[zhushi4+[[x[0]+40, x[1]] for x in zhushi5],form4+"\n"+form5]}
        form = ["名句中的“{x}”指什么？", "名句中“{x}”的意思是什么？", "请写出名句中“{x}”的意思。", "“{x}”在名句中有什么含义？", "名句中“{x}”起着什么意思？", "“{x}”比喻什么？", "“{x}”是什么意思？"]
        #-------------Error handling----------------
        if len(arg) == 0:
            print(termcolor.colored("No argument!", "red"))
            return
        if arg[0] not in ["form4","form5","all"]:
            print(error_unknown(arg[0]))
            return
        #-----------------------------------------------
        #-------------Argument parsing------------------
        zhushilist = options[arg[0]][0]
        mingjulist = options[arg[0]][1].split("\n")
        if "--p" not in arg:
            p_table = [1 for i in range(len(mingjulist))]
        else:
            poptions = {"form4":p4, "form5":p5, "all":p4+p5}
            p_table = poptions[arg[0]]
        #-----------------------------------------------
        try:
            num = 1
            wrong = 0
            review = []
            triad = [] #I call this "triad repeating prevention" hehe
            trained = []
            def onwrong():
                nonlocal wrong, mingju, review, selzhushi, p_table, mingjulist
                wrong+=1
                if not any(mingju in sublist for sublist in review):
                    review.append([mingju, 1, 1, [selzhushi]])
                    p_table[mingjulist.index(mingju)]+=0.5
                else:
                    revindex = review.index([i for i in review if mingju in i][0])
                    review[revindex][1]+=1
                    review[revindex][2]+=1
                    if selzhushi not in review[revindex][3]:
                        review[revindex][3].append(selzhushi)
                    p_table[mingjulist.index(mingju)]+=0.5
            while True:
                mingju = random.choices(mingjulist, p_table)[0]
                while (not any(mingjulist.index(mingju) in sublist for sublist in zhushilist)) or (mingju in triad):
                    mingju = random.choices(mingjulist, p_table)[0]
                triad.append(mingju)
                if len(triad) > 3:
                    del triad[0]
                index = mingjulist.index(mingju)
                zhushi = [x for x in zhushilist if index in x][0]
                selzhushi = random.choices(zhushi[1])[0]
                selform = random.choices(form)[0]
                question = str(num)+". "+mingju+"\n"+selform.format(x=selzhushi[0])+"\n"
                userans = input(question+"Answer: ")
                num+=1
                if mingju not in trained:
                    trained.append(mingju)
                if userans in selzhushi[1]:
                    print("Correct!\n")
                    if any(mingju in sublist for sublist in review):
                        revindex = review.index([i for i in review if mingju in i][0])
                        if review[revindex][2] > 0:
                            p_table[mingjulist.index(mingju)]-=0.25
                            review[revindex][2]-=0.5
                elif len(userans) >= 3:
                    closematches = difflib.get_close_matches(userans, selzhushi[1])
                    if len(closematches) != 0:
                        simratio = difflib.SequenceMatcher(None,closematches[0],userans).ratio()
                        if simratio >= 0.6:
                            print("Correct!")
                            print("Similarity ratio: "+str(round(simratio, 4)))
                            print("Most similar answer: " + closematches[0] + "\n")
                            if any(mingju in sublist for sublist in review):
                                revindex = review.index([i for i in review if mingju in i][0])
                                if review[revindex][2] > 0:
                                    p_table[mingjulist.index(mingju)]-=0.25
                                    review[revindex][2]-=0.5
                        else:
                            print('Better luck next time :(')
                            print("Similarity ratio: "+str(round(simratio, 4)))
                            print('Correct answer: '+str(selzhushi[1])+'\n')
                            onwrong()
                    else:
                        print('Better luck next time :(')
                        print('Correct answer: '+str(selzhushi[1])+'\n')
                        onwrong()
                else:
                    print('Better luck next time :(')
                    print('Correct answer: '+str(selzhushi[1])+'\n')
                    onwrong()
        except KeyboardInterrupt:
            print("\n")
            text = "Total number of tries: "+str(num-1)+"\n"+termcolor.colored("Total wrong answer: "+str(wrong), "red")
            print(text)
            print("Percentage of zhushi trained: {}%".format(str(round(len(trained)/len(zhushilist)*100, 2))))
            rev_mistake = input("Review mistake? [y/n]: ")
            if rev_mistake == "y":
                num = 1
                review.sort(key = lambda x:x[1], reverse = True)
                for i in review:
                    print(str(num)+". "+i[0]+", f="+str(i[1]))
                    for x in i[3]:
                        print("    "+termcolor.colored(x[0]+":"+str(x[1]), "green"))
                    num+=1
            rev_zhushi = input("Review zhushi that are not trained? [y/n]: ")
            if rev_zhushi == "y":
                zhushirevindex = [mingjulist.index(i) for i in trained]
                zhushirev = [i for i in zhushilist if i[0] not in zhushirevindex]
                num = 1
                for i in zhushirev:
                    print(str(num) + ". " + mingjulist[i[0]])
                    for j in i[1]:
                        print(termcolor.colored("    " + j[0]+":"+str(j[1]), "green"))
                    num+=1
            return

    def do_list(self, arg):
        """List mingju according to the arguments provided.
USAGE: list {form4|form5|all} [<start>] [<end>] [-z] [-h]
<start> and <end> is used to specify scope of Mingju to select. (TYPE=integer)
<start> is the index of first mingju, whereas <end> is the index of last mingju. All mingju between these two will be taken.
Use -z to print zhushi, -h to print hanyi, or both to print both of them."""
        arg = arg.split()
        start = end = None
        #-------------Error handling----------------
        if len(arg) == 0:
            print(termcolor.colored("No argument!", "red"))
            return
        if arg[0] not in ["form4","form5","all"]:
            print(error_unknown(arg[0]))
            return
        try:
            start = int(arg[1])
            end = int(arg[2])
        except Exception as e:
            pass
            #print(termcolor.colored(repr(e), "red"))
        #-----------------------------------------------
        options = {"form4":[form4, m4], "form5":[form5, m5], "all":[form4+"\n"+form5, m4+"\n"+m5]}
        a = 1
        if arg[0] == "form4":
            zhushilist = zhushi4
        elif arg[0] == "form5":
            zhushilist = zhushi5
        else:
            zs5temp = [[x[0]+40, x[1]] for x in zhushi5]
            zhushilist = zhushi4 + zs5temp

        textlist = options[arg[0]][0].split("\n")
        textlistold = textlist
        if start != None and end != None:
            textlist = textlist[start-1:end]
        hanyilist = options[arg[0]][1].split("\n")
        for i in textlist:
            print(str(a) + ". " + i)
            if "-z" in arg:
                for x in zhushilist:
                    if x[0] == textlistold.index(i):
                        for y in range(1, len(x[1])):
                            print(termcolor.colored("        " + x[1][y][0] + ": " + str(x[1][y][1]), "cyan"))
            if "-h" in arg:
                print(termcolor.colored("    "+hanyilist[textlistold.index(i)], "green"))
            a+=1

    def do_hanyi(self, arg):
        """Training mode for hanyi. Ctrl-C to quit.
USAGE: hanyi {form4|form5|all} [<start>] [<end>] [--p]
<start> and <end> is used to specify scope of Mingju to select. (TYPE=integer)
<start> is the index of first mingju, whereas <end> is the index of last mingju. All mingju between these two will be taken.
--p enable probabilistic training."""
        start = end = None
        arg = arg.split()
        options = {"form4":[form4, m4, list(p4m)], "form5":[form5, m5, list(p5m)], "all":[form4+"\n"+form5, m4+"\n"+m5, list(p4m+p5m)]}
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
            mingjulist = options[arg[0]][0].split("\n")
            hanyilist = options[arg[0]][1].split("\n")
        else:
            mingjulist = options[arg[0]][0].split("\n")
            mingjulist = mingjulist[start-1:end]
            hanyilist = options[arg[0]][1].split("\n")
            hanyilist = hanyilist[start-1:end]
        #------------------------------------
        #--------------------argparsing-----------------
        if "--p" in arg:
            p_table = options[arg[0]][2]
            if start != None and end != None:
                p_table = p_table[start-1:end]
        else:
            p_table = [1 for i in range(len(mingjulist))]
        #--------------------------------------------------
        try:
            num = 1
            wrong = 0
            review = []
            triad = []
            trained =[]
            score = []
            while True:
                question = random.choices(mingjulist, p_table)[0]
                while question in triad:
                    question=random.choices(mingjulist, p_table)[0]
                triad.append(question)
                if len(triad) > 3:
                    del triad[0]
                answer = hanyilist[mingjulist.index(question)]
                print(str(num) + ". " + question)
                userans = input("Answer: ")
                simpercent = round(difflib.SequenceMatcher(None, userans, answer).ratio()*100, 2)
                score.append(simpercent)
                trained.append(question)
                if simpercent >= 70:
                    print("Similarity: "+termcolor.colored(str(simpercent)+"%", "green"))
                    if any(question in sublist for sublist in review):
                        revindex = review.index([i for i in review if question in i][0])
                        if review[revindex][2] > 0:
                            p_table[mingjulist.index(question)]-=0.25
                            review[revindex][2]-=0.5
                else:
                    print("Similarity: "+termcolor.colored(str(simpercent)+"%", "red"))
                    if not any(question in sublist for sublist in review):
                        review.append([question, 1, 1])
                        p_table[mingjulist.index(question)]+=0.5
                    else:
                        revindex = review.index([i for i in review if question in i][0])
                        review[revindex][1]+=1
                        review[revindex][2]+=1
                        p_table[mingjulist.index(question)]+=0.5
                    wrong+=1
                if simpercent != 100:
                    print("Actual answer: "+answer+"\n")
                else:
                    print("\n")
                num+=1
        except KeyboardInterrupt:
            print("\n")
            text = "Total number of tries: "+str(num-1)+"\n"+termcolor.colored("Total wrong answer: "+str(wrong), "red")
            print(text)
            print("Percentage of hanyi trained: {}%".format(str(round(len(trained)/len(hanyilist)*100, 2))))
            avgscore = round(sum(score)/len(score), 2)
            if avgscore >= 70:
                avgscore = termcolor.colored(str(avgscore)+"%", "green")
            else:
                avgscore = termcolor.colored(str(avgscore)+"%", "red")
            print("Average similarity score: {}".format(avgscore))
            rev_mistake = input("Review mistake? [y/n]: ")
            if rev_mistake == "y":
                num = 1
                review.sort(key = lambda x:x[1], reverse = True)
                for i in review:
                    print(str(num)+". "+i[0]+", f="+str(i[1]))
                    print("   "+termcolor.colored(hanyilist[mingjulist.index(i[0])], "cyan"))
                    num+=1
            rev_hanyi = input("Review hanyi that are not trained? [y/n]: ")
            if rev_hanyi == "y":
                hanyirevindex = [i for i in range(len(mingjulist)) if mingjulist[i] not in trained]
                num = 1
                for i in hanyirevindex:
                    print(str(num) + ". " + mingjulist[i])
                    print(termcolor.colored("    " + hanyilist[i], "green"))
                    num+=1
            return

    def do_exit(self, arg):
        """Quit the program."""
        print("")
        return True

    def do_about(self, arg):
        """About the author and this program."""
        print("中学生背名句")
        print("Version: "+version)
        print("Created by: TheNooB")
        print("Github project page: https://github.com/TheNooB2706/mingju")

    do_EOF = do_exit

def error_unknown(text):
    return termcolor.colored("Unknown input: " + text, "red")

shell().cmdloop()
