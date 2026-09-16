"""One-time, branch-local UX illustration migration; workflow deletes this file."""
from pathlib import Path
from html import escape
import re
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]
NOTE = ROOT / 'notes/06_ux.md'
ART = ROOT / 'assets/diagrams/ux'
ART.mkdir(parents=True, exist_ok=True)
original = NOTE.read_text(encoding='utf-8')
chapter = original
INK, MUTED, NAVY, PALE, BLUE, TEAL, LIGHT = '#0f172a', '#475569', '#243b53', '#f1f5f9', '#1d4ed8', '#087f8c', '#e2e8f0'

def txt(x, y, value, size=18, fill=INK, weight=400, anchor=None):
    a = f' text-anchor="{anchor}"' if anchor else ''
    return f'<text x="{x}" y="{y}" fill="{fill}" font-size="{size}" font-weight="{weight}"{a}>{escape(value)}</text>'

def rect(x, y, w, h, fill=LIGHT, radius=9, stroke=None):
    s = f' stroke="{stroke}"' if stroke else ''
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{radius}" fill="{fill}"{s}/>'

def circle(x, y, r, fill=BLUE):
    return f'<circle cx="{x}" cy="{y}" r="{r}" fill="{fill}"/>'

def line(x1, y1, x2, y2, color=MUTED, width=3, dash=''):
    return f'<path d="M{x1} {y1} L{x2} {y2}" stroke="{color}" stroke-width="{width}" fill="none" {dash}/>'

def panel(x, label, bg='#ffffff'):
    return rect(x, 122, 476, 300, bg, 15, '#cbd5e1') + txt(x+22, 156, label, 21, INK, 700)

def ui(x, y, title, subtitle, action=None, color=BLUE):
    out = rect(x, y, 400, 162, '#ffffff', 11, '#94a3b8')
    out += txt(x+20, y+41, title, 21, INK, 700) + txt(x+20, y+74, subtitle, 16, MUTED)
    if action:
        out += rect(x+20, y+94, 170, 47, color, 8) + txt(x+105, y+123, action, 17, '#ffffff', 700, 'middle')
    return out

def diagram(slug, title, desc, body, footer):
    assert slug not in ('60-30-10',), 'Keep the original hand-authored palette illustration'
    wrapper = (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1040 470" role="img" aria-labelledby="title desc">'
               f'<title id="title">{escape(title)}</title><desc id="desc">{escape(desc)}</desc>'
               f'{rect(0,0,1040,470,"#f8fafc",18)}'
               f'<g font-family="Arial,sans-serif">{txt(34,46,title,29,INK,700)}'
               f'{txt(34,82,footer,16,MUTED)}{body}</g></svg>\n')
    ET.fromstring(wrapper)
    (ART / f'{slug}.svg').write_text(wrapper, encoding='utf-8')

