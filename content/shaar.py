# The shaar: the ornate title page every printed tractate opens with.
# Doubles as the codex's table of contents; links are hash anchors that
# CodexNav resolves to leaves. Entries marked toc-wanting are not yet set.

FOLIO = {
    'type': 'shaar',
    'folio': 'shaar',
    'name': 'Title',
    'title': 'Tractate Aliyah \u00b7 Seder Chashak \u2014 shaar',
    'seder': 'Seder Chashak \u00b7 \u05d7\u05e9\u05da',
    'hebrew': '\u05de\u05e1\u05db\u05ea \u05e2\u05dc\u05d9\u05d9\u05d4',
    'tractate': 'Tractate Aliyah',
    'imprint': ('Being the rules and lore of Mage: the Ascension, arranged after the manner of the '
                'printed Talmud: the law as Mishnah, the fiction as aggada, and around them the '
                'commentaries <em>On the Law</em> and <em>On the Story</em>, with Ein Mishpat, '
                'Masoret, the Later Authorities, and hagahot. An out-of-character disputation and '
                'a fan work; no text of the source is reproduced, and its page numbers are kept '
                'as folio numbers, that the citations of both books may be one. Set in Abbess '
                'and Goudy Old Style after the M20 interior.'),
    # chapters: (chapter_head, [(folio_anchor_or_None, folio_label, entry_title), ...])
    'toc': [
        ('I \u00b7 The Nine Seats', [
            ('2a',   '2',   'Convocation \u00b7 The Betrayal'),
            ('3a',   '3',   'Judgments \u00b7 The Unseated Answer'),
            (None,   '143', 'Cert\u00e1men'),
        ]),
        ('II \u00b7 The Awakening', [
            (None, '38', 'Of Gods and Men'),
            (None, '43', 'The Avatar'),
            (None, '46', 'The Will to Power'),
        ]),
        ('III \u00b7 The World', [
            (None, '62', 'Consensus and Belief'),
            (None, '78', 'The Life-Blood of Reality'),
            (None, '82', 'The Gauntlet'),
        ]),
        ('IV \u00b7 The Worlds Beyond', [
            (None, '89',  'The Penumbra'),
            (None, '91',  'The Three Umbrae'),
            (None, '109', 'The Horizon'),
        ]),
        ('V \u00b7 Avot: The Traditions', [
            ('148a', '148', 'The Akashic Brotherhood \u00b7 The Wheel'),
            ('150a', '150', 'The Celestial Chorus \u00b7 The Reformation'),
            ('152a', '152', 'The Cult of Ecstasy \u00b7 The Burden'),
            ('154a', '154', 'The Dreamspeakers \u00b7 The People'),
            ('156a', '156', 'The Chakravanti \u00b7 Jhor'),
            ('158a', '158', 'The Order of Hermes \u00b7 The Houses'),
            ('160a', '160', 'The Society of Ether \u00b7 Paradigma'),
            ('162a', '162', 'The Verbena \u00b7 The Garden'),
            ('164a', '164', 'The Virtual Adepts \u00b7 The Web'),
        ]),
        ('VI \u00b7 The Union', [
            (None, '168', 'The Precepts'),
            (None, '186', 'Iteration X'),
            (None, '188', 'The New World Order'),
            (None, '190', 'The Progenitors'),
            (None, '192', 'The Syndicate'),
            (None, '194', 'The Void Engineers'),
        ]),
        ('VII \u00b7 The Unseated and the Fallen', [
            (None, '197', 'The Silent Alliance'),
            (None, '224', 'The Fallen'),
            (None, '234', 'The Mad'),
        ]),
        ('VIII \u00b7 The Order of Making', [
            ('250a', '250', 'The Seder of Creation \u00b7 The Fifteen'),
            (None, '273', 'Attributes (luach)'),
            (None, '275', 'Abilities (luach)'),
            (None, '303', 'Backgrounds (luach)'),
            (None, '328', 'Arete and Will'),
        ]),
        ('IX \u00b7 Middot: Measures', [
            ('384a', '384', 'The Golden Rule \u00b7 The Contract'),
            ('385a', '385', 'The Dice \u00b7 The Count'),
            ('393a', '393', 'The Rule of One \u00b7 The Comment'),
            ('406a', '406', 'Health \u00b7 The Wound'),
        ]),
        ('X \u00b7 Strife', [
            ('409a', '409', 'Combat \u00b7 The Gun and the Word'),
            ('423a', '423', 'The Martial Arts and Do \u00b7 The Eight Limbs'),
            ('430a', '430', 'Duels, Old Form \u00b7 The Wager'),
            ('435a', '435', 'Hazards (luach) \u00b7 The Breaking'),
        ]),
        ('XI \u00b7 The Book of Magick', [
            (None,    '500',  'Casting'),
            ('512a',  '512',  'Correspondence \u00b7 The Reach'),
            ('514a',  '514',  'Entropy \u00b7 Fortune'),
            ('515a',  '515',  'Forces \u00b7 Conjunctions'),
            ('516a',  '516',  'Life \u00b7 Healing'),
            ('517a',  '517',  'Matter \u00b7 The Workshop'),
            ('519a',  '519',  'Mind \u00b7 The Seeming'),
            ('520a',  '520',  'Prime \u00b7 The Well'),
            ('521a',  '521',  'Spirit \u00b7 The Crossing'),
            ('522a',  '522',  'Time \u00b7 The Rewind'),
            ('533a',  '533',  'Paradox \u00b7 Witnesses'),
            (None,    '554',  'Quiet'),
            (None,    '567',  'Focus: Belief'),
            (None,    '572',  'Focus: Practice'),
            (None,    '586',  'Focus: Instruments'),
            (None,    '607',  'Rotes and Procedures'),
        ]),
        ('Minor Tractates', [
            (None, 'K.1', 'Kelim: Wonders'),
            (None, 'B.1', 'The Bestiary'),
        ]),
    ],
    'colophon': ('The folios here bound are sixty; the rest are wanting, and the wanting is the plan. '
                 'A tractate that stops accreting commentary is not finished \u2014 it is dead, '
                 'and this one intends to be neither.'),
}
