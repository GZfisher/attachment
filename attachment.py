import streamlit as st

# 定义题目和分类
questions = [
    {"id": 1, "text": "我常常担心另一半不爱我了。", "category": "A"},
    {"id": 2, "text": "我感觉与另一半很容易陷入热恋。", "category": "B"},
    {"id": 3, "text": "我很担心另一半了解真实的我以后，就不再喜欢我了。", "category": "A"},
    {"id": 4, "text": "我感觉自己在分手以后很快就能自愈。我都很惊讶，自己怎么能那么快就忘记一个人。", "category": "C"},
    {"id": 5, "text": "我在单身状态时会非常焦虑，感觉生活若有所失。", "category": "A"},
    {"id": 6, "text": "我在另一半情绪失落的时候，很难给予对方情感支持。", "category": "C"},
    {"id": 7, "text": "每当另一半不在身边，我都很害怕对方被别的人吸引。", "category": "A"},
    {"id": 8, "text": "我非常享受依靠另一半的感觉。", "category": "B"},
    {"id": 9, "text": "对于我来说，独立性比亲密关系更重要。", "category": "C"},
    {"id": 10, "text": "我不想将内心最深处的感觉分享给另一半。", "category": "C"},
    {"id": 11, "text": "每当我与另一半分享感受时，都害怕对方难以感同身受。", "category": "A"},
    {"id": 12, "text": "我对自己的亲密关系大体满意。", "category": "B"},
    {"id": 13, "text": "我不觉得在亲密关系中付出过多。", "category": "B"},
    {"id": 14, "text": "我常常思考自己的恋爱关系。", "category": "A"},
    {"id": 15, "text": "我觉得很难去依靠另一半。", "category": "C"},
    {"id": 16, "text": "我会很快对另一半产生依恋。", "category": "A"},
    {"id": 17, "text": "我能很轻易地将自己的需求传达给对方。", "category": "B"},
    {"id": 18, "text": "我有时会莫名其妙地对另一半发火。", "category": "C"},
    {"id": 19, "text": "我对另一半的情绪十分敏感。", "category": "A"},
    {"id": 20, "text": "我相信大多数人都是诚实可靠的。", "category": "B"},
    {"id": 21, "text": "比起固定的性伴侣来，我更偏爱与不同人之间的露水情缘。", "category": "C"},
    {"id": 22, "text": "我很乐意跟另一半分享自己的想法和感受。", "category": "B"},
    {"id": 23, "text": "我常常担心另一半离我而去以后，我就再也找不到其他人了。", "category": "A"},
    {"id": 24, "text": "另一半离我太近时，我会感觉到焦虑。", "category": "C"},
    {"id": 25, "text": "我在与对方争执时，总会冲动之下说出令我后悔的话，而不擅长就事论事。", "category": "A"},
    {"id": 26, "text": "与另一半的不愉快，不会令我对我们的关系产生怀疑。", "category": "B"},
    {"id": 27, "text": "我的另一半总会提出一些让我觉得过分亲密的请求。", "category": "C"},
    {"id": 28, "text": "我常担心自己不够有魅力。", "category": "A"},
    {"id": 29, "text": "我不善于在恋爱中制造浪漫，有时候别人会觉得我很乏味。", "category": "B"},
    {"id": 30, "text": "不在一起时，我会很想念另一半，然而在一起了又会想逃离。", "category": "C"},
    {"id": 31, "text": "当我与别人意见不一时，能够很从容地表达自己的意见。", "category": "B"},
    {"id": 32, "text": "我不喜欢别人依赖我的感觉。", "category": "C"},
    {"id": 33, "text": "如果我发现自己喜欢的人却喜欢别人，我并不会感到很痛苦。会稍微有些嫉妒，不过这种感觉转瞬即逝。", "category": "B"},
    {"id": 34, "text": "如果我发现自己喜欢的人却喜欢别人，我会感觉到解脱——如此一来对方就不会对我产生占有欲。", "category": "C"},
    {"id": 35, "text": "如果我发现自己喜欢的人却喜欢别人，我会痛苦万分。", "category": "A"},
    {"id": 36, "text": "如果我的约会对象开始渐渐疏远我，我会好奇发生了什么，但不会归咎于我自己。", "category": "B"},
    {"id": 37, "text": "如果我的约会对象开始渐渐疏远我，我会感觉解脱了。", "category": "C"},
    {"id": 38, "text": "如果我的约会对象开始渐渐疏远我，我会觉得自己是不是做错了什么。", "category": "A"},
    {"id": 39, "text": "如果另一半想跟我分手，我会竭尽全力告诉对方，放弃我是个大损失，试试让他嫉妒也无妨。", "category": "A"},
    {"id": 40, "text": "如果我交往了几个月的对象不想再跟我联系了，我会有点受挫，但是很快就好了。", "category": "B"},
    {"id": 41, "text": "有时候在恋爱关系中，我的需要被满足后，我就开始手足无措了。", "category": "C"},
    {"id": 42, "text": "我并不觉得跟前任保持联系有什么问题(仅仅是朋友)，毕竟我们有很多相似之处。", "category": "B"}
    # 在此添加剩余的36个问题...
    # 示例格式：{"id": 7, "text": "问题内容", "category": "A/B/C"},
    # 实际使用时请补充完整42题
]

