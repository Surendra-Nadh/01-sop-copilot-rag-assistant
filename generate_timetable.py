from fpdf import FPDF
import os

class DataScientistTimetable(FPDF):
    def __init__(self):
        super().__init__()
        self.set_auto_page_break(auto=True, margin=20)
        self.primary_color = (41, 128, 185)    # Blue
        self.secondary_color = (46, 204, 113)  # Green
        self.accent_color = (231, 76, 60)      # Red
        self.dark_color = (44, 62, 80)         # Dark blue-gray
        self.light_bg = (236, 240, 241)        # Light gray

    def header(self):
        if self.page_no() > 1:
            self.set_font('Helvetica', 'I', 8)
            self.set_text_color(*self.dark_color)
            self.cell(0, 8, 'Data Scientist Learning Timetable | 8-Week Intensive Program', align='C')
            self.ln(12)

    def footer(self):
        self.set_y(-15)
        self.set_font('Helvetica', 'I', 8)
        self.set_text_color(128, 128, 128)
        self.cell(0, 10, f'Page {self.page_no()}/{{nb}}', align='C')

    def section_title(self, title, color=None):
        if color is None:
            color = self.primary_color
        self.set_fill_color(*color)
        self.set_text_color(255, 255, 255)
        self.set_font('Helvetica', 'B', 14)
        self.cell(0, 12, f'  {title}', fill=True, new_x='LMARGIN', new_y='NEXT')
        self.ln(4)

    def sub_section_title(self, title):
        self.set_text_color(*self.dark_color)
        self.set_font('Helvetica', 'B', 11)
        self.cell(0, 8, title, new_x='LMARGIN', new_y='NEXT')
        self.ln(2)

    def body_text(self, text):
        self.set_text_color(*self.dark_color)
        self.set_font('Helvetica', '', 10)
        self.multi_cell(0, 6, text)
        self.ln(2)

    def add_daily_schedule(self, day, time_slots):
        """Add a day's schedule with time slots"""
        # Day header
        self.set_fill_color(*self.primary_color)
        self.set_text_color(255, 255, 255)
        self.set_font('Helvetica', 'B', 10)
        self.cell(0, 8, f'  {day}', fill=True, new_x='LMARGIN', new_y='NEXT')
        self.ln(1)

        # Time slots
        self.set_font('Helvetica', '', 9)
        for time_slot, activity in time_slots:
            self.set_text_color(*self.dark_color)
            x_start = self.get_x()
            y_start = self.get_y()
            self.cell(35, 6, time_slot, align='L')
            self.set_xy(x_start + 35, y_start)
            self.set_text_color(80, 80, 80)
            self.multi_cell(155, 6, activity)
        self.ln(3)

    def add_milestone(self, text):
        self.set_fill_color(*self.secondary_color)
        self.set_text_color(255, 255, 255)
        self.set_font('Helvetica', 'B', 9)
        self.cell(0, 7, f'  MILESTONE: {text}', fill=True, new_x='LMARGIN', new_y='NEXT')
        self.ln(3)


