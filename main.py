from flask import Flask, render_template, request
import random

app = Flask(__name__)

# Tarot card meanings
TAROT_CARDS = {
    "The Fool": "New beginnings, optimism, trust in life.",
    "The Magician": "Action, the power to manifest.",
    "The High Priestess": "Inaction, going within, the subconscious.",
    "The Empress": "Abundance, nurturing, fertility, life in bloom!",
    "The Emperor": "Structure, stability, rules and power.",
    "The Hierophant": "Institutions, tradition, society and its rules.",
    "The Lovers": "Sexuality, passion, choice, uniting.",
    "The Chariot": "Movement, progress, integration.",
    "Strength": "Courage, subtle power, integration of animal self.",
    "The Hermit": "Meditation, solitude, consciousness.",
    "Wheel of Fortune": "Cycles, change, ups and downs.",
    "Justice": "Fairness, equality, balance.",
    "The Hanged Man": "Surrender, new perspective, enlightenment.",
    "Death": "The end of something, change, the impermeability of all things.",
    "Temperance": "Balance, moderation, being sensible.",
    "The Devil": "Destructive patterns, addiction, giving away your power.",
    "The Tower": "Collapse of stable structures, release, sudden insight.",
    "The Star": "Hope, calm, a good omen!",
    "The Moon": "Mystery, the subconscious, dreams.",
    "The Sun": "Success, happiness, all will be well.",
    "Judgement": "Rebirth, a new phase, inner calling.",
    "The World": "Completion, wholeness, attainment, celebration of life." 
}

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/reading', methods=['POST'])
def reading():
    num_cards = int(request.form.get('num_cards', 3))
    drawn_cards = random.sample(list(TAROT_CARDS.items()), num_cards)
    return render_template('reading.html', cards=drawn_cards)

if __name__ == '__main__':
    app.run(debug=True)
