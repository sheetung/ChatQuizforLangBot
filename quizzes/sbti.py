from __future__ import annotations

import random

from quizzes.base import BaseQuiz, QuizQuestion


DIMENSION_META = {
    "S1": "S1 自尊自信",
    "S2": "S2 自我清晰度",
    "S3": "S3 核心价值",
    "E1": "E1 依恋安全感",
    "E2": "E2 情感投入度",
    "E3": "E3 边界与依赖",
    "A1": "A1 世界观倾向",
    "A2": "A2 规则与灵活度",
    "A3": "A3 人生意义感",
    "Ac1": "Ac1 动机导向",
    "Ac2": "Ac2 决策风格",
    "Ac3": "Ac3 执行模式",
    "So1": "So1 社交主动性",
    "So2": "So2 人际边界感",
    "So3": "So3 表达与真实度",
}

DIMENSION_ORDER = [
    "S1",
    "S2",
    "S3",
    "E1",
    "E2",
    "E3",
    "A1",
    "A2",
    "A3",
    "Ac1",
    "Ac2",
    "Ac3",
    "So1",
    "So2",
    "So3",
]

DIMENSION_EXPLANATIONS = {
    "S1": {"L": "容易先否定自己。", "M": "自信值随状态波动。", "H": "比较稳，不容易被一句话击穿。"},
    "S2": {"L": "常在我是谁里循环缓存。", "M": "大体认得自己，偶尔摇摆。", "H": "对自己的脾气和底线比较清楚。"},
    "S3": {"L": "更在意舒服和安全。", "M": "想上进，也想躺。", "H": "容易被目标和信念推着往前。"},
    "E1": {"L": "关系里警报器很灵。", "M": "在信任和怀疑之间拉扯。", "H": "更愿意相信关系本身。"},
    "E2": {"L": "感情投入偏克制。", "M": "会投入，但会留后手。", "H": "一旦认定就容易认真。"},
    "E3": {"L": "很在意关系温度。", "M": "亲密和独立都要一点。", "H": "再爱也得留一块自己的地。"},
    "A1": {"L": "先怀疑，再靠近。", "M": "观望是本能。", "H": "更愿意相信人性和善意。"},
    "A2": {"L": "规则能绕就绕。", "M": "该守的时候守。", "H": "秩序感较强。"},
    "A3": {"L": "很多事像在走过场。", "M": "人生观半开机。", "H": "做事更有方向。"},
    "Ac1": {"L": "先考虑别翻车。", "M": "想赢，也怕麻烦。", "H": "更容易被推进感点燃。"},
    "Ac2": {"L": "脑内会议经常超时。", "M": "正常犹豫。", "H": "拍板速度快。"},
    "Ac3": {"L": "和死线很有感情。", "M": "状态看时机。", "H": "事情不落地就难受。"},
    "So1": {"L": "社交启动慢热。", "M": "有人来就接。", "H": "更愿意主动打开场子。"},
    "So2": {"L": "熟了就容易划进内圈。", "M": "想亲近，也想留缝。", "H": "靠太近会本能后退半步。"},
    "So3": {"L": "表达更直接。", "M": "会看气氛。", "H": "对不同场景切换更熟练。"},
}

