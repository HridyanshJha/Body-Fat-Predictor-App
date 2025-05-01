from flask import Flask, request, render_template, url_for # type: ignore
import pickle

# Load the model
file1 = open('C:/Users/91962/OneDrive/Desktop/CODING/DATA Science project/BODY FAT Predictor/bodyfatmodel.pkl', 'rb')
rf = pickle.load(file1)
file1.close()

app = Flask(__name__, static_folder='static')

# Add custom context processor for meta tags
@app.context_processor
def inject_meta():
    return {
        'meta': {
            'viewport': 'width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no'
        }
    }

@app.route('/', methods=['GET', 'POST'])
def predict():
    if request.method == 'POST':
        try:
            my_dict = request.form

            density = float(my_dict['density'])
            abdomen = float(my_dict['abdomen'])
            chest = float(my_dict['chest'])
            weight = float(my_dict['weight'])
            hip = float(my_dict['hip'])

            # Validate input ranges
            if not (0.8 <= density <= 1.5 and 
                   40 <= abdomen <= 200 and 
                   60 <= chest <= 200 and 
                   30 <= weight <= 300 and 
                   50 <= hip <= 200):
                return render_template('home.html', error="Please enter valid measurements within normal ranges.")

            # Calculate body fat using the formula from research paper
            body_fat = 495 / density - 450
            
            # Calculate body composition
            fat_mass = (body_fat/100) * weight
            lean_mass = weight - fat_mass
            
            # Calculate body fat category
            if body_fat < 6:
                category = "Essential Fat"
            elif body_fat < 14:
                category = "Athletes"
            elif body_fat < 18:
                category = "Fitness"
            elif body_fat < 25:
                category = "Average"
            else:
                category = "Above Average"

            context = {
                'body_fat': round(body_fat, 2),
                'category': category,
                'measurements': {
                    'density': density,
                    'abdomen': abdomen,
                    'chest': chest,
                    'weight': weight,
                    'hip': hip
                },
                'composition': {
                    'fat_mass': round(fat_mass, 2),
                    'lean_mass': round(lean_mass, 2)
                }
            }

            return render_template('show.html', **context)
            
        except Exception as e:
            print(f"Error: {str(e)}")
            return render_template('home.html', error="An error occurred. Please check your inputs.")

    return render_template('home.html')

def get_health_status(body_fat):
    if body_fat <= 5:
        return "Essential Fat Range - Very Low"
    elif body_fat <= 13:
        return "Athletic Range - Optimal for athletes"
    elif body_fat <= 17:
        return "Fitness Range - Healthy"
    elif body_fat <= 24:
        return "Average Range - Acceptable"
    else:
        return "Above Average - Consider lifestyle changes"

def get_recommendations(body_fat):
    if body_fat <= 5:
        return [
            "Consult a healthcare provider as this is very low",
            "Increase caloric intake",
            "Focus on balanced nutrition",
            "Reduce intense exercise"
        ]
    elif body_fat <= 13:
        return [
            "Maintain current fitness routine",
            "Ensure adequate protein intake",
            "Focus on recovery and rest",
            "Monitor energy levels"
        ]
    elif body_fat <= 17:
        return [
            "Continue balanced diet and exercise",
            "Mix cardio and strength training",
            "Stay hydrated",
            "Get adequate sleep"
        ]
    elif body_fat <= 24:
        return [
            "Maintain healthy lifestyle habits",
            "Regular moderate exercise",
            "Balanced nutrition",
            "Regular health check-ups"
        ]
    else:
        return [
            "Consider increasing physical activity",
            "Focus on portion control",
            "Consult a nutritionist",
            "Regular health monitoring"
        ]

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
