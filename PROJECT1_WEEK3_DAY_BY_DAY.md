# Project 1: Data Analyzer - Week 3 Day-by-Day Execution Plan
### 10+ Hours Daily | 7 Days | Python, NumPy, Pandas, Jupyter

**Target to complete this week:**
- [ ] Machine ready: Anaconda, Jupyter, VS Code, Git
- [ ] Titanic dataset downloaded and cleaned
- [ ] Complete Jupyter Notebook with 10+ charts + 5 insights
- [ ] 1 Python script version
- [ ] GitHub repo pushed with README

**Daily Rule:** 2 hours theory then 3 hours coding then 2 hours project then 1 hour revision + GitHub push. No zero day.

---

## DAY 15 (Monday) - SETUP DAY
**Goal:** Environment ready + understand Jupyter. No coding confusion after today.

### Morning Block (05:00 - 10:00) - 5 hours
**05:00-07:00 - Theory**
- [ ] Video/Read: What is Jupyter Notebook? Points, cells, markdown, code cells vs outputs
- [ ] Learn Jupyter shortcuts: Shift+Enter, Ctrl+Enter, Tab, Esc + navigation
- [ ] Watch: How to install Anaconda and create environment

**07:30-10:00 - Practical Setup (Follow exactly)**
- [ ] 07:30: Download Anaconda from anaconda.com (write install path - no spaces)
- [ ] 08:00: Open Anaconda Prompt → `conda create -n ds2027 python=3.11` → `conda activate ds2027`
- [ ] 08:30: `pip install pandas numpy matplotlib seaborn jupyter ipykernel`
- [ ] 09:00: `python -m ipykernel install --user --name ds2027` → ensures Jupyter uses your env
- [ ] 09:30: Open VS Code → Install Extensions: Python, Jupyter, Pylance
- [ ] 09:30: `git --version` check → If not installed, install Git from git.com
- [ ] 10:00: Test by opening Jupyter → New Notebook → `import pandas; print(pandas.__version__)`

### Afternoon Block (10:30 - 16:00) - 5 hours
**10:30-12:30**
- [ ] Create project folder structure (copy from guide):
```
project1-data-analyzer/
  data/
  notebooks/
  outputs/
  src/
  README.md
```
- [ ] Download Titanic dataset: Kaggle > Search "Titanic Dataset" > Download CSV > Place in `data/titanic.csv`
- [ ] Open it in Notepad to see first 5 lines (check commas, columns)
- [ ] Create first notebook: `notebooks/01_load_data.ipynb` with title cell

**14:00-16:00**
- [ ] Practice: Create 5 markdown cells explaining each step in own words
- [ ] Practice: `print("Hello")`, variables, `type()`, `len()` in Jupyter
- [ ] Learn difference: `.py` script vs `.ipynb` notebook (write in markdown)

### Evening Block (16:30 - 21:00) - 3 hours
- [ ] Create GitHub repo: `project1-data-analyzer` → Push empty folder with README.md
- [ ] 19:00-20:00: Revise notes Day 15 → Push first commit: "Setup completed"
- [ ] 20:00-21:00: Revision flashcards: Jupyter shortcut list

**GitHub Push Today:** Initial folder + README

---

## DAY 16 (Tuesday) - PANDAS BASICS + LOAD DATA
**Goal:** Load Titanic data and understand shape, columns, data types.

### Morning Block (05:00 - 10:00)
**05:00-07:00 - Theory: Pandas**
- [ ] Watch: Pandas Series vs DataFrame, Series = column, DataFrame = table
- [ ] Learn: How Pandas reads CSV, what happens behind `pd.read_csv()`
- [ ] Revise NumPy array vs Pandas (NumPy = numbers only, Pandas = labels + mixed types)

**07:30-10:00 - Code Practice**
- [ ] In notebook, run:
```python
import pandas as pd
import numpy as np

df = pd.read_csv('../data/titanic.csv')
print(df.shape)        # (891, 12) - rows, cols
print(df.head())       # first 5 rows
print(df.tail())       # last 5 rows
print(df.columns.tolist())
print(df.dtypes)
```
- [ ] Check `df.info()` - Shows missing values per column (look for NaN)
- [ ] Check `df.describe()` - Gives mean, std, min, max for numbers
- [ ] Write markdown: "Dataset has 891 passengers, 12 columns"