# 初始化session_state
if 'answers' not in st.session_state:
    st.session_state.answers = {}
if 'submitted' not in st.session_state:
    st.session_state.submitted = False

# 页面标题
st.title("依恋风格评估测试")
st.markdown("请回答以下42个问题，选择'符合'或'不符合':")

# 显示所有问题
for q in questions:
    key = f"q_{q['id']}"
    if key not in st.session_state.answers:
        st.session_state.answers[key] = None
    
    st.subheader(f"问题 {q['id']}")
    st.write(q["text"])
    
    # 使用列布局使选项并排显示
    col1, col2 = st.columns([1, 1])
    with col1:
        if st.button("符合", key=f"yes_{q['id']}", use_container_width=True):
            st.session_state.answers[key] = "符合"
    with col2:
        if st.button("不符合", key=f"no_{q['id']}", use_container_width=True):
            st.session_state.answers[key] = "不符合"
    
    # 显示当前选择状态
    current_answer = st.session_state.answers.get(key)
    if current_answer:
        st.info(f"当前选择: {current_answer}")
    else:
        st.warning("尚未选择")
    
    st.divider()

# 提交按钮
if st.button("提交评估", type="primary"):
    # 检查是否所有问题都已回答
    if all(value is not None for value in st.session_state.answers.values()):
        st.session_state.submitted = True
        
        # 计算各类别符合的数量
        category_count = {"A": 0, "B": 0, "C": 0}
        
        for q in questions:
            key = f"q_{q['id']}"
            if st.session_state.answers[key] == "符合":
                category = q["category"]
                category_count[category] += 1
        
        # 存储结果
        category_count['焦虑'] = category_count.pop('A')
        category_count['安全'] = category_count.pop('B')
        category_count['回避'] = category_count.pop('C')
        st.session_state.category_count = category_count
        
        # 确定主要类型
        max_count = max(category_count.values())
        main_categories = [cat for cat, count in category_count.items() if count == max_count]
        st.session_state.main_categories = main_categories
    else:
        st.error("请回答所有问题后再提交！")

# 显示结果
if st.session_state.get('submitted', False):
    st.success("评估完成！")
    st.balloons()
    
    # 显示统计结果
    st.subheader("评估结果")
    colA, colB, colC = st.columns(3)
    with colA:
        st.metric("焦虑型符合数", st.session_state.category_count["焦虑"])
    with colB:
        st.metric("安全型符合数", st.session_state.category_count["安全"])
    with colC:
        st.metric("回避型符合数", st.session_state.category_count["回避"])
    
    # 显示主要类型
    st.subheader("主要依恋")
    if len(st.session_state.main_categories) == 1:
        st.markdown(f"## 您的类型是：{st.session_state.main_categories[0]}型")
    else:
        st.markdown(f"## 您的类型是：{'/'.join(st.session_state.main_categories)}型（混合型）")
    
    # 类型描述（根据实际需求补充）
    type_descriptions = {
        "焦虑": "你喜欢和恋人在一起，亲密无间，渴望深层的亲密关系。然而，你常常处在不确定中，担心恋人和你不够亲近。情感问题消耗了你的大部分心力，让你疲倦。\
            你容易察觉出感情生活中的细微波动，对恋人的情绪和行为非常敏感。在许多情况下，虽然恋人的情绪确实和你感受的一样有波动，但不一定如你所想是你造成的。\
                在恋情中，你经常给自己消极暗示，情绪波动严重。有时候，你很冲动地说话做事，给恋人带来伤害，也让感情受损，当你意识到自己的负面情绪时，你又会感到懊悔。要是恋人能给你足够的抚慰和安全感，你就会感到很放松，心满意足。",
        "安全": "恋爱中，你会自然而然地充满温情和爱意。你喜欢和恋人亲密无间，通常不会对你们之间的关系忧心忡忡。\
            对待恋爱中的风波，你处之泰然，不会轻易心烦意乱。你可以畅通无阻地与恋人交流自己的想法和心情，也愿意聆听恋人倾诉，理解恋人的心情，并与之合拍。\
                你乐于和恋人分享自己的成功或失败，恋人遇到困难的时候，你会全力支持。",
        "回避": "你认为独立、自由比亲密的恋情更加重要。其实，你也需要亲密关系，你只是不愿意太过亲近，喜欢与恋人保持一点距离。\
            你丝毫不担心感情问题，不怕被拒绝。你不容易向恋人袒露心迹，这使得对方感觉你有些疏远。在恋爱中，一旦恋人表现出亲密的愿望，或者逾越了你个人自由的界限，你就会警觉起来。"
    }
    
    for cat in st.session_state.main_categories:
        st.info(f"**{cat}型特点**: {type_descriptions[cat]}")
    
    # 重置按钮
    if st.button("重新测试"):
        st.session_state.answers = {}
        st.session_state.submitted = False
        st.rerun()

# 侧边栏显示进度
with st.sidebar:
    st.header("答题进度")
    total = len(questions)
    answered = sum(1 for v in st.session_state.answers.values() if v is not None)
    progress = answered / total
    
    st.progress(progress)
    st.caption(f"已完成: {answered}/{total} ({int(progress*100)}%)")
    
    if answered == total:
        st.success("所有问题已完成！")
        st.success("请点击提交按钮查看结果")
    else:
        st.warning(f"还有{total-answered}题待完成")