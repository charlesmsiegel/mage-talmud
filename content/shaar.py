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
            ('2a',   '2a',  'Convocation'),
            ('2b',   '2b',  'The Betrayal'),
            ('3a',   '3a',  'Judgments'),
            (None,   '3b',  'The Unseated Answer'),
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
            ('148a', '148a', 'The Akashayana'),
            (None, '150', 'The Celestial Chorus'),
            (None, '152', 'The Sahajiya'),
            (None, '154', 'The Kha\u2019vadi'),
            (None, '156', 'The Chakravanti'),
            (None, '158', 'The Order of Hermes'),
            (None, '160', 'The Society of Ether'),
            (None, '162', 'The Verbena'),
            (None, '164', 'The Mercurial Elite'),
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
            (None, '250', 'The Seder of Creation'),
            (None, '273', 'Attributes (luach)'),
            (None, '275', 'Abilities (luach)'),
            (None, '303', 'Backgrounds (luach)'),
            (None, '328', 'Arete and Will'),
        ]),
        ('IX \u00b7 Middot: Measures', [
            (None, '384', 'The Golden Rule'),
            (None, '385', 'The Dice'),
            (None, '393', 'The Rule of One'),
            (None, '406', 'Health and Injury'),
        ]),
        ('X \u00b7 Strife', [
            (None, '409', 'Combat'),
            (None, '423', 'The Martial Arts and Do'),
            (None, '430', 'Duels, Old Form'),
            (None, '435', 'Hazards (luach)'),
        ]),
        ('XI \u00b7 The Book of Magick', [
            (None,    '500',  'Casting'),
            (None,    '512',  'Correspondence'),
            (None,    '514',  'Entropy'),
            ('515a',  '515a', 'Forces'),
            (None,    '516',  'Life'),
            (None,    '517',  'Matter'),
            (None,    '519',  'Mind'),
            (None,    '520',  'Prime'),
            (None,    '521',  'Spirit'),
            (None,    '522',  'Time'),
            ('533a',  '533a', 'Paradox'),
            ('533b',  '533b', 'Witnesses'),
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
    'colophon': ('The folios here bound are seven; the rest are wanting, and the wanting is the plan. '
                 'A tractate that stops accreting commentary is not finished \u2014 it is dead, '
                 'and this one intends to be neither.'),
}
