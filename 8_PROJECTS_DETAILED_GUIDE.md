# 8 Major Projects - Step-by-Step Guide
### Data Scientist Roadmap 2027 - Complete Clarity for Every Project

> **How to use this guide:** For each project, follow Step 1 → Step 10 in order.  
> Don't move to next project until current one is pushed to GitHub + README is done.  
> Each project takes 4-7 days with 10+ hours/day.

---

## PROJECT 1: Data Analyzer (Jupyter EDA Report)
**Phase:** 1 - Learn Python  
**Time:** Week 3 (7 days)  
**Tools:** Python, NumPy, Pandas, Matplotlib, Seaborn, Jupyter

**Goal:** Prove you can take a raw CSV file and produce a clean, professional data report with charts and insights.

**Best Dataset:** Titanic (Kaggle) OR Sales CSV OR Airbnb - Download from Kaggle.com

#### Step-by-Step How To Do It:

**Step 1 - Create Folder Structure**
```
project1-data-analyzer/
├── data/           -> raw CSV here
├── notebooks/      -> Jupyter files
├── outputs/        -> charts saved as PNG
├── src/            -> python scripts
└── README.md
```

**Step 2 - Data Collection**
- Go to Kaggle → Search "Titanic Dataset"
- Download CSV → Put in `data/titanic.csv`

**Step 3 - Load Data in Jupyter**
- Open Jupyter Notebook
- `import pandas as pd`, `import numpy as np`
- `df = pd.read_csv('../data/titanic.csv')`
- Print `df.head()`, `df.info()`, `df.describe()` - This is your first check

**Step 4 - Data Cleaning (Most Important)**
- Check missing values: `df.isnull().sum()`
- Fill missing: `df['Age'].fillna(df['Age'].median())`
- Remove duplicates: `df.drop_duplicates()`
- Fix data types: `df['Survived'] = df['Survived'].astype(int)`
- Save cleaned file as `cleaned_titanic.csv`

**Step 5 - Exploratory Data Analysis (EDA)**
Create 10+ charts:
- Histogram: Age distribution
- Bar chart: Survival by Gender
- Pie chart: Class vs Survival
- Pair plot: All numeric columns together
- Correlation heatmap: `sns.heatmap(df.corr(), annot=True)`
- Box plot: Fare vs Survival

**Step 6 - Add Insights (Write in Notebook Markdown)**
For each chart write 2 lines:
> *"From chart: Female passengers survived more (74% vs 19% for males). Insight: Gender is important factor."*

Write 5 Business / Final Insights at end.

**Step 7 - Save Charts**
- `plt.savefig('../outputs/survival_by_gender.png')` for every chart

**Step 8 - Create a Python Script Version**
- Copy important notebook code into `src/analyzer.py`
- Make it run with one command: `python src/analyzer.py`

**Step 9 - README.md**
Write: Project title, Dataset link, Steps done, 5 Insights, How to run, Screenshots

**Step 10 - GitHub Push**
- Create repo `project1-data-analyzer`
- Push with 3 commits: Data, Notebook, Charts

**✅ Done Criteria:** Anyone can open your notebook and understand data in 5 minutes. 10+ charts + 5 insights.

---

## PROJECT 2: Business Insights Report (Statistics + Excel)
**Phase:** 2 - Master Statistics  
**Time:** Week 6  
**Tools:** Excel, SciPy, Statsmodels, Python

**Goal:** Prove you can do statistical testing and give business recommendations, not just charts.

**Best Dataset:** Superstore Sales or Marketing Campaign data from Kaggle

#### Steps:

**Step 1 - Excel Part (Docs Required)**
- Open dataset in Excel
- Create Pivot Table: Sales by Region, by Category
- Create 2 charts in Excel (Bar + Line)
- Save as `excel_analysis.xlsx`

**Step 2 - Hypothesis Testing in Python**
Pick 2 questions:
- Q1: "Is there income difference between Male vs Female?" → Run T-Test `scipy.stats.ttest_ind()`
- Q2: "Does Advertising increase Sales?" → Correlation + Regression

**Step 3 - Confidence Interval**
- Use `statsmodels` to get confidence interval
- Write interpretation: "We are 95% confident average sales is between 2000-2500"