def create_timetable():
    pdf = DataScientistTimetable()
    pdf.alias_nb_pages()

    # ========== COVER PAGE ==========
    pdf.add_page()
    pdf.ln(30)

    # Title box
    pdf.set_fill_color(*pdf.primary_color)
    pdf.rect(10, 50, 190, 50, 'F')
    pdf.set_xy(10, 55)
    pdf.set_text_color(255, 255, 255)
    pdf.set_font('Helvetica', 'B', 24)
    pdf.cell(190, 15, 'DATA SCIENTIST', align='C')
    pdf.set_xy(10, 72)
    pdf.set_font('Helvetica', 'B', 20)
    pdf.cell(190, 12, 'Learning Timetable', align='C')
    pdf.set_xy(10, 88)
    pdf.set_font('Helvetica', '', 12)
    pdf.cell(190, 10, '8-Week Intensive Program', align='C')

    pdf.ln(70)

    # Info box
    pdf.set_fill_color(*pdf.light_bg)
    pdf.rect(30, 110, 150, 60, 'F')
    pdf.set_xy(30, 115)
    pdf.set_text_color(*pdf.dark_color)
    pdf.set_font('Helvetica', 'B', 11)
    pdf.cell(150, 8, 'Program Overview', align='C')
    pdf.set_x(30)
    pdf.set_font('Helvetica', '', 10)
    pdf.ln(10)
    pdf.cell(150, 7, 'Duration: 8 Weeks (2 Months)', align='C')
    pdf.ln(8)
    pdf.cell(150, 7, 'Daily Hours: 9:00 AM - 5:00 PM (8 Hours)', align='C')
    pdf.ln(8)
    pdf.cell(150, 7, 'Days: Monday - Saturday', align='C')
    pdf.ln(8)
    pdf.cell(150, 7, 'Sunday: Review & Practice', align='C')

    pdf.ln(80)

    # Skills covered
    pdf.set_text_color(*pdf.dark_color)
    pdf.set_font('Helvetica', 'B', 11)
    pdf.cell(0, 10, 'Skills You Will Learn:', new_x='LMARGIN', new_y='NEXT')
    pdf.ln(2)
    pdf.set_font('Helvetica', '', 10)
    skills = [
        '  - Python Programming (Beginner to Intermediate)',
        '  - SQL & Database Management',
        '  - Pandas & NumPy for Data Manipulation',
        '  - Data Cleaning & Exploratory Data Analysis',
        '  - Machine Learning Fundamentals',
        '  - Model Evaluation & Feature Engineering',
        '  - End-to-End ML Project Development'
    ]
    for skill in skills:
        pdf.cell(0, 7, skill, new_x='LMARGIN', new_y='NEXT')

    # ========== PAGE 2: WEEKLY OVERVIEW ==========
    pdf.add_page()
    pdf.section_title('8-Week Program Overview')

    overview_data = [
        ('Phase 1', 'Weeks 1-2', 'Python Fundamentals', 'Variables, data types, control flow, functions, OOP basics, file I/O, error handling'),
        ('Phase 2', 'Weeks 3-4', 'SQL & Databases', 'SELECT, WHERE, JOINs, GROUP BY, subqueries, window functions, Python + SQL integration'),
        ('Phase 3', 'Weeks 5-6', 'Pandas & NumPy', 'Arrays, dataframes, indexing, filtering, merging, grouping, missing data, EDA'),
        ('Phase 4', 'Weeks 7-8', 'Machine Learning', 'Regression, classification, clustering, model evaluation, feature engineering, final project'),
    ]

    pdf.set_font('Helvetica', 'B', 9)
    pdf.set_fill_color(*pdf.primary_color)
    pdf.set_text_color(255, 255, 255)
    col_widths = [25, 20, 45, 100]
    headers = ['Phase', 'Weeks', 'Focus Area', 'Key Topics']
    for i, h in enumerate(headers):
        pdf.cell(col_widths[i], 8, h, border=1, fill=True, align='C')
    pdf.ln()

    pdf.set_font('Helvetica', '', 9)
    pdf.set_text_color(*pdf.dark_color)
    for idx, (phase, weeks, focus, topics) in enumerate(overview_data):
        if idx % 2 == 0:
            pdf.set_fill_color(240, 248, 255)
        else:
            pdf.set_fill_color(255, 255, 255)
        pdf.cell(col_widths[0], 8, phase, border=1, fill=True, align='C')
        pdf.cell(col_widths[1], 8, weeks, border=1, fill=True, align='C')
        pdf.cell(col_widths[2], 8, focus, border=1, fill=True, align='C')
        pdf.cell(col_widths[3], 8, topics, border=1, fill=True)
        pdf.ln()

    pdf.ln(8)
    pdf.add_milestone('Complete all 4 phases to become job-ready for junior data scientist roles')

    # ========== PHASE 1: PYTHON ==========
    pdf.add_page()
    pdf.section_title('Phase 1: Python Fundamentals (Weeks 1-2)', pdf.primary_color)

    pdf.sub_section_title('Week 1: Python Basics')
    week1 = [
        ('Monday', [
            ('9:00 AM - 10:30 AM', 'Variables, Data Types (int, float, str, bool)'),
            ('10:30 AM - 10:45 AM', 'Break'),
            ('10:45 AM - 12:30 PM', 'Strings - slicing, methods, formatting'),
            ('12:30 PM - 1:30 PM', 'Lunch Break'),
            ('1:30 PM - 3:00 PM', 'Lists, Tuples, Sets'),
            ('3:00 PM - 3:15 PM', 'Break'),
            ('3:15 PM - 5:00 PM', 'Practice: 15 coding problems on data types'),
        ]),
        ('Tuesday', [
            ('9:00 AM - 10:30 AM', 'Dictionaries - creation, access, methods'),
            ('10:30 AM - 10:45 AM', 'Break'),
            ('10:45 AM - 12:30 PM', 'Conditionals (if/elif/else), comparison operators'),
            ('12:30 PM - 1:30 PM', 'Lunch Break'),
            ('1:30 PM - 3:00 PM', 'Logical operators (and, or, not)'),
            ('3:00 PM - 3:15 PM', 'Break'),
            ('3:15 PM - 5:00 PM', 'Practice: 15 conditional problems'),
        ]),
        ('Wednesday', [
            ('9:00 AM - 10:30 AM', 'Loops - for loops, range(), enumerate()'),
            ('10:30 AM - 10:45 AM', 'Break'),
            ('10:45 AM - 12:30 PM', 'While loops, break, continue'),
            ('12:30 PM - 1:30 PM', 'Lunch Break'),
            ('1:30 PM - 3:00 PM', 'Nested loops, loop patterns'),
            ('3:00 PM - 3:15 PM', 'Break'),
            ('3:15 PM - 5:00 PM', 'Practice: 20 loop-based problems'),
        ]),
        ('Thursday', [
            ('9:00 AM - 10:30 AM', 'Functions - definition, parameters, return values'),
            ('10:30 AM - 10:45 AM', 'Break'),
            ('10:45 AM - 12:30 PM', 'Scope, *args, **kwargs, lambda functions'),
            ('12:30 PM - 1:30 PM', 'Lunch Break'),
            ('1:30 PM - 3:00 PM', 'List/Dict comprehensions'),
            ('3:00 PM - 3:15 PM', 'Break'),
            ('3:15 PM - 5:00 PM', 'Practice: Write 10 functions from scratch'),
        ]),
        ('Friday', [
            ('9:00 AM - 10:30 AM', 'File I/O - reading/writing text files'),
            ('10:30 AM - 10:45 AM', 'Break'),
            ('10:45 AM - 12:30 PM', 'CSV/JSON handling, error handling (try/except)'),
            ('12:30 PM - 1:30 PM', 'Lunch Break'),
            ('1:30 PM - 3:00 PM', 'Modules, pip, importing libraries'),
            ('3:00 PM - 3:15 PM', 'Break'),
            ('3:15 PM - 5:00 PM', 'Practice: File processing exercises'),
        ]),
        ('Saturday', [
            ('9:00 AM - 10:30 AM', 'Review: All Week 1 concepts'),
            ('10:30 AM - 10:45 AM', 'Break'),
            ('10:45 AM - 12:30 PM', 'Practice: Mixed problems (30 questions)'),
            ('12:30 PM - 1:30 PM', 'Lunch Break'),
            ('1:30 PM - 3:00 PM', 'Mini-project: Build a CLI app (to-do list/quiz)'),
            ('3:00 PM - 3:15 PM', 'Break'),
            ('3:15 PM - 5:00 PM', 'Continue mini-project, debug and refine'),
        ]),
        ('Sunday', [
            ('9:00 AM - 12:00 PM', 'Review weak areas, redo difficult problems'),
            ('12:00 PM - 1:00 PM', 'Lunch Break'),
            ('1:00 PM - 3:00 PM', 'Watch Python tutorial videos for reinforcement'),
            ('3:00 PM - 5:00 PM', 'Rest and recharge for Week 2'),
        ]),
    ]

    for day, slots in week1:
        pdf.add_daily_schedule(day, slots)

    pdf.add_page()
    pdf.sub_section_title('Week 2: Intermediate Python')
    week2 = [
        ('Monday', [
            ('9:00 AM - 10:30 AM', 'OOP - Classes and Objects'),
            ('10:30 AM - 10:45 AM', 'Break'),
            ('10:45 AM - 12:30 PM', 'Inheritance, Polymorphism, Encapsulation'),
            ('12:30 PM - 1:30 PM', 'Lunch Break'),
            ('1:30 PM - 3:00 PM', 'Magic methods, property decorators'),
            ('3:00 PM - 3:15 PM', 'Break'),
            ('3:15 PM - 5:00 PM', 'Practice: Build 3 class-based programs'),
        ]),
        ('Tuesday', [
            ('9:00 AM - 10:30 AM', 'Regular Expressions (re module)'),
            ('10:30 AM - 10:45 AM', 'Break'),
            ('10:45 AM - 12:30 PM', 'Pattern matching, search, sub, split'),
            ('12:30 PM - 1:30 PM', 'Lunch Break'),
            ('1:30 PM - 3:00 PM', 'Practice: Text parsing with regex'),
            ('3:00 PM - 3:15 PM', 'Break'),
            ('3:15 PM - 5:00 PM', 'Practice: 15 regex problems'),
        ]),
        ('Wednesday', [
            ('9:00 AM - 10:30 AM', 'Working with APIs (requests library)'),
            ('10:30 AM - 10:45 AM', 'Break'),
            ('10:45 AM - 12:30 PM', 'HTTP methods, JSON parsing'),
            ('12:30 PM - 1:30 PM', 'Lunch Break'),
            ('1:30 PM - 3:00 PM', 'Fetch data from a public API'),
            ('3:00 PM - 3:15 PM', 'Break'),
            ('3:15 PM - 5:00 PM', 'Mini-project: Weather app using API'),
        ]),
        ('Thursday', [
            ('9:00 AM - 10:30 AM', 'Virtual environments, Jupyter Notebook'),
            ('10:30 AM - 10:45 AM', 'Break'),
            ('10:45 AM - 12:30 PM', 'NumPy preview: arrays and operations'),
            ('12:30 PM - 1:30 PM', 'Lunch Break'),
            ('1:30 PM - 3:00 PM', 'Practice: NumPy array exercises'),
            ('3:00 PM - 3:15 PM', 'Break'),
            ('3:15 PM - 5:00 PM', 'Practice: 20 NumPy problems'),
        ]),
        ('Friday', [
            ('9:00 AM - 10:30 AM', 'Matplotlib & Seaborn basics'),
            ('10:30 AM - 10:45 AM', 'Break'),
            ('10:45 AM - 12:30 PM', 'Line plots, bar charts, histograms'),
            ('12:30 PM - 1:30 PM', 'Lunch Break'),
            ('1:30 PM - 3:00 PM', 'Scatter plots, heatmaps'),
            ('3:00 PM - 3:15 PM', 'Break'),
            ('3:15 PM - 5:00 PM', 'Practice: Create 10 different visualizations'),
        ]),
        ('Saturday', [
            ('9:00 AM - 10:30 AM', 'Review: All Week 2 concepts'),
            ('10:30 AM - 10:45 AM', 'Break'),
            ('10:45 AM - 12:30 PM', 'Practice: Mixed problems (30 questions)'),
            ('12:30 PM - 1:30 PM', 'Lunch Break'),
            ('1:30 PM - 3:00 PM', 'Mini-project: Data visualization dashboard'),
            ('3:00 PM - 3:15 PM', 'Break'),
            ('3:15 PM - 5:00 PM', 'Continue project, document your code'),
        ]),
        ('Sunday', [
            ('9:00 AM - 12:00 PM', 'Review weak areas, redo difficult problems'),
            ('12:00 PM - 1:00 PM', 'Lunch Break'),
            ('1:00 PM - 3:00 PM', 'Watch Python/OOP tutorial videos'),
            ('3:00 PM - 5:00 PM', 'Rest and recharge for Phase 2'),
        ]),
    ]

    for day, slots in week2:
        pdf.add_daily_schedule(day, slots)

    pdf.add_milestone('Comfortable writing 100+ line Python programs with OOP')

    # ========== PHASE 2: SQL ==========
    pdf.add_page()
    pdf.section_title('Phase 2: SQL & Databases (Weeks 3-4)', pdf.secondary_color)

    pdf.sub_section_title('Week 3: SQL Fundamentals')
    week3 = [
        ('Monday', [
            ('9:00 AM - 10:30 AM', 'Introduction to Databases, Relational vs NoSQL'),
            ('10:30 AM - 10:45 AM', 'Break'),
            ('10:45 AM - 12:30 PM', 'Tables, rows, columns, data types'),
            ('12:30 PM - 1:30 PM', 'Lunch Break'),
            ('1:30 PM - 3:00 PM', 'SELECT, FROM, WHERE clauses'),
            ('3:00 PM - 3:15 PM', 'Break'),
            ('3:15 PM - 5:00 PM', 'Practice: 20 basic SELECT queries'),
        ]),
        ('Tuesday', [
            ('9:00 AM - 10:30 AM', 'ORDER BY, LIMIT, DISTINCT'),
            ('10:30 AM - 10:45 AM', 'Break'),
            ('10:45 AM - 12:30 PM', 'AND, OR, NOT operators'),
            ('12:30 PM - 1:30 PM', 'Lunch Break'),
            ('1:30 PM - 3:00 PM', 'BETWEEN, LIKE, IN operators'),
            ('3:00 PM - 3:15 PM', 'Break'),
            ('3:15 PM - 5:00 PM', 'Practice: 20 filtering queries'),
        ]),
        ('Wednesday', [
            ('9:00 AM - 10:30 AM', 'Aggregate functions: COUNT, SUM, AVG, MIN, MAX'),
            ('10:30 AM - 10:45 AM', 'Break'),
            ('10:45 AM - 12:30 PM', 'GROUP BY clause'),
            ('12:30 PM - 1:30 PM', 'Lunch Break'),
            ('1:30 PM - 3:00 PM', 'HAVING clause'),
            ('3:00 PM - 3:15 PM', 'Break'),
            ('3:15 PM - 5:00 PM', 'Practice: 20 aggregation queries'),
        ]),
        ('Thursday', [
            ('9:00 AM - 10:30 AM', 'JOINs - INNER JOIN'),
            ('10:30 AM - 10:45 AM', 'Break'),
            ('10:45 AM - 12:30 PM', 'LEFT JOIN, RIGHT JOIN'),
            ('12:30 PM - 1:30 PM', 'Lunch Break'),
            ('1:30 PM - 3:00 PM', 'FULL OUTER JOIN, CROSS JOIN'),
            ('3:00 PM - 3:15 PM', 'Break'),
            ('3:15 PM - 5:00 PM', 'Practice: 15 JOIN queries'),
        ]),
        ('Friday', [
            ('9:00 AM - 10:30 AM', 'Subqueries - WHERE clause subqueries'),
            ('10:30 AM - 10:45 AM', 'Break'),
            ('10:45 AM - 12:30 PM', 'Subqueries - FROM clause (derived tables)'),
            ('12:30 PM - 1:30 PM', 'Lunch Break'),
            ('1:30 PM - 3:00 PM', 'Common Table Expressions (CTEs)'),
            ('3:00 PM - 3:15 PM', 'Break'),
            ('3:15 PM - 5:00 PM', 'Practice: 15 subquery problems'),
        ]),
        ('Saturday', [
            ('9:00 AM - 10:30 AM', 'Window functions: ROW_NUMBER, RANK, DENSE_RANK'),
            ('10:30 AM - 10:45 AM', 'Break'),
            ('10:45 AM - 12:30 PM', 'PARTITION BY, running totals'),
            ('12:30 PM - 1:30 PM', 'Lunch Break'),
            ('1:30 PM - 3:00 PM', 'LAG, LEAD functions'),
            ('3:00 PM - 3:15 PM', 'Break'),
            ('3:15 PM - 5:00 PM', 'Practice: 15 window function problems'),
        ]),
        ('Sunday', [
            ('9:00 AM - 12:00 PM', 'Review all SQL concepts, redo weak areas'),
            ('12:00 PM - 1:00 PM', 'Lunch Break'),
            ('1:00 PM - 3:00 PM', 'SQL challenge: Solve 20 mixed problems'),
            ('3:00 PM - 5:00 PM', 'Rest and recharge'),
        ]),
    ]

    for day, slots in week3:
        pdf.add_daily_schedule(day, slots)

    pdf.add_page()
    pdf.sub_section_title('Week 4: Advanced SQL + Python Integration')
    week4 = [
        ('Monday', [
            ('9:00 AM - 10:30 AM', 'Indexing and query optimization'),
            ('10:30 AM - 10:45 AM', 'Break'),
            ('10:45 AM - 12:30 PM', 'EXPLAIN ANALYZE, query tuning'),
            ('12:30 PM - 1:30 PM', 'Lunch Break'),
            ('1:30 PM - 3:00 PM', 'Database design: normalization, keys'),
            ('3:00 PM - 3:15 PM', 'Break'),
            ('3:15 PM - 5:00 PM', 'Practice: Optimize 10 slow queries'),
        ]),
        ('Tuesday', [
            ('9:00 AM - 10:30 AM', 'Python + SQL: sqlite3 library'),
            ('10:30 AM - 10:45 AM', 'Break'),
            ('10:45 AM - 12:30 PM', 'Connect, create tables, insert data'),
            ('12:30 PM - 1:30 PM', 'Lunch Break'),
            ('1:30 PM - 3:00 PM', 'Execute queries from Python'),
            ('3:00 PM - 3:15 PM', 'Break'),
            ('3:15 PM - 5:00 PM', 'Practice: Build a Python-SQL CRUD app'),
        ]),
        ('Wednesday', [
            ('9:00 AM - 10:30 AM', 'SQLAlchemy ORM basics'),
            ('10:30 AM - 10:45 AM', 'Break'),
            ('10:45 AM - 12:30 PM', 'Define models, create sessions'),
            ('12:30 PM - 1:30 PM', 'Lunch Break'),
            ('1:30 PM - 3:00 PM', 'Query with ORM, relationships'),
            ('3:00 PM - 3:15 PM', 'Break'),
            ('3:15 PM - 5:00 PM', 'Practice: Build ORM-based app'),
        ]),
        ('Thursday', [
            ('9:00 AM - 10:30 AM', 'Advanced: Transactions, constraints'),
            ('10:30 AM - 10:45 AM', 'Break'),
            ('10:45 AM - 12:30 PM', 'Stored procedures, triggers (overview)'),
            ('12:30 PM - 1:30 PM', 'Lunch Break'),
            ('1:30 PM - 3:00 PM', 'Practice: Complex SQL scenarios'),
            ('3:00 PM - 3:15 PM', 'Break'),
            ('3:15 PM - 5:00 PM', 'Practice: 20 advanced SQL problems'),
        ]),
        ('Friday', [
            ('9:00 AM - 10:30 AM', 'Review: All SQL concepts'),
            ('10:30 AM - 10:45 AM', 'Break'),
            ('10:45 AM - 12:30 PM', 'Practice: SQL assessment (30 questions)'),
            ('12:30 PM - 1:30 PM', 'Lunch Break'),
            ('1:30 PM - 3:00 PM', 'Mini-project: Analyze a real dataset with SQL'),
            ('3:00 PM - 3:15 PM', 'Break'),
            ('3:15 PM - 5:00 PM', 'Continue SQL project'),
        ]),
        ('Saturday', [
            ('9:00 AM - 10:30 AM', 'Python + SQL integration review'),
            ('10:30 AM - 10:45 AM', 'Break'),
            ('10:45 AM - 12:30 PM', 'Mini-project: Full-stack data app'),
            ('12:30 PM - 1:30 PM', 'Lunch Break'),
            ('1:30 PM - 3:00 PM', 'Continue project: data pipeline'),
            ('3:00 PM - 3:15 PM', 'Break'),
            ('3:15 PM - 5:00 PM', 'Complete and document project'),
        ]),
        ('Sunday', [
            ('9:00 AM - 12:00 PM', 'Review weak areas, redo difficult problems'),
            ('12:00 PM - 1:00 PM', 'Lunch Break'),
            ('1:00 PM - 3:00 PM', 'Watch SQL tutorial videos'),
            ('3:00 PM - 5:00 PM', 'Rest and recharge for Phase 3'),
        ]),
    ]

    for day, slots in week4:
        pdf.add_daily_schedule(day, slots)

    pdf.add_milestone('Can write complex SQL queries and connect Python to databases')

    # ========== PHASE 3: PANDAS & NUMPY ==========
    pdf.add_page()
    pdf.section_title('Phase 3: Pandas & NumPy (Weeks 5-6)', pdf.accent_color)

    pdf.sub_section_title('Week 5: NumPy')
    week5 = [
        ('Monday', [
            ('9:00 AM - 10:30 AM', 'NumPy arrays vs Python lists'),
            ('10:30 AM - 10:45 AM', 'Break'),
            ('10:45 AM - 12:30 PM', 'Creating arrays: array(), zeros(), ones(), arange()'),
            ('12:30 PM - 1:30 PM', 'Lunch Break'),
            ('1:30 PM - 3:00 PM', 'Array indexing and slicing'),
            ('3:00 PM - 3:15 PM', 'Break'),
            ('3:15 PM - 5:00 PM', 'Practice: 20 array creation problems'),
        ]),
        ('Tuesday', [
            ('9:00 AM - 10:30 AM', 'Array operations: +, -, *, /, dot product'),
            ('10:30 AM - 10:45 AM', 'Break'),
            ('10:45 AM - 12:30 PM', 'Broadcasting and universal functions (ufuncs)'),
            ('12:30 PM - 1:30 PM', 'Lunch Break'),
            ('1:30 PM - 3:00 PM', 'Mathematical functions: sum, mean, std, var'),
            ('3:00 PM - 3:15 PM', 'Break'),
            ('3:15 PM - 5:00 PM', 'Practice: 20 operation problems'),
        ]),
        ('Wednesday', [
            ('9:00 AM - 10:30 AM', 'Array reshaping: reshape(), ravel(), flatten()'),
            ('10:30 AM - 10:45 AM', 'Break'),
            ('10:45 AM - 12:30 PM', 'Stacking: vstack(), hstack(), concatenate()'),
            ('12:30 PM - 1:30 PM', 'Lunch Break'),
            ('1:30 PM - 3:00 PM', 'Splitting: vsplit(), hsplit(), split()'),
            ('3:00 PM - 3:15 PM', 'Break'),
            ('3:15 PM - 5:00 PM', 'Practice: 15 reshaping problems'),
        ]),
        ('Thursday', [
            ('9:00 AM - 10:30 AM', 'Random number generation'),
            ('10:30 AM - 10:45 AM', 'Break'),
            ('10:45 AM - 12:30 PM', 'Random distributions: normal, uniform, binomial'),
            ('12:30 PM - 1:30 PM', 'Lunch Break'),
            ('1:30 PM - 3:00 PM', 'Seeding, random sampling'),
            ('3:00 PM - 3:15 PM', 'Break'),
            ('3:15 PM - 5:00 PM', 'Practice: 15 random generation problems'),
        ]),
        ('Friday', [
            ('9:00 AM - 10:30 AM', 'Linear algebra: matrix operations'),
            ('10:30 AM - 10:45 AM', 'Break'),
            ('10:45 AM - 12:30 PM', 'Determinants, inverses, eigenvalues'),
            ('12:30 PM - 1:30 PM', 'Lunch Break'),
            ('1:30 PM - 3:00 PM', 'Solving linear systems'),
            ('3:00 PM - 3:15 PM', 'Break'),
            ('3:15 PM - 5:00 PM', 'Practice: 15 linear algebra problems'),
        ]),
        ('Saturday', [
            ('9:00 AM - 10:30 AM', 'Review: All NumPy concepts'),
            ('10:30 AM - 10:45 AM', 'Break'),
            ('10:45 AM - 12:30 PM', 'Practice: Mixed NumPy problems (30 questions)'),
            ('12:30 PM - 1:30 PM', 'Lunch Break'),
            ('1:30 PM - 3:00 PM', 'Mini-project: Image processing with NumPy'),
            ('3:00 PM - 3:15 PM', 'Break'),
            ('3:15 PM - 5:00 PM', 'Continue project, document code'),
        ]),
        ('Sunday', [
            ('9:00 AM - 12:00 PM', 'Review weak areas, redo difficult problems'),
            ('12:00 PM - 1:00 PM', 'Lunch Break'),
            ('1:00 PM - 3:00 PM', 'Watch NumPy tutorial videos'),
            ('3:00 PM - 5:00 PM', 'Rest and recharge'),
        ]),
    ]

    for day, slots in week5:
        pdf.add_daily_schedule(day, slots)

    pdf.add_page()
    pdf.sub_section_title('Week 6: Pandas')
    week6 = [
        ('Monday', [
            ('9:00 AM - 10:30 AM', 'Series and DataFrames, head(), info(), describe()'),
            ('10:30 AM - 10:45 AM', 'Break'),
            ('10:45 AM - 12:30 PM', 'Creating DataFrames from dicts, lists, files'),
            ('12:30 PM - 1:30 PM', 'Lunch Break'),
            ('1:30 PM - 3:00 PM', 'Selecting rows and columns (loc, iloc)'),
            ('3:00 PM - 3:15 PM', 'Break'),
            ('3:15 PM - 5:00 PM', 'Practice: 20 selection problems'),
        ]),
        ('Tuesday', [
            ('9:00 AM - 10:30 AM', 'Filtering with boolean indexing'),
            ('10:30 AM - 10:45 AM', 'Break'),
            ('10:45 AM - 12:30 PM', 'Multiple conditions, isin(), between()'),
            ('12:30 PM - 1:30 PM', 'Lunch Break'),
            ('1:30 PM - 3:00 PM', 'Handling missing data: fillna(), dropna()'),
            ('3:00 PM - 3:15 PM', 'Break'),
            ('3:15 PM - 5:00 PM', 'Practice: 20 filtering problems'),
        ]),
        ('Wednesday', [
            ('9:00 AM - 10:30 AM', 'groupby() and aggregation'),
            ('10:30 AM - 10:45 AM', 'Break'),
            ('10:45 AM - 12:30 PM', 'pivot_table(), crosstab()'),
            ('12:30 PM - 1:30 PM', 'Lunch Break'),
            ('1:30 PM - 3:00 PM', 'Merging and joining DataFrames'),
            ('3:00 PM - 3:15 PM', 'Break'),
            ('3:15 PM - 5:00 PM', 'Practice: 20 groupby problems'),
        ]),
        ('Thursday', [
            ('9:00 AM - 10:30 AM', 'Working with dates and times'),
            ('10:30 AM - 10:45 AM', 'Break'),
            ('10:45 AM - 12:30 PM', 'DatetimeIndex, resampling, time zones'),
            ('12:30 PM - 1:30 PM', 'Lunch Break'),
            ('1:30 PM - 3:00 PM', 'apply(), map(), applymap()'),
            ('3:00 PM - 3:15 PM', 'Break'),
            ('3:15 PM - 5:00 PM', 'Practice: 20 datetime problems'),
        ]),
        ('Friday', [
            ('9:00 AM - 10:30 AM', 'Reading/writing CSV, Excel, JSON'),
            ('10:30 AM - 10:45 AM', 'Break'),
            ('10:45 AM - 12:30 PM', 'Data cleaning techniques'),
            ('12:30 PM - 1:30 PM', 'Lunch Break'),
            ('1:30 PM - 3:00 PM', 'String operations in Pandas'),
            ('3:00 PM - 3:15 PM', 'Break'),
            ('3:15 PM - 5:00 PM', 'Practice: 20 data cleaning problems'),
        ]),
        ('Saturday', [
            ('9:00 AM - 10:30 AM', 'Review: All Pandas concepts'),
            ('10:30 AM - 10:45 AM', 'Break'),
            ('10:45 AM - 12:30 PM', 'Practice: Mixed Pandas problems (30 questions)'),
            ('12:30 PM - 1:30 PM', 'Lunch Break'),
            ('1:30 PM - 3:00 PM', 'Mini-project: EDA on a real dataset'),
            ('3:00 PM - 3:15 PM', 'Break'),
            ('3:15 PM - 5:00 PM', 'Continue EDA project, create visualizations'),
        ]),
        ('Sunday', [
            ('9:00 AM - 12:00 PM', 'Review weak areas, redo difficult problems'),
            ('12:00 PM - 1:00 PM', 'Lunch Break'),
            ('1:00 PM - 3:00 PM', 'Watch Pandas tutorial videos'),
            ('3:00 PM - 5:00 PM', 'Rest and recharge for Phase 4'),
        ]),
    ]

    for day, slots in week6:
        pdf.add_daily_schedule(day, slots)

    pdf.add_milestone('Proficient in data wrangling with Pandas and NumPy')

    # ========== PHASE 4: MACHINE LEARNING ==========
    pdf.add_page()
    pdf.section_title('Phase 4: Machine Learning (Weeks 7-8)', (155, 89, 182))

    pdf.sub_section_title('Week 7: ML Foundations')
    week7 = [
        ('Monday', [
            ('9:00 AM - 10:30 AM', 'What is ML? Supervised vs Unsupervised learning'),
            ('10:30 AM - 10:45 AM', 'Break'),
            ('10:45 AM - 12:30 PM', 'Train/test split, overfitting vs underfitting'),
            ('12:30 PM - 1:30 PM', 'Lunch Break'),
            ('1:30 PM - 3:00 PM', 'scikit-learn overview, installation'),
            ('3:00 PM - 3:15 PM', 'Break'),
            ('3:15 PM - 5:00 PM', 'Practice: Load datasets, split data'),
        ]),
        ('Tuesday', [
            ('9:00 AM - 10:30 AM', 'Linear Regression - theory'),
            ('10:30 AM - 10:45 AM', 'Break'),
            ('10:45 AM - 12:30 PM', 'Linear Regression - implementation'),
            ('12:30 PM - 1:30 PM', 'Lunch Break'),
            ('1:30 PM - 3:00 PM', 'Cost function, gradient descent'),
            ('3:00 PM - 3:15 PM', 'Break'),
            ('3:15 PM - 5:00 PM', 'Practice: Build 3 linear regression models'),
        ]),
        ('Wednesday', [
            ('9:00 AM - 10:30 AM', 'Logistic Regression - theory'),
            ('10:30 AM - 10:45 AM', 'Break'),
            ('10:45 AM - 12:30 PM', 'Logistic Regression - implementation'),
            ('12:30 PM - 1:30 PM', 'Lunch Break'),
            ('1:30 PM - 3:00 PM', 'Decision boundaries, sigmoid function'),
            ('3:00 PM - 3:15 PM', 'Break'),
            ('3:15 PM - 5:00 PM', 'Practice: Build 3 logistic regression models'),
        ]),
        ('Thursday', [
            ('9:00 AM - 10:30 AM', 'Evaluation metrics: accuracy, precision, recall, F1'),
            ('10:30 AM - 10:45 AM', 'Break'),
            ('10:45 AM - 12:30 PM', 'Confusion matrix, ROC-AUC'),
            ('12:30 PM - 1:30 PM', 'Lunch Break'),
            ('1:30 PM - 3:00 PM', 'Cross-validation techniques'),
            ('3:00 PM - 3:15 PM', 'Break'),
            ('3:15 PM - 5:00 PM', 'Practice: Evaluate 5 different models'),
        ]),
        ('Friday', [
            ('9:00 AM - 10:30 AM', 'K-Nearest Neighbors (KNN)'),
            ('10:30 AM - 10:45 AM', 'Break'),
            ('10:45 AM - 12:30 PM', 'KNN implementation, choosing K'),
            ('12:30 PM - 1:30 PM', 'Lunch Break'),
            ('1:30 PM - 3:00 PM', 'Decision Trees - theory'),
            ('3:00 PM - 3:15 PM', 'Break'),
            ('3:15 PM - 5:00 PM', 'Practice: Build KNN and Decision Tree models'),
        ]),
        ('Saturday', [
            ('9:00 AM - 10:30 AM', 'Random Forests - theory'),
            ('10:30 AM - 10:45 AM', 'Break'),
            ('10:45 AM - 12:30 PM', 'Random Forests - implementation'),
            ('12:30 PM - 1:30 PM', 'Lunch Break'),
            ('1:30 PM - 3:00 PM', 'Feature importance, ensemble methods'),
            ('3:00 PM - 3:15 PM', 'Break'),
            ('3:15 PM - 5:00 PM', 'Practice: Build Random Forest models'),
        ]),
        ('Sunday', [
            ('9:00 AM - 12:00 PM', 'Review all ML concepts, redo weak areas'),
            ('12:00 PM - 1:00 PM', 'Lunch Break'),
            ('1:00 PM - 3:00 PM', 'Watch ML tutorial videos'),
            ('3:00 PM - 5:00 PM', 'Rest and recharge'),
        ]),
    ]

    for day, slots in week7:
        pdf.add_daily_schedule(day, slots)

    pdf.add_page()
    pdf.sub_section_title('Week 8: Advanced ML + Final Project')
    week8 = [
        ('Monday', [
            ('9:00 AM - 10:30 AM', 'Hyperparameter tuning: GridSearchCV, RandomizedSearchCV'),
            ('10:30 AM - 10:45 AM', 'Break'),
            ('10:45 AM - 12:30 PM', 'Practice: Tune 5 different models'),
            ('12:30 PM - 1:30 PM', 'Lunch Break'),
            ('1:30 PM - 3:00 PM', 'Feature engineering techniques'),
            ('3:00 PM - 3:15 PM', 'Break'),
            ('3:15 PM - 5:00 PM', 'Practice: Feature engineering exercises'),
        ]),
        ('Tuesday', [
            ('9:00 AM - 10:30 AM', 'Feature scaling: StandardScaler, MinMaxScaler'),
            ('10:30 AM - 10:45 AM', 'Break'),
            ('10:45 AM - 12:30 PM', 'Encoding categorical variables'),
            ('12:30 PM - 1:30 PM', 'Lunch Break'),
            ('1:30 PM - 3:00 PM', 'K-Means Clustering - theory'),
            ('3:00 PM - 3:15 PM', 'Break'),
            ('3:15 PM - 5:00 PM', 'Practice: Build clustering models'),
        ]),
        ('Wednesday', [
            ('9:00 AM - 10:30 AM', 'K-Means implementation, elbow method'),
            ('10:30 AM - 10:45 AM', 'Break'),
            ('10:45 AM - 12:30 PM', 'Hierarchical clustering overview'),
            ('12:30 PM - 1:30 PM', 'Lunch Break'),
            ('1:30 PM - 3:00 PM', 'Save/load models: joblib, pickle'),
            ('3:00 PM - 3:15 PM', 'Break'),
            ('3:15 PM - 5:00 PM', 'Practice: Save and deploy models'),
        ]),
        ('Thursday', [
            ('9:00 AM - 10:30 AM', 'Final Project: Choose a dataset (Kaggle)'),
            ('10:30 AM - 10:45 AM', 'Break'),
            ('10:45 AM - 12:30 PM', 'Final Project: Data cleaning and EDA'),
            ('12:30 PM - 1:30 PM', 'Lunch Break'),
            ('1:30 PM - 3:00 PM', 'Final Project: Feature engineering'),
            ('3:00 PM - 3:15 PM', 'Break'),
            ('3:15 PM - 5:00 PM', 'Final Project: Build ML models'),
        ]),
        ('Friday', [
            ('9:00 AM - 10:30 AM', 'Final Project: Model evaluation and tuning'),
            ('10:30 AM - 10:45 AM', 'Break'),
            ('10:45 AM - 12:30 PM', 'Final Project: Create visualizations'),
            ('12:30 PM - 1:30 PM', 'Lunch Break'),
            ('1:30 PM - 3:00 PM', 'Final Project: Write project documentation'),
            ('3:00 PM - 3:15 PM', 'Break'),
            ('3:15 PM - 5:00 PM', 'Final Project: Prepare presentation'),
        ]),
        ('Saturday', [
            ('9:00 AM - 10:30 AM', 'Final Project: Complete and polish'),
            ('10:30 AM - 10:45 AM', 'Break'),
            ('10:45 AM - 12:30 PM', 'Update resume with new skills'),
            ('12:30 PM - 1:30 PM', 'Lunch Break'),
            ('1:30 PM - 3:00 PM', 'Update GitHub with all projects'),
            ('3:00 PM - 3:15 PM', 'Break'),
            ('3:15 PM - 5:00 PM', 'Review entire 8-week journey, plan next steps'),
        ]),
        ('Sunday', [
            ('9:00 AM - 12:00 PM', 'Celebrate! Review your progress'),
            ('12:00 PM - 1:00 PM', 'Lunch Break'),
            ('1:00 PM - 3:00 PM', 'Plan advanced topics: Deep Learning, NLP, etc.'),
            ('3:00 PM - 5:00 PM', 'Rest - you earned it!'),
        ]),
    ]

    for day, slots in week8:
        pdf.add_daily_schedule(day, slots)

    pdf.add_milestone('Complete an end-to-end ML portfolio project from scratch')

    # ========== RESOURCES PAGE ==========
    pdf.add_page()
    pdf.section_title('Recommended Free Resources')

    resources = [
        ('Python', 'Automate the Boring Stuff (automatetheboringstuff.com) | Python.org Tutorial | Corey Schafer YouTube'),
        ('SQL', 'SQLBolt (sqlbolt.com) | Mode SQL Tutorial | HackerRank SQL Practice'),
        ('Pandas', 'Kaggle Pandas Course | 10 Minutes to Pandas | Pandas documentation'),
        ('NumPy', 'NumPy Quickstart | Kaggle NumPy | NumPy documentation'),
        ('Machine Learning', 'Google ML Crash Course | Andrew Ng ML Specialization (Coursera) | Kaggle Learn'),
        ('Practice', 'LeetCode (Python) | HackerRank | Kaggle Competitions'),
        ('Datasets', 'Kaggle Datasets | UCI ML Repository | Google Dataset Search'),
    ]

    pdf.set_font('Helvetica', 'B', 9)
    pdf.set_fill_color(*pdf.primary_color)
    pdf.set_text_color(255, 255, 255)
    pdf.cell(40, 8, 'Topic', border=1, fill=True, align='C')
    pdf.cell(150, 8, 'Resources', border=1, fill=True, align='C')
    pdf.ln()

    pdf.set_font('Helvetica', '', 9)
    pdf.set_text_color(*pdf.dark_color)
    for idx, (topic, resource) in enumerate(resources):
        if idx % 2 == 0:
            pdf.set_fill_color(240, 248, 255)
        else:
            pdf.set_fill_color(255, 255, 255)
        pdf.cell(40, 8, topic, border=1, fill=True, align='C')
        pdf.cell(150, 8, resource, border=1, fill=True)
        pdf.ln()

    pdf.ln(10)
    pdf.section_title('Tips for Success')

    tips = [
        '1. Code every day - consistency beats cramming',
        '2. Type code manually - do not just copy/paste',
        '3. Build projects - they matter more than certificates',
        '4. Use flashcards (Anki) for SQL syntax and Pandas methods',
        '5. Join communities - r/datascience, Kaggle forums, Discord servers',
        '6. Teach what you learn - write blog posts or explain to a friend',
        '7. Take breaks - avoid burnout with the Pomodoro technique',
        '8. Track progress - keep a learning journal',
        '9. Ask questions - use Stack Overflow and Reddit',
        '10. Stay curious - explore topics beyond the curriculum',
    ]

    pdf.set_font('Helvetica', '', 10)
    pdf.set_text_color(*pdf.dark_color)
    for tip in tips:
        pdf.cell(0, 7, tip, new_x='LMARGIN', new_y='NEXT')

    # ========== DAILY SCHEDULE TEMPLATE ==========
    pdf.ln(10)
    pdf.section_title('Daily Schedule Template (9 AM - 5 PM)')

    schedule_template = [
        ('9:00 AM - 10:30 AM', 'Theory / Concept Learning'),
        ('10:30 AM - 10:45 AM', 'Short Break'),
        ('10:45 AM - 12:30 PM', 'Hands-on Practice / Coding'),
        ('12:30 PM - 1:30 PM', 'Lunch Break'),
        ('1:30 PM - 3:00 PM', 'Guided Practice / Exercises'),
        ('3:00 PM - 3:15 PM', 'Short Break'),
        ('3:15 PM - 5:00 PM', 'Projects / Review / Practice'),
    ]

    pdf.set_font('Helvetica', 'B', 9)
    pdf.set_fill_color(*pdf.primary_color)
    pdf.set_text_color(255, 255, 255)
    pdf.cell(50, 8, 'Time', border=1, fill=True, align='C')
    pdf.cell(140, 8, 'Activity', border=1, fill=True, align='C')
    pdf.ln()

    pdf.set_font('Helvetica', '', 9)
    pdf.set_text_color(*pdf.dark_color)
    for idx, (time, activity) in enumerate(schedule_template):
        if idx % 2 == 0:
            pdf.set_fill_color(240, 248, 255)
        else:
            pdf.set_fill_color(255, 255, 255)
        pdf.cell(50, 8, time, border=1, fill=True, align='C')
        pdf.cell(140, 8, activity, border=1, fill=True)
        pdf.ln()

    # Save
    output_path = r'C:\Users\GATEW\OneDrive\Documents\Default Project\Data_Scientist_Timetable.pdf'
    pdf.output(output_path)
    print(f"PDF created successfully at: {output_path}")
    return output_path


if __name__ == '__main__':
    create_timetable()