QUESTIONS = [
    QuizQuestion("q1", "我不仅是屌丝，我还是joker,我还是咸鱼，这辈子没谈过一场恋爱，胆怯又自卑，我的青春就是一场又一场的意淫，每一天幻想着我也能有一个女孩子和我一起压马路，一起逛街，一起玩，现实却是爆了父母金币，读了个烂学校，混日子之后找班上，没有理想，没有目标，没有能力的三无人员，每次看到你能在网上开屌丝的玩笑，我都想哭，我就是地底下的老鼠，透过下水井的缝隙，窥探地上的各种美好，每一次看到这种都是对我心灵的一次伤害，对我生存空间的一次压缩，求求哥们给我们这种小丑一点活路吧，我真的不想在白天把枕巾哭湿一大片", [{"label": "我哭了。。", "value": 1}, {"label": "这是什么。。", "value": 2}, {"label": "这不是我！", "value": 3}], dim="S1"),
    QuizQuestion("q2", "我不够好，周围的人都比我优秀", [{"label": "确实", "value": 1}, {"label": "有时", "value": 2}, {"label": "不是", "value": 3}], dim="S1"),
    QuizQuestion("q3", "我很清楚真正的自己是什么样的", [{"label": "不认同", "value": 1}, {"label": "中立", "value": 2}, {"label": "认同", "value": 3}], dim="S2"),
    QuizQuestion("q4", "我内心有真正追求的东西", [{"label": "不认同", "value": 1}, {"label": "中立", "value": 2}, {"label": "认同", "value": 3}], dim="S2"),
    QuizQuestion("q5", "我一定要不断往上爬、变得更厉害", [{"label": "不认同", "value": 1}, {"label": "中立", "value": 2}, {"label": "认同", "value": 3}], dim="S3"),
    QuizQuestion("q6", "外人的评价对我来说无所吊谓。", [{"label": "不认同", "value": 1}, {"label": "中立", "value": 2}, {"label": "认同", "value": 3}], dim="S3"),
    QuizQuestion("q7", "对象超过5小时没回消息，说自己窜稀了，你会怎么想？", [{"label": "拉稀不可能5小时，也许ta隐瞒了我。", "value": 1}, {"label": "在信任和怀疑之间摇摆。", "value": 2}, {"label": "也许今天ta真的不太舒服。", "value": 3}], dim="E1"),
    QuizQuestion("q8", "我在感情里经常担心被对方抛弃", [{"label": "是的", "value": 1}, {"label": "偶尔", "value": 2}, {"label": "不是", "value": 3}], dim="E1"),
    QuizQuestion("q9", "我对天发誓，我对待每一份感情都是认真的！", [{"label": "并没有", "value": 1}, {"label": "也许？", "value": 2}, {"label": "是的！（问心无愧骄傲脸）", "value": 3}], dim="E2"),
    QuizQuestion("q10", "你的恋爱对象是一个尊老爱幼，温柔敦厚，洁身自好，光明磊落，大义凛然，能言善辩，口才流利，观察入微，见多识广，博学多才，诲人不倦，和蔼可亲，平易近人，心地善良，慈眉善目，积极进取，意气风发，玉树临风，国色天香，倾国倾城，花容月貌的人，此时你会？", [{"label": "就算ta再优秀我也不会陷入太深。", "value": 1}, {"label": "会介于A和C之间。", "value": 2}, {"label": "会非常珍惜ta，也许会变成恋爱脑。", "value": 3}], dim="E2"),
    QuizQuestion("q11", "恋爱后，对象非常黏人，你作何感想？", [{"label": "那很爽了", "value": 1}, {"label": "都行无所谓", "value": 2}, {"label": "我更喜欢保留独立空间", "value": 3}], dim="E3"),
    QuizQuestion("q12", "我在任何关系里都很重视个人空间", [{"label": "我更喜欢依赖与被依赖", "value": 1}, {"label": "看情况", "value": 2}, {"label": "是的！（斩钉截铁地说道）", "value": 3}], dim="E3"),
    QuizQuestion("q13", "大多数人是善良的", [{"label": "其实邪恶的人心比世界上的痔疮更多。", "value": 1}, {"label": "也许吧。", "value": 2}, {"label": "是的，我愿相信好人更多。", "value": 3}], dim="A1"),
    QuizQuestion("q14", "你走在街上，一位萌萌的小女孩蹦蹦跳跳地朝你走来（正脸、侧脸看都萌，用vivo、苹果、华为、OPPO手机看都萌，实在是非常萌的那种），她递给你一根棒棒糖，此时你作何感想？", [{"label": "呜呜她真好真可爱！居然给我棒棒糖！", "value": 3}, {"label": "一脸懵逼，作挠头状", "value": 2}, {"label": "这也许是一种新型诈骗？还是走开为好。", "value": 1}], dim="A1"),
    QuizQuestion("q15", "快考试了，学校规定必须上晚自习，请假会扣分，但今晚你约了女/男神一起玩《绝地求生：刺激战场》（一款刺激的游戏），你怎么办？", [{"label": "翘了！反正就一次！", "value": 1}, {"label": "干脆请个假吧。", "value": 2}, {"label": "都快考试了还去啥。", "value": 3}], dim="A2"),
    QuizQuestion("q16", "我喜欢打破常规，不喜欢被束缚", [{"label": "认同", "value": 1}, {"label": "保持中立", "value": 2}, {"label": "不认同", "value": 3}], dim="A2"),
    QuizQuestion("q17", "我做事通常有目标。", [{"label": "不认同", "value": 1}, {"label": "中立", "value": 2}, {"label": "认同", "value": 3}], dim="A3"),
    QuizQuestion("q18", "突然某一天，我意识到人生哪有什么他妈的狗屁意义，人不过是和动物一样被各种欲望支配着，纯纯是被激素控制的东西，饿了就吃，困了就睡，一发情就想交配，我们简直和猪狗一样没什么区别。", [{"label": "是这样的。", "value": 1}, {"label": "也许是，也许不是。", "value": 2}, {"label": "这简直是胡扯", "value": 3}], dim="A3"),
    QuizQuestion("q19", "我做事主要为了取得成果和进步，而不是避免麻烦和风险。", [{"label": "不认同", "value": 1}, {"label": "中立", "value": 2}, {"label": "认同", "value": 3}], dim="Ac1"),
    QuizQuestion("q20", "你因便秘坐在马桶上（已长达30分钟），拉不出很难受。此时你更像", [{"label": "再坐三十分钟看看，说不定就有了。", "value": 1}, {"label": "用力拍打自己的屁股并说：死屁股，快拉啊！", "value": 2}, {"label": "使用开塞露，快点拉出来才好。", "value": 3}], dim="Ac1"),
    QuizQuestion("q21", "我做决定比较果断，不喜欢犹豫", [{"label": "不认同", "value": 1}, {"label": "中立", "value": 2}, {"label": "认同", "value": 3}], dim="Ac2"),
    QuizQuestion("q22", "此题没有题目，请盲选", [{"label": "反复思考后感觉应该选A？", "value": 1}, {"label": "啊，要不选B？", "value": 2}, {"label": "不会就选C？", "value": 3}], dim="Ac2"),
    QuizQuestion("q23", "别人说你“执行力强”，你内心更接近哪句？", [{"label": "我被逼到最后确实执行力超强。。。", "value": 1}, {"label": "啊，有时候吧。", "value": 2}, {"label": "是的，事情本来就该被推进", "value": 3}], dim="Ac3"),
    QuizQuestion("q24", "我做事常常有计划，____", [{"label": "然而计划不如变化快。", "value": 1}, {"label": "有时能完成，有时不能。", "value": 2}, {"label": "我讨厌被打破计划。", "value": 3}], dim="Ac3"),
    QuizQuestion("q25", "你因玩《第五人格》（一款刺激的游戏）而结识许多网友，并被邀请线下见面，你的想法是？", [{"label": "网上口嗨下就算了，真见面还是有点忐忑。", "value": 1}, {"label": "见网友也挺好，反正谁来聊我就聊两句。", "value": 2}, {"label": "我会打扮一番并热情聊天，万一呢，我是说万一呢？", "value": 3}], dim="So1"),
    QuizQuestion("q26", "朋友带了ta的朋友一起来玩，你最可能的状态是", [{"label": "对朋友的朋友天然有点距离感，怕影响二人关系", "value": 1}, {"label": "看对方，能玩就玩。", "value": 2}, {"label": "朋友的朋友应该也算我的朋友！要热情聊天", "value": 3}], dim="So1"),
    QuizQuestion("q27", "我和人相处主打一个电子围栏，靠太近会自动报警。", [{"label": "认同", "value": 3}, {"label": "中立", "value": 2}, {"label": "不认同", "value": 1}], dim="So2"),
    QuizQuestion("q28", "我渴望和我信任的人关系密切，熟得像失散多年的亲戚。", [{"label": "认同", "value": 1}, {"label": "中立", "value": 2}, {"label": "不认同", "value": 3}], dim="So2"),
    QuizQuestion("q29", "有时候你明明对一件事有不同的、负面的看法，但最后没说出来。多数情况下原因是：", [{"label": "这种情况较少。", "value": 1}, {"label": "可能碍于情面或者关系。", "value": 2}, {"label": "不想让别人知道自己是个阴暗的人。", "value": 3}], dim="So3"),
    QuizQuestion("q30", "我在不同人面前会表现出不一样的自己", [{"label": "不认同", "value": 1}, {"label": "中立", "value": 2}, {"label": "认同", "value": 3}], dim="So3"),
]

