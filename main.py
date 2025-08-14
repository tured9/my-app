from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.spinner import Spinner
from kivy.uix.scrollview import ScrollView
from kivy.core.window import Window
import random
from datetime import date
from plyer import tts  # للنطق الصوتي

# قوائم الأفعال حسب المستويات (من مصادر مثل Oxford وLangeek)
levels = {
    "A1": ['add', 'agree', 'arrive', 'ask', 'be', 'become', 'begin', 'believe', 'break', 'bring', 'build', 'buy', 'call', 'can', 'change', 'check', 'choose', 'clean', 'climb', 'close', 'come', 'compare', 'complete', 'cook', 'cost', 'could', 'create', 'cut', 'decide', 'describe', 'design', 'die', 'do', 'draw', 'drink', 'drive', 'eat', 'enjoy', 'fall', 'feel', 'fill', 'find', 'finish', 'fly', 'follow', 'forget', 'form', 'get', 'give', 'go', 'grow', 'guess', 'have', 'hear', 'help', 'hope', 'imagine', 'include', 'interest', 'introduce', 'join', 'keep', 'know', 'learn', 'leave', 'let', 'like', 'listen', 'live', 'look', 'lose', 'love', 'make', 'mean', 'meet', 'must', 'need', 'open', 'paint', 'park', 'pass', 'pay', 'pick', 'plan', 'play', 'prefer', 'prepare', 'put', 'read', 'remember', 'repeat', 'rest', 'return', 'run', 'say', 'see', 'sell', 'send', 'share', 'show', 'sing', 'sit', 'sleep', 'speak', 'spend', 'stand', 'start', 'stay', 'stop', 'study', 'take', 'talk', 'teach', 'tell', 'think', 'try', 'turn', 'understand', 'use', 'visit', 'wait', 'walk', 'want', 'wash', 'watch', 'will', 'win', 'work', 'write'],
    "A2": ['accept', 'achieve', 'act', 'affect', 'appear', 'apply', 'argue', 'arrange', 'attack', 'attend', 'avoid', 'behave', 'belong', 'borrow', 'break', 'brush', 'burn', 'care', 'catch', 'cause', 'celebrate', 'chat', 'check', 'collect', 'communicate', 'compare', 'compete', 'complain', 'contain', 'continue', 'control', 'cook', 'copy', 'count', 'cover', 'cry', 'cycle', 'deal', 'depend', 'develop', 'disappear', 'discover', 'discuss', 'divide', 'download', 'dream', 'drop', 'earn', 'enter', 'exist', 'expect', 'explain', 'express', 'fail', 'fall', 'farm', 'feed', 'fight', 'fill', 'film', 'fit', 'fix', 'focus', 'follow', 'form', 'fry', 'gather', 'greet', 'guide', 'hate', 'heat', 'hide', 'hit', 'hold', 'hope', 'hurt', 'identify', 'improve', 'increase', 'invent', 'invite', 'involve', 'jump', 'kill', 'knock', 'lead', 'learn', 'leave', 'lend', 'lie', 'light', 'like', 'listen', 'live', 'lock', 'look', 'lose', 'love', 'manage', 'mark', 'marry', 'measure', 'mention', 'miss', 'move', 'notice', 'offer', 'organize', 'own', 'pack', 'pass', 'perform', 'photograph', 'pick', 'plan', 'plant', 'play', 'point', 'post', 'practise', 'prefer', 'prepare', 'present', 'print', 'produce', 'protect', 'provide', 'pull', 'push', 'question', 'rain', 'reach', 'react', 'realize', 'receive', 'recognize', 'recommend', 'record', 'recycle', 'reduce', 'refer', 'refuse', 'relax', 'remove', 'repair', 'replace', 'reply', 'report', 'request', 'research', 'respond', 'rest', 'return', 'review', 'ride', 'ring', 'rise', 'run', 'sail', 'save', 'scan', 'score', 'search', 'seem', 'sell', 'send', 'serve', 'set', 'share', 'shop', 'sign', 'sit', 'sleep', 'smell', 'smile', 'smoke', 'solve', 'sort', 'speak', 'spell', 'spend', 'stand', 'start', 'stay', 'steal', 'stop', 'study', 'support', 'surprise', 'take', 'talk', 'teach', 'tell', 'test', 'text', 'throw', 'touch', 'train', 'travel', 'try', 'turn', 'use', 'visit', 'wait', 'wake', 'walk', 'want', 'warn', 'wash', 'watch', 'wear', 'work', 'write'],
    "B1": ['access', 'achieve', 'act', 'admire', 'admit', 'advise', 'afford', 'age', 'aim', 'analyse', 'announce', 'annoy', 'apologize', 'appreciate', 'arrest', 'assist', 'attach', 'attract', 'award', 'bake', 'balance', 'ban', 'base', 'beat', 'bend', 'benefit', 'bite', 'block', 'board', 'bomb', 'bother', 'breathe', 'bury', 'calculate', 'calm', 'campaign', 'care', 'catch', 'cause', 'celebrate', 'challenge', 'charge', 'cheat', 'claim', 'click', 'climb', 'coach', 'combine', 'comment', 'commit', 'compare', 'compete', 'complain', 'concentrate', 'conclude', 'confirm', 'connect', 'consider', 'consume', 'contact', 'contrast', 'convince', 'cool', 'count', 'cover', 'create', 'cry', 'cut', 'damage', 'deal', 'decorate', 'define', 'deliver', 'depend', 'determine', 'develop', 'direct', 'dislike', 'divide', 'donate', 'doubt', 'dress', 'drop', 'earn', 'educate', 'encourage', 'enjoy', 'escape', 'examine', 'exchange', 'expand', 'expect', 'experience', 'experiment', 'explain', 'express', 'face', 'fail', 'fall', 'fancy', 'fasten', 'fear', 'feature', 'fight', 'file', 'finance', 'fire', 'fit', 'fold', 'force', 'forgive', 'fry', 'fund', 'gather', 'generate', 'get', 'give', 'go', 'govern', 'grab', 'grade', 'grant', 'guard'],
    "B2": ['absorb', 'accommodate', 'accomplish', 'activate', 'adjust', 'anticipate', 'assign', 'assure', 'boost', 'chase', 'cheer', 'chop', 'clarify', 'classify', 'compose', 'comprise', 'confess', 'consult', 'convey', 'cope', 'crack', 'cruise', 'dare', 'depart', 'derive', 'devote', 'differ', 'disappoint', 'discourage', 'distinguish', 'distract', 'disturb', 'dive', 'dump', 'eliminate', 'embrace', 'equip', 'erupt', 'exceed', 'exclude', 'exhibit', 'exploit', 'forbid', 'forecast', 'fulfil', 'heal', 'inherit', 'insert', 'integrate', 'interact', 'invade', 'isolate', 'jail', 'manufacture', 'mate', 'motivate', 'occupy', 'overcome', 'pause', 'perceive', 'proceed', 'prohibit', 'prompt', 'rebuild', 'reckon', 'recruit', 'regulate', 'reinforce', 'relieve', 'resign', 'restore', 'restrict', 'rob', 'ruin', 'scare', 'scratch', 'specialize', 'specify', 'speculate', 'spill', 'spoil', 'starve', 'stimulate', 'strengthen', 'swallow', 'tackle', 'tap', 'trace', 'trigger', 'undergo', 'undertake', 'unfold', 'unite', 'wander', 'withdraw'],
    "C1": ['abolish', 'accelerate', 'accumulate', 'adhere', 'administer', 'advocate', 'allege', 'align', 'allocate', 'amend', 'appoint', 'applaud', 'arm', 'assemble', 'assert', 'attain', 'attribute', 'authorize', 'await', 'betray', 'bind', 'bleed', 'blend', 'bless', 'boast', 'bounce', 'bow', 'breach', 'breed', 'carve', 'cater', 'cease', 'characterize', 'circulate', 'cling', 'coincide', 'collaborate', 'combat', 'commence', 'compel', 'compensate', 'compile', 'complement', 'comply', 'compute', 'conceal', 'concede', 'conceive', 'condemn', 'confer', 'confine', 'confront', 'congratulate', 'conserve', 'consolidate', 'constitute', 'contemplate', 'contend', 'correspond', 'correlate', 'counter', 'craft', 'crawl', 'creep', 'crush', 'cultivate', 'damage', 'deem', 'defy', 'depict', 'deploy', 'deposit', 'deprive', 'descend', 'designate', 'detain', 'deteriorate', 'devise', 'diagnose', 'dictate', 'differentiate', 'diminish', 'dip', 'discard', 'discharge', 'disclose', 'displace', 'dispose', 'dispute', 'disrupt', 'dissolve', 'distort', 'drain', 'drift', 'drown', 'dub', 'echo', 'elevate', 'embark', 'embed', 'embody', 'empower', 'enact', 'encompass', 'endorse', 'endure', 'enforce', 'enrich', 'enrol', 'ensue', 'entitle', 'evacuate', 'evoke', 'exaggerate', 'execute', 'exert', 'expire', 'extract', 'facilitate', 'fade', 'flee', 'flourish', 'forge', 'formulate', 'foster', 'grasp', 'grind', 'grip', 'hail', 'halt', 'harvest', 'haunt', 'heighten', 'hint', 'hook', 'incur', 'induce', 'indulge', 'infect', 'inflict', 'inhibit', 'initiate', 'inject', 'inspect', 'instruct', 'insult', 'interfere', 'intervene', 'invoke', 'kidnap', 'leak', 'leap', 'license', 'linger', 'log', 'loom', 'manipulate', 'march', 'mature', 'maximize', 'merge', 'neglect', 'nod', 'nominate', 'oblige', 'obsess', 'opt', 'overlook', 'oversee', 'overturn', 'overwhelm', 'perceive', 'persist', 'plead', 'pledge', 'plunge', 'pop', 'portray', 'postpone', 'preach', 'precede', 'prescribe', 'preside', 'presume', 'prevail', 'probe', 'proclaim', 'prosecute', 'provoke', 'pump', 'punch', 'query', 'raid', 'rally', 'rape', 'reassure', 'rebel', 'recall', 'recount', 'reform', 'regain', 'reign', 'render', 'renew', 'reproduce', 'reside', 'resume', 'retreat', 'retrieve', 'reverse', 'revive', 'rip', 'rotate', 'ruin', 'sack', 'sacrifice', 'seal', 'seize', 'shed', 'shrink', 'shrug', 'sigh', 'simulate', 'skip', 'slam', 'slap', 'slash', 'smash', 'snap', 'soak', 'soar', 'span', 'spare', 'spark', 'strive', 'stumble', 'stun', 'sue', 'suppress', 'surrender', 'sustain', 'swing', 'tempt', 'terminate', 'testify', 'tighten', 'tolerate', 'toss', 'trace', 'trail', 'transmit', 'trap', 'undergo', 'undertake', 'unify', 'unveil', 'upgrade', 'uphold', 'utilize', 'vanish', 'violate', 'vow', 'weaken', 'weave', 'whip', 'widen', 'wipe', 'yell', 'yield'],
    "C2": ['abate', 'absolve', 'admonish', 'allude', 'ameliorate', 'belie', 'coalesce', 'debunk', 'denounce', 'deplore', 'deride', 'deter', 'disparage', 'enervate', 'engender', 'enhance', 'enunciate', 'exacerbate', 'exalt', 'expedite', 'exploit', 'extol', 'fabricate', 'facilitate', 'foment', 'garner', 'genuflect', 'harangue', 'hinder', 'impel', 'impede', 'implore', 'incite', 'inculcate', 'indoctrinate', 'instigate', 'juxtapose', 'kindle', 'lament', 'mitigate', 'mollify', 'obfuscate', 'obliterate', 'pacify', 'palliate', 'preclude', 'precipitate', 'protract', 'ratify', 'rebuke', 'reconcile', 'redress', 'refute', 'relegate', 'relinquish', 'renounce', 'repudiate', 'rescind', 'substantiate', 'transcend', 'vacillate']
}