### Afternoon Block (10:30 - 16:00)
**10:30-12:30 - Deep Practice**
- [ ] `df['Name'].head()` vs `df[['Name', 'Age']]` - Single vs multiple columns
- [ ] `df.shape[0]` for rows, `df.shape[1]` for columns
- [ ] Select rows: `df.iloc[0:5]`, `df.loc[0:5, 'Age']` - Learn iloc vs loc difference (write 5 lines)
- [ ] Filter: `df[df['Survived']==1].head()` - Passengers who survived

**14:00-16:00 - Project Work**
- [ ] Take screenshots of outputs for README
- [ ] Create `notebooks/02_explore.ipynb` - Save all exploration code
- [ ] Mini-exercise: Answer in markdown - "How many columns? Which column is target?"

### Evening Block (16:30 - 21:00)
- [ ] Revise all Pandas basics from today (15 min flashcards)
- [ ] 19:00-20:00: Notes + GitHub push "Added data loading notebook"
- [ ] 20:00-21:00: Practice custom: Load another CSV (e.g., sample sales) in 5 min

**GitHub Push Today:** `02_explore.ipynb` + data file

---

## DAY 17 (Wednesday) - DATA CLEANING
**Goal:** Clean data like professional - fix missing, duplicates, wrong types.

### Morning Block (05:00 - 10:00)
**05:00-07:00 - Theory**
- [ ] Learn: Why clean? Missing values impact model, duplicates cause wrong stats
- [ ] Study 3 ways to handle missing: Drop, Fill with mean/median, Fill with mode
- [ ] When to use mean vs median (median better if outliers exist)

**07:30-10:00 - Cleaning Code**
- [ ] Check missing:
```python
print(df.isnull().sum())
# Cabin has many missing (688), Age 177, Embarked 2
```
- [ ] Drop column with too many missing: `df = df.drop('Cabin', axis=1)` - Cabin not useful
- [ ] Fill numeric: `df['Age'] = df['Age'].fillna(df['Age'].median())`
- [ ] Fill categorical: `df['Embarked'] = df['Embarked'].fillna(df['Embarked'].mode()[0])`
- [ ] Remove duplicates: `print(df.duplicated().sum())` → `df = df.drop_duplicates()`
- [ ] Convert types: `df['Survived'] = df['Survived'].astype(int)`

### Afternoon Block (10:30 - 16:00)
**10:30-12:30 - More Cleaning Practice**
- [ ] Save cleaned: `df.to_csv('../data/cleaned_titanic.csv', index=False)`
- [ ] Reload cleaned file → `df_clean = pd.read_csv('../data/cleaned_titanic.csv')` → Check `df_clean.isnull().sum()` should be 0
- [ ] Practice renaming columns: `df.columns = ['PassengerId','Survived','Pclass','Name','Sex',...]`
- [ ] Handle string: `df['Sex'] = df['Sex'].str.lower()` - Make consistent

**14:00-16:00 - Project Notebook**
- [ ] Create `notebooks/03_cleaning.ipynb` - Full cleaning steps with markdown explanations
- [ ] Before/After proof: Print shape before cleaning (891,12) vs after (891,11) - cabin removed
- [ ] Write in markdown: What you cleaned and why (2 lines per step)

### Evening Block (16:30 - 21:00)
- [ ] Revise cleaning checklist: Missing → Duplicates → Types → Save
- [ ] Push cleaned CSV + notebook to GitHub
- [ ] 20:00-21:00: Quick test: Open cleaned CSV in Excel - Check it looks good

**GitHub Push Today:** `03_cleaning.ipynb` + `cleaned_titanic.csv`

---

## DAY 18 (Thursday) - MATPLOTLIB + SEABORN VISUALIZATION
**Goal:** Make 10 beautiful charts. Notebook should look like professional report.

### Morning Block (05:00 - 10:00)
**05:00-07:00 - Theory**
- [ ] Learn Matplotlib: `plt.figure(figsize=(10,6))`, `plt.title()`, `plt.xlabel()`, `plt.ylabel()`, `plt.show()`
- [ ] Difference: Matplotlib = low-level control | Seaborn = beautiful stats charts easy
- [ ] Study chart types: Histogram (distribution), Bar (categories), Pie (parts), Line (trend), Heatmap (correlation)

