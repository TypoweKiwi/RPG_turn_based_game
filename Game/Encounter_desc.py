import random
#Templates written using Gemini AI
hostile_locations = [
    "a cursed graveyard",
    "the ruins of an ancient temple",
    "a mist-shrouded forest",
    "a desolate mountain pass",
    "a battlefield forgotten by time",
    "an abandoned village",
    "a sunken crypt beneath the marshes",
    "the mouth of a dark cave",
    "a scorched wasteland",
    "the edge of a forbidden swamp"
]

hostile_sights = [
    "the gnarled, grasping branches of the trees",
    "tombstones leaning at unnatural angles",
    "skeletons half-buried in the muddy ground",
    "strange, phosphorescent fungi casting a pale glow",
    "abandoned, rusted weaponry scattered about",
    "walls covered in disturbing, half-erased symbols",
    "a thick fog that seems to crawl rather than drift",
    "a flock of crows watching you in silence",
    "the dry, blackened bones of animals",
    "a single, distant light that suddenly flickers out"
]

hostile_sounds = [
    "the snap of a twig somewhere in the darkness",
    "a low, guttural growl carried on the wind",
    "a skittering sound, just beyond the edge of your vision",
    "a deathly silence where the normal sounds of nature are absent",
    "an echo of a long-past battle that seems to return with the wind",
    "a quiet, repeating whisper with unintelligible words",
    "the scraping of stone on stone from somewhere deep inside",
    "the sound of dripping water that echoes unnaturally",
    "a distant, mournful cry",
    "a sudden, loud crack, followed by a profound silence"
]

hostile_feelings_sensations = [
    "a sudden, piercing chill with no natural source",
    "the heavy, damp air that makes it hard to breathe",
    "a prickling on the back of your neck, as if you're being watched",
    "an overwhelming sense of loss and sorrow",
    "a pulsing headache that grows stronger with every step",
    "a strange, metallic taste in your mouth",
    "the feeling that the ground beneath your feet is somehow... sick",
    "a stickiness in the air that clings to your skin like a web",
    "a wave of irrational fear that clenches your stomach",
    "a disorienting feeling that you've been this way before"
]

hostile_intro_templates = [
    "\nAs you enter {location}, you're immediately struck by {feeling_sensation}. All around you, you see {sight}, and the only thing you can hear is {sound}.",
    "\nThe air grows thick as you approach {location}. From the distance comes {sound}, and your attention is drawn to {sight}. You are overcome by {feeling_sensation}.",
    "\n{location} greets you with a malevolent silence. Only after a moment do you notice {sound}, as {feeling_sensation} crawls up your spine. You can see {sight} everywhere.",
    "\nThe path leads you directly into {location}. The first thing you notice is {sight}. A moment later, {feeling_sensation} makes you all freeze and listen. The wind carries {sound}.",
    "\nYou stand at the edge of {location}. The stench of decay hits your nostrils, and {feeling_sensation} grips your heart. Your gaze falls upon {sight}, and from the darkness comes {sound}. Something is very wrong here.",
    "\nEven the sun seems to avoid this place. {location} is quiet, too quiet. Only {sound} breaks the dead silence. Your attention is captured by {sight} and the accompanying {feeling_sensation}."
]

safe_locations = [
    "a quiet woodland glade",
    "a sunlit hillside",
    "a tranquil village square",
    "the gates of a friendly outpost",
    "a mossy clearing beside a stream",
    "a cozy forest path",
    "a grassy knoll under a blue sky",
    "a small shrine to a forgotten god",
    "a blooming meadow",
    "a gentle riverbank"
]

safe_sights = [
    "sunbeams filtering through a green canopy of leaves",
    "a herd of deer drinking from a nearby stream",
    "smoke curling lazily from a distant chimney",
    "bees buzzing over wildflowers",
    "the clear, babbling water of a brook",
    "cart tracks on the road, indicating recent traffic",
    "a massive, ancient tree that seems to radiate peace",
    "colorful butterflies dancing in the air",
    "ripe berries hanging from bushes",
    "a sturdy stone bridge crossing the river"
]

safe_sounds = [
    "the song of birds echoing through the forest",
    "the gentle rustle of wind in the leaves",
    "the hum of insects in the warm air",
    "the distant sounds of conversation and laughter",
    "the soft babbling of a nearby creek",
    "the shouts of children playing in the distance",
    "the calm lowing of cattle in a pasture",
    "the sound of wind chimes from a nearby home",
    "the crunch of leaves underfoot",
    "the gentle splash of a fish jumping from the water"
]

safe_feelings_sensations = [
    "the warmth of the sun on your skin, loosening tense muscles",
    "a refreshing, light breeze",
    "the scent of freshly cut grass and wildflowers",
    "a sense of relief that washes away the weariness of travel",
    "the familiar smell of a campfire and baking bread",
    "the feeling that you can finally let your guard down for a moment",
    "a quiet peace that allows you to gather your thoughts",
    "the smell of damp earth after a recent, brief shower",
    "a pleasant exhaustion combined with a sense of safety",
    "a sudden wave of optimism and hope"
]

safe_intro_templates = [
    "\nAfter a long journey, you arrive at {location}. Your eyes are greeted by {sight}, and the air is filled with {sound}. You are filled with {feeling_sensation}.",
    "\n{location} is a welcome change after the hardships of your journey. You stop for a moment to admire {sight}. From the distance, you can hear {sound}, and {feeling_sensation} finally allows you to breathe.",
    "\nYou find shelter in {location}. You listen to {sound}, and your gaze is drawn to {sight}. It is here, for the first time in a long while, that you experience {feeling_sensation}.",
    "\nThe path widens, leading into {location}. The {feeling_sensation} is almost palpable. All around you, you can hear {sound}, and you see {sight}. It seems you can rest here.",
    "\nAt last! {location} appears before you like an oasis. You stop, and your ears are filled with {sound}. Your eyes fall upon {sight}, and {feeling_sensation} spreads through your bodies."
]

def generate_encounter_desc(hostile):
    if hostile:
        template = random.choice(hostile_intro_templates)
        return template.format(
            location=random.choice(hostile_locations),
            sight=random.choice(hostile_sights),
            sound=random.choice(hostile_sounds),
            feeling_sensation=random.choice(hostile_feelings_sensations)
        )
    else:
        template = random.choice(safe_intro_templates)
        return template.format(
            location=random.choice(safe_locations),
            sight=random.choice(safe_sights),
            sound=random.choice(safe_sounds),
            feeling_sensation=random.choice(safe_feelings_sensations)
        )

    