# قاموس للأفعال غير المنتظمة (من قائمة CEFR)
irregular_verbs = {
    'be': {'past': 'was/were', 'part': 'been'},
    'have': {'past': 'had', 'part': 'had'},
    'do': {'past': 'did', 'part': 'done'},
    'say': {'past': 'said', 'part': 'said'},
    'go': {'past': 'went', 'part': 'gone'},
    'get': {'past': 'got', 'part': 'got/gotten'},
    'make': {'past': 'made', 'part': 'made'},
    'know': {'past': 'knew', 'part': 'known'},
    'think': {'past': 'thought', 'part': 'thought'},
    'take': {'past': 'took', 'part': 'taken'},
    'see': {'past': 'saw', 'part': 'seen'},
    'come': {'past': 'came', 'part': 'come'},
    'find': {'past': 'found', 'part': 'found'},
    'give': {'past': 'gave', 'part': 'given'},
    'tell': {'past': 'told', 'part': 'told'},
    'feel': {'past': 'felt', 'part': 'felt'},
    'become': {'past': 'became', 'part': 'become'},
    'leave': {'past': 'left', 'part': 'left'},
    'put': {'past': 'put', 'part': 'put'},
    'mean': {'past': 'meant', 'part': 'meant'},
    'keep': {'past': 'kept', 'part': 'kept'},
    'let': {'past': 'let', 'part': 'let'},
    'begin': {'past': 'began', 'part': 'begun'},
    'show': {'past': 'showed', 'part': 'shown'},
    'hear': {'past': 'heard', 'part': 'heard'},
    'run': {'past': 'ran', 'part': 'run'},
    'hold': {'past': 'held', 'part': 'held'},
    'bring': {'past': 'brought', 'part': 'brought'},
    'write': {'past': 'wrote', 'part': 'written'},
    'sit': {'past': 'sat', 'part': 'sat'},
    'stand': {'past': 'stood', 'part': 'stood'},
    'lose': {'past': 'lost', 'part': 'lost'},
    'pay': {'past': 'paid', 'part': 'paid'},
    'meet': {'past': 'met', 'part': 'met'},
    'set': {'past': 'set', 'part': 'set'},
    'learn': {'past': 'learnt/learned', 'part': 'learnt/learned'},
    'lead': {'past': 'led', 'part': 'led'},
    'understand': {'past': 'understood', 'part': 'understood'},
    'speak': {'past': 'spoke', 'part': 'spoken'},
    'read': {'past': 'read', 'part': 'read'},
    'spend': {'past': 'spent', 'part': 'spent'},
    'grow': {'past': 'grew', 'part': 'grown'},
    'win': {'past': 'won', 'part': 'won'},
    'buy': {'past': 'bought', 'part': 'bought'},
    'send': {'past': 'sent', 'part': 'sent'},
    'build': {'past': 'built', 'part': 'built'},
    'fall': {'past': 'fell', 'part': 'fallen'},
    'cut': {'past': 'cut', 'part': 'cut'},
    'sell': {'past': 'sold', 'part': 'sold'},
    'light': {'past': 'lit', 'part': 'lit'},
    'drive': {'past': 'drove', 'part': 'driven'},
    'break': {'past': 'broke', 'part': 'broken'},
    'wear': {'past': 'wore', 'part': 'worn'},
    'hit': {'past': 'hit', 'part': 'hit'},
    'eat': {'past': 'ate', 'part': 'eaten'},
    'teach': {'past': 'taught', 'part': 'taught'},
    'cost': {'past': 'cost', 'part': 'cost'},
    'catch': {'past': 'caught', 'part': 'caught'},
    'draw': {'past': 'drew', 'part': 'drawn'},
    'choose': {'past': 'chose', 'part': 'chosen'},
    'seek': {'past': 'sought', 'part': 'sought'},
    'deal': {'past': 'dealt', 'part': 'dealt'},
    'fight': {'past': 'fought', 'part': 'fought'},
    'throw': {'past': 'threw', 'part': 'thrown'},
    'rise': {'past': 'rose', 'part': 'risen'},
    'shoot': {'past': 'shot', 'part': 'shot'},
    'lie': {'past': 'lay', 'part': 'lain'},
    'lay': {'past': 'laid', 'part': 'laid'},
    'prove': {'past': 'proved', 'part': 'proven/proved'},
    'hang': {'past': 'hung/hanged', 'part': 'hung/hanged'},
    'forget': {'past': 'forgot', 'part': 'forgotten'},
    'spring': {'past': 'sprang', 'part': 'sprung'},
    'shake': {'past': 'shook', 'part': 'shaken'},
    'fly': {'past': 'flew', 'part': 'flown'},
    'dream': {'past': 'dreamt/dreamed', 'part': 'dreamt/dreamed'},
    'sing': {'past': 'sang', 'part': 'sung'},
    'beat': {'past': 'beat', 'part': 'beaten'},
    'wind': {'past': 'wound', 'part': 'wound'},
    'hurt': {'past': 'hurt', 'part': 'hurt'},
    'strike': {'past': 'struck', 'part': 'struck/stricken'},
    'sleep': {'past': 'slept', 'part': 'slept'},
    'stick': {'past': 'stuck', 'part': 'stuck'},
    'drink': {'past': 'drank', 'part': 'drunk'},
    'hide': {'past': 'hid', 'part': 'hidden'},
    'ride': {'past': 'rode', 'part': 'ridden'},
    'feed': {'past': 'fed', 'part': 'fed'},
    'fit': {'past': 'fit/fitted', 'part': 'fit/fitted'},
    'spread': {'past': 'spread', 'part': 'spread'},
    'speed': {'past': 'sped/speeded', 'part': 'sped/speeded'},
    'blow': {'past': 'blew', 'part': 'blown'},
    'burn': {'past': 'burnt/burned', 'part': 'burnt/burned'},
    'lean': {'past': 'leant/leaned', 'part': 'leant/leaned'},
    'shut': {'past': 'shut', 'part': 'shut'},
    'bear': {'past': 'bore', 'part': 'born/borne'},
    'ring': {'past': 'rang', 'part': 'rung'},
    # أضف المزيد إذا أردت
}