DRINK_GATE_Q1 = QuizQuestion(
    "drink_gate_q1",
    "您平时有什么爱好？",
    [{"label": "吃喝拉撒", "value": 1}, {"label": "艺术爱好", "value": 2}, {"label": "饮酒", "value": 3}, {"label": "健身", "value": 4}],
    special=True,
    kind="drink_gate",
)
DRINK_GATE_Q2 = QuizQuestion(
    "drink_gate_q2",
    "您对饮酒的态度是？",
    [{"label": "小酌怡情，喝不了太多。", "value": 1}, {"label": "我习惯将白酒灌在保温杯，当白开水喝，酒精令我信服。", "value": 2}],
    special=True,
    kind="drink_trigger",
)

TYPE_LIBRARY = {
    "CTRL": {"cn": "拿捏者", "intro": "怎么样，被我拿捏了吧？", "desc": "像人形任务管理器，规则感、推进力和拿捏能力都很强。"},
    "ATM-er": {"cn": "送钱者", "intro": "你以为我很有钱吗？", "desc": "可靠到像一台老 ATM 机，总在替别人支付时间、精力和耐心。"},
    "Dior-s": {"cn": "屌丝", "intro": "等着我屌丝逆袭。", "desc": "对成功学和消费主义自带免疫，擅长躺平式看穿一切。"},
    "BOSS": {"cn": "领导者", "intro": "方向盘给我，我来开。", "desc": "效率与秩序感都很强，喜欢掌控方向。"},
    "THAN-K": {"cn": "感恩者", "intro": "我感谢苍天！我感谢大地！", "desc": "自带温润和正能量滤镜，习惯从糟糕里找出可感恩的部分。"},
    "OH-NO": {"cn": "哦不人", "intro": "哦不！我怎么会是这个人格？！", "desc": "风险感知灵敏，特别擅长提前规避混乱。"},
    "GOGO": {"cn": "行者", "intro": "gogogo~出发咯", "desc": "想到就做，行动和完成欲很强。"},
    "SEXY": {"cn": "尤物", "intro": "您就是天生的尤物！", "desc": "存在感和吸引力很强，不太需要刻意表达。"},
    "LOVE-R": {"cn": "多情者", "intro": "爱意太满，现实显得有点贫瘠。", "desc": "情感丰沛，容易认真，也容易浪漫化关系。"},
    "MUM": {"cn": "妈妈", "intro": "或许...我可以叫你妈妈吗....?", "desc": "共情力强，温柔且擅长照顾他人。"},
    "FAKE": {"cn": "伪人", "intro": "已经，没有人类了。", "desc": "很会切换社交面具，适应不同场景。"},
    "OJBK": {"cn": "无所谓人", "intro": "我说随便，是真的随便。", "desc": "很多事都不太想争，主打一个都行。"},
    "MALO": {"cn": "吗喽", "intro": "人生是个副本，而我只是一只吗喽。", "desc": "脑洞和顽皮感都很强，喜欢打破一点无聊。"},
    "JOKE-R": {"cn": "小丑", "intro": "原来我们都是小丑。", "desc": "很会活跃气氛，也可能用玩笑包住情绪。"},
    "WOC!": {"cn": "握草人", "intro": "卧槽，我怎么是这个人格？", "desc": "表面惊呼，内里常常早有判断。"},
    "THIN-K": {"cn": "思考者", "intro": "已深度思考100s。", "desc": "思辨性强，独处和分析都很有存在感。"},
    "SHIT": {"cn": "愤世者", "intro": "这个世界，构石一坨。", "desc": "嘴上嫌弃，手上收拾，愤世外壳下常有强执行。"},
    "ZZZZ": {"cn": "装死者", "intro": "我没死，我只是在睡觉。", "desc": "平时低反应，死线一到突然觉醒。"},
    "POOR": {"cn": "贫困者", "intro": "我穷，但我很专。", "desc": "会把精力狠狠砸进真正重要的一件事里。"},
    "MONK": {"cn": "僧人", "intro": "没有那种世俗的欲望。", "desc": "边界感强，特别需要自己的清净空间。"},
    "IMSB": {"cn": "傻者", "intro": "认真的么？我真的是傻逼么？", "desc": "脑内一半冲锋一半自我否定，戏很多。"},
    "SOLO": {"cn": "孤儿", "intro": "我哭了，我怎么会是孤儿？", "desc": "容易自我保护，主动拉开距离。"},
    "FUCK": {"cn": "草者", "intro": "操！这是什么人格？", "desc": "生命力野蛮，规则感弱，情绪拨片感明显。"},
    "DEAD": {"cn": "死者", "intro": "我，还活着吗？", "desc": "对很多主流意义和欲望都有点失去兴趣。"},
    "IMFW": {"cn": "废物", "intro": "我真的...是废物吗？", "desc": "安全感偏弱，也比较容易认真和依赖。"},
    "HHHH": {"cn": "傻乐者", "intro": "哈哈哈哈哈哈。", "desc": "标准人格库都对你的脑回路罢工了。"},
    "DRUNK": {"cn": "酒鬼", "intro": "烈酒烧喉，不得不醉。", "desc": "隐藏人格触发，乙醇亲和性过强。"},
}

