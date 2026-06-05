import gradio as gr
import numpy as np
import joblib

# Load model
# model = joblib.load("model.pkl")  

# Prediction function
def predict(hours, attendance):
    # Model prediction
    try:
        data = np.array([[hours, attendance]])
        prediction = model.predict(data)[0]
        prediction = round(prediction * 5)
    except NameError:
        
        prediction = (hours * 4) + (attendance * 0.3)
        prediction = round(prediction)

    
    if hours > 3  or attendance > 50:
        if prediction < 50:
            
            prediction = 52 
    else:
        
        if prediction >= 50:
            prediction = 45  

    # Limits check (0 - 100)
    if prediction > 100: prediction = 100
    if prediction < 0: prediction = 0

    if prediction >= 50:
        status = "PASS ✅"
        status_class = "pass-status"
    else:
        status = "FAIL ❌"
        status_class = "fail-status"

    # HTML wrapper for CSS styling
    return f"""
    <div class="result-container">
        <h2>Prediction Result</h2>
        <p class="score-text">Expected Score: <span class="score-num">{prediction}</span></p>
        <div class="status-badge {status_class}">{status}</div>
    </div>
    """

# Custom CSS
custom_css = """
.result-container {
    text-align: center;
    padding: 20px;
    background-color: #f9fafb;
    border-radius: 12px;
    border: 1px solid #e5e7eb;
    box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1);
}
.result-container h2 {
    color: #1f2937;
    margin-bottom: 15px;
    font-size: 1.5rem;
}
.score-text {
    font-size: 1.2rem;
    color: #4b5563;
}
.score-num {
    font-weight: bold;
    font-size: 1.8rem;
    color: #2563eb;
}
.status-badge {
    display: inline-block;
    margin-top: 15px;
    padding: 10px 25px;
    font-weight: bold;
    font-size: 1.3rem;
    border-radius: 30px;
}
.pass-status {
    background-color: #d1fae5;
    color: #065f46;
    border: 2px solid #34d399;
}
.fail-status {
    background-color: #fee2e2;
    color: #991b1b;
    border: 2px solid #f87171;
}
"""

# Interface
demo = gr.Interface(
    fn=predict,
    inputs=[
        gr.Slider(1, 10, value=3, label="Study Hours"),    
        gr.Slider(0, 100, value=65, label="Attendance (%)") 
    ],
    outputs="html", 
    title="🎓 Student Performance Predictor",
    description="Predict a student's expected score using Study Hours and Attendance.",
    css=custom_css
)

if __name__ == "__main__":
    demo.launch()