**Step 4 - Linear Regression**
- `import statsmodels.api as sm`
- Fit model: Sales ~ Ad_Spend + Discount
- Check R², p-value - If p < 0.05, factor is significant

**Step 5 - Write Business Report (PDF style in Notebook)**
Structure:
1. Business Problem (2 lines)
2. Data Summary
3. Test Results (with p-values)
4. 5 Recommendations: "Increase ad spend on Instagram because p=0.01"

**Step 6 - Visuals**
- Regression plot
- Residual plot
- Excel chart screenshots

**Step 7 - README + GitHub**
- Upload Excel + Notebook
- README must have "Business Recommendations" section

**✅ Done Criteria:** Report has statistical proof (p-value, CI) + business decisions.

---

## PROJECT 3: Sales Dashboard (SQL + Power BI + Tableau)
**Phase:** 3 - Data Analysis & Viz  
**Time:** Week 8-9 (10 days)  
**Tools:** SQL, Pandas, Power BI, Tableau

**Goal:** Prove you can extract data with SQL and make live business dashboard.

#### Steps:

**Step 1 - Database Setup**
- Download Sales DB (SQLite) OR use MySQL
- Load 3 tables: Orders, Customers, Products into DB
- Check with `SELECT * FROM Orders LIMIT 5;`

**Step 2 - Write 20 SQL Queries**
Categories:
- Top 5 products by sales: `ORDER BY SUM(Price) DESC LIMIT 5`
- Monthly growth: `GROUP BY DATE_TRUNC('month', OrderDate)`
- Region-wise profit: `JOIN + GROUP BY Region`
- Write all queries and save in `queries.sql` file

**Step 3 - Clean Data in Python**
- Connect Python to SQL using `sqlalchemy`
- `pd.read_sql("SELECT...", engine)` → Load in Pandas
- Save clean file for Power BI

**Step 4 - Power BI Dashboard (Main)**
- Open Power BI Desktop
- Import clean CSV
- Create Relationships: CustomerID, ProductID
- Add 10 visuals:
  - KPI Cards: Total Sales, Total Profit, Orders
  - Bar: Sales by Month
  - Map: Sales by State
  - Line: Profit Trend
  - Slicer: Filter by Year, Category
- Add DAX measure: `Total Sales = SUM(Sales[Amount])`

**Step 5 - Tableau Version**
- Redo same 5 best charts in Tableau Public (free)
- Publish to Tableau Public → Get link

**Step 6 - Publish**
- Save Power BI as `.pbix`
- Take screenshots → Put in README
- Publish Tableau link in README

**Step 7 - GitHub**
Repo contains: `queries.sql`, `clean_data.csv`, `dashboard.pbix`, `screenshots/`, `README.md`

**✅ Done Criteria:** Live Tableau link + Power BI file + SQL file. Looks like real company's dashboard.

---

## PROJECT 4: Customer Churn Predictor (Machine Learning)
**Phase:** 4 - Machine Learning  
**Time:** Week 12-13  
**Tools:** Scikit-learn, XGBoost, LightGBM, Optuna

**Goal:** Predict if a customer will leave company. Explain model accuracy, precision, recall.

**Dataset:** Telco Customer Churn (Kaggle) - Very famous interview dataset

#### Steps:

**Step 1 - Load + Understand**
- Load CSV, print shape, check missing values
- Target column = `Churn` (Yes/No → 1/0)

**Step 2 - EDA**
- Churn % by Contract Type, by Tenure
- Charts: Who is leaving? New customers churn more?
- Write 3 findings

**Step 3 - Feature Engineering**
- One-Hot Encoding for categorical: `pd.get_dummies()`
- Train-Test Split: 80% train, 20% test
- Scaling for numeric: `StandardScaler`

**Step 4 - Train 3 Models**
```text
1. RandomForestClassifier()
2. XGBClassifier() - XGBoost
3. LGBMClassifier() - LightGBM
```
- Train all 3, print accuracy for each

**Step 5 - Evaluate Properly**
- Confusion Matrix
- Precision, Recall, F1-Score (most important for churn)
- ROC Curve - Show which model is best

**Step 6 - Hyperparameter Tuning with Optuna**
- `optuna.create_study()` → Try 20 trials for XGBoost
- Get best params, retrain model
- Save best model: `joblib.dump(model, 'churn_model.pkl')`