**07:30-10:00 - First 5 Charts (Save each as PNG)**
- [ ] Chart 1 - Survival Pie:
```python
df['Survived'].value_counts().plot.pie(autopct='%1.1f%%', title='Survival Rate')
plt.savefig('../outputs/01_survival_pie.png')
```
- [ ] Chart 2 - Survival by Gender (Bar):
```python
sns.barplot(data=df, x='Sex', y='Survived')
plt.title('Survival by Gender'); plt.savefig('../outputs/02_survival_gender.png')
```
- [ ] Chart 3 - Age Histogram:
```python
sns.histplot(data=df, x='Age', bins=20, kde=True)
plt.savefig('../outputs/03_age_dist.png')
```
- [ ] Chart 4 - Fare vs Class:
```python
sns.boxplot(data=df, x='Pclass', y='Fare')
plt.savefig('../outputs/04_fare_class.png')
```
- [ ] Chart 5 - Count Sex:
```python
df['Sex'].value_counts().plot.bar()
plt.savefig('../outputs/05_sex_count.png')
```

### Afternoon Block (10:30 - 16:00)
**10:30-12:30 - Next 5 Charts**
- [ ] Chart 6 - Correlation Heatmap:
```python
sns.heatmap(df.corr(numeric_only=True), annot=True, cmap='coolwarm')
plt.savefig('../outputs/06_heatmap.png')
```
- [ ] Chart 7 - Survival by Pclass:
```python
sns.barplot(data=df, x='Pclass', y='Survived')
plt.savefig('../outputs/07_pclass.png')
```
- [ ] Chart 8 - Pair Plot: `sns.pairplot(df[['Age','Fare','Survived']])` → save
- [ ] Chart 9 - Embarked vs Survival bar
- [ ] Chart 10 - Family size impact: Create new col `df['FamilySize'] = df['SibSp']+df['Parch']+1` → bar chart

**14:00-16:00 - Make It Look Professional**
- [ ] Add title, labels, tighten `plt.tight_layout()` for every chart
- [ ] Set Seaborn style: `sns.set_style("whitegrid")`
- [ ] Check all PNGs in `outputs/` folder - View each one

### Evening Block (16:30 - 21:00)
- [ ] Write 1 insight per chart in markdown under chart (e.g., "Females survived 74% more")
- [ ] Push all 10 PNGs + notebook to GitHub
- [ ] Revise: Which chart for which question (memorize)

**GitHub Push Today:** `04_visuals.ipynb` + 10 chart PNGs

---

## DAY 19 (Friday) - INSIGHTS + PYTHON SCRIPT VERSION
**Goal:** Turn visuals into business story + create script that runs with one command.

### Morning Block (05:00 - 10:00)
**05:00-07:00 - Theory: How to write insights**
- [ ] Framework: Observation → Numbers → Business Meaning → Action
- [ ] Bad: "Chart shows survival" | Good: "First class 62% survived vs 3rd class 24% - price/income matters"
- [ ] Learn to quantify: Always add % and count in insight

**07:30-10:00 - Write 5 Final Insights in Notebook**
- [ ] Insight 1 - Gender: Female 74% survival
- [ ] Insight 2 - Class: First class 1.6x more survival
- [ ] Insight 3 - Age: Children under 10 survived more
- [ ] Insight 4 - Fare: Higher fare = higher survival (correlation 0.26)
- [ ] Insight 5 - Family: Solo travelers survived less than with family
- [ ] Create `notebooks/final_report.ipynb` - Combine best cells into one final notebook

### Afternoon Block (10:30 - 16:00)
**10:30-12:30 - Convert to Python Script**
- [ ] Create `src/analyzer.py`:
```python
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('data/cleaned_titanic.csv')
print(df.head())
print(df['Survived'].mean())
# Add 3 chart codes
```
- [ ] Test: `python src/analyzer.py` → Should print output without error
- [ ] Add `if __name__ == "__main__":` - Professional script structure
- [ ] Add comments per function

**14:00-16:00 - Polish Final Notebook**
- [ ] Add Table of Contents markdown at top
- [ ] Add Introduction: "This notebook analyzes Titanic survival..."
- [ ] Add Conclusion section
- [ ] Kernel → Restart & Run All → Ensure no errors
- [ ] Save final: `notebooks/Titanic_EDA_Final.ipynb`

### Evening Block (16:30 - 21:00)
- [ ] Create README draft (see Day 21 for final)
- [ ] Push `final_report.ipynb` + `analyzer.py` to GitHub
- [ ] Revise: Explain any chart to friend in 30 seconds each (practice aloud)

**GitHub Push Today:** Final notebook + Python script

---

## DAY 20 (Saturday) - REVISION + MINI CHALLENGE
**Goal:** Master basics without notebook help. Build speed.

### Morning Block (05:00 - 10:00)
**05:00-07:00 - No-Video Revision**
- [ ] Close all guides. Open empty Jupyter.
- [ ] Without seeing tutorial, load CSV, clean missing, make 3 charts in 1 hour (speed test)

