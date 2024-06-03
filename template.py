import random
emotions_list = [
	"lighthearted fun, amusement, mirth, joviality, laughter, playfulness, silliness, jesting",
	"happiness, excitement, joy, exhilaration, delight, jubilation, bliss, Cheerfulness",
	"ecstasy, pleasure, bliss, rapture, Beatitude",
	"contentment, relaxation, peacefulness, calmness, satisfaction, Ease, Serenity, fulfillment, gladness, lightness, serenity, tranquility",
	"thankfulness, gratitude, appreciation, gratefulness",
	"sympathy, compassion, warmth, trust, caring, Clemency, forgiveness, Devotion, Tenderness, Reverence",
	"infatuation, having a crush, romantic desire, fondness, butterflies in the stomach, adoration",
	"hope, enthusiasm, optimism, Anticipation, Courage, Encouragement, Zeal, fervor, inspiration, Determination",
	"triumph, superiority",
	"pride, dignity, self-confidently, honor, self-consciousness",
	"interest, fascination, curiosity, intrigue",
	"awe, awestruck, wonder",
	"astonishment, surprise, amazement, shock, startlement",
	"concentration, deep focus, engrossment, absorption, attention",
	"contemplation, thoughtfulness, pondering, reflection, meditation, Brooding, Pensiveness",
	"relief, respite, alleviation, solace, comfort, liberation",
	"yearning, longing, pining, wistfulness, nostalgia, Craving, desire, Envy, homesickness, saudade",
	"teasing, bantering, mocking playfully, ribbing, provoking lightly",
	"impatience, irritability, irritation, restlessness, short-temperedness, exasperation",
	"sexual lust, carnal desire, lust, feeling horny, feeling turned on",
	"doubt, distrust, suspicion, skepticism, uncertainty, Pessimism",
	"fear, terror, dread, apprehension, alarm, horror, panic, nervousness",
	"worry, anxiety, unease, anguish, trepidation, Concern, Upset, pessimism, foreboding",
	"confusion, bewilderment, flabbergasted, disorientation, Perplexity",
	"embarrassment, shyness, mortification, discomfiture, awkwardness, Self-Consciousness",
	"shame, guilt, remorse, humiliation, contrition",
	"disappointment, regret, dismay, letdown, chagrin",
	"sadness, sorrow, grief, melancholy, Dejection, Despair, Self-Pity, Sullenness, heartache, mournfulness, misery",
	"resentment, acrimony, bitterness, cynicism, rancor",
	"contempt, disapproval, scorn, disdain, loathing, Detestation",
	"disgust, revulsion, repulsion, abhorrence, loathing",
	"anger, rage, fury, hate, irascibility, enragement, Vexation, Wrath, Peevishness, Annoyance",
	"spite, sadism, malevolence, malice, desire to harm, schadenfreude",
	"sourness, tartness, acidity, acerbity, sharpness",
	"physical pain, suffering, torment, ache, agony",
	"helplessness, powerlessness, desperation, submission",
	"fatigue, exhaustion, weariness, lethargy, burnout, Weariness",
	"numbness, detachment, insensitivity, emotional blunting, apathy, existential void, boredom, stoicism, indifference",
	"being drunk, stupor, intoxication, disorientation, altered perception",
	"jealousy, envy, covetousness"
]



ethnicities = [
	"Asian",
	"Black or African American",
	"Hispanic or Latino",
	"American Indian or Alaska Native",
  "Indian",
	"Native Hawaiian or Other Pacific Islander",
	"White",
  "white caucasian european",
  "white caucasian north american",
	"Middle Eastern",
	"North African",
	"South Asian",
  "arabic",
	"Southeast Asian"
]

genders = ["man", "woman"]

intensities = ["intense","subtle", ""]

ages = []

results=[]
# Start with the provided ages and increment by 10 years
start_age = 20
end_age = 80

file = open('emo_prompts.txt','w')


while start_age <= end_age:
    age_range_string = f"of {start_age} years"
    ages.append(age_range_string)
    start_age += 10
for emotion_index in range(len(emotions_list)):
    emotion = emotions_list[emotion_index]

    for gender_index in range(len(genders)):
        gender = genders[gender_index]

        for age_index in range(len(ages)):
            age = ages[age_index]

            # Loop through all ethnicities
            for ethnicity_index in range(len(ethnicities)):
                ethnicity = ethnicities[ethnicity_index]
                for i in range (1):
                  emotions= emotion.split(", ")
                  index= random.randint(0,len(emotions)-1)
                  selected_emotion1= emotions[index]
                  del emotions[index]
                  index= random.randint(0,len(emotions)-1)
                  selected_emotion2= emotions[index]

                  for intensity in intensities:

                    # Combine emotion, gender, age, and ethnicity
                    combined_string = f"Very realistic high quality portrait DSLR photo of a {ethnicity} {gender} {age} who seems to be feeling genuine {intensity} {selected_emotion1} and {selected_emotion2}. The {gender} is looking into the camera. Ultra-realistic DSLR photo with blurred background."
                    print(combined_string)
                    file.writelines(combined_string+ '\n')
                    results.append(combined_string)


file.close()

negative_prompt = "misshaped, exaggerated, acting, grimacing, grimace, fingers, low quality, lowres, fake, photoshop, extreme"

print(len(results))
# misshaped, exaggerated, acting, grimacing, grimace, fingers, low quality, lowres, fake, photoshop, extreme