# بيانات إضافية للأفعال (عينة، أضف 1500 لكل مستوى هنا)
verb_data = {
    'be': {
        'ipa': '/biː/',
        'idioms': {'be all ears': {'en': 'I\'m all ears.', 'ar': 'أنا كل أذنين.'}},
        'phrasal': {'be up to': {'en': 'What are you up to?', 'ar': 'ماذا تفعل؟'}},
        'explanation': {'en': 'The verb "be" is used for identity and state.', 'ar': 'الفعل "be" يستخدم للهوية والحالة.'},
        'examples': {'en': 'I am happy.', 'ar': 'أنا سعيد.'},
        'adjective_form': 'being (as in "being happy")',  # صفة/حال
        'adverb_form': 'N/A for verbs, but participles can modify.'
    },
    'go': {
        'ipa': '/ɡəʊ/',
        'idioms': {'go the extra mile': {'en': 'He goes the extra mile.', 'ar': 'يبذل جهدًا إضافيًا.'}},
        'phrasal': {'go on': {'en': 'Go on with your work.', 'ar': 'استمر في عملك.'}},
        'explanation': {'en': 'The verb "go" means to move from one place to another.', 'ar': 'الفعل "go" يعني التحرك من مكان إلى آخر.'},
        'examples': {'en': 'I go to school.', 'ar': 'أذهب إلى المدرسة.'},
        'adjective_form': 'gone (as in "gone missing")',
        'adverb_form': 'going (as in "going quickly")'
    },
    'have': {
        'ipa': '/hæv/',
        'idioms': {'have a ball': {'en': 'We had a ball at the party.', 'ar': 'استمتعنا كثيرًا في الحفلة.'}},
        'phrasal': {'have on': {'en': 'What do you have on?', 'ar': 'ماذا ترتدي؟'}},
        'explanation': {'en': 'The verb "have" indicates possession.', 'ar': 'الفعل "have" يشير إلى الملكية.'},
        'examples': {'en': 'I have a book.', 'ar': 'لدي كتاب.'},
        'adjective_form': 'having (as in "having fun")',
        'adverb_form': 'N/A'
    },
    # أضف بيانات لـ 1500 فعل لكل مستوى هنا، مثل 'do': {...}, إلخ. ابحث عن IPA وإيديومات لكل فعل.
}