NORMAL_TYPES = [
    {"code": "CTRL", "pattern": "HHH-HMH-MHH-HHH-MHM"},
    {"code": "ATM-er", "pattern": "HHH-HHM-HHH-HMH-MHL"},
    {"code": "Dior-s", "pattern": "MHM-MMH-MHM-HMH-LHL"},
    {"code": "BOSS", "pattern": "HHH-HMH-MMH-HHH-LHL"},
    {"code": "THAN-K", "pattern": "MHM-HMM-HHM-MMH-MHL"},
    {"code": "OH-NO", "pattern": "HHL-LMH-LHH-HHM-LHL"},
    {"code": "GOGO", "pattern": "HHM-HMH-MMH-HHH-MHM"},
    {"code": "SEXY", "pattern": "HMH-HHL-HMM-HMM-HLH"},
    {"code": "LOVE-R", "pattern": "MLH-LHL-HLH-MLM-MLH"},
    {"code": "MUM", "pattern": "MMH-MHL-HMM-LMM-HLL"},
    {"code": "FAKE", "pattern": "HLM-MML-MLM-MLM-HLH"},
    {"code": "OJBK", "pattern": "MMH-MMM-HML-LMM-MML"},
    {"code": "MALO", "pattern": "MLH-MHM-MLH-MLH-LMH"},
    {"code": "JOKE-R", "pattern": "LLH-LHL-LML-LLL-MLM"},
    {"code": "WOC!", "pattern": "HHL-HMH-MMH-HHM-LHH"},
    {"code": "THIN-K", "pattern": "HHL-HMH-MLH-MHM-LHH"},
    {"code": "SHIT", "pattern": "HHL-HLH-LMM-HHM-LHH"},
    {"code": "ZZZZ", "pattern": "MHL-MLH-LML-MML-LHM"},
    {"code": "POOR", "pattern": "HHL-MLH-LMH-HHH-LHL"},
    {"code": "MONK", "pattern": "HHL-LLH-LLM-MML-LHM"},
    {"code": "IMSB", "pattern": "LLM-LMM-LLL-LLL-MLM"},
    {"code": "SOLO", "pattern": "LML-LLH-LHL-LML-LHM"},
    {"code": "FUCK", "pattern": "MLL-LHL-LLM-MLL-HLH"},
    {"code": "DEAD", "pattern": "LLL-LLM-LML-LLL-LHM"},
    {"code": "IMFW", "pattern": "LLH-LHL-LML-LLL-MLL"},
]