**Step 7 - Feature Importance**
- Plot: Which 5 features matter most? (e.g., Tenure, MonthlyCharges)
- Write business insight: "Customers with tenure <12 months churn 50% more"

**Step 8 - Deploy Preview**
- Save model + scaler
- Create simple test prediction: Give one customer data → Predict churn?

**Step 9 - README**
- Problem, Accuracy table (3 models comparison), Feature Importance chart, Business actions to reduce churn

**✅ Done Criteria:** Accuracy > 80%, 3 models compared with Optuna, confusion matrix + ROC curve included.

---

## PROJECT 5: AI Chatbot + Image Classifier (Deep Learning + GenAI)
**Phase:** 5 - Deep Learning & GenAI  
**Time:** Week 15-17  
**Tools:** PyTorch, Hugging Face, OpenAI API, FastAPI/Streamlit

### Part A: Image Classifier

**Step 1 - Dataset**
- Use CIFAR-10 OR Plant Disease OR Food-5K from Kaggle/torchvision
- `torchvision.datasets.CIFAR10()` - No download needed, auto download

**Step 2 - Build CNN in PyTorch**
- Layers: Conv → ReLU → Pool → Fully Connected
- Define `class MyCNN(nn.Module)`
- 5-10 epochs training

**Step 3 - Train + Test**
- Loss = CrossEntropyLoss, Optimizer = Adam
- Print accuracy every epoch → Aim 85%+

**Step 4 - Save Model**
- `torch.save(model.state_dict(), 'cnn_model.pth')`

### Part B: Generative AI Chatbot (RAG)

**Step 5 - Hugging Face Basics**
- Use pipeline: `pipeline("sentiment-analysis")` → Run first test
- Try `pipeline("text-generation")`

**Step 6 - Build Q&A Bot with OpenAI**
- Install `openai`, `langchain`
- Create simple bot: User question → OpenAI API → Answer
- Test with 5 questions

**Step 7 - RAG (Chat with PDF)**
- Load PDF → Split into chunks
- Embed with `sentence-transformers`
- Store in Chroma Vector DB
- When user asks → Retrieve chunk → Send to LLM → Answer

**Step 8 - Combine Into One App**
- Streamlit UI: Two tabs → "Image Classifier" + "AI PDF Chatbot"
- Upload image → Show prediction
- Upload PDF → Ask questions

**✅ Done Criteria:** Both models work + Streamlit app with screenshots. Upload to HF Spaces later.

---

## PROJECT 6: Big Data ETL Pipeline (Spark + Snowflake + AWS)
**Phase:** 6 - Data Engineering & Cloud  
**Time:** Week 19-20  
**Tools:** Apache Spark, Databricks, Snowflake, AWS S3

**Goal:** Prove you can handle big data (1GB+), move it to cloud, and store in warehouse.

**Dataset:** 1GB Sales data (Kaggle) OR NYC Taxi data

#### Steps:

**Step 1 - Upload to AWS S3**
- Create S3 Bucket
- Upload raw CSV → `s3://my-bucket/raw/`

**Step 2 - Process with Spark (PySpark)**
- Create Databricks account (free) OR local Spark
- Read from S3 in Spark DataFrame
- Transformations: `df.filter()`, `groupBy().sum()`, `join()`
- Handle large data fast (show Spark logs)

**Step 3 - Save Processed Data**
- Save as Parquet to `s3://my-bucket/processed/`
- Parquet is faster than CSV for big data

**Step 4 - Load into Snowflake**
- Create Snowflake account (free trial)
- Create table: `CREATE TABLE sales_processed...`
- Copy data from S3 stage → Snowflake table

**Step 5 - Query in Snowflake**
- Run SQL: Top customers, monthly sales
- Screenshot results

**Step 6 - Documentation**
- Draw pipeline diagram: S3 → Spark → S3 → Snowflake
- README: Architecture, steps, technologies, benefits

**✅ Done Criteria:** Pipeline diagram + Screenshots of S3, Spark job, Snowflake table. Code in GitHub.

---

## PROJECT 7: Production ML Service (MLflow + Docker + FastAPI + Kubernetes)
**Phase:** 7 - MLOps  
**Time:** Week 21-22  
**Tools:** MLflow, Docker, FastAPI, Kubernetes

