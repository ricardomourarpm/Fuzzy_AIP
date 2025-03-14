Here is a structured **README.md** file for the **Mamdani_AIP_2Phase_english.py** script based on the information extracted from the provided PDF document.

---

## README.md  

# Two-Stage Fuzzy Inference System for Submarine AIP Selection  

### Overview  
This repository contains the implementation of a **Decision Support System (DSS)** using a **two-stage Mamdani Fuzzy Inference Model** to evaluate and recommend **Air-Independent Propulsion (AIP)** systems for submarines. The model aims to improve the selection process by considering **operational, economic, and environmental** factors, reducing human subjectivity in decision-making.

### Features  
- **Two-stage fuzzy inference:**  
  - Stage 1: Evaluates operational, economic, and environmental scores.  
  - Stage 2: Aggregates these scores to generate a final **recommendation level**.  
- **Fuzzy Mamdani Model:** Utilizes fuzzy logic to handle uncertainty and qualitative decision factors.  
- **Multiple AIP system evaluation:** Compares **Fuel Cells (FC)**, **Stirling Engines (SE)**, **Steam Turbines (ST)**, and **Diesel Engines (DE)**.  
- **Normalization and ranking:** Outputs a final recommendation score between **0% and 100%**.  
- **Expert-driven rule set:** Developed based on **Portuguese Navy (PoN) submarine specialists'** knowledge.  

---

## Installation  

### Prerequisites  
Ensure you have **Python 3.x** installed along with the required libraries:  

```bash
pip install numpy scipy skfuzzy matplotlib
```

---

## Usage  

### Running the Script  
Execute the **Mamdani_AIP_2Phase_english.py** script to generate recommendation scores for AIP systems:  

```bash
python Mamdani_AIP_2Phase_english.py
```

### Output  
The script will generate:  
- **Membership function plots** for the fuzzy variables.  
- **Final ranking of AIP systems** with a recommendation score (0–100%).  

---

## Methodology  

### 1. Input Variables  
The system evaluates **nine** key variables grouped into three subcategories:  

| **Category**  | **Variables**  |  
|--------------|--------------|  
| **Operational**  | Efficiency, Power, Acoustic Signature  |  
| **Economic**  | Acquisition Cost, Maintenance Cost, Operating Cost  |  
| **Environmental**  | Thermal Emission, Byproducts, Size  |  

### 2. Fuzzy Inference Process  
The **Mamdani Fuzzy Model** follows:  
1. **Fuzzification:** Converts crisp numerical values into fuzzy linguistic terms.  
2. **Inference:** Applies expert-defined fuzzy rules to generate intermediate scores.  
3. **Defuzzification:** Uses the **centroid method** to obtain a crisp output value.  
4. **Normalization:** Scales the final score to **0–100%** for easy interpretation.  

### 3. Evaluation of AIP Systems  
The DSS evaluates four AIP systems:  

| **AIP System** | **Recommendation Score (%)** |  
|---------------|----------------------------|  
| **Fuel Cells (FC)** | 86%  |  
| **Stirling Engines (SE)** | 49%  |  
| **Steam Turbines (ST)** | 24%  |  
| **Diesel Engines (DE)** | 24%  |  

---

## Results  

- **Fuel Cells (FC)** emerge as the most recommended **(86%)**, offering superior efficiency and stealth.  
- **Stirling Engines (SE)** are **moderately recommended** (**49%**), balancing cost and noise.  
- **Steam Turbines (ST) and Diesel Engines (DE)** receive **low scores (24%)**, mainly due to high acoustic signatures and environmental impact.  

### Visualization  
The system generates **star plots** and **fuzzy membership function graphs** for enhanced interpretability.  

---

## References  
This implementation is based on the research article:  
**"Two-Stage Fuzzy Inference for Submarine Air-Independent Propulsion Selection"**  
by **Nuno Pessanha Santos, Ricardo Moura, and Ana Reis Sintra**.  

For more details, visit the **full research paper** or the **GitHub repository**:  
🔗 [Full Implementation Code](https://github.com/ricardomourarpm/Fuzzy_AIP/blob/main/Mamdani_AIP_2Phase_english.py)  

---

## Contributors  
- **Ricardo Moura**  
- **Nuno Pessanha Santos**  
- **Ana Reis Sintra**  

---

## License  
This project is licensed under the **MIT License**. See the `LICENSE` file for details.  

---

Let me know if you need any modifications! 🚀