# دالة للحصول على التصريف والمعلومات
def get_verb_info(verb):
    if verb in irregular_verbs:
        past = irregular_verbs[verb]['past']
        part = irregular_verbs[verb]['part']
    else:
        past = verb + 'ed'
        part = verb + 'ed'
    gerund = verb + 'ing'
    third = verb + 's' if not verb.endswith(('s', 'sh', 'ch', 'x', 'o')) else verb + 'es'

    tenses = {
        'Simple Present': f'I {verb}',
        'Present Third Person': f'He {third}',
        'Simple Past': f'I {past}',
        'Past Participle': part,
        'Gerund/Present Participle': gerund,
        'Future': f'I will {verb}',
        'Present Continuous': f'I am {gerund}',
        'Past Continuous': f'I was {gerund}',
        'Future Continuous': f'I will be {gerund}',
        'Present Perfect': f'I have {part}',
        'Past Perfect': f'I had {part}',
        'Future Perfect': f'I will have {part}',
    }

    data = verb_data.get(verb, {})
    ipa = data.get('ipa', 'N/A - Add IPA')
    idioms = data.get('idioms', {})
    phrasal = data.get('phrasal', {})
    explanation = data.get('explanation', {'en': 'No explanation added.', 'ar': 'لا شرح مضاف.'})
    examples = data.get('examples', {'en': 'No example.', 'ar': 'لا مثال.'})
    adj_form = data.get('adjective_form', 'N/A - Participles can be adjectives.')
    adv_form = data.get('adverb_form', 'N/A - Gerund for manner.')

    info = f"Verb: {verb}\nPronunciation: {ipa}\n\nTenses:\n"
    for t, ex in tenses.items():
        info += f"{t}: {ex}\n"
    info += f"\nExplanation:\nEN: {explanation['en']}\nAR: {explanation['ar']}\n"
    info += f"\nExamples:\nEN: {examples['en']}\nAR: {examples['ar']}\n"
    info += f"\nAdjective Form: {adj_form}\nAdverb Form: {adv_form}\n"
    if idioms:
        info += "\nIdioms:\n"
        for idm, ex in idioms.items():
            info += f"{idm}: EN: {ex['en']} AR: {ex['ar']}\n"
    if phrasal:
        info += "\nPhrasal Verbs:\n"
        for phr, ex in phrasal.items():
            info += f"{phr}: EN: {ex['en']} AR: {ex['ar']}\n"
    return info