**Goal:** Take Project 4 model and turn into live API that companies can use.

**Reuse:** Your Churn model from Project 4

#### Steps:

**Step 1 - MLflow Tracking**
- `mlflow.start_run()`
- Log params: `mlflow.log_params({"max_depth": 5})`
- Log metrics: `mlflow.log_metric("accuracy", 0.87)`
- Log model: `mlflow.sklearn.log_model(model, "model")`
- Open MLflow UI → Screenshot of experiments

**Step 2 - Build FastAPI**
```text
POST /predict
Input: {"tenure": 12, "monthly_charge": 70, "contract": "Month-to-month"}
Output: {"churn_prediction": "Yes", "probability": 0.82}
```
- Create `main.py` with FastAPI
- Load model with `joblib.load()`
- Test at `http://127.0.0.1:8000/docs` (Swagger UI)

**Step 3 - Dockerize**
- Create `Dockerfile`:
  ```
  FROM python:3.9
  WORKDIR /app
  COPY . /app
  RUN pip install -r requirements.txt
  CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
  ```
- Build: `docker build -t churn-api .`
- Run: `docker run -p 8000:8000 churn-api`

**Step 4 - Kubernetes (Basic)**
- Install Minikube + kubectl
- Create `deployment.yaml`
- Deploy: `kubectl apply -f deployment.yaml`
- Get URL: `kubectl get pods` → Should be Running

**Step 5 - README**
- MLflow screenshot, Swagger screenshot, Docker commands, K8s status

**✅ Done Criteria:** Live API docs working + Docker image built + MLflow experiment logged.

---

## PROJECT 8: Capstone AI App (Full Portfolio Project)
**Phase:** 8 - Build Real-World Projects  
**Time:** Week 23-24  
**Tools:** All previous skills + Streamlit + GitHub + HF Spaces

**Goal:** One complete app that uses everything: Data → ML → API → UI → Cloud. This is your interview hero project.

**Idea:** "AI Sales Forecaster for Small Business"
- Owner uploads Sales CSV → System predicts next month sales + shows dashboard + AI chatbot for advice

#### Steps:

**Step 1 - Architecture Design (Draw First)**
```
CSV Upload -> Spark Clean (optional) -> ML Model -> FastAPI -> Streamlit UI -> HF Spaces Deploy
```

**Step 2 - Build ML Model**
- Reuse learnings: Train Sales prediction model (Regression)
- Predict next 30 days sales
- Save model

**Step 3 - FastAPI Backend**
- Same as Project 7 - Create `/forecast` endpoint
- Input CSV path / data, Output prediction

**Step 4 - Streamlit Frontend**
- Page 1: Upload CSV, Show data preview
- Page 2: Dashboard (Charts like Project 3)
- Page 3: Forecast chart (Line chart of predicted sales)
- Page 4: AI Chatbot (Connect to Project 5 chatbot: "How to improve sales?")

**Step 5 - Docker + Deploy**
- Dockerize the app
- Deploy Streamlit to HF Spaces / Render / Streamlit Cloud
- Get live link

**Step 6 - GitHub + Kaggle Portfolio**
- Pin this repo on GitHub profile
- Upload 2 notebooks to Kaggle (Project 1 + Project 4)
- Add live demo link everywhere

**Step 7 - Final README (Make It Professional)**
- Problem, Solution, Tech Stack diagram, Live Link, Screenshots/GIF, How to run, Results, Future Improvements

**Step 8 - Resume & LinkedIn**
- Add under projects: "Built AI Sales Forecaster - ML + FastAPI + Streamlit, Live Demo link"
- Record 2-min demo video

**✅ Done Criteria:** Live link works, anyone can upload CSV and get forecast. This single project proves all 8 phases.

---

## Final Portfolio Checklist (Before Applying for Job)

- [ ] 8 GitHub repos, all with README + screenshots
- [ ] 1 Live demo link (Project 8 on HF Spaces)
- [ ] Kaggle profile with 2-3 notebooks
- [ ] Tableau Public dashboard link
- [ ] MLflow experiment screenshot
- [ ] Resume PDF with 3 best projects listed
- [ ] LinkedIn profile with portfolio link

**Interview Tip:** Project 8 = Story to tell. Project 4 = ML depth. Project 3 = Business skill. These 3 will get you interviews.