class SbtiQuiz(BaseQuiz):
    key = "sbti"
    title = "sbti 测试"

    def build_questions(self) -> list[QuizQuestion]:
        questions = list(QUESTIONS)
        random.shuffle(questions)
        insert_index = random.randint(1, len(questions))
        return questions[:insert_index] + [DRINK_GATE_Q1] + questions[insert_index:]

    def render_intro(self) -> str:
        return (
            "SBTI 私聊测试开始。\n"
            "这是一个对话式娱乐测试，我会逐题发给你，你只要回复选项字母或数字就行。\n"
            "中途回复 `取消` 可以结束，重新发送 `/测试 sbti` 会从头开始。\n\n"
            "本测试仅供娱乐。"
        )

    def apply_answer(
        self,
        questions: list[QuizQuestion],
        answers: dict[str, int],
        current_index: int,
        answer_value: int,
    ) -> tuple[list[QuizQuestion], dict[str, int], int]:
        updated_answers = dict(answers)
        current_question = questions[current_index]
        updated_answers[current_question.id] = answer_value
        updated_questions = list(questions)

        if current_question.id == DRINK_GATE_Q1.id:
            if answer_value == 3:
                updated_questions.insert(current_index + 1, DRINK_GATE_Q2)
            else:
                updated_answers.pop(DRINK_GATE_Q2.id, None)
                updated_questions = [question for question in updated_questions if question.id != DRINK_GATE_Q2.id]

        return updated_questions, updated_answers, current_index + 1

    def render_result(self, answers: dict[str, int]) -> str:
        raw_scores = {dim: 0 for dim in DIMENSION_META}
        levels: dict[str, str] = {}
        for question in QUESTIONS:
            raw_scores[question.dim] += int(answers.get(question.id, 0))
        for dim, score in raw_scores.items():
            levels[dim] = self._sum_to_level(score)

        user_vector = [self._level_num(levels[dim]) for dim in DIMENSION_ORDER]
        ranked = []
        for normal_type in NORMAL_TYPES:
            pattern_vector = [self._level_num(level) for level in normal_type["pattern"].replace("-", "")]
            distance = 0
            exact = 0
            for idx, value in enumerate(pattern_vector):
                diff = abs(user_vector[idx] - value)
                distance += diff
                if diff == 0:
                    exact += 1
            similarity = max(0, round((1 - distance / 30) * 100))
            ranked.append(
                {
                    **normal_type,
                    **TYPE_LIBRARY[normal_type["code"]],
                    "distance": distance,
                    "exact": exact,
                    "similarity": similarity,
                }
            )

        ranked.sort(key=lambda item: (item["distance"], -item["exact"], -item["similarity"]))
        best_normal = ranked[0]

        if answers.get(DRINK_GATE_Q2.id) == 2:
            final_type = {"code": "DRUNK", **TYPE_LIBRARY["DRUNK"]}
            badge = "匹配度 100% · 酒精异常因子已接管"
            sub = f"常规人格参考是 {best_normal['code']}（{best_normal['cn']}），但隐藏人格已激活。"
        elif best_normal["similarity"] < 60:
            final_type = {"code": "HHHH", **TYPE_LIBRARY["HHHH"]}
            badge = f"标准人格库最高匹配仅 {best_normal['similarity']}%"
            sub = "标准人格库对你的脑回路集体罢工了，于是系统把你强制分配给了 HHHH。"
        else:
            final_type = best_normal
            badge = f"匹配度 {best_normal['similarity']}% · 精准命中 {best_normal['exact']}/15 维"
            sub = "维度命中度较高，当前结果可视为你的第一人格画像。"

        top_three = " / ".join(f"{item['code']}({item['similarity']}%)" for item in ranked[:3])
        dim_lines = []
        for dim in DIMENSION_ORDER:
            level = levels[dim]
            dim_lines.append(
                f"- {DIMENSION_META[dim]}: {level} / {raw_scores[dim]}分 · {DIMENSION_EXPLANATIONS[dim][level]}"
            )

        return "\n".join(
            [
                "SBTI 测试结果",
                f"{final_type['code']}（{final_type['cn']}）",
                final_type["intro"],
                badge,
                sub,
                "",
                "人格解读：",
                final_type["desc"],
                "",
                f"前三匹配：{top_three}",
                "",
                "十五维度评分：",
                *dim_lines,
                "",
                "本测试仅供娱乐，请勿当作医学、心理诊断或人生判决书。",
            ]
        )

    def _sum_to_level(self, score: int) -> str:
        if score <= 3:
            return "L"
        if score == 4:
            return "M"
        return "H"

    def _level_num(self, level: str) -> int:
        return {"L": 1, "M": 2, "H": 3}[level]