**07:30-10:00 - Practice Set**
- [ ] 20 Questions: Write answers from memory:
  - `df.shape`, `df.info()`, `df.describe()`, `df.isnull().sum()`, `df.fillna()`, `df.drop_duplicates()`, `df.groupby()`, `df.corr()`, `sns.heatmap()`, `plt.savefig()`
- [ ] 5 Groupby Practice:
```python
df.groupby('Sex')['Survived'].mean()
df.groupby('Pclass')['Fare'].mean()
```

### Afternoon Block (10:30 - 16:00)
**10:30-12:30 - New Dataset Challenge**
- [ ] Download second CSV (Sales / Iris)
- [ ] In new notebook, do full flow in 2 hours: Load → Clean → 3 Charts → 2 Insights
- [ ] Time yourself - Aim to finish in 90 min by end of day

**14:00-16:00 - NumPy Revision**
- [ ] Practice: Create array, slicing, mean, reshape
- [ ] Connect: "NumPy is backend of Pandas - every Pandas column is NumPy array"

### Evening Block (16:30 - 21:00)
- [ ] Create cheat sheet `cheatsheet_pandas.md` - All functions with example
- [ ] Push cheat sheet to GitHub
- [ ] 20:00-21:00: Light revision - SQL preview (SELECT, WHERE) for next week

**GitHub Push Today:** Cheat sheet + second dataset notebook

---

## DAY 21 (Sunday) - PROJECT COMPLETION + PORTFOLIO
**Goal:** Make project look like professional portfolio. Ready for interview.

### Morning Block (05:00 - 10:00)
**05:00-07:00 - Final README.md (Write completely)**
- [ ] Use this template:
```markdown
# Titanic Data Analyzer
## Overview - 2 lines what project does
## Dataset - Kaggle link
## Tech Stack - Python, Pandas, Seaborn
## Project Structure - show folder tree
## Key Insights - List 5 insights with numbers
## How to Run - Step 1 conda env, Step 2 notebook path
## Outputs - Embed 3 best chart images: ![chart](../outputs/01...)
## Results - Survival rate table
## Future Scope - What you will add next in Project 4
```
- [ ] Add 3 screenshots inline - Use `![Survival](outputs/01_survival_pie.png)`

**07:30-10:00 - GitHub Polish**
- [ ] Add repo topics: python, pandas, eda, data-analysis
- [ ] Add About description on GitHub right panel
- [ ] Pin this repo to your GitHub profile
- [ ] Check repo on mobile - Looks good?

### Afternoon Block (10:30 - 16:00)
**10:30-12:30 - Final Checks**
- [ ] Restart & Run All on final notebook → 0 errors
- [ ] Check all files: data, notebooks, outputs, src, README
- [ ] Add `.gitignore` file - Ignore `.ipynb_checkpoints`
- [ ] Create `requirements.txt`: `pip freeze > requirements.txt`

**14:00-16:00 - Prepare for Next Week**
- [ ] Light preview Statistics: What is p-value? (just intro, no deep)
- [ ] Update tracker: Mark Week 3 complete
- [ ] Plan Week 4: List Excel files to download

### Evening Block (16:30 - 21:00)
- [ ] Final GitHub push + Tag release v1.0
- [ ] 19:00-20:00: Write LinkedIn post: "Completed Project 1 - Data Analyzer with 10 charts and insights. Repo link inside."
- [ ] 20:00-21:00: Celebrate + Rest - No new study

**GitHub Push Today:** Final README + requirements.txt + .gitignore

---

## FINAL CHECKLIST - Is Project 1 Done?

- [ ] 10+ Charts saved as PNG in `outputs/`
- [ ] Cleaned CSV exists (0 missing values)
- [ ] Final Notebook runs from top to bottom without error
- [ ] Python script `analyzer.py` runs with one command
- [ ] README with insights + screenshots + runnable steps
- [ ] GitHub repo public with 5+ commits
- [ ] Can explain every chart in interview without looking

**If missing any → Fix on Day 21 afternoon before moving to Week 4.**

---

## Daily 10-Hour Slot Recap (Memorize)

| Slot | Time | Work |
|------|------|------|
| Learning | 05:00-07:00 | Theory Video |
| Coding | 07:30-10:00 | Practice Code |
| Learning 2 | 10:30-12:30 | Next Topic |
| Project | 14:00-16:00 | Build Project |
| Extra | 16:30-18:00 | Project Continue |
| Revision | 19:00-21:00 | Notes + GitHub |

**Time Taken: 10.5 hours/day × 7 = 73.5 hours week.**