class DailyVerbsApp(App):
    def build(self):
        Window.size = (360, 640)  # حجم شاشة هاتف
        layout = BoxLayout(orientation='vertical')
        
        # اختيار المستوى
        level_spinner = Spinner(text='A1', values=list(levels.keys()))
        layout.add_widget(level_spinner)
        
        # زر للحصول على الأفعال اليومية
        get_button = Button(text='Get Daily Verbs')
        layout.add_widget(get_button)
        
        # عرض المعلومات
        self.info_label = Label(text='', size_hint_y=None, height=1000, text_size=(340, None))
        scroll = ScrollView()
        scroll.add_widget(self.info_label)
        layout.add_widget(scroll)
        
        def get_daily_verbs(instance):
            level = level_spinner.text
            verb_list = levels.get(level, [])
            if not verb_list:
                self.info_label.text = "No verbs in this level."
                return
            
            # عشوائي يومي بناءً على التاريخ والمستوى
            day_seed = date.today().toordinal() + hash(level)
            random.seed(day_seed)
            daily_verbs = random.sample(verb_list, min(2, len(verb_list)))
            
            info_text = ""
            for verb in daily_verbs:
                info_text += get_verb_info(verb) + "\n\n"
                # زر للنطق
                speak_button = Button(text=f'Pronounce {verb}')
                speak_button.bind(on_press=lambda x, v=verb: tts.speak(v))
                layout.add_widget(speak_button)
            
            self.info_label.text = info_text
            self.info_label.height = self.info_label.texture_size[1]
        
        get_button.bind(on_press=get_daily_verbs)
        
        return layout

if __name__ == '__main__':
    DailyVerbsApp().run()