# Each image is a specific, labeled teaching example rather than a generic text-only flowchart.
steps = ['Define task','Observe','Synthesize','Sketch','Prototype','Evaluate','Ship','Monitor']
b = ''
for i, label in enumerate(steps):
    x = 44 + (i % 4)*247
    y = 142 + (i//4)*136
    b += rect(x,y,224,93,'#dbeafe' if i<4 else '#ccfbf1',12) + circle(x+26,y+46,15,BLUE if i<4 else TEAL)
    b += txt(x+26,y+52,str(i+1),15,'#ffffff',700,'middle') + txt(x+47,y+53,label,17,INK,700)
    if i%4!=3: b += line(x+224,y+46,x+243,y+46,BLUE,3)
b += line(966,235,966,262,TEAL,3) + line(44,389,44,425,TEAL,3) + txt(65,440,'Repeat when evidence challenges the design',16,TEAL,700)
diagram('ux-process','UX is an iterative evidence loop','Eight stages show how defining a task, observing, testing and monitoring connect, with a return loop to new questions.',b,'A handoff is not the end of research; revisit decisions after release.')

b = panel(34,'BEFORE · scattered content') + panel(530,'AFTER · meaningful groups')
for x,y,w in [(67,191,120),(281,189,175),(92,273,236),(351,304,100),(201,361,128)]: b += rect(x,y,w,35,'#cbd5e1',4)
b += rect(559,185,416,65,'#dbeafe',8)+txt(579,226,'Order summary',20,INK,700)
b += rect(559,263,416,65,'#dcfce7',8)+txt(579,305,'Delivery details',20,INK,700)
b += rect(559,340,240,54,BLUE,8)+txt(679,374,'Continue to payment',17,'#ffffff',700,'middle')
diagram('structure','Structure: group by task','The left scatters blocks without clear relationships. The right groups order summary, delivery and payment in a predictable sequence.',b,'Test whether people can locate the next step without explanation.')

b = panel(34,'BEFORE · ambiguous icons') + panel(530,'AFTER · labeled controls')
for i,s in enumerate(['?','★','≡']): b += rect(92+i*116,230,72,65,LIGHT,8)+txt(128+i*116,274,s,29,INK,700,'middle')
b += ui(569,188,'Shipping information','Fees, delivery dates, and returns','View shipping',TEAL)
diagram('visibility','Visibility: reveal relevant affordances','Three unlabeled icons compete with a clearly labeled shipping-information card and action.',b,'Discoverability requires meaningful names, not only decorative icons.')

b = panel(34,'BEFORE · silent submission') + panel(530,'AFTER · status and recovery')
b += ui(70,197,'Your changes','The Save action gives no response','Save')
b += rect(567,185,395,57,'#dbeafe',8)+txt(587,221,'Saving…  Step 1: request in progress',16,INK)
b += rect(567,256,395,57,'#dcfce7',8)+txt(587,292,'Saved  ·  changes are available',16,'#166534',700)
b += rect(567,327,395,57,'#fee2e2',8)+txt(587,363,'Could not save · Retry',16,'#991b1b',700)
diagram('feedback','Feedback: communicate real system status','Before shows an action with no response; after illustrates loading, success, and actionable failure states.',b,'Show truthful status in text; do not announce success before completion.')

b = panel(34,'BEFORE · irreversible delete') + panel(530,'AFTER · confirm and undo')
b += rect(77,228,218,60,'#b91c1c',8)+txt(186,265,'Delete forever',19,'#ffffff',700,'middle')+txt(77,323,'No description or recovery',16,MUTED)
b += rect(569,191,388,126,'#ffffff',10,'#94a3b8')+txt(591,224,'Delete this draft?',20,INK,700)
b += txt(591,250,'This can be restored for 30 seconds.',16,MUTED)
b += rect(591,264,144,42,'#e2e8f0',7)+txt(663,291,'Cancel',16,INK,700,'middle')
b += rect(752,264,175,42,'#b91c1c',7)+txt(839,291,'Delete draft',16,'#ffffff',700,'middle')
b += rect(569,331,388,55,'#dcfce7',8)+txt(591,365,'Draft deleted  ·  Undo',17,'#166534',700)
diagram('tolerance','Tolerance: prevent errors and support recovery','The left has an unexplained irreversible delete. The right names the object, offers cancel, and includes a time-limited undo example.',b,'Only promise undo if the application really supports recovery.')

b = panel(34,'BEFORE · inconsistent actions') + panel(530,'AFTER · consistent meaning')
for x,y,w,c,s in [(71,198,155,'#e2e8f0','SAVE'),(256,264,158,'#f59e0b','Submit'),(99,342,212,'#1d4ed8','Finish!')]: b += rect(x,y,w,50,c,5)+txt(x+w/2,y+31,s,16,'#ffffff' if c!='#e2e8f0' else INK,700,'middle')
for i,(s,c) in enumerate([('Save draft',BLUE),('Save changes',BLUE),('Delete draft','#b91c1c')]):
    y=186+i*69; b += rect(576,y,205,49,c,8)+txt(678,y+30,s,16,'#ffffff',700,'middle')
diagram('consistency','Consistency: make equivalent actions predictable','The left uses unrelated wording and styles for save-like actions. The right names distinct actions consistently and preserves a separate destructive style.',b,'Consistency covers labels and behavior, not just colors.')

b = panel(34,'BEFORE · unrelated proximity') + panel(530,'AFTER · grouped by meaning')
for i,(x,y) in enumerate([(86,211),(215,224),(375,191),(130,351),(326,334),(267,283)]): b += circle(x,y,24,BLUE if i%2 else TEAL)
for y,colors in [(216,[BLUE,BLUE,BLUE]),(335,[TEAL,TEAL,TEAL])]:
    b+=rect(574,y-48,386,96,'#f1f5f9',12,'#cbd5e1')
    for j,c in enumerate(colors): b+=circle(649+j*99,y,21,c)
diagram('gestalt','Gestalt: proximity and similarity','Scattered blue and teal circles become two close, visually consistent groups. Grouping suggests relations that must also be expressed by labels in a real UI.',b,'Do not use color alone to communicate group membership.')

b = panel(34,'BEFORE · 12 equal-looking choices') + panel(530,'AFTER · task-oriented groups')
for i in range(12):
    x=65+(i%3)*142;y=188+(i//3)*54;b+=rect(x,y,123,43,LIGHT,7)+txt(x+61,y+28,'Option '+str(i+1),15,INK,400,'middle')
for i,(s,c) in enumerate([('Shop by category','#dbeafe'),('Search products','#dcfce7'),('View recent','#fef3c7')]):
    y=194+i*71;b+=rect(561,y,404,59,c,9)+txt(583,y+37,s,19,INK,700)
diagram('hicks-law','Hick–Hyman: choices and decision time','An example of 12 unrelated options compared with three clear entry paths. This illustrates possible organization, not measured response times.',b,'Decision time depends on familiarity, meaning, probability and context.')

b = rect(42,138,956,258,'#ffffff',10,'#94a3b8')+rect(42,138,591,258,'#dbeafe',0)+rect(633,138,365,258,'#243b53',0)
b+=txt(337,270,'Main area · 61.8%',23,INK,700,'middle')+txt(815,270,'Sidebar · 38.2%',21,'#ffffff',700,'middle')
diagram('golden-ratio','Golden ratio: a possible proportion','A schematic content/sidebar split of about 61.8 percent and 38.2 percent. It does not establish a universal preference or accessibility benefit.',b,'Use proportions as a sketching option; measure reading and layout.')

b=rect(45,162,950,82,LIGHT,8)+rect(45,162,760,82,TEAL,8)+rect(805,162,190,82,NAVY,8)
b+=txt(425,212,'80 observed events · two features',21,'#ffffff',700,'middle')+txt(901,212,'20 events',18,'#ffffff',700,'middle')
for i in range(10):
    x=47+i*96;b+=rect(x,281,77,64,TEAL if i<2 else '#cbd5e1',6)+txt(x+38,323,'F'+str(i+1),17,'#ffffff' if i<2 else INK,700,'middle')
b+=txt(50,393,'Hypothetical example: 2 of 10 features account for 80 of 100 recorded actions.',17,MUTED)
diagram('pareto','Pareto 80/20: check the data','A hypothetical observed activity split illustrates 2 of 10 features associated with 80 of 100 actions, not a universal UX distribution.',b,'Do not hide infrequent but critical tasks solely from usage counts.')

b=rect(68,137,903,258,'#ffffff',10,'#94a3b8')
for i,w in enumerate([780,650,540,720,490,655,680,430]):
    y=177+i*25;b+=rect(105,y,w,9,'#cbd5e1',2)
b+=line(101,157,908,157,'#e11d48',8)+line(101,213,634,213,'#e11d48',8)+line(102,157,102,369,'#e11d48',7)
b+=txt(701,366,'Illustrative scan trace',18,'#be123c',700)
diagram('f-pattern','F-shaped scanning: one observed pattern','A schematic document with a top horizontal scan, a shorter second line, and a left-edge vertical path. Not actual eye-tracking data.',b,'Scanning changes with content, language direction, and task.')

b=rect(228,126,578,290,'#dbeafe',4)+rect(228,319,578,97,'#bbf7d0',0)+circle(613,223,56,'#f59e0b')
for x in (421,613): b+=line(x,126,x,416,'#ffffff',3)
for y in (223,320): b+=line(228,y,806,y,'#ffffff',3)
for x in (421,613):
    for y in (223,320): b+=circle(x,y,7,'#be123c')
b+=txt(84,256,'Subject placed near',16,MUTED)+txt(84,279,'a grid intersection',16,MUTED)
diagram('rule-of-thirds','Rule of thirds: composition grid','A three-by-three grid overlays a landscape illustration; intersection dots indicate optional placements for a subject.',b,'Compositional aid, not a requirement to avoid centering.')

b=panel(34,'BEFORE · tiny, distant target')+panel(530,'AFTER · larger, nearby target')
b+=circle(98,362,13,INK)+line(98,362,396,202,'#e11d48',4)+rect(399,182,40,32,BLUE,4)
b+=circle(605,362,13,INK)+line(605,362,725,296,TEAL,4)+rect(728,246,195,69,BLUE,12)+txt(825,287,'Next step',21,'#ffffff',700,'middle')
diagram('fitts-law','Fitts: distance and target size','Two pointer paths show a small distant target versus a larger nearby target; labels explain the design tradeoff.',b,'Check actual pointer/touch tasks and WCAG target-size requirements.')

b=panel(34,'BEFORE · unexpected navigation')+panel(530,'AFTER · familiar labeled navigation')
b+=rect(77,190,383,184,LIGHT,9)+txt(100,226,'Dashboard',21,INK,700)
for i,s in enumerate(['◈','☆','?']): b+=circle(151+i*113,340,27,NAVY)+txt(151+i*113,349,s,23,'#ffffff',700,'middle')
b+=rect(562,190,395,66,NAVY,7)
for i,s in enumerate(['Home','Courses','Help']): b+=txt(591+i*124,232,s,17,'#ffffff',700)
b+=txt(581,321,'Page content appears below the navigation',17,INK)
diagram('jakobs-law','Jakob’s law: familiar patterns','A page hides navigation behind unlabeled unusual icons; a second uses conventional labeled links at the top.',b,'Preserve familiar patterns when appropriate to your audience.')

b=panel(34,'BEFORE · one ungrouped list')+panel(530,'AFTER · meaningful chunks')
for i in range(9): b+=txt(79,196+i*23,'Item '+str(i+1),16,INK)
for j,(label,entries) in enumerate([('Account',['Profile','Security','Billing']),('Content',['Library','Saved','History']),('Support',['Help','Contact','Status'])]):
    x=558+j*139;b+=rect(x,182,126,209,LIGHT,8)+txt(x+10,208,label,16,BLUE,700)
    for k,e in enumerate(entries): b+=txt(x+10,249+k*40,e,14,INK)
diagram('chunking','Chunking: organize related information','Nine ungrouped labels on the left become three titled groups of three on the right. The numbers are illustrative, not a universal memory threshold.',b,'Group by users’ mental models; validate headings with tasks.')

b=panel(34,'BEFORE · manual repetitive entry')+panel(530,'AFTER · assist, allow edits')
for i,s in enumerate(['Street','City','Region','Postcode','Country']): b+=rect(65,181+i*43,388,35,LIGHT,5)+txt(79,205+i*43,s,16,MUTED)
b+=rect(562,186,388,54,'#ffffff',7,'#94a3b8')+txt(582,220,'Postcode',17,INK)
b+=rect(562,253,388,70,'#dcfce7',7)+txt(582,284,'Suggested city and region',17,INK,700)+txt(582,306,'Review or edit the suggestion',15,MUTED)
b+=rect(562,339,171,49,BLUE,7)+txt(648,369,'Continue',16,'#ffffff',700,'middle')
diagram('teslers-law','Tesler: do not export avoidable complexity','A form asks for repeated address fields; a second offers optional postcode-assisted suggestions that users can review and edit.',b,'Only auto-fill when source data is reliable and editable.')

b=panel(34,'BEFORE · every setting at once')+panel(530,'AFTER · essentials then advanced')
for i in range(8): b+=rect(67,185+i*26,386,21,LIGHT,4)+txt(77,201+i*26,'Setting '+str(i+1),14,MUTED)
b+=ui(562,180,'Profile settings','Name and email first','Save')
b+=rect(562,358,386,50,LIGHT,6)+txt(583,390,'Advanced settings  ▸',18,INK,700)
diagram('progressive-disclosure','Progressive disclosure: start with essentials','Eight settings crowd the first panel; the second foregrounds identity fields and labels advanced options as available on demand.',b,'Do not hide required fields or necessary warnings.')

b=panel(34,'BEFORE · remember a command')+panel(530,'AFTER · recognize an action')
b+=rect(77,223,384,64,NAVY,8)+txt(96,264,'Enter command: _______',19,'#ffffff')+txt(77,327,'Recall the delete shortcut?',17,MUTED)
for i,s in enumerate(['Edit','Share','Delete']):
    x=560+i*132;b+=rect(x,223,120,65,BLUE if i<2 else '#b91c1c',8)+txt(x+60,262,s,19,'#ffffff',700,'middle')
b+=txt(561,337,'Visible labels reduce memory demands.',17,MUTED)
diagram('recognition','Recognition over recall: show available actions','A command-only input requires recalling syntax; labeled Edit, Share, and Delete controls expose available actions.',b,'Make labels descriptive; still support expert shortcuts.')


def section(start, end):
    a=chapter.index(start);z=chapter.index(end,a+len(start));return a,z,chapter[a:z]

def replace_in_section(start, end, old, new, flags=0):
    global chapter
    a,z,part=section(start,end)
    if isinstance(old,str):
        assert part.count(old)==1, (start,'expected exactly one match',part.count(old))
        part=part.replace(old,new)
    else:
        part,n=old.subn(new,part)
        assert n==1,(start,'matches',n)
    chapter=chapter[:a]+part+chapter[z:]

def image(slug,alt):
    return f'![{alt}](../assets/diagrams/ux/{slug}.svg)'

# Replace existing ASCII images in the original chapter rather than copying text to companion notes.
replace_in_section('### The UX Design Process','## Identifying the Target Audience',re.compile(r'```\n\s*1\. Problem Definition.*?\n```',re.S), image('ux-process','Eight-stage UX process, showing research, prototyping, evaluation and iteration'))
replace_in_section('### Gestalt Principles','## Intriguing Design Observations',re.compile(r'```\n\+[-+ ]+.*?\n```',re.S),image('gestalt','Before and after: Gestalt proximity and similarity group related elements'))
for head,next_head,slug,alt in [
    ("### Golden Ratio (Φ)",'### 80/20 Rule','golden-ratio','Golden-ratio schematic: 61.8% content and 38.2% sidebar'),
    ('### 80/20 Rule','### F-Pattern','pareto','Hypothetical 80/20 chart comparing two frequent features and eight less-used features'),
    ('### F-Pattern','### 60-30-10 Rule','f-pattern','Schematic F-shaped scanning path over a web article'),
    ('### 60-30-10 Rule','### Rule of Thirds','60-30-10','60–30–10 proportional color palette and example interface'),
]:
    replace_in_section(head,next_head,re.compile(r'Visualization:\s*\n```.*?\n```',re.S),'**Visual example:**\n\n'+image(slug,alt))
# The rule of thirds is last in the existing file.
a=chapter.index('### Rule of Thirds')
part=chapter[a:]
part,n=re.subn(r'Visualization:\s*\n```.*?\n```','**Visual example:**\n\n'+image('rule-of-thirds','Rule-of-thirds grid with four intersections and an example focal point'),part,flags=re.S)
assert n==1,('thirds diagram count',n)
chapter=chapter[:a]+part
# The original Hick diagram linked an opaque external image; keep a local, editable example instead.
replace_in_section("### Hick's Law",'### Golden Ratio', '![output](https://github.com/user-attachments/assets/0406562f-c15b-4e90-b779-dff1b589f903)',image('hicks-law','Hick–Hyman heuristic: twelve choices versus organized task groups'))
replace_in_section("### Hick's Law",'### Golden Ratio',re.compile(r'```\n\s*Reaction Time \(RT\) = a \+ b \* log2\(n \+ 1\)\n```'), 'For a simple choice-reaction experiment, one common form is **RT = a + b × log₂(n + 1)**. The constants depend on the task, and real interfaces add familiarity, scanning, labels and complexity.')
# Correct claims which presented visual heuristics as measured or universal laws.
for old,new in [
 ('The goal is to ensure the experience is intuitive and seamless.','The goal is to make important tasks useful, understandable, accessible, and effective; evaluate these outcomes with users rather than assuming any interface is universally intuitive.'),
 ('The Golden Ratio, approximately 1.618, is a mathematical ratio commonly found in nature, art, and architecture. It is believed to be aesthetically pleasing and is used to create harmony and balance in design.','The golden ratio is approximately 1.618. It can be used as an optional layout proportion, but there is no universal evidence that interfaces using it are more usable or aesthetically preferred. Let content needs, readable line lengths, device sizes and testing determine final dimensions.'),
 ('- Creates a naturally pleasing look that feels comfortable to the user.','- Offers a repeatable starting proportion for a sketch, not a guaranteed pleasant result.'),
 ('- Helps in establishing a clear visual hierarchy by proportionally sizing elements.','- Can help explore size relationships; hierarchy still depends on content, labels and contrast.'),
 ('The **80/20 Rule**, or **Pareto Principle**, suggests that approximately 80% of effects come from 20% of causes. In design, this means that a small number of features often account for the majority of user engagement.','The **80/20 rule** is a heuristic that a minority of inputs sometimes accounts for a majority of observed effects. It is **not** a measured law that precisely 20% of interface features receive 80% of engagement. Check representative analytics and qualitative needs before prioritizing; infrequent security, recovery and accessibility functions can still be essential.'),
 ('- Recognize the 20% of features that deliver 80% of the value.','- Investigate which features support important tasks, even when usage is low.'),
 ('When scanning content, especially on web pages, users tend to read in an **F-pattern**. This pattern reflects how users\' eyes move across and down the page.','Some eye-tracking studies have observed **F-shaped scanning** on certain text-heavy pages, particularly when content is not well formatted. It is not a universal reading path: task, page structure, content, language direction and device influence scanning. The figure below is schematic, **not** measured eye-tracking data.'),
 ('- Place important information and navigation elements in the top-left area.','- Put important content early in a logical reading order; do not assume every language starts at the top left.'),
 ('- Position key headlines and calls-to-action at the top and left sides.','- Make headings and actions easy to find based on the task and reading direction.'),
 ('The **60-30-10 Rule** is a guideline for color usage in design, ensuring a balanced and harmonious palette.','The **60–30–10 rule** is an optional composition heuristic: roughly 60% dominant surface, 30% supporting surfaces and 10% accent by visual area. It is not a CSS requirement, a pixel-by-pixel quota or an accessibility standard. Count the relative visual impression rather than forcing exact percentages.'),
 ('- Prevents any one color from overpowering the design.','- Offers a starting point for experimenting with visual emphasis, not a guaranteed balance.'),
 ('- Creates a unified look that is aesthetically pleasing.','- Can make a palette more deliberate when semantic colors and readable contrast are considered separately.'),
 ('While not included in the original notes, the **Rule of Thirds** is another valuable design principle worth mentioning.','The **rule of thirds** is a composition aid borrowed from photography: a three-by-three grid can suggest where to place a focal subject. It is optional rather than a universal UI-layout standard.'),
 ('- Achieve a more engaging and dynamic layout by avoiding centered placement.','- Compare an off-center composition with a centered one; choose based on content and task, not a blanket ban on centering.'),
 ('- Position key elements at intersection points to naturally draw the user\'s eye.','- Try placing a focal subject near an intersection, then test whether the content remains readable and important controls are discoverable.'),
 ('2. Prepare the topics and questions in advance. Having a structured questionnaire with potential answers can guide the discussion.','2. Prepare open-ended topics and neutral questions in advance. Prewritten answer choices are appropriate for some surveys, but can lead participants in exploratory interviews.'),
 ('- Ensure that the interface provides instant feedback for user actions through visual cues, animations, or sounds, confirming that input has been received and is being processed.','- Provide timely, truthful feedback for user actions; do not claim an operation succeeded until it actually completed. Use accessible text/status messages as appropriate, not animation or color alone.'),
 ('- Providing right-click or long-press menus that reveal additional options related to a particular element, allowing users to access advanced features without cluttering the main interface.','- Providing a labeled visible way to reach advanced options. Right-click and long-press can be shortcuts but should not be the only discoverable interaction.'),
]:
    assert chapter.count(old)==1, ('source phrase changed or duplicated',old[:55],chapter.count(old))
    chapter=chapter.replace(old,new)
# Add concise decision guidance immediately inside each original named principle.
principles=[
 ('### The Structure Principle','structure','Structure: scattered content versus clear task-oriented groups','In practice: group related controls, preserve an understandable reading order, and make the next task clear. Grouping is a hypothesis until someone can find the information without coaching.'),
 ('### The Visibility Principle in User Interface Design','visibility','Visibility: ambiguous icons versus a discoverable labeled action','Do not use a pointer cursor as the only sign of interactivity. Expose essential actions with clear text and usable keyboard focus; make hidden options reachable through a visible label.'),
 ('### The Feedback Principle','feedback','Feedback: no response versus loading, success, and error messages','Distinguish the states **received**, **working**, **completed**, and **failed**. Make progress claims only when real progress is known, and tell users how to recover when an operation fails.'),
 ('### The Tolerance Principle','tolerance','Tolerance: irreversible deletion versus a clear confirmation and undo','Prefer prevention for dangerous actions and a genuine recovery path for reversible ones. Confirmation interrupts a task; use it where risk warrants the interruption, not on every click.'),
 ('### The Consistency Principle','consistency','Consistency: scattered styles versus stable action labels and semantics','Keep equivalent actions and terms predictable across screens, while differentiating genuinely different outcomes. A consistent color scheme alone does not guarantee consistent behavior.'),
 ('### Gestalt Principles','gestalt','Gestalt: proximity and similarity make relationships visible','Proximity and similarity are perceptual clues, not a replacement for headings, labels, semantic markup, or accessible grouping. Check that the relationships remain clear without color.'),
]
for heading,slug,alt,lesson in principles:
    needle=heading+'\n'
    assert chapter.count(needle)==1,heading
    chapter=chapter.replace(needle,needle+'\n'+image(slug,alt)+'\n\n'+lesson+'\n',1)
# Complement old law and rule sections with concrete design tests and caveats.
insertions=[
 ("### Hick's Law",'**Apply and test:** compare a single overwhelming list with clearly labeled categories, search or filters. Keep important paths visible; grouping adds clicks and can be worse for a familiar audience. Measure task completion and wrong turns rather than asserting a fixed time saving.'),
 ('### Golden Ratio (Φ)','**Try it:** sketch a content/sidebar split near 62/38, then compare it with a content-driven layout at narrow widths and 200% zoom. The ratio is a composition option, not an accessibility or quality score.'),
 ('### 80/20 Rule (Pareto Principle)','**Try it:** group representative feature-use counts, then inspect the long tail for rare but essential recovery, privacy and accessibility tasks. Never infer importance only from frequency.'),
 ('### F-Pattern','**Try it:** give a reader a specific finding task, watch where they look and what they miss, and rewrite headings if necessary. Do not call the schematic SVG an eye-tracking heatmap.'),
 ('### 60-30-10 Rule (Color Distribution)','**Try it:** choose a light dominant surface, a supporting panel and an accent action. Inspect the resulting UI in grayscale, test contrast for all text and controls, and keep success/error meaning independent of hue. Example tokens:\n\n```css\n:root {\n  --surface: #f8fafc;\n  --support: #243b53;\n  --accent: #087f8c;\n}\n.page { background: var(--surface); }\n.sidebar { background: var(--support); color: white; }\n.primary-action { background: var(--accent); color: white; }\n```\n\nThe tokens do **not** enforce 60/30/10 mathematically; the distribution depends on actual rendered areas.'),
 ('### Rule of Thirds','**Try it:** overlay a three-by-three grid on a hero illustration and compare center and intersection placements while checking cropping, heading legibility and mobile composition.'),
]
for heading,lesson in insertions:
    needle=heading+'\n';assert chapter.count(needle)==1,heading
    chapter=chapter.replace(needle,needle+'\n'+lesson+'\n',1)
# Append additional requested heuristics in this original chapter, without creating a companion.
chapter += '''

## Further UX laws and frontend applications

These are **models and design prompts**, not rules that predict the performance of a particular website. Each figure is a schematic example: build a prototype, define a task, and check with people who use the product.

### Fitts’s Law: distance and target size

![Fitts’s Law comparison of a small distant target and a larger nearby target](../assets/diagrams/ux/fitts-law.svg)

For pointing tasks, movement time depends partly on target distance and effective target width. Do not assume that a big button always belongs near every other element: placement, errors, grouping, and the user's input method also matter. Give primary pointer/touch controls enough usable target area and separation. Test them on small screens, with zoom, and with keyboard navigation; pointer target size alone does not make a control accessible.

**Exercise:** move a small icon action into a labeled button with a larger hit area, keep its accessible name, and compare misclicks on a touch device. Reference: [WCAG 2.2 target size (minimum)](https://www.w3.org/WAI/WCAG22/Understanding/target-size-minimum.html).

### Jakob’s Law: familiar conventions

![Jakob’s Law illustration: unexpected navigation versus labeled links in a familiar location](../assets/diagrams/ux/jakobs-law.svg)

People bring expectations from other products. A recognizable navigation pattern can lower the effort of learning, but convention is a starting hypothesis, not proof that a particular placement fits every task. Depart from a convention when research demonstrates a benefit and still provide discoverable labels, consistent behavior and keyboard access.

**Exercise:** compare two navigation prototypes with the same destinations and task; note first click, completion and misunderstandings.

### Chunking and the limits of Miller’s Law

![Chunking: nine disconnected labels versus three meaningful groups](../assets/diagrams/ux/chunking.svg)

Human working memory is limited, but the often quoted **seven plus or minus two** is not a universal maximum number of visible navigation items or an instruction to put exactly seven links in every menu. Familiarity, meaning and task change what people can handle. Group by useful categories and label those categories clearly, rather than hiding essential paths behind arbitrary numeric limits.

**Exercise:** ask someone to find a support option in an ungrouped list and in a version grouped by the user's terminology. Record wrong turns, not just subjective preference.

### Tesler’s Law: where complexity belongs

![Tesler’s Law example: a lengthy manual address form versus editable assisted suggestions](../assets/diagrams/ux/teslers-law.svg)

Some task complexity cannot simply disappear. An interface can handle reliable repetition through sensible defaults, constrained inputs or optional autofill, but hidden automation may create serious errors. Make suggestions reviewable and editable; maintain an ordinary manual path when data is unavailable or the suggestion is wrong.

**Exercise:** prototype address suggestions; test a wrong postcode, international address, keyboard-only path and no-network condition.

### Progressive disclosure

![Progressive disclosure: all settings visible versus essentials with an expandable advanced section](../assets/diagrams/ux/progressive-disclosure.svg)

Show what a user needs for the current task while making optional complexity discoverable on demand. Do **not** hide legal information, required fields, safety warnings, or frequent actions simply to create a cleaner-looking screen. An expandable section should have a clear label, appropriate expanded state, and keyboard support.

**Exercise:** compare how quickly a first-time user finds the main setting and how an experienced user finds the advanced control. Both matter.

### Recognition over recall

![Recognition over recall: memorized commands compared with labeled visible actions](../assets/diagrams/ux/recognition.svg)

Visible actions and examples let people recognize options instead of remembering undocumented syntax. Shortcuts remain useful for experts, but should supplement recognizable controls. A destructive action still needs an accurate name and an appropriate confirmation or recovery model.

**Exercise:** hide shortcut documentation and ask a newcomer to find Edit, Share and Delete. Restore visible labels and repeat with the same task criteria.

### UX decision checklist

Before shipping a change, write down: the user and task; the observed problem (separate from your hypothesis); the smallest viable prototype; what success and failure look like; keyboard, screen-reader and touch considerations; responsive/zoom behavior; error recovery; and what evidence would make you reconsider the design. Keep consent and privacy in mind when recording sessions, and describe study outcomes with their sample and conditions.

**References:** [Nielsen Norman Group: 10 usability heuristics](https://www.nngroup.com/articles/ten-usability-heuristics/), [W3C WCAG 2.2](https://www.w3.org/TR/WCAG22/), [MDN: accessibility](https://developer.mozilla.org/en-US/docs/Web/Accessibility), [Nielsen Norman Group: F-shaped scanning](https://www.nngroup.com/articles/f-shaped-pattern-reading-web-content/).
'''
# The visual rules still need text, not only image labels: ensure references are local and all generated assets parse.
assert len(chapter)>len(original)
NOTE.write_text(chapter,encoding='utf-8')
for p in sorted(ART.glob('*.svg')): ET.parse(p)
refs=set(re.findall(r'\.\./assets/diagrams/ux/([\w-]+\.svg)',chapter))
for ref in refs: assert (ART/ref).is_file(),ref
assert len(refs)==19,(len(refs),refs)
assert '[Color Distribution Bar]' not in chapter
assert '[Golden Rectangle]' not in chapter
assert '[F-Pattern Heat Map]' not in chapter
assert '[Rule of Thirds Grid]' not in chapter
assert '1. Problem Definition\n    ---' not in chapter
print(f'Updated original UX chapter: {len(original.splitlines())} -> {len(chapter.splitlines())} lines; {len(refs)} local SVG links; {len(list(ART.glob("*.svg")))} SVG files.')
